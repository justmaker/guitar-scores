#!/usr/bin/env python3
"""Auto-generate index.md for beginner/intermediate/advanced from song files."""
import os
import re

DOCS_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs')

CATEGORIES = {
    'beginner': {'title': '初級', 'desc': '適合剛開始學吉他的曲目，主要使用開放和弦。'},
    'intermediate': {'title': '中級', 'desc': '需要封閉和弦或較複雜和弦進行的曲目。'},
    'advanced': {'title': '進階', 'desc': '有轉調、複雜編曲或大量封閉和弦的曲目。'},
}

def extract_info(filepath):
    """Extract song title and metadata from a .md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get h1 title (e.g. "# 稻香 - 周杰倫")
    m = re.search(r'^# (.+)$', content, re.MULTILINE)
    if not m:
        return None
    title = m.group(1)

    # Split "歌名 - 歌手"
    parts = title.split(' - ', 1)
    song = parts[0].strip()
    artist = parts[1].strip() if len(parts) > 1 else ''

    # Get chords count from "## 使用和弦" section
    m = re.search(r'## 使用和弦\n\n(.+?)(?:\n\n|\n##)', content, re.DOTALL)
    chords = ''
    if m:
        chord_line = m.group(1)
        # Count links and plain text chords
        n_links = len(re.findall(r'\[([^\]]+)\]', chord_line))
        n_plain = len(re.findall(r'(?:^|,\s*)([A-G])', chord_line)) - n_links
        total = n_links + max(0, n_plain)
        if total > 0:
            chords = str(total)

    return {'song': song, 'artist': artist, 'chords': chords, 'filename': os.path.basename(filepath)}


def generate_index(category):
    """Generate index.md content for a category."""
    info = CATEGORIES[category]
    cat_dir = os.path.join(DOCS_DIR, category)
    
    songs = []
    for f in sorted(os.listdir(cat_dir)):
        if f == 'index.md' or not f.endswith('.md'):
            continue
        filepath = os.path.join(cat_dir, f)
        data = extract_info(filepath)
        if data:
            songs.append(data)

    lines = [f"# {info['title']}\n", f"\n{info['desc']}\n"]

    if songs:
        lines.append("\n| 歌曲 | 歌手 | 和弦數 |")
        lines.append("|------|------|--------|")
        for s in songs:
            link = f"[{s['song']}]({s['filename']})"
            lines.append(f"| {link} | {s['artist']} | {s['chords']} |")

    lines.append("")
    return '\n'.join(lines)


def main():
    for category in CATEGORIES:
        content = generate_index(category)
        index_path = os.path.join(DOCS_DIR, category, 'index.md')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {index_path}")


if __name__ == '__main__':
    main()
