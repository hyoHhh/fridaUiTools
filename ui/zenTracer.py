# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zenTracer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZenTracerDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(963, 678)
        self.gridLayout_7 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listClasses2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listClasses2.setMaximumSize(QtCore.QSize(16777215, 130))
        self.listClasses2.setObjectName("listClasses2")
        self.gridLayout_2.addWidget(self.listClasses2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtClassBreak = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtClassBreak.setObjectName("txtClassBreak")
        self.horizontalLayout_3.addWidget(self.txtClassBreak)
        self.btnClassBreakAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClassBreakAdd.setObjectName("btnClassBreakAdd")
        self.horizontalLayout_3.addWidget(self.btnClassBreakAdd)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtMethodBreak = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMethodBreak.setObjectName("txtMethodBreak")
        self.horizontalLayout_4.addWidget(self.txtMethodBreak)
        self.btnMethodBreakAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMethodBreakAdd.setObjectName("btnMethodBreakAdd")
        self.horizontalLayout_4.addWidget(self.btnMethodBreakAdd)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chkStack = QtWidgets.QCheckBox(self.groupBox_6)
        self.chkStack.setObjectName("chkStack")
        self.gridLayout_3.addWidget(self.chkStack, 0, 0, 1, 1)
        self.chkMatch = QtWidgets.QCheckBox(self.groupBox_6)
        self.chkMatch.setObjectName("chkMatch")
        self.gridLayout_3.addWidget(self.chkMatch, 0, 2, 1, 1)
        self.chkInit = QtWidgets.QCheckBox(self.groupBox_6)
        self.chkInit.setObjectName("chkInit")
        self.gridLayout_3.addWidget(self.chkInit, 0, 1, 1, 1)
        self.chkMatchMethod = QtWidgets.QCheckBox(self.groupBox_6)
        self.chkMatchMethod.setObjectName("chkMatchMethod")
        self.gridLayout_3.addWidget(self.chkMatchMethod, 0, 3, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 3, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabTracer = QtWidgets.QTableWidget(self.groupBox_3)
        self.tabTracer.setObjectName("tabTracer")
        self.tabTracer.setColumnCount(0)
        self.tabTracer.setRowCount(0)
        self.gridLayout_5.addWidget(self.tabTracer, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.cmbPackage = QtWidgets.QComboBox(self.groupBox_5)
        self.cmbPackage.setObjectName("cmbPackage")
        self.cmbPackage.addItem("")
        self.gridLayout_4.addWidget(self.cmbPackage, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnClassStringAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassStringAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassStringAdd.setObjectName("btnClassStringAdd")
        self.gridLayout_6.addWidget(self.btnClassStringAdd, 0, 1, 1, 1)
        self.btnClassFileAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassFileAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassFileAdd.setObjectName("btnClassFileAdd")
        self.gridLayout_6.addWidget(self.btnClassFileAdd, 0, 0, 1, 1)
        self.btnClassBundle = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassBundle.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassBundle.setObjectName("btnClassBundle")
        self.gridLayout_6.addWidget(self.btnClassBundle, 0, 3, 1, 1)
        self.btnClassBase64 = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassBase64.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassBase64.setObjectName("btnClassBase64")
        self.gridLayout_6.addWidget(self.btnClassBase64, 0, 4, 1, 1)
        self.btnClassStringBuilderAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassStringBuilderAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassStringBuilderAdd.setObjectName("btnClassStringBuilderAdd")
        self.gridLayout_6.addWidget(self.btnClassStringBuilderAdd, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtClass = QtWidgets.QLineEdit(self.groupBox)
        self.txtClass.setObjectName("txtClass")
        self.horizontalLayout.addWidget(self.txtClass)
        self.btnClassAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnClassAdd.setObjectName("btnClassAdd")
        self.horizontalLayout.addWidget(self.btnClassAdd)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listClasses1 = QtWidgets.QListWidget(self.groupBox)
        self.listClasses1.setMaximumSize(QtCore.QSize(16777215, 130))
        self.listClasses1.setObjectName("listClasses1")
        self.gridLayout.addWidget(self.listClasses1, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtMethod = QtWidgets.QLineEdit(self.groupBox)
        self.txtMethod.setObjectName("txtMethod")
        self.horizontalLayout_2.addWidget(self.txtMethod)
        self.btnMethodAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnMethodAdd.setObjectName("btnMethodAdd")
        self.horizontalLayout_2.addWidget(self.btnMethodAdd)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_7, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ZenTracer"))
        self.groupBox_2.setTitle(_translate("Dialog", "fbreak"))
        self.label_3.setText(_translate("Dialog", "类名："))
        self.btnClassBreakAdd.setText(_translate("Dialog", "添加"))
        self.label_4.setText(_translate("Dialog", "函数名："))
        self.btnMethodBreakAdd.setText(_translate("Dialog", "添加"))
        self.groupBox_6.setTitle(_translate("Dialog", "其他选项"))
        self.chkStack.setText(_translate("Dialog", "打印堆栈"))
        self.chkMatch.setText(_translate("Dialog", "模糊匹配类"))
        self.chkInit.setText(_translate("Dialog", "hook init"))
        self.chkMatchMethod.setText(_translate("Dialog", "模糊匹配函数"))
        self.groupBox_3.setTitle(_translate("Dialog", "结果"))
        self.groupBox_5.setTitle(_translate("Dialog", "进程缓存数据选择"))
        self.label_5.setText(_translate("Dialog", "进程："))
        self.cmbPackage.setItemText(0, _translate("Dialog", "选择缓存数据"))
        self.groupBox_4.setTitle(_translate("Dialog", "快捷操作"))
        self.btnClassStringAdd.setText(_translate("Dialog", "String"))
        self.btnClassFileAdd.setText(_translate("Dialog", "File"))
        self.btnClassBundle.setText(_translate("Dialog", "Bundle"))
        self.btnClassBase64.setText(_translate("Dialog", "Base64"))
        self.btnClassStringBuilderAdd.setText(_translate("Dialog", "StringBuilder"))
        self.groupBox.setTitle(_translate("Dialog", "trace"))
        self.label.setText(_translate("Dialog", "类名："))
        self.btnClassAdd.setText(_translate("Dialog", "添加"))
        self.label_2.setText(_translate("Dialog", "函数名："))
        self.btnMethodAdd.setText(_translate("Dialog", "添加"))
        self.groupBox_7.setTitle(_translate("Dialog", "提示"))
        self.label_7.setText(_translate("Dialog", "提示2、默认不hook构造函数，hook init则添加构造函数处理"))
        self.label_6.setText(_translate("Dialog", "提示1、添加函数必须设置对应的所属类，如果类未设置hook函数，则hook全部，如果设置了，则匹配出对应函数hook"))
        self.label_8.setText(_translate("Dialog", "提示3、默认非模糊匹配，必须完全一致的名称才hook，模糊匹配则无需填完整类名和函数名"))

