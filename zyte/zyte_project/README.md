# Scrapy Books Crawler with Zyte API

## Project Overview

This project is a web scraping crawler built with **Scrapy** that
extracts book data from the following web site:

https://books.toscrape.com/

The main goal of the project is to create a **web scraping
architecture** that integrates with the **Zyte API** for scalable and
reliable crawling.

The scraper collects book metadata and exports the results in
**compressed JSON Lines (`.jl.gz`) format**.

------------------------------------------------------------------------

# Features

-   Scrapy-based crawling architecture
-   Integration with Zyte API for browser rendering
-   Retry and error handling
-   Randomized Headers
-   Clean data extraction using Item Loaders
-   Export to compressed JSON Lines (`.jl.gz`)

------------------------------------------------------------------------

# Data Extracted

The spider collects the following fields for each book:

  Field          Description
  -------------- ----------------------------------------
  title          Book title
  price          Book price
  availability   Stock availability
  rating         Star rating into numeric value
  url            URL of the book page

Example:

``` json
{"title": "Black Dust", "price": "34.53", "availability": "In stock", "rating": 5, "url": "https://books.toscrape.com/catalogue/black-dust_976/index.html"}
```

------------------------------------------------------------------------

# Project Architecture

The project follows a modular structure to improve maintainability and
scalability.

    zyte_project
    │
    ├── items/        # Scrapy data models
    ├── loaders/      # Item loaders for data cleaning
    ├── middlewares/  # Middlewares
    ├── pipelines/    # Data processing
    ├── services/     # External API helpers (Zyte integration)
    ├── spiders/      # Crawler
    │
    └── settings.py   # Project configuration

### Design Principles

The project separates responsibilities across modules:

  Module        Responsibility
  ------------- ---------------------------------------
  items         Defines structured data models
  loaders       Normalizes and processes scraped data
  middlewares   Controls request/response behavior
  pipelines     Handles post-processing and storage
  services      Encapsulates third-party integrations
  spiders       Implements crawling and parsing logic

This architecture is similar to patterns used in **production scraping
systems**.

------------------------------------------------------------------------

# Zyte API Integration

The crawler integrates with Zyte using the `scrapy-zyte-api` package.

Requests can be routed through Zyte by adding metadata to Scrapy
requests.

(`services/zyte_client.py`):

``` python
def zyte_browser_request():
    return {
        "zyte_api": {
            "browserHtml": True
        }
    }
```

Usage inside the spider:

``` python
yield scrapy.Request(
    url,
    meta=zyte_browser_request()
)
```

This call Zyte to **render the page in a browser environment** before
returning the HTML.

------------------------------------------------------------------------

# Data Export

The project uses Scrapy's **Feed Export** feature to automatically
generate compressed output.

Configuration in `settings.py`:

``` python
FEEDS = {
    "data/books/run={execution_date}.jl.gz": {
        "format": "jsonlines",
        "encoding": "utf-8",
        "store_empty": False,
    }
}
```

Advantages:

-   JSON Lines format
-   gzip compression
-   partition by run date.

------------------------------------------------------------------------

# Error Handling and Reliability

The project includes retry logic for common scraping failures:

-   rate limiting
-   temporary server errors
-   infrastructure failures

Handled HTTP codes:

    429, 500, 502, 503, 504, 520, 521, 522, 524


------------------------------------------------------------------------

# Installation

Clone the repository:

    git clone <repository-url>
    cd zyte_project

Create a virtual environment:

    python -m venv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

# Environment Variables

Create a `.env` file and add your Zyte API key:

    ZYTE_API_KEY=your_api_key_here

The project uses `python-dotenv` to load environment variables.

------------------------------------------------------------------------

# Running the Spider

Run the crawler with:

    scrapy crawl books

After execution finishes, the output file will be available at:

    data/books.jl.gz

------------------------------------------------------------------------