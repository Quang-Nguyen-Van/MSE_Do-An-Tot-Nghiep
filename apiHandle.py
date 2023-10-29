import json
import requests

def loginAPI(userName, password):
    header = {"accept": "*/*", "Content-Type": "application/json"}
    datas= {"userName": userName, "password": password}
    
    response = requests.post("https://api.mhzppe.com/auth/login", data=json.dumps(datas), headers=header)
    if response.status_code == 201:
        response.json()['accessToken']
        return True, response.json()['accessToken']
        
    elif response.status_code == 403:
        return False, ''
    

def loadInUseSchedule(accessToken):
    
    header = {"accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {accessToken}"}

    response = requests.get("https://api.mhzppe.com/schedules/inUse", headers=header)

    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 403:
        return False, ""

def loadSchedules(accessToken):
    
    header = {"accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {accessToken}"}

    response = requests.get("https://api.mhzppe.com/schedules", headers=header)

    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 403:
        return False, "" 
    
def setSlotStatus(accessToken, slot_id, status):
    header = {"accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {accessToken}"}
    
    response = requests.patch("https://api.mhzppe.com/slot/"+ str(slot_id) +"/status?statusCode=" + str(status), headers=header)

    if response.status_code == 200:
        return True, response.json()
    else:
        return False, ""