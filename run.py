import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
# from apiHandle import API_HANDLE
import apiHandle
import requests
import json

from loginHandle import LOGIN_HANDLE
from mainHandle import MAIN_HANDLE

## Start UI class
class UI():
    accessToken = ""
    
    def __init__(self):
        self.mainUI = QMainWindow()
        self.mainHandle = MAIN_HANDLE(self.mainUI)
        # self.apiHandle = API_HANDLE()
        self.mainHandle.btnLogout.clicked.connect(lambda: self.loadLoginForm())
        
        self.loginUI = QMainWindow()
        if len(self.accessToken) == 0:
            self.loginHandle = LOGIN_HANDLE(self.loginUI)
        else:
            self.loadMainForm(1)
        # self.loginHandle.btnLogin.clicked.connect(lambda: self.loadMainForm(1))
                
        # self.loginHandle.btnLogin.clicked.connect(lambda: self.apiHandle.loginAPI(username, paswd))
        # self.loginHandle.txtPassword.returnPressed.connect(lambda: self.Login())
        
        self.loginHandle.btnLogin.clicked.connect(lambda: self.Login())
        self.loginHandle.txtPassword.returnPressed.connect(lambda: self.Login())
                
        self.loginUI.show()
                    
    def Login(self):
        username = self.loginHandle.txtUserName.text()
        paswd = self.loginHandle.txtPassword.text()
        
        isLogedin, self.accessToken = apiHandle.loginAPI(username, paswd)
        self.mainHandle.accessToken = self.accessToken
        # isLogedin = self.loginHandle.doLogin()
        if isLogedin:
            self.loadMainForm(1)            

    # def doLogin(self):
    #     username = self.loginHandle.txtUserName.text()
    #     passwd = self.loginHandle.txtPassword.text()
    #     header = {"accept": "*/*", "Content-Type": "application/json"}
    #     datas= {"userName": username, "password": passwd}
        
    #     response = requests.post("https://api.mhzppe.com/auth/login", data=json.dumps(datas), headers=header)
    #     # print(response.status_code)
    #     if response.status_code == 201:
    #         self.accessToken = response.json()['accessToken']
    #         # self.showMessageInfo(accessToken)
    #         self.loadMainForm(1)
            
    #     elif response.status_code == 403:
    #         self.showMessageInfo("Incorrect Username or Password!")
            
    # def showMessageInfo(self, message):
    #     msg = QMessageBox() 
    #     msg.setIcon(QMessageBox.Information)
        
    #     msg = QMessageBox() 
    #     msg.setIcon(QMessageBox.Information) 
        
    #     # setting message for Message Box 
    #     msg.setText(message) 
        
    #     # setting Message box window title 
    #     msg.setWindowTitle("Information MessageBox") 
        
    #     # declaring buttons on Message Box 
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
    #     retval = msg.exec_()
    
            
    def loadMainForm(self, data):        
        if len(self.accessToken) > 10:
            loaded, self.mainHandle.list_schedules = apiHandle.loadSchedules(self.accessToken)  
            if loaded:          
                self.mainHandle.loadSchedules()            
            
        self.loginUI.close()
        self.mainUI.show()

    def loadScheduleForm(self):                
        self.mainUI.close()
        self.scheduleUI.show()
        
    def loadLoginForm(self):
        self.accessToken = ""
        self.mainUI.hide()
        self.loginUI.show()
        
## End UI class



if __name__ == "__main__":
    app = QApplication([])    
    
    ui = UI()
    sys.exit(app.exec_())