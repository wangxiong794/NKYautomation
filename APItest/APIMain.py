# coding=utf-8
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from APITest import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.window().show()
    ex = Ui_MainWindow()
    ex.setupUi(win)
    sys.exit(app.exec_())
