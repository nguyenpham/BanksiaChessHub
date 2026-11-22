Felicity endgame tablebases for chess, **3-5 men, one-side cut**: 145 endgames, distance to mate (DTM), 2,778,025,452 bytes. Made 2026-10-19 (checksums stamped 2026-10-30).

**One-side cut:** only the White-to-move file of each endgame is kept (`NAME.w.fegtb`). The prober answers a Black-to-move position exactly with a one-ply search over its White-to-move children, so the set answers every probe the full set (8.1 GB) answers, at less than half the size.

| file | what | endgames | size |
|---|---|---:|---:|
| `felicity-chess-3-4men.zip` | all 3 and 4 men (folders `1`, `1-1`, `2`) | 35 | 12.8 MB |
| `felicity-chess-5men-part1.zip` | 5 men: one piece against two (`1-2`, e.g. kqkrp), three against a bare king (`3`, e.g. kbbnk) | 55 | 1.03 GB |
| `felicity-chess-5men-part2.zip` | 5 men: two pieces against one (`2-1`, e.g. krpkr) | 55 | 1.73 GB |

- **A 5-men part needs the 3-4 men** (after a capture, the rebuilt Black-to-move score probes the smaller tables). Each part works with the 3-4 men alone, without the other part.
- Every zip unpacks into the same folder `felicity-chess/`: unpack them all in one place and point the program at `felicity-chess`. The prober searches the sub-folders.
- The zips are **not compressed** (stored): the files are LZMA-compressed already; 7-Zip at its best setting saved 0.23 %.
- **Banksia GUI:** *Tools › Download › Felicity* downloads, unpacks and adds them (Settings › Books & EGTBs) in one click per part; the 5-men rows bring the 3-4 men along.
- Format: signature 556683, LZMA, 4 KB blocks, the piece order chosen per endgame. Read by the Felicity prober of 2026-10-19 or later (the one in Banksia GUI); **older probers refuse these files**, including the one of the public `nguyenpham/FelicityEgtb`.
- Each file carries its own checksum in the header (bytes 112-127), so a file can be checked on its own. `SHA256SUMS.txt` lists the zips and every file inside them.

Checked before publishing (2026-11-22): the zips were unpacked with Windows' `tar`, and `fegtbsum verify` found all 145 files good; when they were made, every legal cell read back through the prober equalled the plain one-side cut (11,250,821,036 cells, 0 different), which was checked against the full set (26,233,354 positions, 0 mismatches).

Code and data are freeware / MIT.
