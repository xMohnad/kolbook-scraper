import asyncio
from scraper import fetch_chapters, capture_chapter
from utils import filter_chapters


async def kolbook(novel_url, start: int = 0, end: int = None):
    """
    Fetch chapters from the novel URL and process them.

    Args:
        novel_url (str): The URL of the novel.
        start (int): The chapter number to start from. Defaults to 0.
        end (int): The chapter number to stop at. If not specified, continues to the end of the list.

    """
    try:
        chapters, name = await fetch_chapters(novel_url)
        filtered_chapters = await filter_chapters(chapters, start, end)
        print(f"{len(filtered_chapters)} chapters will be fetched")

        for chapter in filtered_chapters:
            chapter_id = chapter[0]
            chapter_num = chapter[1]
            chapter_title = chapter[2]

            chapter_url = f"https://kolbook.xyz/wp-json/wp/v2/posts/{chapter_id}"
            await capture_chapter(chapter_url, name, chapter_title, chapter_num)

            print(f"Finished downloading chapter: {chapter_num}")

    except Exception as e:
        print(f"An error occurred while processing the novel: {e}")


# Usage example
url = "https://kolbook.xyz/series/the-dominating/"
asyncio.run(kolbook(novel_url=url, start=1, end=2))
