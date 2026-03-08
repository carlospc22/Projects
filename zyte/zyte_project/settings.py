import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

execution_date=date.today()

BOT_NAME = "zyte_project"

SPIDER_MODULES = ["zyte_project.spiders"]
NEWSPIDER_MODULE = "zyte_project.spiders"

DOWNLOADER_MIDDLEWARES = {

    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 633,

    "zyte_project.middlewares.zyte_error_handler.ZyteAPIErrorMiddleware": 700,
}

REQUEST_FINGERPRINTER_CLASS = "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
ADDONS = {}

ZYTE_API_KEY = os.getenv("ZYTE_API_KEY")

ZYTE_API_TRANSPARENT_MODE = True
ROBOTSTXT_OBEY = False

DOWNLOAD_TIMEOUT = 60
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 1


FEEDS = {
    f"data/books/run={execution_date}.jl.gz": {
        "format": "jsonlines",
        "encoding": "utf-8",
        "store_empty": False,
    }
}

RETRY_ENABLED = True
RETRY_TIMES = 5

RETRY_HTTP_CODES = [
    429,
    500,
    502,
    503,
    504,
    520,
    521,
    522,
    524
]


FEED_EXPORT_ENCODING = "utf-8"
