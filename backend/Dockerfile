FROM python:3.8-alpine3.16
WORKDIR /app
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev g++ make
COPY app/requirements.txt /requirements.txt 
RUN pip install -r  /requirements.txt

# RUN apk --purge del .build-deps


COPY run.sh /run.sh
RUN chmod +x /run.sh
ENTRYPOINT ["sh"]
CMD ["/run.sh"]
