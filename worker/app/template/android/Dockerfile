FROM  redroid/redroid:11.0.0-latest

ADD native-bridge.tar /
COPY build.prop  /system/build.prop 
COPY frida-server-15.1.27 /data/data/frida-server
#COPY mitm ca
COPY c8750f0d.0 /system/etc/security/cacerts/

