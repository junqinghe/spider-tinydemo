# -*- coding: utf-8 -*-

# Scrapy settings for sp1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#爬虫名称
BOT_NAME = 'sp1'

#爬虫应用路径
SPIDER_MODULES = ['sp1.spiders']
NEWSPIDER_MODULE = 'sp1.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sp1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

#请求并发数
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

#延迟下载秒数
#DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#单域名并发数 和单ip并发数
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否支持cookies
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
#用于查看当前爬虫信息，操作爬虫等
#使用telnet ip port，然后通过命令操作
# TELNETCONSOLE_ENABLED = True
# TELNETCONSOLE_HOST = '127.0.0.1'
# TELNETCONSOLE_PORT = [6023,]




# Override the default request headers:
#默认请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sp1.middlewares.Sp1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sp1.middlewares.Sp1DownloaderMiddleware': 543,
#}

# Enable or disable extensions
#自定义扩展，基于信号进行调用
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
#定义pipeline处理请求
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'sp1.pipelines.Sp1Pipeline': 300,    #数字是优先级，越小越优先
# }

#默认爬虫最大深度，需要自己设置
# DEPTH_LIMI=2



# 14. 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
# 先进先出，广度优先

# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# 15. 调度器队列
# SCHEDULER = 'scrapy.core.scheduler.Scheduler'
# from scrapy.core.scheduler import Scheduler


# 16. 访问URL去重
# DUPEFILTER_CLASS = 'step8_king.duplication.RepeatUrl'



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
##开始自动限速
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
##初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
##最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#平均每秒并发数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
##是否显示
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'




###############scrapy redis########

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
#
# from scrapy_redis.scheduler import Scheduler
# from scrapy_redis.queue import PriorityQueue
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'          # 默认使用优先级队列（默认），其他：PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
# SCHEDULER_QUEUE_KEY = '%(spider)s:requests'                         # 调度器中请求存放在redis中的key
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"                  # 对保存到redis中的数据进行序列化，默认使用pickle
# SCHEDULER_PERSIST = True                                            # 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空
# SCHEDULER_FLUSH_ON_START = False                                    # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
# SCHEDULER_IDLE_BEFORE_CLOSE = 10                                    # 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）。
# SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'                  # 去重规则，在redis中保存时对应的key
# SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'# 去重规则对应处理的类
#

from scrapy_redis.pipelines import RedisPipeline
# ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 300,
# }
# REDIS_ITEMS_KEY = '%(spider)s:items'
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

#
# REDIS_HOST = '10.211.55.13'                           # 主机名
# REDIS_PORT = 6379                                     # 端口
# # REDIS_URL = 'redis://user:pass@hostname:9001'       # 连接URL（优先于以上配置）
# # REDIS_PARAMS  = {}                                  # Redis连接参数             默认：REDIS_PARAMS = {'socket_timeout': 30,'socket_connect_timeout': 30,'retry_on_timeout': True,'encoding': REDIS_ENCODING,}）
# # REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient' # 指定连接Redis的Python模块  默认：redis.StrictRedis
# REDIS_ENCODING = "utf-8"                              # redis编码类型             默认：'utf-8'


############起始url###设置后爬虫那里不需要提供url了，它可自动去url里面取url进行爬虫，如爬虫baidu.py
# REDIS_START_URLS_AS_SET = False
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

