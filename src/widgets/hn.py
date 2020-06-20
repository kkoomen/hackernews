#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtWidgets import QVBoxLayout, QWidget
from widgets.hn_item import HackerNewsItemWidget
from spiders.hn import HackerNewsSpider
from signals.overview import OverviewSignal


class HackerNewsWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.widgets = []

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        OverviewSignal.changed.connect(self.render)
        self.render()

    def render(self, url=''):
        spider = HackerNewsSpider()
        spider.crawl(url)
        for widget in self.widgets:
            self.layout.removeWidget(widget)
            widget.setParent(None)
        for item in spider.contents:
            child_widget = HackerNewsItemWidget(self, item)
            self.widgets.append(child_widget)
            self.layout.addWidget(child_widget)

    def set_active_item(self, id):
        for child in self.widgets:
            if child.item['id'] == id:
                child.setStyleSheet(
                    """
                    HackerNewsItemWidget {
                        border-left: 3px solid #ff6600;
                    }
                    HackerNewsItemWidget #title {
                        color: #fff;
                    }
                    """
                )
            else:
                child.setStyleSheet('')
