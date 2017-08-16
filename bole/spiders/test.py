# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from bole import items

class MySpider(RedisSpider):
    name = 'test'

    def parse(self,response):
        urls = response.xpath('//div[@id="archive"]/div/div[2]/p/a[1]/@href').extract()
        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first('')
        for url in urls:
            yield Request(url,callback=self.parse_info)
        if next_url != '':
            yield Request(next_url, callback=self.parse)

    def parse_info(self, response):
        # do stuff
        item = items.BoleItem()
        item['title'] = response.xpath('//h1/text()').extract_first()
        return item
