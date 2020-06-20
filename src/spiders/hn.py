#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from .utils import Spider
import re


class HackerNewsSpider(Spider):
    def __init__(self, **kwargs):
        Spider.__init__(
            self, base_url='https://news.ycombinator.com', name='HackerNews', **kwargs)

    def crawl(self, url=''):
        Spider.crawl(self, url)

    @property
    def contents(self):
        overview = []
        for item in self.response.select('#hnmain .itemlist .athing'):
            title = item.contents.pop()
            storylink = title.select('.storylink')
            sibling = item.next_sibling.select('.subtext')
            site = title.select('.sitestr')
            user = sibling[0].select('.hnuser')

            page = { 'id': item.get('id') }

            if len(storylink) > 0:
                page['title'] = storylink[0].string
                page['url'] = storylink[0].get('href')

            if len(sibling) > 0:
                page['points'] = sibling[0].select('.score')[0].string if len(sibling[0].select('.score')) > 0 else None
                page['posted'] = sibling[0].select('.age')[0].string if len(sibling[0].select('.age')) > 0 else None
                page['comments'] = sibling[0].find(text=re.compile('\d+\xa0comments')).replace(u'\xa0', u' ') if sibling[0].find(text=re.compile('\d+\xa0comments')) else None
                page['detail_page'] = sibling[0].select('a[href^="item?id="]')[0].get('href') if len(sibling[0].select('a[href^="item?id="]')) > 0 else None

            if len(site) > 0:
                page['site'] = site[0].string if len(site) > 0 else None
                page['url'] = storylink[0].get('href')

            if len(user) > 0:
                page['user'] = {
                    'profile': user[0].get('href'),
                    'name': user[0].string,
                }
            overview.append(page)
        return overview
