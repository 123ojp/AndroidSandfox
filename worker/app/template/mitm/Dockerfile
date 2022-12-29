FROM  mitmproxy/mitmproxy
RUN pip install requests
COPY keys/* /root/.mitmproxy/
COPY mitmHandler.py /home/mitmproxy/
CMD /bin/bash -c 'mitmdump -s /home/mitmproxy/mitmHandler.py'