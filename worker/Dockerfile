FROM ubuntu:20.04
RUN apt update
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y install androguard python3 python3-pip docker docker-compose android-tools-adb 
COPY app/requirements.txt /requirements.txt 
RUN pip install -r  /requirements.txt

#COPY app /app
COPY run.sh /run.sh
RUN chmod +x /run.sh
ENTRYPOINT ["sh"]
CMD ["/run.sh"]