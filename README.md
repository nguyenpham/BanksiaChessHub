# BanksiaChessHub
Chess stuff for both human and computers

Free data for chess players and chess programs, published as [releases](https://github.com/nguyenpham/BanksiaChessHub/releases)
(this repository holds no data itself). Banksia GUI downloads and installs them from **Tools › Download**.

| Release | What | Files | Banksia GUI tab |
|---|---|---|---|
| [`felicity-chess5men`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/felicity-chess5men) | Felicity endgame tablebases, chess 3-5 men, distance to mate, one-side cut (145 endgames, 2.78 GB) | `felicity-chess-3-4men.zip` (12.8 MB), `felicity-chess-5men-part1.zip` (1.03 GB), `felicity-chess-5men-part2.zip` (1.73 GB), `SHA256SUMS.txt` | Felicity |
| [`banksiamasters-db`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-db) | Banksia Masters database: 8,008,264 games between human players (OCGDB / SQLite) | `banksiamasters.ocgdb.db3.7z` (855 MB) | Game databases |
| [`banksiamasters-obs`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-obs) | Banksia Masters opening book, OOBS | `banksiamasters.obs.db3.7z` (29.8 MB) | Opening books |
| [`banksiamasters-polyglot`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/banksiamasters-polyglot) | Banksia Masters opening book, Polyglot | `banksiamasters.bin.7z` (7.8 MB) | Opening books |
| [`lichess-puzzles`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/lichess-puzzles) | Lichess Puzzles: 2,440,210 puzzles as games (OCGDB / SQLite; rating and themes as comments) | `lichesspuzzles2-4M.ocgdb.db3.zip` (148 MB) | Game databases |
| [`whale-epd`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/whale-epd) | Whale EPD collection: 57,500 test positions with their EPD operations (SQLite) | `whale.epd.db3.zip` (1.6 MB) | Game databases |
| [`fruit-book`](https://github.com/nguyenpham/BanksiaChessHub/releases/tag/fruit-book) | Fruit opening book (Fabien Letouzey), Polyglot | `fruit.bin.zip` (365 KB) | Opening books |
| `bsg-chess1`, `bsg-chess2`, `bsg-chess-reader`, `bsg-xq-reader` | Banksia GUI's / MoonRiver's own neural networks (AI assistant, board readers) | | Neural networks |

**Release names** (owner, 2026-11-22): tags, titles and file names carry **no dates**
(`banksiamasters-db`, not `banksiamasters-db-2026-11-20`). Tablebase releases do not say "cut" in their names either
(`felicity-chess5men`, "Felicity EGTB, chess 3-5 men"); the notes explain the one-side cut. A new version replaces the files of the same
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

## Lichess Puzzles, Whale EPD, Fruit book (2026-11-23)

Until 2026-11-23 these three were served from `banksiagui.com/dl/` (Cloudflare R2); they moved here and
the server's copies were deleted, with every other database and book it had (Banksia GUI `docs/download.md` §14).
The files are the server's, repacked without the `__MACOSX/` entries the old zips carried; contents unchanged.

| File | Unpacks to | SHA-256 of the zip | SHA-256 of the file | Source, licence |
|---|---|---|---|---|
| `lichesspuzzles2-4M.ocgdb.db3.zip` | `lichesspuzzles2-4M.ocgdb.db3`, 372,609,024 bytes | `6ef0ef4a42cb2ee62e40b47da1735a073e7ff641da88963bc4878c872ec2f8d7` | `6eb219f1985ae57d4083a3481c3fbc638440e7104db275f912ef80701d1b68dd` | [Lichess puzzle database](https://database.lichess.org/#puzzles), CC0; converted April 2022 (OCGDB 0.6, Moves2) |
| `whale.epd.db3.zip` | `whale.epd.db3`, 6,066,176 bytes | `2796de0b2799ef1784bbc33ecfc1438e531f30ef3b4a41b2441ec299e4551fc1` | `91b9ae50258af0ef6a08da3912ca531268aaad2f94e0bda2eeabc33e2cba36e0` | collected from EPD test suites by the Banksia Team, July 2022 |
| `fruit.bin.zip` | `fruit.bin`, 503,680 bytes | `d3b933793c5c786be353fa1d742a4ee3be126cb922e9269668370d5925ca60b6` | `4db07cd6d0d3ad7600140197cb9ef759981f028a7072d18774f109970648b734` | the opening book of the Fruit engine, Fabien Letouzey |

## Licence

MIT (see `LICENSE`); the data are freeware.
