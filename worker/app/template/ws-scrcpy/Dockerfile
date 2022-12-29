FROM alpine:3.14 AS builder
RUN apk add --no-cache nodejs npm python3 make g++ git
RUN cd / ; git clone https://github.com/NetrisTV/ws-scrcpy.git
WORKDIR /ws-scrcpy
RUN npm install
RUN npm run dist
WORKDIR dist
RUN npm install

FROM alpine:3.14 AS runner

RUN apk add --no-cache android-tools npm
COPY --from=builder /ws-scrcpy/dist /root/ws-scrcpy

WORKDIR /root/ws-scrcpy
COPY run.sh /run.sh
RUN chmod +x /run.sh
CMD '/run.sh'