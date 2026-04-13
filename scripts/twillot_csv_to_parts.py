"""
從 Twillot 匯出 CSV 產生 twillot-bookmark-part-XX-of-N.md 分檔。
"""
import csv
import html
import re
import sys
from pathlib import Path

DEFAULT_CSV = Path(r"c:\Users\fyu\Downloads\twillot-bookmark-2026-04-13.csv")
DEFAULT_OUT = Path(r"c:\Users\fyu\Desktop\Note\twillot-bookmark-parts")
DEFAULT_NUM_PARTS = 22


def row_to_block(row: dict) -> str:
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
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CSV
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    num_parts = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_NUM_PARTS

    if not csv_path.is_file():
        raise SystemExit(f"CSV not found: {csv_path}")

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    blocks = [row_to_block(r).rstrip() + "\n" for r in rows]
    total = len(blocks)

    out_dir.mkdir(parents=True, exist_ok=True)

    # 刪除舊版不同份數的分檔（避免資料夾內混雜 of-20、of-22）
    for old in out_dir.glob("twillot-bookmark-part-*-of-*.md"):
        m = re.search(r"-of-(\d+)\.md$", old.name)
        if m and int(m.group(1)) != num_parts:
            old.unlink()

    for i in range(num_parts):
        start = i * total // num_parts
        end = (i + 1) * total // num_parts
        chunk = blocks[start:end]
        part_no = i + 1
        a, b = start + 1, end
        header = (
            f"# Twillot 書籤（精簡）— 第 {part_no}/{num_parts} 部\n\n"
            f"原檔：`{csv_path.name}` · 全檔共 **{total}** 則 · "
            f"**本部第 {a}–{b} 則**（共 {len(chunk)} 則）\n\n"
            "---\n\n"
        )
        body = "\n\n".join(chunk)
        out_path = out_dir / f"twillot-bookmark-part-{part_no:02d}-of-{num_parts}.md"
        out_path.write_text(header + body + "\n", encoding="utf-8")

    print(f"CSV: {csv_path}")
    print(f"Total: {total} posts -> {num_parts} files in {out_dir}")


if __name__ == "__main__":
    main()
