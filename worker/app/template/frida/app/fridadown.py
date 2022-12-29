from logger import *
import requests
Logger.nlog("× Frida Stoped")
update_url= os.environ.get('REPORT_URL')  + '/update'
pdata = {
    'status':5
}
tmp = requests.post(update_url,data = pdata).json()
