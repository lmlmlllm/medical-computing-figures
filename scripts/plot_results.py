#!/usr/bin/env python3
"""Plot published aggregate values from explicit mappings; no invented inference or raw-data reconstruction."""
import argparse,csv,hashlib,json,math,os,sys
from pathlib import Path
from render import safe_output

def plot(data,mapping,out):
    out=safe_output(out);m=json.loads(mapping.read_text())
    required=['source','measure','unit','analysis_unit','denominator','aggregation','error_definition','scope','caption']
    missing=[k for k in required if not m.get(k)]
    if missing:raise ValueError('Mapping missing: '+', '.join(missing))
    with data.open(newline='') as f:rows=list(csv.DictReader(f))
    if not rows:raise ValueError('Input has no data rows')
    seen=set()
    for r in rows:
        if not all(r.get(k) for k in ['series','group','value','source_location']):raise ValueError('CSV requires series,group,value,source_location')
        key=(r['series'],r['group'])
        if key in seen:raise ValueError(f'Duplicate aggregate {key}')
        seen.add(key);r['value']=float(r['value'])
        if not math.isfinite(r['value']):raise ValueError('Non-finite value')
        if m['unit']=='percent' and not 0<=r['value']<=100:raise ValueError('Percent outside 0..100')
    os.environ.setdefault('MPLCONFIGDIR',str(out/'.mplconfig'))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'svg.fonttype':'none','pdf.fonttype':42,'font.size':9,'font.family':'DejaVu Sans'})
    groups=list(dict.fromkeys(r['group'] for r in rows));series=list(dict.fromkeys(r['series'] for r in rows))
    series_ids={s:m.get('series_ids',{}).get(s,'series-'+str(i)) for i,s in enumerate(series)}
    if len(set(series_ids.values()))!=len(series_ids):raise ValueError('Duplicate series SVG IDs')
    fig,ax=plt.subplots(figsize=(7.1,max(3,len(groups)*.44+1.1)),layout='constrained')
    for j,s in enumerate(series):
        rr=[r for r in rows if r['series']==s];ys=[groups.index(r['group'])+(j-(len(series)-1)/2)*.20 for r in rr]
        points=ax.scatter([r['value'] for r in rr],ys,label=s,s=36,marker=['o','s','^','D'][j%4],color=['#4E79A7','#8870AC','#469885','#A66B40'][j%4],zorder=3);points.set_gid(series_ids[s])
        for r,y in zip(rr,ys):ax.annotate(f"{r['value']:g}",(r['value'],y),xytext=(7,0),textcoords='offset points',va='center',fontsize=8)
    ax.set_yticks(range(len(groups)),groups);ax.invert_yaxis();ax.set_xlabel(m['measure']+' ('+m['unit']+')');ax.set_title(m.get('title','Published aggregate values'),loc='left',fontsize=11,pad=36)
    if m['unit']=='percent':
        ax.set_xlim(-3,105);ax.set_xticks(range(0,101,20))
    else:
        lo=min(0.,min(r['value'] for r in rows));hi=max(0.,max(r['value'] for r in rows))
        span=hi-lo or 1.
        ax.set_xlim(lo-.08*span,hi+.20*span)
    ax.grid(axis='x',color='#E5EAF0');ax.spines[['top','right','left']].set_visible(False);ax.legend(frameon=False,loc='lower left',bbox_to_anchor=(0,1.015),borderaxespad=0,ncol=min(len(series),4),fontsize=8)
    axis_limits=list(ax.get_xlim())
    for ext in ['png','svg','pdf']:fig.savefig(out/f'figure.{ext}',dpi=240)
    plt.close(fig)
    report={'input_sha256':hashlib.sha256(data.read_bytes()).hexdigest(),'mapping_sha256':hashlib.sha256(mapping.read_bytes()).hexdigest(),'mapped_rows':rows,'n_rows':len(rows),'matplotlib':matplotlib.__version__,'python':sys.version.split()[0],'scope':m['scope'],'no_inference_added':True,'axis_limits':axis_limits,'series_svg_ids':series_ids,'visual_check':'required separately'}
    (out/'data_mapping.json').write_text(json.dumps(report,indent=2));(out/'caption.md').write_text(m['caption']+'\n');return report

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('data',type=Path);p.add_argument('--mapping',required=True,type=Path);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
    try:print(json.dumps(plot(a.data,a.mapping,a.out),indent=2));return 0
    except (OSError,ValueError,KeyError,ImportError) as e:print(f'Plot failed: {e}',file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
