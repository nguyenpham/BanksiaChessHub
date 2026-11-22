# BanksiaChessHub
Chess stuff for both human and computers

Free data for chess players and chess programs, published as [releases](https://github.com/nguyenpham/BanksiaChessHub/releases)
(this repository holds no data itself). Banksia GUI downloads and installs them from **Tools › Download**.

| Release | What | Files | Banksia GUI tab |
|---|---|---|---|
| [`felicity-chess5men-cut`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/felicity-chess5men-cut) | Felicity endgame tablebases, chess 3-5 men, distance to mate, one-side cut (145 endgames, 2.78 GB) | `felicity-chess-3-4men.zip` (12.8 MB), `felicity-chess-5men-part1.zip` (1.03 GB), `felicity-chess-5men-part2.zip` (1.73 GB), `SHA256SUMS.txt` | Felicity |
| [`banksiamasters-db`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-db) | Banksia Masters database: 8,008,264 games between human players (OCGDB / SQLite) | `banksiamasters.ocgdb.db3.7z` (855 MB) | Game databases |
| [`banksiamasters-obs`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-obs) | Banksia Masters opening book, OOBS | `banksiamasters.obs.db3.7z` (29.8 MB) | Opening books |
| [`banksiamasters-polyglot`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-polyglot) | Banksia Masters opening book, Polyglot | `banksiamasters.bin.7z` (7.8 MB) | Opening books |
| `bsg-chess1`, `bsg-chess2`, `bsg-chess-reader`, `bsg-xq-reader` | Banksia GUI's / MoonRiver's own neural networks (AI assistant, board readers) | | Neural networks |

**Release names** (owner, 2026-11-22): tags, titles and file names carry **no dates**
(`banksiamasters-db`, not `banksiamasters-db-2026-11-20`). A new version replaces the files of the same
release, or takes a version word (`-v2`) when old programs must keep the old files. The four dated tags
of 2026-11-20/22 were renamed that day; their old download links no longer answer.

## Felicity tablebases, chess 3-5 men (2026-11-22)

Every chess endgame of up to 5 pieces (both kings included), with the **exact distance to mate**.

- **One-side cut:** only the White-to-move file of each endgame is kept (`NAME.w.fegtb`). The prober
  answers a Black-to-move position exactly by a one-ply search over its children, so the 2.78 GB answer
  every probe the full set (8.1 GB, both sides) answers.
- **Three parts**, each under GitHub's 2 GiB limit and useful on its own with the 3-4 men:
  - `felicity-chess-3-4men.zip`: all 3 and 4 men, 35 endgames (folders `1`, `1-1`, `2`);
  - `felicity-chess-5men-part1.zip`: 5 men with one piece against two (`1-2`, e.g. kqkrp) or three
    against a lone king (`3`, e.g. kbbnk), 55 endgames;
  - `felicity-chess-5men-part2.zip`: 5 men with two pieces against one (`2-1`, e.g. krpkr), 55 endgames.
- **A 5-men part needs the 3-4 men**: after a capture the rebuilt Black-to-move score probes the smaller
  tables. Promotions stay inside the same part, so part 1 and part 2 do not need each other.
- All zips unpack into one folder, `felicity-chess/`; point the program at it (sub-folders are searched).
- **Not compressed** (the zips are *stored*): the files are LZMA-compressed already; 7-Zip at its best
  setting saved 0.23 %.
- Format: signature 556683, LZMA, 4 KB blocks, piece order chosen per endgame. It needs the Felicity
  prober of 2026-10-19 or later (the one in Banksia GUI); older probers, the public
  [FelicityEgtb](https://github.com/nguyenpham/FelicityEgtb)'s among them, refuse these files.
- Each file has its own checksum in its header (bytes 112-127, stamped 2026-10-30). `SHA256SUMS.txt`
  lists the zips and every file in them.
- Checked before publishing (2026-11-22): unpacked with Windows' `tar`, `fegtbsum verify` found the 145
  files good; a file differs from the draft of 2026-10-19 (`FelicityEGTB-chess5men` `cut-w-1`) only in
  those 16 checksum bytes.

How the release was made: Banksia GUI `docs/download.md` §12.

## Licence

MIT (see `LICENSE`); the data are freeware.
