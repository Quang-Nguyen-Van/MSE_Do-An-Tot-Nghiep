from schedule_details import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import requests, json


class SCHEDULE_DETAILS_HANDLE(Ui_MainWindow):
    user = ""
    accessToken = ""
        
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)
        self.tblDays.setColumnWidth(0, 20)
        self.tblDays.setColumnWidth(1, 80)
        self.tblDays.setColumnWidth(2, 60)
