import csv
import html
from pathlib import Path

CSV_PATH = Path(r"c:\Users\fyu\Downloads\twillot-bookmark-2026-04-06 (2).csv")
PART_PATH = Path(
    r"c:\Users\fyu\Desktop\Note\twillot-bookmark-parts\twillot-bookmark-part-01-of-20.md"
)

OLD_HEADER_LINE = (
    "原檔：`twillot-bookmark.md` · 全檔共 3930 則 · **本部第 1–196 則**（共 196 則）"
)
NEW_HEADER_LINE = (
    "原檔：`twillot-bookmark.md` · 已併入 `twillot-bookmark-2026-04-06 (2).csv`（7 則）"
    " · 全檔共 3937 則 · **本部第 1–203 則**（共 203 則）"
)


def row_to_block(row: dict) -> str:
    u = (row.get("Username") or "").strip()
    s = (row.get("Screen Name") or "").strip()
    url = (row.get("URL") or "").strip()
    c = row.get("Content") or ""
    c = c.replace("\\n", "\n")
    c = html.unescape(c)
    return (
        f"**作者** {u}（@{s}）  \n"
        f"**貼文連結** {url}  \n\n"
        f"**正文**\n\n{c}\n\n---\n\n"
    )


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    append_md = "".join(row_to_block(r) for r in rows)
    text = PART_PATH.read_text(encoding="utf-8")

    if OLD_HEADER_LINE not in text:
        raise SystemExit(f"Expected header line not found: {OLD_HEADER_LINE!r}")

    text = text.replace(OLD_HEADER_LINE, NEW_HEADER_LINE, 1)
    text = text.rstrip() + "\n\n" + append_md
    PART_PATH.write_text(text, encoding="utf-8")
    print(f"Appended {len(rows)} posts from {CSV_PATH.name}")


if __name__ == "__main__":
    main()
