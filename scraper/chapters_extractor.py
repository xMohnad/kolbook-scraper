from .request import pyparse


async def fetch_chapters(url: str):
    """
    Fetches and parses chapters from the provided URL.

    Args:
        url (str): The URL of the novel to parse..

    Returns:
        tuple: tuple: A tuple containing a list of chapters (each chapter is a list with id, number, and title)
            And the name of the novel
    """
    try:
        soup = await pyparse(url=url)

        name = soup.find("h1", class_="entry-title").get_text(strip=True)
        content = soup.find("div", class_="bixbox bxcl epcheck")

        chapters = []
        for li in reversed(content.findAll("li")):
            chapter_id = li["data-id"]
            chapter_num = li.find("div", class_="epl-num").text
            chapter_title = li.find("div", class_="epl-title").text

            chapters.append([chapter_id, chapter_num, chapter_title])

        return chapters, name
    except Exception as e:
        print(f"An error occurred while fetching chapter links: {e}")
        return None, None


# Usage example:
# chapters, name = await fetch_chapter("https://kolbook.xyz/series/the-dominating/")
