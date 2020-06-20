#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QVBoxLayout, QWidget
from signals.page import PageSignal
from widgets.scroll_area import ScrollArea


class ContentInnerWidget(QWidget):
    def __init__(self, container):
        QWidget.__init__(self, container)
        PageSignal.changed.connect(self.render)
        self.view = QWebEngineView()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.view)

        self.setLayout(self.layout)

    def render(self, url):
        self.view.load(QUrl(url))
        self.view.show()


class ContentWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        contentScrollArea = ScrollArea()
        contentScrollArea.setWidgetResizable(True)
        contentScrollArea.setWidget(ContentInnerWidget(contentScrollArea))

        self.layout.addWidget(contentScrollArea)
        self.setLayout(self.layout)
