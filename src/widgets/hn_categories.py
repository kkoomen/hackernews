#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""


from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout
from widgets.hn_category import HackerNewsCategoryWidget

class HackerNewsCategoriesWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('padding: 10px; background-color: rgba(255, 255, 255, 0.05); border-bottom: 1px solid #aaa;')
        self.widgets = []

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        categories = [
            {
                'label': 'home',
                'path': 'news',
            },
            {
                'label': 'new',
                'path': 'newest',
            },
            {
                'label': 'past',
                'path': 'front',
            },
            {
                'label': 'ask',
                'path': 'ask',
            },
            {
                'label': 'show',
                'path': 'show',
            },
            {
                'label': 'jobs',
                'path': 'jobs',
            },
        ]
        for category in categories:
            widget = HackerNewsCategoryWidget(self, category)
            self.layout.addWidget(widget)
            self.widgets.append(widget)
        self.set_active_item('home')
        self.setLayout(self.layout)

    def set_active_item(self, label):
        for child in self.widgets:
            if child.category['label'] == label:
                child.setStyleSheet('background-color: #ff6600')
            else:
                child.setStyleSheet('')
