#coding:utf-8
import sys
import os

import scrapy
import urllib

from first.items import meizituItemSpider

reload(sys)
sys.setdefaultencoding('utf-8')

next_page_link=[]

def download(url):
	print url

	filename=url[-18:]
	path='I:/craw_pic/meizitu/'
	name=path+filename.replace('/','_')
	if not os.path.exists(name):
		urllib.urlretrieve(url,name)
	else:
		print 'this pic exists error'

class meizitu_spider(scrapy.Spider):

	name="meizitu_spider"
	start_urls=['http://www.meizitu.com/a/list_1_1.html']
	allow_urls=['www.meizitu.com']

	def parse(self,response):
		for i in response.xpath("//ul[@class='wp-list clearfix']/li/div/div/a/@href").extract():
			yield scrapy.Request(i,callback=self.parse_picture)

		pages_link=response.xpath("//div[@id='wp_page_numbers']/ul/li/a/@href").extract()
		full_page_link='http://www.meizitu.com/a/'+pages_link[-2]
		if full_page_link not in next_page_link:
			yield scrapy.Request(full_page_link,callback=self.parse)
		else:
			print '1111111111111111111'

	def parse_picture(self,response):
		item=meizituItemSpider()
		item['pic_name'] = response.selector.xpath("//title/text").extract()
		item['pic_url'] = response.selector.xpath("//div/p/img/@src").extract()
		yield item

		for url in item['pic_url']:
			download(url)
