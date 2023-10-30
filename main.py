# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        # MainWindow.resize(1024, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 800))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_header = QtWidgets.QFrame(self.centralwidget)
        self.frm_header.setMinimumSize(QtCore.QSize(800, 100))
        self.frm_header.setMaximumSize(QtCore.QSize(1024, 100))
        self.frm_header.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frm_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_header.setLineWidth(0)
        self.frm_header.setObjectName("frm_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frm_header)
        self.frame.setMinimumSize(QtCore.QSize(150, 35))
        self.frame.setMaximumSize(QtCore.QSize(200, 35))
        self.frame.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frm_header)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self.frm_header)
        self.frame_5.setMinimumSize(QtCore.QSize(150, 35))
        self.frame_5.setMaximumSize(QtCore.QSize(200, 35))
        self.frame_5.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.lbUser = QtWidgets.QLabel(self.frame_5)
        self.lbUser.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.lbUser.setText("")
        self.lbUser.setObjectName("lbUser")
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frm_header)
        self.frm_table = QtWidgets.QFrame(self.centralwidget)
        self.frm_table.setMinimumSize(QtCore.QSize(800, 150))
        self.frm_table.setMaximumSize(QtCore.QSize(1024, 300))
        self.frm_table.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frm_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_table.setLineWidth(0)
        self.frm_table.setObjectName("frm_table")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frm_table)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tblSchedule = QtWidgets.QTableWidget(self.frm_table)
        self.tblSchedule.setEnabled(True)
        self.tblSchedule.setMinimumSize(QtCore.QSize(0, 100))
        self.tblSchedule.setMaximumSize(QtCore.QSize(16777215, 300))
        self.tblSchedule.setMouseTracking(True)
        self.tblSchedule.setTabletTracking(True)
        self.tblSchedule.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tblSchedule.setAutoFillBackground(True)
        self.tblSchedule.setStyleSheet("QTableWidget {\n"
"    border-radius: 3px;\n"
"    border: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: left;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::Item {\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    color: #000;\n"
"    padding-left: 3px;\n"
"    \n"
"}")
        self.tblSchedule.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblSchedule.setLineWidth(0)
        self.tblSchedule.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tblSchedule.setAlternatingRowColors(True)
        self.tblSchedule.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblSchedule.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblSchedule.setShowGrid(False)
        self.tblSchedule.setGridStyle(QtCore.Qt.NoPen)
        self.tblSchedule.setCornerButtonEnabled(True)
        self.tblSchedule.setRowCount(5)
        self.tblSchedule.setColumnCount(5)
        self.tblSchedule.setObjectName("tblSchedule")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblSchedule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblSchedule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblSchedule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblSchedule.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblSchedule.setHorizontalHeaderItem(4, item)
        self.tblSchedule.horizontalHeader().setDefaultSectionSize(120)
        self.tblSchedule.horizontalHeader().setMinimumSectionSize(50)
        self.tblSchedule.horizontalHeader().setStretchLastSection(True)
        self.tblSchedule.verticalHeader().setVisible(False)
        self.tblSchedule.verticalHeader().setMinimumSectionSize(24)
        self.verticalLayout.addWidget(self.tblSchedule)
        self.verticalLayout_2.addWidget(self.frm_table)
        self.frm_button = QtWidgets.QFrame(self.centralwidget)
        self.frm_button.setMinimumSize(QtCore.QSize(800, 100))
        self.frm_button.setMaximumSize(QtCore.QSize(1024, 100))
        self.frm_button.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frm_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_button.setLineWidth(0)
        self.frm_button.setObjectName("frm_button")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_button)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnLogout = QtWidgets.QPushButton(self.frm_button)
        self.btnLogout.setMinimumSize(QtCore.QSize(80, 40))
        self.btnLogout.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogout.setFont(font)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 209, 255);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-radius: 10px\n"
"}")
        self.btnLogout.setObjectName("btnLogout")
        self.horizontalLayout_3.addWidget(self.btnLogout)
        self.verticalLayout_2.addWidget(self.frm_button)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.showFullScreen()
        # MainWindow.setWindowFlag(Qt.FramelessWindowHint)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "IRRIGATION SYSTEM"))
        item = self.tblSchedule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tblSchedule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tblSchedule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tblSchedule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Active"))
        item = self.tblSchedule.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Actions"))
        self.btnLogout.setText(_translate("MainWindow", "LOGOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
