from scrapy.crawler import CrawlerProcess

from my_spyder.my_spyder.spiders.authors import AuthorsSpider
from my_spyder.my_spyder.spiders.quotes import QuotesSpider


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()

