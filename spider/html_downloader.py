#coding:utf-8
'''
Created on 2016年6月11日

@author: 12054
'''
import urllib2

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

'''
url="http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000"
a=HtmlDownloader()
print a.download(url)
'''