import scrapy
from zyte_project.items.book_item import BookItem
from zyte_project.loaders.book_loader import BookLoader
from zyte_project.services.zyte_client import zyte_browser_request
from zyte_project.utils.headers import random_headers

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rating_translate={
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
    }
    headers=random_headers()

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(
                url,
                headers=self.headers,
                meta=zyte_browser_request()
            )

    def parse(self, response):
        books = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"][article[@class="product_pod"]]')
        base_url=self.start_urls[0] 
        for book in books:
            loader = BookLoader(item=BookItem(), selector=book)
            title = book.xpath("./article/h3/a/@title").get()
            price = book.xpath('./article/div/p[@class="price_color"]/text()').re_first(r"([\d\.\,]+)")
            availability = book.xpath('./article/div[@class="product_price"]/p[@class="instock availability"]/text()').getall()
            availability = "".join(availability).strip()

            rating = book.xpath('./article/p[contains(@class,"star-rating")]/@class').re_first(r"([A-z]+)$")

            url = book.xpath("./article/h3/a/@href").get()
            product_url= base_url+'catalogue/' + url

            loader.add_value("title", title)
            loader.add_value("price", price)
            loader.add_value("availability", availability)
            loader.add_value("rating", self.rating_translate.get(rating.lower(),rating))
            loader.add_value("url", product_url)
        

            yield loader.load_item()


        next_page = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page:
            page=f"{base_url}{next_page}" if 'catalogue' in next_page else f"{base_url}catalogue/{next_page}"
            yield response.follow(page, 
                                  callback=self.parse,
                                  headers=self.headers,
                                  meta=zyte_browser_request())