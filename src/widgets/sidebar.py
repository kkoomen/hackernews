#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QVBoxLayout, QWidget
from widgets.hn import HackerNewsWidget
from widgets.hn_categories import HackerNewsCategoriesWidget
from widgets.scroll_area import ScrollArea

class SidebarInnerWidget(QWidget):
    def __init__(self, container):
        QWidget.__init__(self, container)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.hn = HackerNewsWidget()
        self.hn.setStyleSheet('color: #aaa;')
        self.layout.addWidget(self.hn)

        self.layout.setAlignment(self.hn, Qt.AlignTop)
        self.setLayout(self.layout)


class SidebarWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setFixedWidth(450)

        self.layout.addWidget(HackerNewsCategoriesWidget())

        sidebarScrollArea = ScrollArea()
        sidebarScrollArea.setWidgetResizable(True)
        sidebarScrollArea.setWidget(SidebarInnerWidget(sidebarScrollArea))
        self.layout.addWidget(sidebarScrollArea)
        self.setLayout(self.layout)
