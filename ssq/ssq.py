#!/usr/bin/python2
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import re
import requests

__author__ = 'wendale'

_PREFIX = 'http://www.17500.cn/ssq/'


def execute():
    response = requests.get(_PREFIX + 'all.php')
    soup = BeautifulSoup(response.content)
    # print soup.prettify()
    all_url = soup.find_all('a', attrs={'href': re.compile('^details.php.')})
    for url in all_url:
        # print '%s: %s' % (url.string, url['href'])
        request_one(url.string[11:18], url['href'])
    print ''


def request_one(name, url):
    response = requests.get(_PREFIX + url)
    soup = BeautifulSoup(response.content)
    red_balls = soup.find_all('font', attrs={'color': 'red'})
    blue_ball = soup.find_all('font', attrs={'color': 'blue'})
    print name + ',' + \
          ','.join(ball.string for ball in filter(lambda ball: ball.string.isdigit(), red_balls)) + \
          ',' + blue_ball[0].string


if __name__ == '__main__':
    execute()