#!/usr/bin/env python3
"""Structural/source-reference checks only; never substitutes for visual/scientific review."""
import argparse, json, sys
from pathlib import Path

KINDS={'data_flow','computation','supervision','optimization','temporal','contains','grouping','comparison','adjacency','association','activation','inhibition','causal','evidence','hypothesis','parameter_sharing',
       'control_setting','wireless_energy_transfer','electrical_conduction',
       'electrical_stimulation','physiological_measurement'}
STATUS={'confirmed','conflict','unknown','hypothesis','inference'}

def validate(d):
    errors, issues=[],[]
    for k in ['figure','sources','semantics','visual','caption']:
        if k not in d: errors.append(f'missing {k}')
    if errors:return errors,issues
    for k in ['id','version','purpose','material_version','excluded_inferences']:
        if not d['figure'].get(k):errors.append(f'figure missing {k}')
    sources=d['sources'];sem=d['semantics'];ids=set();rids=set()
    if not sem.get('elements'):errors.append('no elements')
    for e in sem.get('elements',[]):
        ident=e.get('id')
        if not isinstance(ident,str) or not ident or ident in ids:errors.append(f'bad/duplicate element ID {ident}')
        ids.add(ident)
        for k in ['label','role','stage','source_refs']:
            if not e.get(k):errors.append(f'{ident}: missing {k}')
        for s in e.get('source_refs',[]):
            if s not in sources:errors.append(f'{ident}: unknown source {s}')
        if d['visual'].get('type') != 'aggregate_dotplot' and ident not in d['visual'].get('nodes',{}):errors.append(f'{ident}: missing layout')
    for e in sem.get('relations',[]):
        ident=e.get('id')
        if not isinstance(ident,str) or not ident or ident in rids or ident in ids:errors.append(f'bad/duplicate relation ID {ident}')
        rids.add(ident)
        for k in ['source','target','type','direction','stage','condition','source_refs','status']:
            if k not in e or e[k] in ['',None,[]]:errors.append(f'{ident}: missing {k}')
        for k in ['source','target']:
            if e.get(k) not in ids:errors.append(f'{ident}: unresolved {k}')
        if e.get('type') not in KINDS:errors.append(f'{ident}: unsupported relationship')
        if e.get('direction') not in {'directed','undirected'}:errors.append(f'{ident}: invalid direction')
        if e.get('status') not in STATUS:errors.append(f'{ident}: invalid status')
        if e.get('status') in {'conflict','unknown','inference'}:issues.append(f'{ident}: {e["status"]}; scientific review unresolved')
        for s in e.get('source_refs',[]):
            if s not in sources:errors.append(f'{ident}: unknown source {s}')
    for k,allowed in [('nodes',ids),('edges',rids)]:
        extra=set(d['visual'].get(k,{}))-allowed
        if extra:errors.append(f'unknown visual {k} {sorted(extra)}')
    for sid,s in sources.items():
        if not s.get('location') or not (s.get('url') or s.get('file')):errors.append(f'{sid}: untraceable source')
    return errors,issues

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('spec',type=Path);p.add_argument('--compare',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.spec.read_text());errors,issues=validate(d)
        same=None
        if a.compare:
            old=json.loads(a.compare.read_text());oe,oi=validate(old);errors.extend('previous: '+e for e in oe)
            same=old['semantics']==d['semantics']
        result={'structural_pass':not errors,'errors':errors,'unresolved':issues,'semantic_preserved':same,'scope':'IDs, required fields, source references and exact semantic comparison only; no pixels or scientific validity checked'}
        print(json.dumps(result,indent=2,ensure_ascii=False))
        return 1 if errors or same is False else 2 if issues else 0
    except (OSError,ValueError,KeyError,TypeError) as e:print(f'Invalid input: {e}',file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
