# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.selector import Selector
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    # start_urls = ['http://chouti.com/']
    cookie_dict={}
    url='https://dig.chouti.com/'
    def start_requests(self):  #该函数在这里修改了返回函数

        yield Request(url=self.url,callback=self.login)

    def login(self,response):
        from scrapy.http.cookies import CookieJar
        cookie_jar=CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value
        data={
            # 'phone':'86XXXXXXXXX',手机号
            # 'password':'woshiniba',
            # 'oneMonth':1,
        }

        from urllib.parse import urlencode

        yield Request(url='https://dig.chouti.com/login',
                      method='POST',
                      headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'},
                      body=urlencode(data),
                      cookies=self.cookie_dict,
                      callback=self.check_login)

    def check_login(self,response):  #因为登陆后返回的是一个字典数据，所以要再发送请求一次

        yield Request(url=self.url,
                      callback=self.parse3,
                      cookies=self.cookie_dict,
                      dont_filter=True  #因为这页面是第二次访问，并且第一次没有带cookie，现在再访问会被去重过滤掉，所以要先不用去重
                      )
    #
    def parse3(self,response):
        '''开始为所欲为了'''
        # link_num=Selector(response=response).xpath('//div[@class="part2"]/@share-linkid').extract()
        # print(link_num)
        # for item in link_num:
        #     vote_ip='https://dig.chouti.com/link/vote?linksId='+item
        #     print(vote_ip)
        #     yield Request(url=vote_ip,
        #                   method='POST',
        #                   cookies=self.cookie_dict,
        #                   callback=self.parse4
        #                   )

        page_num=Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_num:
            page_ip='https://dig.chouti.com'+page
            yield Request(url=page_ip,
                          cookies=self.cookie_dict,
                          callback=self.parse3
                          )
    def parse4(self, response):
        print(response.text)
        print('22222')