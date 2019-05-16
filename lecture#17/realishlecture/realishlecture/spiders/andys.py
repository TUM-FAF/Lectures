"""
Andy's Pizza Menu Scraper
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from realishlecture.items import AndysCompany
from realishlecture.itemloaders import AndysLoader


class AndysSpider(CrawlSpider):

	name = "andys"

	allowed_domains = ['andys.md']
	start_urls = ['https://www.andys.md/en/pages/menu/']

	rules = (
		Rule(LinkExtractor(allow = (r'\/en\/pages\/menu\/')), callback = 'parse_page', follow = True),
	)

	def parse_page(self, response):
		for menu_item in response.xpath("//*[contains(@id, 'mmmhd')]"):
			l = AndysLoader(item = AndysCompany(), selector = menu_item)

			l.add_value("url", response.url)

			l.add_xpath("name", "h5/text()")
			l.add_xpath("price", "descendant::*[@class = 'ands_price']/text()")

			l.add_xpath("portion_weight", "descendant::*[@class = 'bf_1']/text()", re = r"\((.+?)\)")
			l.add_xpath("desc", "descendant::*[@class = 'descr']/p[last() - 1]/text()")

			yield l.load_item()
