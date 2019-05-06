import scrapy
import datetime

from ..items import ExchangeRateItem


class BankOfTaiwanSpider(scrapy.Spider):
    name = 'bank_of_taiwan'
    allowed_domains = ['rate.bot.com.tw']
    start_urls = ['https://rate.bot.com.tw/xrt?Lang=zh-TW']

    def parse(self, response):
        item = ExchangeRateItem()
        item['source'] = self.name
        item['currency'] = response.xpath(
            '/html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[1]/div/div[3]/text()').extract_first().strip()
        item['rate_buy'] = response.xpath(
            '/html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[2]/text()').extract_first()  # 現金買入
        item['rate_sell'] = response.xpath(
            '/html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()').extract_first()  # 現金賣出
        item['create_time'] = datetime.datetime.now()
        print(item['source'])
        print(item['currency'])
        print(item['rate_buy'])
        print(item['rate_sell'])
        print(item['create_time'])
        yield item
