import docker,subprocess,time,random,os 
import traceback
import sys
class IFrida:
    def __init__(self):
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.IMAGE_NAME = 'abox-frida'
        print(subprocess.run(["docker", "build","-t",self.IMAGE_NAME,'template/frida'], check=True))
    def start(self,android_id,report_url,apk_url,apk_id):
        flag = 0
        self.android_id = android_id
        while True:
            #if True:
            try:
                self.nowContainer = self.client.containers.run(self.IMAGE_NAME, 
                    detach=True,
                    environment=[
                        "REPORT_URL="+report_url,
                        "APK_URL="+apk_url,
                        "APK_ID="+apk_id,
                    ],
                    links={self.android_id:'android'},
                    volumes={
                        } 
                    )
                break
            #else:
            except:
                print(traceback.format_exc())
                time.sleep(0.5)
                flag +=1
                if flag > 5:
                    raise BaseException("Docker api Error 5 times")
        print("Frida Docker started id " ,self.nowContainer.id[:12], flush=True)
    def stop(self):
        self.nowContainer.stop()
        self.nowContainer.remove()

    