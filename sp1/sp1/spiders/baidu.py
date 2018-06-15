# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisSpider
class BaiduSpider(RedisSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']  #起始url自己去取redis里面取

    def parse(self, response):
        pass
