from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

def clean_text(value):
    return value.strip()


class BookLoader(ItemLoader):
    default_output_processor = TakeFirst()

    title_in = MapCompose(clean_text)
    price_in = MapCompose(clean_text)

