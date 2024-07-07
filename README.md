# kolbook-scraper

`kolbook-scraper` is designed to scrape and process novels hosted on the kolbook website. This tool fetches chapter links, retrieves their content, and converts them into LaTeX format.

## Usage

1. **Fetch Chapters**: Use the `fetch_chapters` function to retrieve the chapter from the novel URL.
2. **Process Chapter**: Use the `capture_chapter` function to fetch and convert chapter content into LaTeX format.
3. **Save Files**: Save the processed content into `.tex` files.

_Example:_

```python
# main.py
import asyncio
from scraper import fetch_chapter_links, capture_chapter

url = "https://kolbook.xyz/series/the-dominating/"
asyncio.run(kolbook(novel_url=url, start=1, end=10))
```

_In this example:_

-   **start**: The chapter number to start from. If not specified, starts from the first item.
-   **end**: The chapter number to stop at. If not specified, continues to the end.

Adjust the values of `start` and `end` as needed to process the desired range of chapters.

## Installation

To use `kolbook-scraper`, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

-   Python 3.7+
-   `httpx==0.27.0`
-   `beautifulsoup4==4.12.3`
-   `fake-useragent==1.5.1`

## Related Projects

[kolnovel-scraper](https://github.com/PurpleHallos/kolnovel-scraper) helped me a lot as a reference and provided valuable insights during the development of `kolbook-scraper`.
