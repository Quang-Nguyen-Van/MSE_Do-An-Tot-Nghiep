# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vd1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 671, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtHoTen = QtWidgets.QTextEdit(self.groupBox)
        self.txtHoTen.setGeometry(QtCore.QRect(110, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtHoTen.setFont(font)
        self.txtHoTen.setObjectName("txtHoTen")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(396, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cbGioiTinh = QtWidgets.QComboBox(self.groupBox)
        self.cbGioiTinh.setGeometry(QtCore.QRect(490, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbGioiTinh.setFont(font)
        self.cbGioiTinh.setObjectName("cbGioiTinh")
        self.cbGioiTinh.addItem("")
        self.cbGioiTinh.addItem("")
        self.cbGioiTinh.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 671, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.chkCafe = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkCafe.setGeometry(QtCore.QRect(40, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chkCafe.setFont(font)
        self.chkCafe.setObjectName("chkCafe")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(310, 50, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.spinNguoiLon = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinNguoiLon.setGeometry(QtCore.QRect(140, 100, 42, 22))
        self.spinNguoiLon.setObjectName("spinNguoiLon")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 91, 16))
        self.label_5.setObjectName("label_5")
        self.spinTreEm = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinTreEm.setGeometry(QtCore.QRect(140, 150, 42, 22))
        self.spinTreEm.setObjectName("spinTreEm")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 480, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineTienTra = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTienTra.setGeometry(QtCore.QRect(290, 490, 201, 31))
        self.lineTienTra.setObjectName("lineTienTra")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 500, 31, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG ĐẶT VÉ"))
        self.groupBox.setTitle(_translate("MainWindow", "THÔNG TIN KHÁCH HÀNG"))
        self.label_2.setText(_translate("MainWindow", "HỌ TÊN"))
        self.label_3.setText(_translate("MainWindow", "GIỚI TÍNH"))
        self.cbGioiTinh.setItemText(0, _translate("MainWindow", "Nam"))
        self.cbGioiTinh.setItemText(1, _translate("MainWindow", "Nữ"))
        self.cbGioiTinh.setItemText(2, _translate("MainWindow", "BD"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DỊCH VỤ"))
        self.chkCafe.setText(_translate("MainWindow", "CAFE"))
        self.checkBox.setText(_translate("MainWindow", "SNACK"))
        self.label_4.setText(_translate("MainWindow", "NGƯỜI LỚN"))
        self.label_5.setText(_translate("MainWindow", "TRẺ EM"))
        self.pushButton.setText(_translate("MainWindow", "TIỀN TRẢ"))
        self.label_6.setText(_translate("MainWindow", "VND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())