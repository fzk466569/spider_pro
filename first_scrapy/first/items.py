from scrapy.item import Item, Field


class meizituItemSpider(Item):
    pic_name=Field()
    pic_url=Field()