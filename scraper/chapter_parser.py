from .request import pyparse, parse_html
from pathlib import Path


def escape_latex_special_chars(text):
    """Escape special characters for LaTeX."""
    return text.replace("&", "\\&").replace("%", "\\%").replace("$", "\\$")


async def fetch_and_parse_chapter(url):
    """Fetch and parse the chapter content from the given URL."""
    chapter_data = await pyparse(url=url)
    story_content = chapter_data["content"]["rendered"]
    soup = parse_html(story_content)
    return [p.get_text(separator="\n") for p in soup.find_all("p")]


def prepare_latex_content(title, paragraphs):
    """Prepare the LaTeX content from the chapter title and paragraphs."""
    latex_chapter_title = f"\\chapter{{{title}}}\n\n"
    latex_content = latex_chapter_title
    for para in paragraphs:
        para = escape_latex_special_chars(para)
        latex_content += f"{para}\n\n".rstrip() + "\n"
    return latex_content


def save_latex_file(directory, num, content):
    """Save the LaTeX content to a .tex file."""
    directory_path = Path(directory)
    directory_path.mkdir(parents=True, exist_ok=True)
    file_path = directory_path / f"{num}.tex"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


async def capture_chapter(url, name, title, num):
    """Main function to capture and save the chapter as a LaTeX file."""
    try:
        paragraphs = await fetch_and_parse_chapter(url)
        latex_content = prepare_latex_content(title, paragraphs)
        save_latex_file(name, num, latex_content)
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage example:
# await capture_chapter("https://kolbook.xyz/wp-json/wp/v2/posts/{id}", "output_dir", "Chapter 1 Title", 1)
"""
<li class="tseplsfrst" data-ID="215289">
    <a href="https://kolbook.xyz/shaag24the-dominatingz435ggye-215289/">
        <div class="epl-num">الفصل 1</div>
        <div class="epl-title">العودة بنجاح</div>
        <div class="epl-date">يونيو 6, 2024</div>
    </a>
</li>
"""
