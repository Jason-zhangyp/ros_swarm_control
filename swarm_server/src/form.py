# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 643)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(660, 0))
        Form.setMaximumSize(QtCore.QSize(660, 16777215))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.paramHorizontalLayout = QtWidgets.QHBoxLayout()
        self.paramHorizontalLayout.setObjectName("paramHorizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.paramHorizontalLayout.addWidget(self.label_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("LoadParamsButton")
        self.paramHorizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("SaveParamsButton")
        self.paramHorizontalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.paramHorizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.paramHorizontalLayout)
        self.MenuhorizontalLayout = QtWidgets.QHBoxLayout()
        self.MenuhorizontalLayout.setObjectName("MenuhorizontalLayout")
        self.SelectAllcheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.SelectAllcheckBox.sizePolicy().hasHeightForWidth())
        self.SelectAllcheckBox.setSizePolicy(sizePolicy)
        self.SelectAllcheckBox.setMaximumSize(QtCore.QSize(24, 24))
        self.SelectAllcheckBox.setShortcut("")
        self.SelectAllcheckBox.setCheckable(False)
        self.SelectAllcheckBox.setObjectName("SelectAllcheckBox")
        self.MenuhorizontalLayout.addWidget(self.SelectAllcheckBox)
        self.ConnectAllButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ConnectAllButton.setObjectName("ConnectAllButton")
        self.MenuhorizontalLayout.addWidget(self.ConnectAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.MenuhorizontalLayout.addItem(spacerItem1)
        self.ModeAllComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ModeAllComboBox.setObjectName("ModeAllComboBox")
        self.MenuhorizontalLayout.addWidget(self.ModeAllComboBox)
        self.ArmAllButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ArmAllButton.setObjectName("ArmAllButton")
        self.MenuhorizontalLayout.addWidget(self.ArmAllButton)
        self.DisarmAllButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DisarmAllButton.setObjectName("DisarmAllButton")
        self.MenuhorizontalLayout.addWidget(self.DisarmAllButton)
        self.verticalLayout.addLayout(self.MenuhorizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.AddhorizontalLayout = QtWidgets.QHBoxLayout()
        self.AddhorizontalLayout.setObjectName("AddhorizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.AddhorizontalLayout.addItem(spacerItem2)
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.AddhorizontalLayout.addWidget(self.addButton)
        self.dellButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dellButton.setObjectName("dellButton")
        self.AddhorizontalLayout.addWidget(self.dellButton)
        self.verticalLayout.addLayout(self.AddhorizontalLayout)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 520, 394, 109))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.OriginGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.OriginGridLayout.setObjectName("OriginGridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.OriginGridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.OriginGridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.OriginGridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.OriginPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OriginPushButton.setObjectName("OriginPushButton")
        self.OriginGridLayout.addWidget(self.OriginPushButton, 0, 2, 1, 1)

        self.LatSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.LatSpinBox.setDecimals(10)
        self.LatSpinBox.setMinimum(-90.0)
        self.LatSpinBox.setMaximum(90.0)
        self.LatSpinBox.setObjectName("LatSpinBox")
        self.OriginGridLayout.addWidget(self.LatSpinBox, 0, 1, 1, 1)
        self.LonSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.LonSpinBox.setDecimals(10)
        self.LonSpinBox.setMinimum(-180.0)
        self.LonSpinBox.setMaximum(180.0)
        self.LonSpinBox.setObjectName("LonSpinBox")
        self.OriginGridLayout.addWidget(self.LonSpinBox, 1, 1, 1, 1)
        self.AltSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.AltSpinBox.setDecimals(10)
        self.AltSpinBox.setMinimum(-100.0)
        self.AltSpinBox.setMaximum(120.0)
        self.AltSpinBox.setObjectName("AltSpinBox")
        self.OriginGridLayout.addWidget(self.AltSpinBox, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Swarm control"))
        self.label_6.setText(_translate("Form", "Params:"))
        self.pushButton_4.setText(_translate("Form", "open"))
        self.pushButton_3.setText(_translate("Form", "save"))
        self.SelectAllcheckBox.setText(_translate("Form", "CheckBox"))
        self.ConnectAllButton.setText(_translate("Form", "connect"))
        self.ArmAllButton.setText(_translate("Form", "Arm"))
        self.DisarmAllButton.setText(_translate("Form", "Disarm"))
        self.addButton.setText(_translate("Form", "Add"))
        self.dellButton.setText(_translate("Form", "Del"))
        self.label_5.setText(_translate("Form", "Alt:"))
        self.label_2.setText(_translate("Form", "Lon:"))
        self.label.setText(_translate("Form", "Lat:"))
        self.OriginPushButton.setText(_translate("Form", "Set origin"))

