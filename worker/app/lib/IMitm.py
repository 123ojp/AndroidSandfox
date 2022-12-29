import docker,subprocess,time,random,os 
import traceback
import sys
class IMitm:
    def __init__(self):
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.IMAGE_NAME = 'abox-mitm'
        print(subprocess.run(["docker", "build","-t",self.IMAGE_NAME,'template/mitm'], check=True))
    def start(self,report_url):
        flag = 0
        while True:
            #if True:
            try:
                self.nowContainer = self.client.containers.run(self.IMAGE_NAME, 
                    detach=True,
                    environment=[
                        "REPORT_URL="+report_url,
                    ],
                    )
                break
            #else:
            except:
                print(traceback.format_exc())
                time.sleep(0.5)
                flag +=1
                if flag > 5:
                    raise BaseException("Docker api Error 5 times")
        print("IMITM Docker started id " ,self.nowContainer.id[:12], flush=True)
    def stop(self):
        self.nowContainer.stop()
        self.nowContainer.remove()

    