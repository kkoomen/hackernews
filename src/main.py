#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et

import sys

from PySide2.QtCore import Slot
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QAction, QApplication, QMainWindow
from widgets.app import AppWidget


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle('Hacker News')
        self.resize(1440, 800)
        # self.setWindowState(Qt.WindowMaximized)
        # TODO: self.setWindowIcon()

        # Exit
        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.exit)

        # Add our main widget
        self.setCentralWidget(widget)

    @Slot()
    def exit(self, checked):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = AppWidget()
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())
