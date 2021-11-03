# coding=utf-8
import sys

from PyQt5.QtWidgets import QApplication

from service.autoUI import MyGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyGui()
    sys.exit(app.exec_())