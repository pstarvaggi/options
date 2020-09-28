from scrapy import Spider, Request
from options.items import OptionsItem
import datetime

class OptionsSpider(Spider):
	name = 'options_spider'
	allowed_urls = ['https://finance.yahoo.com']
	start_urls = ['https://finance.yahoo.com/quote/AAPL/options?p=AAPL']

	def parse(self, response):
		date_urls = response.xpath('//*[@id="Col1-1-OptionContracts-Proxy"]//select/option/@value').extract()
		date_urls = ['https://finance.yahoo.com/quote/AAPL/options?date='+timestamp+'&p=AAPL&straddle=false' for \
		timestamp in date_urls]

		for url in date_urls:
			yield Request(url = url, callback = self.parse_date_page)

	def parse_date_page(self, response):
		print(response)

	