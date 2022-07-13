# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhangyz\OneDrive\2.科研工作\2021-08_广西地质灾害\公路滑坡风险监测预警系统示范平台\ui_echarts.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pyecharts.charts import Bar
from qgis.core import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1413, 1090)
        self.frame_1 = QtWidgets.QFrame(Form)
        self.frame_1.setGeometry(QtCore.QRect(10, 220, 463, 391))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.splitter_width = 2
        self.splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.splitter1.setHandleWidth(self.splitter_width)

        self.echart_1 = QWebEngineView()
        bar = Bar()
        bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
        # 也可以传入路径参数，如 bar.render("mycharts.html")
        # bar.render(r'Cbar.html')
        self.echart_1.load(QtCore.QUrl("https://www.baidu.com/"))

        self.splitter1.addWidget(self.echart_1)
        self.splitter1.setSizes([1, 13])


        # self.spliter1.addWidget(self.frame_1)
        # self.spliter1.addWidget(self.echart_1)

        # self.frame_2 = QtWidgets.QFrame(Form)
        # self.frame_2.setGeometry(QtCore.QRect(479, 220, 463, 391))
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        # self.frame_3 = QtWidgets.QFrame(Form)
        # self.frame_3.setGeometry(QtCore.QRect(948, 220, 463, 391))
        # self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_3.setObjectName("frame_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
