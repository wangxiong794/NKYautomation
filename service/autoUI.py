# coding=utf-8
import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QPlainTextEdit
from service.page.matterApplyPage import matterApply
from service.logger import Log


class MyGui(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.thread = None  # 初始化线程
        self.log = Log()

    def initUI(self):
        # 主窗口
        self.window = QMainWindow()
        self.window.setWindowTitle('内控易自动化')
        self.window.resize(600, 400)
        self.window.move(300, 310)
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("点击开始，开始测试，请稍后！")
        self.textEdit.move(200, 25)
        self.textEdit.resize(350, 300)
        self.budgetApplication = QPushButton("事前申请",self.window)
        self.budgetApplication.setChecked(True)
        self.budgetApplication.move(50,50)
        self.budgetApplication.clicked[bool].connect(self.budgetApplicationTest1)

        self.reimburse = QPushButton('报销申请',self.window)
        self.reimburse.setChecked(True)
        self.reimburse.move(50, 100)
        self.reimburse.clicked[bool].connect(self.reimburseRun)

        self.contract = QPushButton('合同申请',self.window)
        self.contract.setChecked(True)
        self.contract.move(50, 150)
        self.contract.clicked[bool].connect(self.contractRun)

        self.matterApply = QPushButton('重要事项', self.window)
        self.matterApply.move(50, 400)
        self.matterApply.setChecked(True)
        self.matterApply.clicked[bool].connect(self.matterApplyRun)
        self.window.show()

    def budgetApplicationTest1(self):
        self.budgetApplication1 = QPushButton("事前申请1", self.window)
        self.budgetApplication1.setChecked(True)
        self.budgetApplication1.move(50, 200)
        self.budgetApplication1.clicked[bool].connect(self.budgetApplicationRun)

    def matterApplyRun(self):
        pass
        # self.thread = runMatterApplyThread()
        # self.thread.signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # self.thread.start()

    def budgetApplicationRun(self):
        pass

    def reimburseRun(self):
        pass

    def contractRun(self):
        pass

    def test1(self):
        self.thread = run_test1()
        self.thread.signal.connect(self.call_backlog)
        self.thread.start()

    def call_backlog(self, msg):
        self.textEdit.appendPlainText(msg)
        self.log.info(msg)


class run_test1(QtCore.QThread):
    _msg = pyqtSignal(str)

    def __init__(self):
        super(run_test1,self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        self._msg.emit('操作成功')

    @property
    def signal(self):
        return self._msg

class runMatterApplyThread(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(runMatterApplyThread, self).__init__()
        self.a = matterApply()

    def __del__(self):
        self.wait()

    def run(self):

        self._signal.emit('启动成功，开始打开浏览器')
        try:
            self.a.login()
            self._signal.emit('登录成功，正在开始退出')
            self.a.driver.quit()
            self._signal.emit('退出成功。耶')
        except:
            self.a.screenShot()
            self.a.driver.quit()
            self._signal.emit('项目超时，请检查原因后重试')

    @property
    def signal(self):
        return self._signal


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyGui()
    sys.exit(app.exec_())
