from scrapy import Spider, Request
from options.items import OptionsItem
import datetime

class OptionsSpider(Spider):
    name = 'options_spider'
    allowed_urls = ['https://finance.yahoo.com']

    ticker = input('Please enter the ticker of the underlying stock\n').upper()
    
    start_urls = ['https://finance.yahoo.com/quote/'+ticker+'/options']

    def parse(self, response):
        date_urls = response.xpath('//*[@id="Col1-1-OptionContracts-Proxy"]//select/option/@value').extract()
        date_urls = ['https://finance.yahoo.com/quote/AAPL/options?date='+timestamp for \
        timestamp in date_urls]

        for url in date_urls:
            yield Request(url = url, callback = self.parse_date_page)

    def parse_date_page(self, response):
        calls = response.xpath('//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr')
        puts = response.xpath('//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[2]/div[2]/div/table/tbody/tr')

        for call in calls:
            item = OptionsItem()
            item['contract'] = call.xpath('./td[1]//text()').extract_first()
            item['last_trade'] = call.xpath('./td[2]//text()').extract_first()
            item['strike'] = call.xpath('./td[3]//text()').extract_first()
            item['last_price'] = call.xpath('./td[4]//text()').extract_first()
            item['bid'] = call.xpath('./td[5]//text()').extract_first()
            item['ask'] = call.xpath('./td[6]//text()').extract_first()
            item['change'] = call.xpath('./td[7]//text()').extract_first()
            item['pct_change'] = call.xpath('./td[8]//text()').extract_first()
            item['volume'] = call.xpath('./td[9]//text()').extract_first()
            item['open_int'] = call.xpath('./td[10]//text()').extract_first()
            item['imp_vol'] = call.xpath('./td[11]//text()').extract_first()
            yield item

        for put in puts:
            item = OptionsItem()
            item['contract'] = put.xpath('./td[1]//text()').extract_first()
            item['last_trade'] = put.xpath('./td[2]//text()').extract_first()
            item['strike'] = put.xpath('./td[3]//text()').extract_first()
            item['last_price'] = put.xpath('./td[4]//text()').extract_first()
            item['bid'] = put.xpath('./td[5]//text()').extract_first()
            item['ask'] = put.xpath('./td[6]//text()').extract_first()
            item['change'] = put.xpath('./td[7]//text()').extract_first()
            item['pct_change'] = put.xpath('./td[8]//text()').extract_first()
            item['volume'] = put.xpath('./td[9]//text()').extract_first()
            item['open_int'] = put.xpath('./td[10]//text()').extract_first()
            item['imp_vol'] = put.xpath('./td[11]//text()').extract_first()
            yield item


    