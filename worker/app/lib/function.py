import os,shutil, string, random,requests
def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def hasMITM(url):
    job = requests.post(url,data = {}).json()
    feature = job['msg']['hook_feature'].split(',')
    if 'mitm' in feature:
        return True
    return False

class WorkerJobStatus:
    NOJOB  = 0
    NEWJOB = 1
    ALLOCATE_JOB = 2
    NO_PERMISSION = 3

class APPStatus:
    INIT = 0
    WORKER_GOT = 1
    ALLOCATE = 2
    START = 3
    FRIDA_RESTART = 4
    FRIDA_DOWN = 5
    FINISH = 100
    FAIL = 999
    
def update_status_msg(update_url,msg):
    pdata = {
                    'status_msg': msg
                }
    job = requests.post(update_url,data = pdata).json()