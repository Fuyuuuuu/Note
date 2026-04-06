"""Split twillot-bookmark.md into N part files by post boundaries."""
import re
import sys
from pathlib import Path


def main() -> None:
    src = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else r"c:\Users\fyu\Desktop\Note\twillot-bookmark.md"
    )
    out_dir = Path(
        sys.argv[2]
        if len(sys.argv) > 2
        else str(src.parent / "twillot-bookmark-parts")
    )
    num_parts = int(sys.argv[3]) if len(sys.argv) > 3 else 20

    text = src.read_text(encoding="utf-8")
    parts = re.split(r"(?=^\*\*作者\*\*)", text, flags=re.MULTILINE)
    header = parts[0].rstrip() + "\n\n"
    posts = parts[1:]
    n = len(posts)
    if n == 0:
        raise SystemExit("No posts found (no **作者** lines).")

    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(num_parts):
        start = i * n // num_parts
        end = (i + 1) * n // num_parts
        chunk = posts[start:end]
        body = "".join(chunk)
        part_no = i + 1
        new_header = (
            f"# Twillot 書籤（精簡）— 第 {part_no}/{num_parts} 部\n\n"
            f"原檔：`{src.name}` · 全檔共 {n} 則 · **本部第 {start + 1}–{end} 則**（共 {len(chunk)} 則）\n\n"
            "---\n\n"
        )
        out_path = out_dir / f"twillot-bookmark-part-{part_no:02d}-of-{num_parts:02d}.md"
        out_path.write_text(new_header + body, encoding="utf-8")
        print(f"{out_path.name}: posts {start + 1}–{end} ({len(chunk)} 則)")

    print(f"Done. Output: {out_dir}")


if __name__ == "__main__":
    main()
