import docker,subprocess,time,random,os 
import traceback
import sys
class IWsScrcpy:
    def __init__(self):
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.getRandomPort()
        print(subprocess.run(["docker", "build","-t","wsscrcpy",'template/ws-scrcpy'], check=True))
    def start(self,android_id):
        self.android_id = android_id
        flag = 0
        while True:
            #if True:
            try:
                self.nowContainer = self.client.containers.run('wsscrcpy', 
                    ports={'8000/tcp': self.port},
                    detach=True,
                    links={self.android_id:'android'},
                    restart_policy={"Name": "always"},
                    privileged=True)
                break
            #else:
            except:
                print(traceback.format_exc())
                self.getRandomPort()
                time.sleep(0.5)
                flag +=1
                if flag > 5:
                    raise BaseException("Docker api Error 5 times")
        print("IWsScrcpy Docker started id " ,self.nowContainer.id[:12],"Port",self.port, flush=True)
        flag = 0
        while True:
            if flag > 5:
                raise BaseException("adb connect Error 5 times")
            exec_log = self.nowContainer.exec_run('adb connect android:5555')
            if str(exec_log).find('Connection refused') > 0:
                time.sleep(5)
                flag +=1
                continue
            break
        self.nowContainer.exec_run('adb root')
        print("IWsScrcpy Adb connected")
        
    def stop(self):
        self.nowContainer.stop()
        self.nowContainer.remove()
    def getRandomPort(self):
        self.port =  random.randint(int(os.environ.get('PORT_START')),int(os.environ.get('PORT_END')))

    