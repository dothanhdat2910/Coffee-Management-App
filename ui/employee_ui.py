# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_employee(object):
    def setupUi(self, employee):
        employee.setObjectName("employee")
        employee.resize(706, 434)
        employee.setStyleSheet("QPushButton#btn_b1{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b1:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b1:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_b2{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b2:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b2:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#btn_b3{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b3:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b3:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"QPushButton#btn_b4{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b4:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b4:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_b5{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b5:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b5:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_b6{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b6:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b6:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_b7{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b7:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b7:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"QPushButton#btn_b8{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b8:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b8:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"QPushButton#btn_b9{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b9:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b9:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_b10{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b10:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b10:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"QPushButton#btn_b11{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b11:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b11:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}\n"
"\n"
"QPushButton#btn_b12{\n"
"background-color: rgba(16, 30, 41, 240);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b12:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(16, 30, 41,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b12:hover{\n"
"backgound-color: rgba(16, 30, 41,200);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(employee)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 700, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
"border-radius: 5px;\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_b1 = QtWidgets.QPushButton(self.tab)
        self.btn_b1.setGeometry(QtCore.QRect(10, 10, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b1.setFont(font)
        self.btn_b1.setStyleSheet("")
        self.btn_b1.setObjectName("btn_b1")
        self.btn_b2 = QtWidgets.QPushButton(self.tab)
        self.btn_b2.setGeometry(QtCore.QRect(100, 10, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b2.setFont(font)
        self.btn_b2.setStyleSheet("")
        self.btn_b2.setObjectName("btn_b2")
        self.btn_b4 = QtWidgets.QPushButton(self.tab)
        self.btn_b4.setGeometry(QtCore.QRect(10, 90, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b4.setFont(font)
        self.btn_b4.setStyleSheet("")
        self.btn_b4.setObjectName("btn_b4")
        self.btn_b7 = QtWidgets.QPushButton(self.tab)
        self.btn_b7.setGeometry(QtCore.QRect(10, 170, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b7.setFont(font)
        self.btn_b7.setStyleSheet("")
        self.btn_b7.setObjectName("btn_b7")
        self.btn_b10 = QtWidgets.QPushButton(self.tab)
        self.btn_b10.setGeometry(QtCore.QRect(10, 250, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b10.setFont(font)
        self.btn_b10.setStyleSheet("")
        self.btn_b10.setObjectName("btn_b10")
        self.btn_b5 = QtWidgets.QPushButton(self.tab)
        self.btn_b5.setGeometry(QtCore.QRect(100, 90, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b5.setFont(font)
        self.btn_b5.setStyleSheet("")
        self.btn_b5.setObjectName("btn_b5")
        self.btn_b8 = QtWidgets.QPushButton(self.tab)
        self.btn_b8.setGeometry(QtCore.QRect(100, 170, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b8.setFont(font)
        self.btn_b8.setStyleSheet("")
        self.btn_b8.setObjectName("btn_b8")
        self.btn_b11 = QtWidgets.QPushButton(self.tab)
        self.btn_b11.setGeometry(QtCore.QRect(100, 250, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b11.setFont(font)
        self.btn_b11.setStyleSheet("")
        self.btn_b11.setObjectName("btn_b11")
        self.btn_b6 = QtWidgets.QPushButton(self.tab)
        self.btn_b6.setGeometry(QtCore.QRect(190, 90, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b6.setFont(font)
        self.btn_b6.setStyleSheet("")
        self.btn_b6.setObjectName("btn_b6")
        self.btn_b9 = QtWidgets.QPushButton(self.tab)
        self.btn_b9.setGeometry(QtCore.QRect(190, 170, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b9.setFont(font)
        self.btn_b9.setStyleSheet("")
        self.btn_b9.setObjectName("btn_b9")
        self.btn_b12 = QtWidgets.QPushButton(self.tab)
        self.btn_b12.setGeometry(QtCore.QRect(190, 250, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b12.setFont(font)
        self.btn_b12.setStyleSheet("")
        self.btn_b12.setObjectName("btn_b12")
        self.btn_b3 = QtWidgets.QPushButton(self.tab)
        self.btn_b3.setGeometry(QtCore.QRect(190, 10, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b3.setFont(font)
        self.btn_b3.setStyleSheet("")
        self.btn_b3.setObjectName("btn_b3")
        self.btn_tt = QtWidgets.QPushButton(self.tab)
        self.btn_tt.setGeometry(QtCore.QRect(550, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_tt.setFont(font)
        self.btn_tt.setStyleSheet("QPushButton#btn_tt{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_tt:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_tt:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_tt.setObjectName("btn_tt")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(280, 11, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.comboBox.setObjectName("comboBox")
        self.btn_add = QtWidgets.QPushButton(self.tab)
        self.btn_add.setGeometry(QtCore.QRect(610, 10, 75, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton#btn_add{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_add:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_add:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(550, 10, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.spinBox.setObjectName("spinBox")
        self.txt_b = QtWidgets.QLineEdit(self.tab)
        self.txt_b.setGeometry(QtCore.QRect(330, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_b.setFont(font)
        self.txt_b.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_b.setObjectName("txt_b")
        self.table_bill = QtWidgets.QTableWidget(self.tab)
        self.table_bill.setGeometry(QtCore.QRect(280, 80, 401, 241))
        self.table_bill.setMinimumSize(QtCore.QSize(401, 0))
        self.table_bill.setMaximumSize(QtCore.QSize(401, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.table_bill.setFont(font)
        self.table_bill.setStyleSheet("QTableWidget{\n"
"background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);\n"
"padding: 2px\n"
"}")
        self.table_bill.setObjectName("table_bill")
        self.table_bill.setColumnCount(4)
        self.table_bill.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_bill.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_bill.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_bill.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_bill.setHorizontalHeaderItem(3, item)
        self.btn_upd = QtWidgets.QPushButton(self.tab)
        self.btn_upd.setGeometry(QtCore.QRect(415, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_upd.setFont(font)
        self.btn_upd.setStyleSheet("QPushButton#btn_upd{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_upd:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_upd:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_upd.setObjectName("btn_upd")
        self.btn_xoa = QtWidgets.QPushButton(self.tab)
        self.btn_xoa.setGeometry(QtCore.QRect(280, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xoa.setFont(font)
        self.btn_xoa.setStyleSheet("QPushButton#btn_xoa{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_xoa:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_xoa:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_xoa.setObjectName("btn_xoa")
        self.txt_money = QtWidgets.QLineEdit(self.tab)
        self.txt_money.setGeometry(QtCore.QRect(570, 40, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_money.setFont(font)
        self.txt_money.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_money.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_money.setObjectName("txt_money")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(290, 40, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(480, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_b0 = QtWidgets.QPushButton(self.tab)
        self.btn_b0.setGeometry(QtCore.QRect(10, 330, 255, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b0.setFont(font)
        self.btn_b0.setStyleSheet("QPushButton#btn_b0{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_b0:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_b0:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_b0.setObjectName("btn_b0")
        self.btn_b2.raise_()
        self.btn_b4.raise_()
        self.btn_b7.raise_()
        self.btn_b10.raise_()
        self.btn_b5.raise_()
        self.btn_b8.raise_()
        self.btn_b11.raise_()
        self.btn_b6.raise_()
        self.btn_b9.raise_()
        self.btn_b12.raise_()
        self.btn_b3.raise_()
        self.btn_tt.raise_()
        self.comboBox.raise_()
        self.btn_add.raise_()
        self.spinBox.raise_()
        self.txt_b.raise_()
        self.table_bill.raise_()
        self.btn_upd.raise_()
        self.btn_xoa.raise_()
        self.txt_money.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btn_b0.raise_()
        self.btn_b1.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_logout = QtWidgets.QPushButton(self.tab_2)
        self.btn_logout.setGeometry(QtCore.QRect(310, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n"
"background-color: rgba(2, 65, 118, 255);\n"
"color: rgba(255,255,255,200);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btn_logout:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(2, 65, 118,100);\n"
"backgound-posotion:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_logout:hover{\n"
"backgound-color: rgba(2, 65, 118,200);\n"
"}")
        self.btn_logout.setObjectName("btn_logout")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(160, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(160, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(160, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txt_name = QtWidgets.QLineEdit(self.tab_2)
        self.txt_name.setGeometry(QtCore.QRect(260, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_name.setObjectName("txt_name")
        self.txt_phone = QtWidgets.QLineEdit(self.tab_2)
        self.txt_phone.setGeometry(QtCore.QRect(260, 90, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_phone.setFont(font)
        self.txt_phone.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_phone.setObjectName("txt_phone")
        self.txt_id = QtWidgets.QLineEdit(self.tab_2)
        self.txt_id.setGeometry(QtCore.QRect(260, 150, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_id.setFont(font)
        self.txt_id.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_id.setObjectName("txt_id")
        self.txt_pass = QtWidgets.QLineEdit(self.tab_2)
        self.txt_pass.setGeometry(QtCore.QRect(260, 210, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_pass.setFont(font)
        self.txt_pass.setStyleSheet("background-color: rgba(16, 30, 41, 240)  ;\n"
"color: rgba(255,255,255,200);")
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setObjectName("txt_pass")
        self.tabWidget.addTab(self.tab_2, "")
        employee.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(employee)
        self.statusbar.setObjectName("statusbar")
        employee.setStatusBar(self.statusbar)

        self.retranslateUi(employee)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(employee)

    def retranslateUi(self, employee):
        _translate = QtCore.QCoreApplication.translate
        employee.setWindowTitle(_translate("employee", "Nhân viên"))
        self.btn_b1.setText(_translate("employee", "BÀN 1"))
        self.btn_b2.setText(_translate("employee", "BÀN 2"))
        self.btn_b4.setText(_translate("employee", "BÀN 4"))
        self.btn_b7.setText(_translate("employee", "BÀN 7"))
        self.btn_b10.setText(_translate("employee", "BÀN 10"))
        self.btn_b5.setText(_translate("employee", "BÀN 5"))
        self.btn_b8.setText(_translate("employee", "BÀN 8"))
        self.btn_b11.setText(_translate("employee", "BÀN 11"))
        self.btn_b6.setText(_translate("employee", "BÀN 6"))
        self.btn_b9.setText(_translate("employee", "BÀN 9"))
        self.btn_b12.setText(_translate("employee", "BÀN 12"))
        self.btn_b3.setText(_translate("employee", "BÀN 3"))
        self.btn_tt.setText(_translate("employee", "Thanh toán"))
        self.btn_add.setText(_translate("employee", "Add"))
        self.txt_b.setToolTip(_translate("employee", "<html><head/><body><p align=\"center\"><br/>SDSD</p></body></html>"))
        self.txt_b.setWhatsThis(_translate("employee", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.table_bill.horizontalHeaderItem(0)
        item.setText(_translate("employee", "Món"))
        item = self.table_bill.horizontalHeaderItem(1)
        item.setText(_translate("employee", "Số lượng"))
        item = self.table_bill.horizontalHeaderItem(2)
        item.setText(_translate("employee", "Đơn giá"))
        item = self.table_bill.horizontalHeaderItem(3)
        item.setText(_translate("employee", "Chú thích"))
        self.btn_upd.setText(_translate("employee", "Cập nhật"))
        self.btn_xoa.setText(_translate("employee", "Xóa bill"))
        self.label.setText(_translate("employee", "Bàn"))
        self.label_2.setText(_translate("employee", "Tổng tiền"))
        self.btn_b0.setText(_translate("employee", "MANG VỀ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("employee", "Bán hàng"))
        self.btn_logout.setText(_translate("employee", "Đăng xuất"))
        self.label_3.setText(_translate("employee", "Tên:"))
        self.label_5.setText(_translate("employee", "SĐT:"))
        self.label_6.setText(_translate("employee", "ID:"))
        self.label_7.setText(_translate("employee", "Mật khẩu:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("employee", "Thông tin tài khoản"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    employee = QtWidgets.QMainWindow()
    ui = Ui_employee()
    ui.setupUi(employee)
    employee.show()
    sys.exit(app.exec_())