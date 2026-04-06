"""Twillot export CSV -> minimal Markdown (author, link, body)."""
import csv
import html
import sys
from pathlib import Path


def main() -> None:
    src = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else r"c:\Users\fyu\Downloads\twillot-bookmark-2026-04-06 (1).csv"
    )
    dst = Path(
        sys.argv[2]
        if len(sys.argv) > 2
        else str(src.with_suffix(".md").resolve())
    )

    with src.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    parts: list[str] = [
        "# Twillot 書籤（精簡）\n\n",
        f"來源：`{src}` · 共 {len(rows)} 則\n\n",
        "---\n",
    ]

    for row in rows:
        username = (row.get("Username") or "").strip()
        screen = (row.get("Screen Name") or "").strip()
        url = (row.get("URL") or "").strip()
        content = row.get("Content") or ""
        content = content.replace("\\n", "\n")
        content = html.unescape(content)

        parts.append(f"\n**作者** {username}（@{screen}）  \n")
        parts.append(f"**貼文連結** {url}  \n\n**正文**\n\n{content}\n\n---\n")

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {len(rows)} posts to {dst}")


if __name__ == "__main__":
    main()
