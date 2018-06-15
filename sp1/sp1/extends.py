from scrapy import signals

class MyExtension(object):   #记得在settings注册才能用
                                # EXTENSIONS = {
                                #     'sp1.extends.MyExtension':300,
                                # }
    def __init__(self,value):
        self.value=value

    @classmethod
    def from_crawler(cls,crawler):
        val=crawler.settings.getint('MMMM')
        ext=cls(val)

        #促发spider_opened信号时执行对象opened,函数,由于classmethod中，没有self，所以对象用ext
        crawler.signals.connect(ext.opened,signal=signals.spider_opened)
        # 促发spider_closed信号时执行对象closed,函数,由于classmethod中，没有self，所以对象用ext
        crawler.signals.connect(ext.closed, signal=signals.spider_opened)
        return ext

    def opened(self,spider):
        print('open')

    def closed(self,spider):
        print('close')


"""
各种信号：前面得加上signals.
			engine_started
			engine_stoped
			spider_idle     爬虫闲置的时候
			spider_closed
			spider_error
			request_scheduled   调度器开始的时候
			request_dropped
			response_received
			response_downloaded
			item_scraped
			item_drop
"""

