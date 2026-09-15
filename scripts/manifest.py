#!/usr/bin/env python3
import argparse,hashlib,os,fnmatch
from pathlib import Path
EXCLUDES=['.DS_Store','Thumbs.db','desktop.ini','*.tmp']; CHUNK=1<<20
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(CHUNK),b''): h.update(b)
    return h.hexdigest()
def main():
    p=argparse.ArgumentParser(); p.add_argument('raw_dir'); p.add_argument('--out'); a=p.parse_args()
    raw=Path(a.raw_dir).resolve(); out=Path(a.out).resolve() if a.out else raw.parent/(raw.parent.name+'.sha256')
    rows=[]; total=0
    for dp,_,fs in os.walk(raw):
        for n in fs:
            if any(fnmatch.fnmatch(n,x) for x in EXCLUDES): continue
            q=Path(dp)/n
            if q.is_symlink() or q.resolve()==out: continue
            rel=q.relative_to(raw).as_posix(); size=q.stat().st_size; total+=size; rows.append((rel,sha(q)))
    rows.sort(); out.write_text(''.join(f'{h}  {r}\n' for r,h in rows),encoding='utf-8')
    print('file_manifest_path:',out); print('manifest_sha256:',sha(out)); print('file_count:',len(rows)); print('total_bytes:',total)
if __name__=='__main__': main()
