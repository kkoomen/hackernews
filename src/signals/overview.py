#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtCore import QObject, Signal


class OverviewObject(QObject):
    changed = Signal(dict)

    def __init__(self):
        QObject.__init__(self)

    def change(self, url):
        self.changed.emit(url)


OverviewSignal = OverviewObject()
