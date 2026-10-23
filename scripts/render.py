#!/usr/bin/env python3
"""Render an evidence-linked explicit-layout figure spec to editable SVG, PDF and PNG."""
import argparse, copy, hashlib, json, math, os, sys
from pathlib import Path
from check_spec import validate

def safe_output(path):
    p=Path(path).absolute()
    if any(x.is_symlink() for x in [p,*p.parents]):raise ValueError('Output and its parents must not be symlinks')
    p.mkdir(parents=True,exist_ok=True)
    if any(x.is_symlink() for x in p.iterdir()):raise ValueError('Output contains symlinks; choose a clean output directory')
    return p

def rebase_local_sources(d, source_spec_path, out):
    """Keep local evidence paths valid when exporting a spec to another folder."""
    local={key:source['file'] for key,source in d['sources'].items() if source.get('file')}
    if not local:
        return d
    if source_spec_path is None:
        raise ValueError('Local source files require source_spec_path (the input specification path)')
    base=Path(source_spec_path).absolute().parent
    delivered=copy.deepcopy(d)
    for key,value in local.items():
        if not isinstance(value,str):
            raise ValueError(f'{key}: local source file must be a path string')
        original=(base/value).resolve()
        if not original.is_file():
            raise ValueError(f'{key}: local source file does not exist: {original}')
        delivered['sources'][key]['file']=os.path.relpath(original,Path(out).absolute())
    return delivered

def render(d,out,source_spec_path=None):
    errors,issues=validate(d)
    if errors:raise ValueError('; '.join(errors))
    kind=d['visual'].get('type','explicit_layout_diagram')
    if kind != 'explicit_layout_diagram':
        raise ValueError(f'Unsupported visual type {kind!r}: use its dedicated renderer; this helper requires top-left box coordinates in drawing units')
    d=rebase_local_sources(d,source_spec_path,out)
    out=safe_output(out)
    os.environ.setdefault('MPLCONFIGDIR',str(out/'.mplconfig'))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, Rectangle
    from matplotlib.path import Path as MPath
    from matplotlib import rcParams
    rcParams.update({'svg.fonttype':'none','pdf.fonttype':42,'font.family':'DejaVu Sans'})
    style=json.loads((Path(__file__).resolve().parents[1]/'assets/style.json').read_text())
    v=d['visual'];w,h=v.get('canvas',[1200,740]);width=v.get('width_mm',180)/25.4
    fig,ax=plt.subplots(figsize=(width,width*h/w));fig.subplots_adjust(0,0,1,1)
    ax.set(xlim=(0,w),ylim=(h,0));ax.axis('off');fig.patch.set_facecolor('white')
    scale=width*72/w
    def label(x,y,t,size=15,weight='normal',ha='left',gid=None,color=None):
        artist=ax.text(x,y,t,fontsize=size*scale,va='center',ha=ha,fontweight=weight,color=color or style['text'],linespacing=1.35,zorder=5)
        if gid:artist.set_gid(gid)
    for p in v.get('panels',[]):
        x,y,pw,ph=p['box'];r=Rectangle((x,y),pw,ph,facecolor=p.get('fill','#F7F9FB'),edgecolor='#D4DCE6',linewidth=.5,zorder=0);r.set_gid(p['id']);ax.add_patch(r)
        label(x+16,y+23,p['label'],size=p.get('fontsize',20),weight='bold',gid=p['id']+'-label')
    for t in v.get('annotations',[]):label(t['x'],t['y'],t['text'],t.get('size',14),t.get('weight','normal'),gid=t.get('id'))
    nodes=v['nodes'];elements={n['id']:n for n in d['semantics']['elements']}
    def port(ident,side):
        x,y,nw,nh=nodes[ident]['box'];return {'left':(x,y+nh/2),'right':(x+nw,y+nh/2),'top':(x+nw/2,y),'bottom':(x+nw/2,y+nh)}[side]
    for e in d['semantics'].get('relations',[]):
        ev=v.get('edges',{}).get(e['id'],{});s=ev.get('from','right');t=ev.get('to','left')
        pts=[port(e['source'],s),*ev.get('via',[]),port(e['target'],t)]
        codes=[MPath.MOVETO]+[MPath.LINETO]*(len(pts)-1)
        arrow='-|>' if e['direction']=='directed' else '-'
        if e['type']=='inhibition':arrow='-['
        patch=FancyArrowPatch(path=MPath(pts,codes),arrowstyle=arrow,mutation_scale=7,linewidth=ev.get('linewidth',.9),linestyle=ev.get('style','--' if e['type'] in {'supervision','optimization'} else '-'),color=ev.get('color',style['arrow']),zorder=2)
        patch.set_gid(e['id']);ax.add_patch(patch)
        if ev.get('label'):
            q=ev.get('label_at',[(pts[0][0]+pts[-1][0])/2,(pts[0][1]+pts[-1][1])/2-12]);label(*q,ev['label'],size=ev.get('label_size',19),ha='center',gid=e['id']+'-label')
    for ident,n in nodes.items():
        x,y,nw,nh=n['box'];role=elements[ident]['role'];r=Rectangle((x,y),nw,nh,facecolor=n.get('fill',style.get(role,style['model'])),edgecolor=n.get('border',style['border']),linewidth=.8,zorder=3);r.set_gid(ident);ax.add_patch(r)
        label(x+nw/2,y+nh/2,elements[ident]['label'],n.get('fontsize',16),ha='center',gid=ident+'-label')
    for fmt in ['svg','pdf','png']:fig.savefig(out/f'figure.{fmt}',dpi=240,metadata={'Creator':'medical-computing-figures'} if fmt=='pdf' else None)
    plt.close(fig)
    (out/'figure_spec.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (out/'caption.md').write_text(d['caption']+'\n')
    import xml.etree.ElementTree as ET
    tree=ET.parse(out/'figure.svg');ns={'s':'http://www.w3.org/2000/svg'}
    manifest={'figure_id':d['figure']['id'],'spec_sha256':hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest(),'matplotlib':matplotlib.__version__,'python':sys.version.split()[0],'nodes':list(elements),'relations':[e['id'] for e in d['semantics'].get('relations',[])],'svg_text_objects':len(tree.findall('.//s:text',ns)),'svg_raster_images':len(tree.findall('.//s:image',ns)),'size_mm':[v.get('width_mm',180),v.get('width_mm',180)*h/w],'unresolved':issues,'visual_review':'REQUIRED: output generation is not visual inspection'}
    (out/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');return manifest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('spec',type=Path);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
    try:print(json.dumps(render(json.loads(a.spec.read_text()),a.out,source_spec_path=a.spec),indent=2));return 0
    except (ValueError,OSError,KeyError,ImportError) as e:print(f'Render failed: {e}',file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
