#!/usr/bin/env python3
from pathlib import Path
import csv,re,uuid,sys
ROOT=Path(__file__).resolve().parents[1]; REG=ROOT/'registry'
NULL={'nap','unk'}
def rows(name):
    p=REG/f'registry--{name}.csv'
    with p.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f)),list(csv.DictReader(p.open(newline='',encoding='utf-8')).fieldnames or [])
def main():
    errs=[]
    with (REG/'registry--dictionary.csv').open(newline='',encoding='utf-8') as f: spec=list(csv.DictReader(f))
    by={}
    for s in spec: by.setdefault(s['table_iid'],[]).append(s)
    loaded={}
    for t in ('packages','parties','party-roles'):
        p=REG/f'registry--{t}.csv'
        with p.open(newline='',encoding='utf-8') as f:
            dr=csv.DictReader(f); hdr=dr.fieldnames or []; rr=list(dr); loaded[t]=rr
        expected=[x['column_iid'] for x in sorted(by[t],key=lambda x:int(x['ordinal']))]
        if hdr!=expected: errs.append(f'{p.name}: header does not match dictionary')
        for i,r in enumerate(rr,2):
            for s in by[t]:
                v=(r.get(s['column_iid']) or '').strip()
                if s['required']=='yes' and (not v or v in NULL): errs.append(f'{p.name}:{i} {s["column_iid"]} required')
                if v and v not in NULL and s['value_domain_type']=='enum':
                    allowed=s['allowed_values'].split('|')
                    if v not in allowed: errs.append(f'{p.name}:{i} {s["column_iid"]}={v!r} not in {allowed}')
    ds={r['ds_iid'] for r in loaded['packages'] if r['ds_iid']}; rel={r['release_slug'] for r in loaded['packages'] if r['release_slug']}; parties={r['party_iid'] for r in loaded['parties'] if r['party_iid']}
    for i,r in enumerate(loaded['party-roles'],2):
        if r['ds_iid'] not in ds: errs.append(f'party-roles:{i} unknown ds_iid')
        if r['release_slug'] and r['release_slug'] not in rel: errs.append(f'party-roles:{i} unknown release_slug')
        if r['party_iid'] not in parties: errs.append(f'party-roles:{i} unknown party_iid')
    if errs:
        print('\n'.join('ERROR: '+e for e in errs)); sys.exit(1)
    print('Registry validation passed.')
if __name__=='__main__': main()
