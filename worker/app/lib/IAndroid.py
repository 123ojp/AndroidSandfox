import docker,subprocess,time,random,os,string

class IAndroid:
    def __init__(self):
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.getRandomPort()
        print(subprocess.run(["docker", "build","-t","android_sandbox_emu",'template/android'], check=True))
    def start(self,mitm_id,hasMITM):
        flag = 0
        while True:
            #if True:
            container = self.client.containers.get(mitm_id)
            ip_add = container.attrs['NetworkSettings']['IPAddress']
            self.conf = self.getporxyconf(ip_add)
            try:
                vol = {}
                if hasMITM:
                    vol[self.conf] = {'bind': '/data/system/users/0/settings_global.xml', 'mode': 'ro'}
                self.nowContainer = self.client.containers.run('android_sandbox_emu', 
                    #ports={'5555/tcp': self.port},
                    links={mitm_id:'mitm'},
                    detach=True,
                    privileged=True,
                    volumes=vol
                    )
                break
            #else:
            except:
                self.getRandomPort()
                time.sleep(0.5)
                flag +=1
                if flag > 5:
                    raise BaseException("Docker api Error 5 times")
        print("Android Docker started id " ,self.nowContainer.id[:12],"Port ",self.port, flush=True)
        time.sleep(5)
        flag = 0
        while True:
            if flag > 5:
                raise BaseException("Frida Error 5 times")
            try:
                self.nowContainer.exec_run('/data/data/frida-server',detach=True)
                check = str(self.nowContainer.exec_run('ps -A'))
                if check.find('frida')>0:
                    break
            except:
                time.sleep(5)
                flag +=1
                continue
        print("frida-server Started")
    def stop(self):
        self.nowContainer.stop()
        self.nowContainer.remove()
        os.remove(self.filename)
    def getRandomPort(self):
        self.port =  random.randint(int(os.environ.get('PORT_START')),int(os.environ.get('PORT_END')))
    def getporxyconf(self,ip):
        with open('template/android/setting.xml') as f:
            contents = f.read()
            f.close()
            self.filename =  "/tmp/abox/" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

            f = open(self.filename, "a")
            f.write(contents.replace('$HOST$',ip))
            f.close()
            return self.filename
                