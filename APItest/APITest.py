# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APITest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.requestUI = QtWidgets.QFormLayout()
        self.requestUI.setObjectName("requestUI")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.requestUI.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.inName = QtWidgets.QLineEdit(self.centralwidget)
        self.inName.setObjectName("inName")
        self.requestUI.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inName)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.requestUI.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.inMethod = QtWidgets.QLineEdit(self.centralwidget)
        self.inMethod.setObjectName("inMethod")
        self.requestUI.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inMethod)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.requestUI.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.inKey = QtWidgets.QTextEdit(self.centralwidget)
        self.inKey.setObjectName("inKey")
        self.requestUI.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inKey)
        self.gridLayout.addLayout(self.requestUI, 0, 0, 1, 1)
        self.clearData = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearData.sizePolicy().hasHeightForWidth())
        self.clearData.setSizePolicy(sizePolicy)
        self.clearData.setMinimumSize(QtCore.QSize(0, 40))
        self.clearData.setObjectName("clearData")
        self.gridLayout.addWidget(self.clearData, 2, 1, 1, 1)
        self.responseUI = QtWidgets.QFormLayout()
        self.responseUI.setObjectName("responseUI")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.responseUI.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.outCode = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.outCode.sizePolicy().hasHeightForWidth())
        self.outCode.setSizePolicy(sizePolicy)
        self.outCode.setMinimumSize(QtCore.QSize(0, 0))
        self.outCode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.outCode.setObjectName("outCode")
        self.responseUI.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.outCode)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.responseUI.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.outData = QtWidgets.QListView(self.centralwidget)
        self.outData.setObjectName("outData")
        self.responseUI.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.outData)
        self.gridLayout.addLayout(self.responseUI, 0, 1, 1, 1)
        self.startTest = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTest.sizePolicy().hasHeightForWidth())
        self.startTest.setSizePolicy(sizePolicy)
        self.startTest.setMinimumSize(QtCore.QSize(0, 40))
        self.startTest.setObjectName("startTest")
        self.gridLayout.addWidget(self.startTest, 3, 1, 1, 1)
        self.stopConnection = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopConnection.sizePolicy().hasHeightForWidth())
        self.stopConnection.setSizePolicy(sizePolicy)
        self.stopConnection.setMinimumSize(QtCore.QSize(0, 40))
        self.stopConnection.setMaximumSize(QtCore.QSize(16777215, 40))
        self.stopConnection.setObjectName("stopConnection")
        self.gridLayout.addWidget(self.stopConnection, 2, 0, 1, 1)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.loginButton.setStyleSheet("")
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clearData.clicked.connect(self.inKey.clear)
        self.clearData.clicked.connect(self.outData.clearSelection)
        self.clearData.clicked.connect(self.outCode.clearSelection)
        self.clearData.clicked.connect(self.inName.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "内控易接口测试工具"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">接口名称：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请求方法：</span></p></body></html>"))
        self.inMethod.setText(_translate("MainWindow", "POST"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请求参数：</span></p></body></html>"))
        self.clearData.setText(_translate("MainWindow", "快速清空"))
        self.label_5.setText(_translate("MainWindow", "返回状态码："))
        self.label_6.setText(_translate("MainWindow", "返回数据："))
        self.startTest.setText(_translate("MainWindow", "开始测试"))
        self.stopConnection.setText(_translate("MainWindow", "断开链接"))
        self.loginButton.setText(_translate("MainWindow", "登录"))
