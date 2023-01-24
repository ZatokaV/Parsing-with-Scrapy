import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json", "FEED_EXPORT_ENCODING": 'utf-8'}
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            "fullname": extract_with_css('h3.author-title::text'),
            "born_date": extract_with_css('.author-born-date::text'),
            "born_location": extract_with_css('.author-born-location::text'),
            "description": extract_with_css('.author-description::text'),
        }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

