import os,requests
REPORT_URL = os.environ.get('REPORT_URL') + '/log'
FILE_LIST = []
NAT_LIST=[]
class Logger:
    def postLog(type,data):
        data = {
            'type':type,
            'data': data
        }
        requests.post(REPORT_URL,
            json = data
        ).text
    def log(msg):
        print(msg)
        Logger.postLog(msg['type'],msg['data'])
    def nlog(msg):
        print(msg)
        Logger.postLog('frida-msg',msg)
    def flog(msg):
        print(msg)
        Logger.postLog('frida-file',msg)
    def tags(msg):
        Logger.postLog('tags',msg)
    def analyzer(msg):
        global FILE_LIST
        if msg['type'] == 'open':
            if not msg['path'] in FILE_LIST:
                Logger.flog(msg['path'])
                FILE_LIST.append(msg['path'])
        elif msg['type'] in ['frida-faccessat','frida-java-exists']:
            if not msg['path'] in FILE_LIST:
                Logger.log(msg)
                FILE_LIST.append(msg['path'])
        elif msg['type'] =='root':
            Logger.tags("Root Detection")
        elif msg['type'].find('frida-Native-')>-1:
            data = str(msg['data']['value']) 
            if not data in NAT_LIST:
                Logger.log(msg)
                NAT_LIST.append(data)
        else :
            Logger.log(msg)
