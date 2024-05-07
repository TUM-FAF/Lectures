import scrapy
from scrapy.http import Request
from urllib.parse import urljoin


class MaklerSpider(scrapy.Spider):
    name = "makler"
    # allowed_domains = ["markler.md"]
    # start_urls = ["https://makler.md/md/dating/marriage-posts/an/37427"]
    # response.xpath("//article/descendant::a/@href").extract()

    start_url = "https://makler.md/md/dating"

    def start_requests(self):
        return [Request(
            url=self.start_url,
            callback=self.parse_page
        )]

    def parse_page(self, response):
        # print(f"PAGE URL: {response.url}")

        # Find all urls of articles
        for announcement_url in response.xpath("//article/descendant::a/@href").extract():
            # Make requests to those urls, parsing them
            yield Request(
                url=urljoin("https://makler.md", announcement_url),
                callback=self.parse
            )

        # Visit the next pages
        for pagination_url in response.xpath("//ul[@id='paginator_pagesList']/descendant::a/@href").extract():
            yield Request(
                url=urljoin(self.start_url, pagination_url),
                callback=self.parse_page
            )

    def parse(self, response):
        anouncement_name = response.xpath("//h1[@itemprop='name']/strong/text()").extract_first()
        announcement_telephone = response.xpath("//ul[@id='item_phones']/li/text()").extract_first()

        return {
            "announcement_name": anouncement_name,
            "announcement_telephone": announcement_telephone,
            "announcement_url": response.url,
        }
