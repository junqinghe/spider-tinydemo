# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xioahua.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']
    # .xpath('//div[@class="index_img list_center"]')
    def parse(self, response):
        photo=Selector(response=response).xpath('//div[@class="index_img list_center"]/ul/li/a/@href').extract()
        print(photo)
        page_list=Selector(response=response).xpath('//div[@class="listpage"]/ol/li/a/@href').extract()
        for page in page_list:
            new_page="{0}/{1}".format('http://www.521609.com/daxuexiaohua',page)
            yield Request(url=new_page,callback=self.parse)





