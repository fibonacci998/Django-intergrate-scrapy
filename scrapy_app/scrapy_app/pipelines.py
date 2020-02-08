from main.models import Quote
from pydispatch import dispatcher
from scrapy import signals

class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        quote = Quote(text=item.get('text'), author=item.get('author'))
        quote.unique_id = self.unique_id
        quote.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')
