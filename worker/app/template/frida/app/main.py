# -*- coding: utf-8 -*-
from __future__ import print_function
import threading,os
import frida,time
from frida_tools.application import Reactor
from logger import *
_PackageName = os.environ.get('APK_ID')

# merge hook js code
jscode = ""
# walk through hook folder
job = requests.post(os.environ.get('REPORT_URL') +'/update',data = {}).json()
feature = job['msg']['hook_feature'].split(',')
for dirPath, dirNames, fileNames in os.walk("hook"):
    for f in fileNames:
        if not f.find('.js'):
            continue
        if not f.replace('.js','') in feature:
            continue
        if f.replace('.js','') =='Syscall' and 'BypassRoot' in  feature : #syscall's conflict BypassRoot file syscall
            continue
        js_path =  os.path.join(dirPath, f)
        with open(js_path) as fp:
            jscode += fp.read()
            jscode += "\n"

#f = open("/tmp/tmp.txt", "a")
#f.write(jscode)
#f.close()

def call_backend_started():
    update_url= os.environ.get('REPORT_URL')  + '/update'
    pdata = {
        'job_start_time':'a',
        'status':3
    }
    tmp = requests.post(update_url,data = pdata).json()
screen = ScreenShot()
class Application(object):
    def __init__(self):
        self._stop_requested = threading.Event()
        self._reactor = Reactor(run_until_return=lambda reactor: self._stop_requested.wait())
        frida_mgr = frida.get_device_manager()

        for tmpdevice in frida_mgr.enumerate_devices():
            if(tmpdevice.id == "android:5555"):
                self._device =tmpdevice
        self._sessions = set()

        self._device.on("child-added", lambda child: self._reactor.schedule(lambda: self._on_child_added(child)))
        self._device.on("child-removed", lambda child: self._reactor.schedule(lambda: self._on_child_removed(child)))
        self._device.on("output", lambda pid, fd, data: self._reactor.schedule(lambda: self._on_output(pid, fd, data)))

    def run(self):
        self._reactor.schedule(lambda: self._start())
        self._reactor.run()

    def _start(self):
        self.starttime = time.time()
        Logger.nlog("✔ Start app ("+_PackageName+")")
        call_backend_started()
        screen.start()
        pid = self._device.spawn([_PackageName])
        self._instrument(pid)

    def _stop_if_idle(self):
        if len(self._sessions) == 0:
            self._stop_requested.set()

    def _instrument(self, pid):
        Logger.nlog("✔ Frida Attach APP (pid={})".format(pid))
        import subprocess
        #callProcess = subprocess.Popen("adb shell strace -p "+str(pid)+"> /tmp/teest", shell=True)

        try:
            session = self._device.attach(pid)
        except Exception as e:
            Logger.nlog("Frida Error: {}".format(str(e)))
            return
        session.on("detached", lambda reason: self._reactor.schedule(lambda: self._on_detached(pid, session, reason)))
        print("✔ enable_child_gating()")
        session.enable_child_gating()
        print("✔ create_script()")
        script = session.create_script(jscode)
        script.on("message", lambda message, data: self._reactor.schedule(lambda: self._on_message(pid, message)))
        print("✔ load()")
        script.load()
        print("✔ resume(pid={})".format(pid))
        self._device.resume(pid)
        self._sessions.add(session)

    def _on_child_added(self, child):
        Logger.nlog("⚡ child_added: {}".format(child))
        self._instrument(child.pid)

    def _on_child_removed(self, child):
        Logger.nlog("⚡ child_removed: {}".format(child))

    def _on_output(self, pid, fd, data):
        print("⚡ output: pid={}, fd={}, data={}".format(pid, fd, repr(data)))

    def _on_detached(self, pid, session, reason):
        Logger.nlog("⚡ detached: pid={}, reason='{}'".format(pid, reason))
        self._sessions.remove(session)
        self._reactor.schedule(self._stop_if_idle, delay=0.5)
        screen.stop()
        if time.time() - self.starttime < 5:
            Logger.tags('stop immediately')

    def _on_message(self, pid, message):
        print("⚡ message: pid={}, payload={}".format(pid, message))
        if not message['type'] == 'error':
            Logger.analyzer(message['payload'])


app = Application()
app.run()