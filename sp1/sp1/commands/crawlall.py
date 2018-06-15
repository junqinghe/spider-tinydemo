from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list:
            # print(name)

            self.crawler_process.crawl(name, **opts.__dict__)
        self.crawler_process.start()


# 在settings.py 中添加配置 COMMANDS_MODULE = '项目名称.目录名称'
# 在项目目录执行命令：scrapy crawlall