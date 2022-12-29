FROM nginx:alpine
RUN apk add --update nodejs npm
RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-init
COPY nginx.conf  /etc/nginx/conf.d/default.conf  


COPY ./vue-project /app
WORKDIR  /app
RUN npm install
RUN npm run build
RUN cp -rf /app/dist/* /usr/share/nginx/html/ 
#COPY nginx.conf /etc/nginx/conf.d/
