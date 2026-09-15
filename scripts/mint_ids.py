#!/usr/bin/env python3
import argparse,uuid,re,os,time
from datetime import datetime,timezone
IID_RE=re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
def uuid7(ms=None):
    if ms is None: ms=int(time.time()*1000)
    ms &= (1<<48)-1; rand=int.from_bytes(os.urandom(10),'big')
    return uuid.UUID(int=(ms<<80)|(0x7<<76)|(((rand>>64)&0xfff)<<64)|(0b10<<62)|(rand&((1<<62)-1)))
def day_ms(s):
    return int(datetime.strptime(s,'%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp()*1000)
def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True)
    d=sp.add_parser('dataset'); d.add_argument('ds_iid')
    r=sp.add_parser('release'); r.add_argument('ds_iid'); r.add_argument('dataset_id'); r.add_argument('--ingest',required=True); r.add_argument('--rev',type=int,default=1)
    q=sp.add_parser('party'); q.add_argument('party_iid')
    a=p.parse_args()
    if a.cmd in ('dataset','release') and not IID_RE.fullmatch(a.ds_iid): p.error('ds_iid must be lowercase kebab-case')
    if a.cmd=='party' and not IID_RE.fullmatch(a.party_iid): p.error('party_iid must be lowercase kebab-case')
    if a.cmd=='dataset': print('dataset_id:',uuid.uuid4()); print('ds_iid:',a.ds_iid)
    elif a.cmd=='party': print('party_id:',uuid.uuid4()); print('party_iid:',a.party_iid)
    else:
        uuid.UUID(a.dataset_id); rid=uuid7(day_ms(a.ingest)); slug=f"{a.ds_iid}--ing{a.ingest.replace('-','')}--r{a.rev:03d}"
        print('dataset_id:',a.dataset_id); print('ds_iid:',a.ds_iid); print('release_id:',rid); print('release_slug:',slug)
if __name__=='__main__': main()
