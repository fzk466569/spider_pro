#coding:utf-8
'''
Created on 2016年6月11日

@author: 12054
'''
from spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain():
    def __init__(self):#管理--下载--解析--输出
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url() and count<10:#如果有待爬去的url
            try:
                new_url=self.urls.get_new_url()#取出一个url
                print 'craw %d:%s' %(count,new_url)
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except:
                print 'craw filed'
            finally:
                count+=1
        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/link?url=K9LykNspoTTzGb_PewApXSZwc4yj8rwhWIa_MowQ4PYabRXSigir1yKwQ8-u1ZXjNH9yBou9_N9dvyroV-vh2a"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    print 'end'

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    