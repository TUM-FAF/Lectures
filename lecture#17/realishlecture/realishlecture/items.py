import scrapy

class AndysCompany(scrapy.Item):
	url = scrapy.Field()
	name = scrapy.Field()
	desc = scrapy.Field()
	price = scrapy.Field()
	portion_weight = scrapy.Field()
