#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractproperty
from datetime import datetime


class Spider(ABC):
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def log(self, msg):
        print('{} [{}] {}'.format(datetime.now().astimezone().replace(microsecond=0).isoformat(), self.__class__.__name__, msg))

    def crawl(self, url):
        self.url = self.absolute_url(url)
        self.log(self.url)
        html = requests.get(self.url).text
        self.response = BeautifulSoup(html, 'html.parser')

    def absolute_url(self, path):
        return '{}/{}'.format(self.base_url, path.strip('/'))

    @abstractproperty
    def contents(self):
        raise NotImplementedError
