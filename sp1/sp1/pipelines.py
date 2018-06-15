# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

####可以放文件
class Sp1Pipeline(object):    #该类执行前要记得在setting中注册了才能用
    def process_item(self, item, spider):
        """

        :param item:   yield 回来的值
        :param spider:  是爬虫对象（ XiaohuaSpider(scrapy.Spider)或抽屉或其他的）
        :return:
        """
        print(item)
        return item

    @classmethod            #还有以下方法
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.getint('MMMM')
        print('执行from——crawler，实例化对象')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('关闭爬虫')

#####可以放数据库
from scrapy.exceptions import DropItem
class Sp2Pipeline(object):    #该类执行前要记得在setting中注册了才能用
    def process_item(self, item, spider):
        """

        :param item:   yield 回来的值
        :param spider:  是爬虫对象（XiaohuaSpider(scrapy.Spider)或抽屉或其他的）
        :return:
        """
        if spider.name=="chouti":
            pass

        print(item)
        #将item传递给下一个pipeline的process_item方法
        return item
        # return DropItem()  ##下一个pipeline的process_item方法就不再执行


    @classmethod            #还有以下方法
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.getint('MMMM')
        print('执行from——crawler，实例化对象')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('关闭爬虫')






"""Sp1Pipeline该类运行时
1.先检测是否有from_crawler(cls)方法，如果有先执行
    obj=类.from_crawler
    如果没有就
    obj=类()   #相当只是生成该对象
2.然后
    obj.open_spider()
    爬虫运行，并执行parse各种方法,一旦yield item，就反复执行
        process_item(）
3.再关闭爬虫
    执行close_spider
  
"""