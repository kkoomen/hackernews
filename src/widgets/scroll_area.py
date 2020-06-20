#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


"""
TODO
"""

from PySide2.QtWidgets import QScrollArea


class ScrollArea(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setStyleSheet(
            """
            QScrollArea {
                position: absolute;
                border: 0;
            }
            QScrollBar:vertical {
                width: 8px;
            }
            QScrollBar:horizontal {
                height: 8px;
            }
            QScrollBar:vertical,
            QScrollBar:horizontal {
                border: none;
                background: none;
                border-radius: 0;
            }
            QScrollBar::handle:horizontal,
            QScrollBar::handle:vertical {
                background: #ff6600;
                border-radius: 4px;
            }
            """
        )
