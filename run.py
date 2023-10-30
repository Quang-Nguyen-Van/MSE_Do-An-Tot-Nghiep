import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

import apiHandle


from loginHandle import LOGIN_HANDLE
from mainHandle import MAIN_HANDLE

## Start UI class
class UI():
    accessToken = ""
    
    def __init__(self):
        self.mainUI = QMainWindow()
        self.mainHandle = MAIN_HANDLE(self.mainUI)

        self.mainHandle.btnLogout.clicked.connect(lambda: self.loadLoginForm())
        
        self.loginUI = QMainWindow()
        if len(self.accessToken) == 0:
            self.loginHandle = LOGIN_HANDLE(self.loginUI)
        else:
            self.loadMainForm(1)

        
        self.loginHandle.btnLogin.clicked.connect(lambda: self.Login())
        self.loginHandle.txtPassword.returnPressed.connect(lambda: self.Login())
                
        self.loginUI.show()
                    
    def Login(self):
        username = self.loginHandle.txtUserName.text()
        paswd = self.loginHandle.txtPassword.text()
        
        isLogedin, self.accessToken = apiHandle.loginAPI(username, paswd)
        self.mainHandle.accessToken = self.accessToken

        if isLogedin:
            self.loadMainForm(1)            

       
            
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
        self.loginUI.show()
        self.mainUI.close()
        
        
## End UI class



if __name__ == "__main__":
    app = QApplication([])    
    
    ui = UI()
    sys.exit(app.exec_())