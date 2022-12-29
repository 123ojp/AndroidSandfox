import requests
import os 
import time
from lib import *
import signal,traceback
import sys
BACKEND = os.environ.get('API_HOST')
WORKER_HOST = os.environ.get('WORKER_HOST')
WORKER_PROTOCOL = os.environ.get('WORKER_PROTOCOL')
WORKER_DOCKER_ID = os.environ.get('HOSTNAME')
DEBUG = os.environ.get('DEBUG')
ANDROID_START_TIMEOUT = int(os.environ.get('ANDROID_START_TIMEOUT'))
if not BACKEND:
    print("No Backend Found Termetate")
    exit(1)
worker_uuid = id_generator()
android = IAndroid()
wsScrcpy = IWsScrcpy()
mitm = IMitm()
frida = IFrida()
def signal_handler(sig, frame):
    print('Worker Exiting')
    stopeverything()
    sys.exit(0)
def stopeverything():
    print("Stoping Android Docker", flush=True)
    try:
        android.stop()
    except:
        pass
    print("Stoping ws scrcpy Docker", flush=True)
    try:
        wsScrcpy.stop()
    except:
        pass
    print("Stoping mitm Docker", flush=True)
    try:
        mitm.stop()
    except:
        pass
    print("Stoping frida Docker", flush=True)
    try:
        frida.stop()
    except:
        pass

signal.signal(signal.SIGINT, signal_handler)
print('='*25+"Everythings good Worker Wait Jobs"+'='*25, flush=True)
try:
    while True:
        #get job
        job = requests.get(BACKEND + 'worker/getjob/' + worker_uuid).json()
        if job['type'] != WorkerJobStatus.NEWJOB:
            print('\r'+job['msg'],end="")
            time.sleep(5)
            continue
        time.sleep(1)
        cjob = requests.get(BACKEND + 'worker/confirmjob/' + worker_uuid + '/' + str(job['msg']['app_id'])).json()
        print('\n',cjob['msg'])
        if cjob['type'] != WorkerJobStatus.ALLOCATE_JOB:
            print("Not mine job")
            continue
        #start wsScrcpy
        report_url = BACKEND+'worker/'+ str(job['msg']['app_id'])
        apk_url = BACKEND+ 'worker/uploads/apk/'+ job['msg']['uuid'] +'.apk'
        apk_id = job['msg']['name']
        update_url = BACKEND + 'worker/' + str(job['msg']['app_id']) +'/update'
        update_status_msg(update_url,"Starting MITM (0/4)")
        mitm.start( report_url )
        update_status_msg(update_url,"Starting Android (1/4)")
        android.start(mitm.nowContainer.id,hasMITM(update_url))
        update_status_msg(update_url,"Starting Android Viewer (2/4)")
        wsScrcpy.start(android.nowContainer.id)
        # start frida script donwload apk install apk
        update_status_msg(update_url,"Starting Frida (3/4)")
        frida.start(android.nowContainer.id,report_url,apk_url,apk_id)
        # post wsScrcpy url
        pdata = {
            'scrcpy_url': "http://"+WORKER_HOST+":" +str(wsScrcpy.port)+"/"
        }
        job = requests.post(update_url,data = pdata).json()
        #sleep util time up
        stop_time = int(job['msg']['job_start_time']) + job['msg']['job_alive_time']
        timeoutflag = False
        while stop_time >  int(time.time()):
            time.sleep(1)
            job = requests.get(BACKEND + 'worker/' + str(job['msg']['app_id']) + '/status').json()
            stop_time = int(job['msg']['job_start_time']) + job['msg']['job_alive_time']
            # check too long not start
            if job['msg']['status']<APPStatus.START and int(time.time()) - int(job['msg']['last_worker_time']) > ANDROID_START_TIMEOUT :
                print("Start timeout Stopping Job to init state", flush=True)
                update_status_msg(update_url,"Start timeout Stopping Job to init state")
                pdata = {
                    'status': APPStatus.WORKER_GOT
                }
                tmp = requests.post(update_url,data = pdata).json()
                stopeverything()
                timeoutflag =True
                break
            # if user call restart frida
            if job['msg']['status'] == APPStatus.FRIDA_RESTART:
                print("User requests restart app & frida", flush=True)
                update_status_msg(update_url,"Restarting Frida")
                try :
                    frida.stop()
                except:
                    pass
                frida.start(android.nowContainer.id,report_url,apk_url,apk_id)
                pdata = {
                    'status': APPStatus.START # or ALLOCATE?
                }
                job = requests.post(update_url,data = pdata).json()

        if timeoutflag :
            continue
        # stop when job_alive_time  
        # tell backend task stoped
        pdata = {
            'status': APPStatus.FINISH
        }
        tmp = requests.post(update_url,data = pdata).json()
        update_status_msg(update_url,"Stopping")
        print("Stopping Job", flush=True)
        stopeverything()
 
except:
    print(traceback.format_exc())
    stopeverything()
    #restart to init if possible
    pdata = {
                    'status': APPStatus.WORKER_GOT
                }
    tmp = requests.post(update_url,data = pdata).json()

