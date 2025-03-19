import asyncio
import json
from crawler.crawler import Crawler
from models.deepseek_processor import DeepSeekProcessor

async def main():
    # 1. Configure components
    crawler = Crawler()
    processor = DeepSeekProcessor()
    
    # 2. Scrape website
    url = "https://youngla.com/collections/mens-all"
    scraped_content = await crawler.scrape(url)
    
    # 3. Process with DeepSeek
    structured_data = processor.process_content(scraped_content)
    
    # 4. Save output
    with open("output.json", "w") as f:
        json.dump(json.loads(structured_data), f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())