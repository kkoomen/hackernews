#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide2.QtGui import QFont
from signals.page import PageSignal

class HackerNewsItemWidget(QWidget):
    def __init__(self, parent, item):
        QWidget.__init__(self)
        self.parent = parent
        self.item = item
        self.mouseReleaseEvent = self.show

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(10, 10, 10, 10)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.title = QLabel(self.item['title'])
        self.title.setObjectName('title')
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setPointSize(16)
        self.title.setFont(titleFont)
        self.title.setWordWrap(True)
        self.layout.addWidget(self.title)

        labels = []
        if 'points' in self.item:
            labels.append(self.item['points'])
        if 'comments' in self.item:
            labels.append(self.item['comments'])
        if 'user' in self.item:
            labels.append('by {}'.format(self.item['user']['name']))
        labels = [label for label in labels if label]
        if len(labels) > 0:
            self.layout.addWidget(QLabel(' ･ '.join(labels)))

        self.setLayout(self.layout)

    def show(self, event):
        self.parent.set_active_item(self.item['id'])
        PageSignal.change(self.item['url'])
