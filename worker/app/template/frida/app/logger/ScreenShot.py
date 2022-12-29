import os,requests,subprocess,time,threading
REPORT_URL = os.environ.get('REPORT_URL') + '/screenshot'
class ScreenShot:
    def __init__(self):
        self.stopflag = False
    def mainThread(self): 
        time.sleep(1)
        while not self.stopflag:
            print(subprocess.run("adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > /tmp/screen.png", check=True,shell = True))
            files = {'file': open('/tmp/screen.png', 'rb')}
            print(requests.post(REPORT_URL,files=files).json())
            time.sleep(30)

    def stop(self):
        self.stopflag = True
    def start(self):
        t = threading.Thread(target = self.mainThread)
        t.start()

        

