#!/usr/bin/python2
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import os
import re
import requests

__author__ = 'wendale'

_URL_QUEUE = []

_DONE = set()

def execute(host, dst):
    _URL_QUEUE.append('http://%s/' % host)
    if not os.path.exists(dst):
        os.makedirs(dst)
    crawle(host, dst)


def extract_path(url):
    pattern = re.compile(r'http://[^/]*(.*)')
    match = pattern.search(url)
    path = match.group(1) if match else None
    if '.' in path:
        items = path.split('/')
        return '/'.join(items[:-1]), items[-1]
    else:
        return path, 'index.htm'


def crawle(host, dst):
    while _URL_QUEUE:
        url = _URL_QUEUE.pop()
        # 记录已经爬取
        _DONE.add(url)
        try:
            response = requests.get(url)

            # 保存内容
            (path, file) = extract_path(url)
            if not os.path.exists(dst + path):
                os.makedirs(dst + path)
            with open('%s%s/%s' % (dst, path, file), 'w') as target:
                target.writelines(response.content.replace(host, 'localhost'))

            # 把页面内链添加到队列
            soup = BeautifulSoup(response.content)
            urls = soup.find_all('a', attrs={'href': re.compile(r'.*%s.*' % host)})
            for url in urls:
                if url['href'] not in _DONE:
                    _URL_QUEUE.append(url['href'])
        except Exception, e:
            print url

        print 'url:%d, done:%d' % (len(_URL_QUEUE), len(_DONE))


if __name__ == '__main__':
    execute('db-engines.com', 'db')

