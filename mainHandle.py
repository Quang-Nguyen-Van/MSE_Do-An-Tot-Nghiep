from main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
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
              
                            
    # def loadSchedules(self):
        
    #     header = {"accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {self.accessToken}"}

    #     response = requests.get("https://api.mhzppe.com/schedules", headers=header)
    #     # print(response.status_code)
    #     if response.status_code == 200:
    #         self.list_schedules = response.json()

    #         # print(self.list_schedules)
    #         nb_schedule = len(self.list_schedules)
    #         self.tblSchedule.setRowCount(nb_schedule)
    #         for row, schedule in enumerate(self.list_schedules):
    #             item = QtWidgets.QTableWidgetItem(str(schedule['id']))

    #             item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    #             self.tblSchedule.setItem(row, 0, item)
    #             item.setTextAlignment(Qt.AlignHCenter)
    #             item = QtWidgets.QTableWidgetItem(str(schedule['title']))

    #             item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    #             self.tblSchedule.setItem(row, 1, item)
                
    #             item = QtWidgets.QTableWidgetItem(str(schedule['description']))
    #             item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    #             self.tblSchedule.setItem(row, 2, item)
                
    #             item = QtWidgets.QTableWidgetItem(str(schedule['isActive']))
    #             item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    #             item.setTextAlignment(Qt.AlignHCenter)
    #             self.tblSchedule.setItem(row, 3, item)
                
    #             button = QtWidgets.QPushButton("Details")                
    #             button.setMaximumSize(QtCore.QSize(80, 30))
    #             button.setStyleSheet("QPushButton{\n"
    #                                         "    background-color:rgb(0, 209, 255);\n"
    #                                         "    border: none;\n"
    #                                         "    border-radius: 10px;\n"
    #                                         "    color: white;\n"
    #                                         "    font-weight: bold;\n"
    #                                         "}\n"
    #                                         "\n"
    #                                         "QPushButton::hover{\n"
    #                                         "    background-color:rgb(0, 170, 255);\n"
    #                                         "    border-radius: 10px\n"
    #                                         "}")
                
    #             button.clicked.connect(lambda: self.viewDetails(schedule['id']))
    #             self.tblSchedule.setCellWidget(row, 4, button)

            
    #     elif response.status_code == 403:
    #         self.showMessageInfo("Incorrect Username or Password!")    
            
    
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
            # # Get the row of the button clicked
            # row = self.tblSchedule.indexAt(button.pos()).row()

            # # Retrieve data for the selected row
            # id_item = self.tblSchedule.item(row, 0)
            # first_name_item = self.tblSchedule.item(row, 1)
            # last_name_item = self.tblSchedule.item(row, 2)

            # if id_item and first_name_item and last_name_item:
            #     id_value = id_item.text()
            #     first_name = first_name_item.text()
            #     last_name = last_name_item.text()

            #     # Implement your logic to view details here
            #     print(f"View details for ID: {id_value}, Name: {first_name} {last_name}")
    
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
                
                # layout = QtWidgets.QHBoxLayout()

                # saveButtonItem = QtWidgets.QPushButton('Save')
                # editButtonItem = QtWidgets.QPushButton('Edit')
                

                # self.tableWidget.setCellWidget(0, 4, cellWidget)
                
                button = QtWidgets.QPushButton("Play")                
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
                                            "    border-radius: 7px;\n"
                                            "}")
                
                button.clicked.connect(lambda: self.changeSlotStatus())
                self.scheduleHandle.tblSlot.setCellWidget(row, 4, button)
                
                # canCelbutton = QtWidgets.QPushButton("Cancel")                
                # canCelbutton.setMaximumSize(QtCore.QSize(70, 25))
                # canCelbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                # canCelbutton.setStyleSheet("QPushButton{\n"
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
                
                # canCelbutton.clicked.connect(lambda: self.changeSlotStatus())
                
                # layout.addWidget(button)
                # layout.addWidget(canCelbutton)

                # cellWidget = QtWidgets.QWidget()
                # cellWidget.setLayout(layout)
                
                # self.scheduleHandle.tblSlot.setCellWidget(row, 4, cellWidget)
                # self.scheduleHandle.tblSlot.setCellWidget(row, 4, canCelbutton)
                
    def changeSlotStatus(self):
        # Get the row of the button clicked
        button = self.scheduleHandle.tblSlot.sender()
        row = self.scheduleHandle.tblSlot.indexAt(button.pos()).row()

        # Retrieve data for the selected row
        slot_id = self.scheduleHandle.tblSlot.item(row, 0).text()
        slot_status = self.scheduleHandle.tblSlot.item(row, 3).text()
        
        updated, resp = apiHandle.setSlotStatus(self.accessToken, slot_id, 1)
        if updated:
            print(resp)
            statusStr = 'Cancel'
            if resp['status'] == 1:
                statusStr = "Active"
            elif resp['status'] == 2:
                statusStr = "Done"
            self.scheduleHandle.tblSlot.item(row, 3).setText(statusStr)

        # if id_item and first_name_item and last_name_item:
        #     id_value = id_item.text()
        #     first_name = first_name_item.text()
        #     last_name = last_name_item.text()

        #     # Implement your logic to view details here
        #     print(f"View details for ID: {id_value}, Name: {first_name} {last_name}")