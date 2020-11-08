import scrapy


class CNBCspider(scrapy.Spider):
    name = "madmoney"
    start_urls = ['']
#sample link: https://www.cnbc.com/2020/08/06/cramers-lightning-round-virgin-galactic-requires-a-10-year-view.html
# yyyy/mm/dd + '/cramers-lightning-round'
