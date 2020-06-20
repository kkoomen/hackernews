#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtWidgets import QHBoxLayout, QWidget
from widgets.sidebar import SidebarWidget
from widgets.content import ContentWidget


class AppWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(SidebarWidget())
        self.layout.addWidget(ContentWidget())
        self.setLayout(self.layout)
