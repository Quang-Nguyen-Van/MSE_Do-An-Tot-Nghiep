from main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from qtwidgets import Toggle

from Utilities import modbus485

import serial as serial
from Utilities.softwaretimer import *
from Utilities.modbus485 import *
import Utilities.modbus485
from Utilities.togglebutton import *
# from mqtt import *
from Utilities.constant import *

import apiHandle
from schedule_detailsHandle import SCHEDULE_DETAILS_HANDLE


class MAIN_HANDLE(Ui_MainWindow):
    user = ""
    accessToken = ""
    list_schedules = ""
        
    def __init__(self, mainwindow):        
        super().__init__()
        self.setupUi(mainwindow)
        self.tblSchedule.setColumnWidth(0, 50)
        self.tblSchedule.setColumnWidth(1, 170)
        self.tblSchedule.setColumnWidth(2, 300)
        self.tblSchedule.setColumnWidth(3, 60)
        self.tblSchedule.setColumnWidth(4, 60)
        
        self.scheduleUI = QMainWindow()
        self.scheduleHandle = SCHEDULE_DETAILS_HANDLE(self.scheduleUI)
        self.scheduleHandle.btnBack.clicked.connect(lambda: self.scheduleUI.close())
        
    
    def loadSchedules(self):
        nb_schedule = len(self.list_schedules)
        self.tblSchedule.setRowCount(nb_schedule)
        for row, schedule in enumerate(self.list_schedules):
            item = QtWidgets.QTableWidgetItem(str(schedule['id']))

            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tblSchedule.setItem(row, 0, item)
            item.setTextAlignment(Qt.AlignCenter)
            item = QtWidgets.QTableWidgetItem(str(schedule['title']))

            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tblSchedule.setItem(row, 1, item)
            
            item = QtWidgets.QTableWidgetItem(str(schedule['description']))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tblSchedule.setItem(row, 2, item)
            
            item = QtWidgets.QTableWidgetItem(str(schedule['isActive']))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter)
            self.tblSchedule.setItem(row, 3, item)
            
            button = QtWidgets.QPushButton("Details")                
            button.setMaximumSize(QtCore.QSize(80, 30))
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button.setStyleSheet("QPushButton{\n"
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
            
            button.clicked.connect(lambda: self.viewDetails(schedule['id']))
            self.tblSchedule.setCellWidget(row, 4, button)            
          
    
    def viewDetails(self, schedule_id):
        button = self.tblSchedule.sender()
        if button:
            schedule = list(map(lambda x:x if x["id"] == schedule_id else "", self.list_schedules))
            schedule = list(filter(lambda x: len(x) > 0, schedule))[0]
            self.scheduleHandle.lblTitle.setText(schedule['title'])      
            self.scheduleHandle.lblDescription.setText(schedule['description'])
            self.scheduleHandle.chbxActive.setChecked(True)
            nb_day = len(schedule['days'])

            self.scheduleHandle.tblDays.setRowCount(nb_day)
            for row, day in enumerate(schedule['days']):                              
                item = QtWidgets.QTableWidgetItem(str(day['id']))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblDays.setItem(row, 0, item)
                item.setTextAlignment(Qt.AlignHCenter)
                
                item = QtWidgets.QTableWidgetItem(str(day['title']))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblDays.setItem(row, 1, item)
                item.setTextAlignment(Qt.AlignHCenter)
                
                button = QtWidgets.QPushButton("View")                
                button.setMaximumSize(QtCore.QSize(70, 25))
                button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                button.setStyleSheet("QPushButton{\n"
                                            "    background-color:rgb(0, 209, 255);\n"
                                            "    border: none;\n"
                                            "    border-radius: 7px;\n"
                                            "    color: white;\n"
                                            "    font-weight: bold;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::hover{\n"
                                            "    background-color:rgb(0, 170, 255);\n"
                                            "    border-radius: 7px\n"
                                            "}")
                
                button.clicked.connect(lambda: self.dayDetails(schedule['days']))
                self.scheduleHandle.tblDays.setCellWidget(row, 2, button)
            
            self.scheduleUI.show()    
    
    def dayDetails(self, days):     
        button = self.scheduleHandle.tblDays.sender()
        if button:
            row = self.scheduleHandle.tblDays.indexAt(button.pos()).row()
            day_id = self.scheduleHandle.tblDays.item(row, 0).text()
            day = list(map(lambda x:x if x["id"] == int(day_id) else "", days))
            day = list(filter(lambda x: len(x) > 0, day))

            self.scheduleHandle.tblSlot.clearContents()
            self.scheduleHandle.tblSlot.setRowCount(0)
            nb_slot = len(day[0]['slots'])
            self.scheduleHandle.tblSlot.setRowCount(nb_slot)
                    
            for row, slot in enumerate(day[0]['slots']):
                item = QtWidgets.QTableWidgetItem(str(slot['id']))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblSlot.setItem(row, 0, item)
                item.setTextAlignment(Qt.AlignHCenter)
                
                item = QtWidgets.QTableWidgetItem(str(slot['startTime']))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblSlot.setItem(row, 1, item)
                item.setTextAlignment(Qt.AlignHCenter)   
                
                item = QtWidgets.QTableWidgetItem(str(slot['endTime']))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblSlot.setItem(row, 2, item)
                item.setTextAlignment(Qt.AlignHCenter)
                
                statusStr = 'Cancel'
                
                if slot['status'] == 1:
                    statusStr = "Active"
                elif slot['status'] == 2:
                    statusStr = "Done"
                item = QtWidgets.QTableWidgetItem(statusStr)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.scheduleHandle.tblSlot.setItem(row, 3, item)
                item.setTextAlignment(Qt.AlignHCenter)
                
                # button = QtWidgets.QPushButton("Play")                
                # button.setMaximumSize(QtCore.QSize(70, 25))
                # button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                # button.setStyleSheet("QPushButton{\n"
                #                             "    background-color:rgb(0, 209, 255);\n"
                #                             "    border: none;\n"
                #                             "    border-radius: 7px;\n"
                #                             "    color: white;\n"
                #                             "    font-weight: bold;\n"
                #                             "}\n"
                #                             "\n"
                #                             "QPushButton::hover{\n"
                #                             "    background-color:rgb(0, 170, 255);\n"
                #                             "    border-radius: 7px;\n"
                #                             "}")
                
                # button.clicked.connect(lambda: self.changeSlotStatus())
                
                toggle = Toggle()
                toggle.clicked.connect(self.changeSlotStatus)
                
                self.scheduleHandle.tblSlot.setCellWidget(row, 4, toggle)                                
                
    def changeSlotStatus(self, emitted):
        # Get the row of the button clicked
        button = self.scheduleHandle.tblSlot.sender()
        row = self.scheduleHandle.tblSlot.indexAt(button.pos()).row()

        stt = 2
        if emitted:
            stt = 1
            
        ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)            
        m485 = Utilities.modbus485.Modbus485(ser)
        print("Button1 is click", stt)
        if stt == 1:
            m485.modbus485_send(relay1_ON)
        else:
            m485.modbus485_send(relay1_OFF)
        pass    
        # Retrieve data for the selected row
        slot_id = self.scheduleHandle.tblSlot.item(row, 0).text()
        slot_status = self.scheduleHandle.tblSlot.item(row, 3).text()
        
        updated, resp = apiHandle.setSlotStatus(self.accessToken, slot_id, stt)
        if updated:
            print(resp)
            statusStr = 'Cancel'
            if resp['status'] == 1:
                statusStr = "Running"
            elif resp['status'] == 2:
                statusStr = "Done"
            self.scheduleHandle.tblSlot.item(row, 3).setText(statusStr)
