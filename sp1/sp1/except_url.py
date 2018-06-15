##自定义去重规则
from scrapy.dupefilter import RFPDupeFilter    #默认的去重放在这里面，所以我们可以自己构造这个方法，然后放在setting中运行
                                            #DUPEFILTER_CLASS = 'sp1.except_url.RepURL'


class RepURL:
    def __init__(self):
        self.visited_url=set()

    @classmethod
    def from_settings(cls,settings):
        '''
        初始化时，调用
        :param settings:
        :return:
        '''
        return cls()

    def request_seen(self,request):
        """
        检测当前请求是否已经被访问过
        :param request:
        :return: True表示已经访问过；False表示未访问过
        """
        if request.url in self.visited_url:
            return True
        self.visited_url.add(request.url)
        return False

    def open(self):
        """
        开始爬去请求时，调用
        :return:
        """
        print('open replication')

    def close(self, reason):
        """
        结束爬虫爬取时，调用
        :param reason:
        :return:
        """
        print('close replication')

    def log(self, request, spider):
        """
        记录日志
        :param request:
        :param spider:
        :return:
        """
        print('repeat', request.url)

