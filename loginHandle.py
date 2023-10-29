from login import Ui_Login
from PyQt5.QtWidgets import QMessageBox
import requests
import json

class LOGIN_HANDLE(Ui_Login):
    accessToken = ""
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

    def showMessageInfo(self, message):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
        
        # setting message for Message Box 
        msg.setText(message) 
        
        # setting Message box window title 
        msg.setWindowTitle("Information MessageBox") 
        
        # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()