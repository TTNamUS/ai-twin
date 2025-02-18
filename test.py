# import asyncio
# from crawl4ai import *

# async def main():
#     async with AsyncWebCrawler() as crawler:
#         result = await crawler.arun(
#             url="https://www.nbcnews.com/business",
#         )

#         with open("output.md", "w", encoding="utf-8") as f:
#             f.write(result.markdown)


# if __name__ == "__main__":
#     asyncio.run(main())

import ai_twin

print(ai_twin.__name__)
