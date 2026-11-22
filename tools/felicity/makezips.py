"""Pack the Felicity chess 3-5 men one-side cut (a4k) into store-only zips for a GitHub release.

usage: python -I makezips.py SRC_A4K DRAFT_SHA256SUMS OUTDIR
Each zip holds felicity-chess/<group>/<name>.w.fegtb, so all parts extract into one folder.

Run on 2026-11-22 with SRC_A4K = D:/share-phampc/chess/felicity/fegtb-cut-repack/a4k and the SHA256SUMS of the
draft release cut-w-1 of nguyenpham/FelicityEGTB-chess5men: all 145 "MISMATCH" lines are expected, that list
is from before the files were checksum-stamped (2026-10-30, FelicityEGTBBK docs/Checksum.md §4); `cmp -l`
showed only header bytes 112-127 differ, and `fegtbsum verify` on the unpacked zips found 145 good
(fegtbsum-verify.txt). The zips are stored (no compression): 7-Zip -mx=9 saved 0.23 %.
"""
import hashlib, os, sys, zipfile

src, sums_path, out = sys.argv[1:4]
PARTS = [
    ("felicity-chess-3-4men.zip", ["1", "1-1", "2"]),
    ("felicity-chess-5men-part1.zip", ["1-2", "3"]),
    ("felicity-chess-5men-part2.zip", ["2-1"]),
]
TOP = "felicity-chess"

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()

draft = {}
for line in open(sums_path, encoding="utf-8"):
    d, n = line.split()
    draft[n] = d

os.makedirs(out, exist_ok=True)
allsums, zipsums, bad, seen = [], [], 0, set()
for zname, groups in PARTS:
    zpath = os.path.join(out, zname)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_STORED, allowZip64=False) as z:
        for g in groups:
            for n in sorted(os.listdir(os.path.join(src, g))):
                p = os.path.join(src, g, n)
                d = sha(p)
                if draft.get(n) != d:
                    bad += 1
                    print("MISMATCH", g, n, d, draft.get(n))
                seen.add(n)
                allsums.append(f"{d}  {TOP}/{g}/{n}")
                z.write(p, f"{TOP}/{g}/{n}")
    with zipfile.ZipFile(zpath) as z:
        t = z.testzip()
        cnt = len(z.namelist())
    zipsums.append(f"{sha(zpath)}  {zname}")
    print(zname, cnt, "files", os.path.getsize(zpath), "bytes, testzip:", t or "ok")

missing = set(draft) - seen
print("files", len(seen), "mismatches", bad, "missing", sorted(missing))
with open(os.path.join(out, "SHA256SUMS.txt"), "w", newline="\n") as f:
    f.write("\n".join(zipsums + allsums) + "\n")
