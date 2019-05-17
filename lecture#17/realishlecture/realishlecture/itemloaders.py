from scrapy.loader import ItemLoader
from scrapy.loader.processors import *

class AndysLoader(ItemLoader):
	default_input_processor = MapCompose(str.strip)
	default_output_processor = TakeFirst()
