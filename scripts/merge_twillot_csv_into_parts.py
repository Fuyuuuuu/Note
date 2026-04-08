"""
將 Twillot 匯出 CSV 合併進 twillot-bookmark-parts/*.md：
- 保留現有貼文順序
- 新 CSV 貼文接在後面（依 CSV 列順序）
- 以 URL 去重（已存在則略過）
- 重新均分為 20 部並覆寫各 part 檔
"""
import csv
import html
import re
import sys
from pathlib import Path

PARTS_DIR = Path(r"c:\Users\fyu\Desktop\Note\twillot-bookmark-parts")
POST_START = re.compile(r"^\*\*作者\*\*", re.MULTILINE)


def normalize_url(url: str) -> str:
    u = (url or "").strip().lower()
    u = u.replace("twitter.com/", "x.com/")
    return u.rstrip("/")


def parse_post_blocks(md: str) -> list[str]:
    """回傳每則貼文區塊（含 **作者** 至結尾 ---）。"""
    chunks = re.split(r"(?=^\*\*作者\*\*)", md, flags=re.MULTILINE)
    out: list[str] = []
    for ch in chunks:
        ch = ch.strip()
        if ch.startswith("**作者**"):
            out.append(ch)
    return out


def block_url(block: str) -> str | None:
    m = re.search(r"^\*\*貼文連結\*\*\s+(\S+)", block, re.MULTILINE)
    return normalize_url(m.group(1)) if m else None


def csv_row_to_block(row: dict) -> str:
    username = (row.get("Username") or "").strip()
    screen = (row.get("Screen Name") or "").strip()
    url = (row.get("URL") or "").strip()
    content = row.get("Content") or ""
    content = content.replace("\\n", "\n")
    content = html.unescape(content)
    return (
        f"**作者** {username}（@{screen}）  \n"
        f"**貼文連結** {url}  \n\n"
        f"**正文**\n\n{content}\n\n---\n"
    )


def main() -> None:
    csv_path = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else r"c:\Users\fyu\Downloads\twillot-bookmark-2026-04-07.csv"
    )
    if not csv_path.is_file():
        raise SystemExit(f"CSV not found: {csv_path}")

    part_files = sorted(PARTS_DIR.glob("twillot-bookmark-part-*-of-20.md"))
    if len(part_files) != 20:
        raise SystemExit(f"Expected 20 part files in {PARTS_DIR}, got {len(part_files)}")

    blocks: list[str] = []
    seen: set[str] = set()
    for fp in part_files:
        text = fp.read_text(encoding="utf-8")
        for b in parse_post_blocks(text):
            u = block_url(b)
            if u:
                seen.add(u)
            # 正規化結尾：確保以 --- 結尾
            b = b.rstrip()
            if not b.endswith("---"):
                b = b.rstrip("-") + "\n\n---"
            blocks.append(b)

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    added = 0
    skipped_dup = 0
    for row in rows:
        u = normalize_url(row.get("URL") or "")
        if not u:
            continue
        if u in seen:
            skipped_dup += 1
            continue
        seen.add(u)
        nb = csv_row_to_block(row).rstrip() + "\n"
        blocks.append(nb)
        added += 1

    total = len(blocks)
    num_parts = 20

    for i in range(num_parts):
        start = i * total // num_parts
        end = (i + 1) * total // num_parts
        chunk = blocks[start:end]
        part_no = i + 1
        a, b = start + 1, end
        header = (
            f"# Twillot 書籤（精簡）— 第 {part_no}/20 部\n\n"
            f"原檔：Twillot 書籤 · 已合併 `{csv_path.name}`（新增 **{added}** 則，略過重複 **{skipped_dup}** 則）"
            f" · 全檔共 **{total}** 則 · **本部第 {a}–{b} 則**（共 {len(chunk)} 則）\n\n"
            "---\n\n"
        )
        body = "\n\n".join(chunk)
        out_path = PARTS_DIR / f"twillot-bookmark-part-{part_no:02d}-of-20.md"
        out_path.write_text(header + body + "\n", encoding="utf-8")

    print(f"Total posts: {total} (was {total - added}, +{added}, skipped dup {skipped_dup})")
    print(f"Wrote {PARTS_DIR}/ twillot-bookmark-part-01..20-of-20.md")


if __name__ == "__main__":
    main()
