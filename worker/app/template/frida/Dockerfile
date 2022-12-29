FROM ubuntu:20.04
RUN apt update
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y install androguard python3 python3-pip docker docker-compose android-tools-adb 
RUN apt -y install wget
COPY app/requirements.txt /requirements.txt 
RUN pip install -r  /requirements.txt
COPY app /app
WORKDIR /app
CMD /app/run.sh
