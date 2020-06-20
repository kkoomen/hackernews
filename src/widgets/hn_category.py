#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel
from signals.overview import OverviewSignal

class HackerNewsCategoryWidget(QLabel):
    def __init__(self, parent, category):
        QLabel.__init__(self, category['label'])
        self.parent = parent
        self.category = category
        self.setAlignment(Qt.AlignCenter)
        self.mouseReleaseEvent = self.click_handler

    def click_handler(self, event):
        self.parent.set_active_item(self.category['label'])
        OverviewSignal.change(self.category['path'])
