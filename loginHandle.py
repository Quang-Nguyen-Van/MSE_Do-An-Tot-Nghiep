from login import Ui_Login
from PyQt5.QtWidgets import QMessageBox
import requests
import json

class LOGIN_HANDLE(Ui_Login):
    accessToken = ""
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

    def doLogin(self):
        username = self.txtUserName.text()
        passwd = self.txtPassword.text()
        header = {"accept": "*/*", "Content-Type": "application/json"}
        datas= {"userName": username, "password": passwd}
        
        response = requests.post("https://api.mhzppe.com/auth/login", data=json.dumps(datas), headers=header)
        if response.status_code == 201:
            self.accessToken = response.json()['accessToken']
            return True
            
        elif response.status_code == 403:
            self.showMessageInfo("Incorrect Username or Password!")
            return False
            
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