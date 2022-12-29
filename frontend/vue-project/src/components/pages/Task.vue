<template>
  <div class="h-100 d-flex">

    <div class="row d-flex m-0 flex-fill">
      <div class="col-md-8 p-0 d-flex flex-column">

        <div class="resize-wrapper">
          <div class="resize-box" id="resize-box"></div>
          <div class="resize-line"></div>
          <div class="m-1 resize-real-content">
            <vue-good-table :columns="log_table" :rows="log" :sort-options="{
              enabled: true,
              initialSortBy: {field: 'id', type: 'asc'}
            }" :search-options="{
              enabled: true,
              searchFn: logSearchFun,
            }">
              <template slot="table-row" slot-scope="props">
                <span v-if="props.column.field == 'type'">
                    <span  v-for="(name, index) in props.row.type.split('-')">
                      <span v-if="index == 0" class="badge badge-secondary"> {{name}}</span>
                      <span v-else-if="index == 1" class="badge badge-success"> {{name}}</span>
                      <span v-else-if="index == 2" class="badge badge-info"> {{name}}</span>
                      <span v-else class="badge badge-info"> {{name}}</span>
                    </span> 
                </span>
                <span v-else-if="props.column.field == 'dataWtype'">
                  <span v-if="props.row.dataWtype.type == 'mitm-http'">
                    {{props.row.dataWtype.data.url}}
                    <b-button v-b-modal="'http_modal_'+props.row.id" class="float-right" variant="info">更多</b-button>
                    <b-modal :id="'http_modal_'+props.row.id" :title="props.row.dataWtype.data.url" size="xl">
                      <http-request :req="props.row.dataWtype.data.req_raw" :res="props.row.dataWtype.data.res_raw">
                      </http-request>
                    </b-modal>
                  </span>
                  <span v-else>
                    <span v-if="typeof(props.row.dataWtype.data) == 'object'">
                      <p class="m-0" v-for="(value, name, index) in props.row.dataWtype.data">
                        <span class="badge badge-light">{{name}} </span>: 
                        {{value}} 
                      </p>
                    </span>
                    <span v-else>
                      {{props.row.dataWtype.data}}
                    </span>
                  </span>
                </span>
                <span v-else>
                  {{props.formattedRow[props.column.field]}}
                </span>
              </template>
            </vue-good-table>

          </div>
        </div>
        <div class="flex-fill">
          <div class="tab-group">
            <input type="radio" id="tab1" name="tab" checked>
            <label for="tab1"><i class="fa fa-code"></i> Controller</label>
            <input type="radio" id="tab2" name="tab">
            <label for="tab2"><i class="fa fa-history"></i> Shell</label>
            <input type="radio" id="tab3" name="tab">
            <label for="tab3"><i class="fa fa-pencil"></i> File System</label>
            <input type="radio" id="tab4" name="tab">
            <label for="tab4"><i class="fa fa-share-alt"></i> Share</label>
            <div class="line"></div>
            <div class="content-container  bg-dark text-light">
              <div class="content" id="c1">
                <div class="d-flex align-items-center" style="padding: 10px;height: 100%;">
                  <b-row class="w-100">
                    <b-col cols="auto">
                      <b-img width="100%" class="round" :src="appicon" alt="Image 1"
                        onerror="this.onerror=null;this.src='https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg';">
                      </b-img>
                    </b-col>
                    <b-col>
                      <h5>APP 名稱 : {{ app.app_displayname }}</h5>
                      <p v-if="app.status==3">狀態 : Running</p>
                      <p v-else-if="app.status==100">狀態 : Finish</p>
                      <p v-else>狀態 : {{ app.status_msg }}</p>

                      <p>APP Package ID : {{ app.name }}</p>
                      <p>MD5 Hash : {{ app.md5 }}</p>
                    </b-col>
                    <b-col cols="auto" v-if="!isFinish">
                      <h5>剩餘時間 {{  Math.floor(remainTime/60) }} : {{ remainTime%60 }}</h5>

                      <b-button variant="danger" class="float-right" @click="stopTask">停止</b-button>
                      <b-button variant="info" :disabled="addTimeisDisabled" class="float-right" @click="addTime">增加 30
                        秒</b-button>
                      <br> <br>
                      <b-button variant="warning" :disabled="reStartAppDisabled" class="float-right"
                        @click="reStartApp">重啟APP & Frida</b-button>

                    </b-col>
                    <b-col cols="auto" v-if="isFinish">
                      <b-button variant="success" :disabled="reRunisDisabled" class="float-right" @click="reRunTask">
                        重新跑一次 </b-button>
                    </b-col>
                  </b-row>
                </div>
              </div>

              <div class="content" id="c2">
                <iframe v-if="!isFinish" id="android-tm" class="h-100 w-100" :src="tmurl"></iframe>
                <div v-if="isFinish" class="finishcover">
                  <div class="finishcover-message">Disconnect</div>
                </div>
              </div>
              <div class="content" id="c3">
                <iframe v-if="!isFinish" id="android-fs" class="h-100 w-100" :src="fsystemurl"></iframe>
                <div v-if="isFinish" class="finishcover">
                  <div class="finishcover-message">Disconnect</div>
                </div>
              </div>

              <div class="content m-2" id="c4">
                <h3>Share</h3>
                <p>This product is currently not shareable.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="wrap col-md-4" style="background-color: hsl(0deg 0% 85%);">

        <iframe v-if="!isFinish" id="android-screen" class="frame" :src="screenurl"></iframe>
        <vueper-slides v-if="isFinish" :touchable="false" fade fractions progress autoplay>
          <vueper-slide v-for="(pic, i) in screen" :key="i" :title="convertUnixTime(pic.created_date)"
            :image="getScreenFullpath(pic.path)">
          </vueper-slide>
        </vueper-slides>
      </div>


    </div>
  </div>
</template>
<script>
  import {
    mapGetters,
    mapActions
  } from 'vuex'

  import HttpRequest from './HttpRequest.vue'
  import {
    VueperSlides,
    VueperSlide
  } from 'vueperslides'
  import 'vueperslides/dist/vueperslides.css'
  export default {
    components: {
      HttpRequest,
      VueperSlides,
      VueperSlide
    },
    data() {
      return {
        baseurl: "",
        screenurl: null,
        fsystemurl: null,
        tmurl: null,
        reload_last_time: 0,
        id: 0,
        app: null,
        firstLoadID: 0,
        isFinish: false,
        remainTime: 0,
        addTimeisDisabled: false,
        logIntervalTimer: null,
        log: null,
        appicon: null,
        screen: null,
        reRunisDisabled: false,
        reStartAppDisabled: false,
        log_table: [{
            label: 'ID',
            field: 'id',
            type: 'number',
            firstSortType: 'desc',
            width: '15px',
          },
          {
            label: 'Created On',
            field: 'created_date',
            formatFn: this.convertUnixTime,
            width: '60px',
          },
          {
            label: 'Type',
            field: 'type',
            width: '70px',

          },
          {
            label: 'Data',
            field: 'dataWtype',
            sortable: false,
            width: '55%',
          },
        ]
      }
    },
    created: function () {
      this.id = this.$route.params.id;
      this.getInfo()
      //Listen size change then reload iframe for terminal iframe
      setTimeout(() => {
        const elem = document.querySelector('#resize-box');
        new ResizeObserver(this.reloadiframe).observe(elem)
      }, 100)
      this.firstLoadID = setInterval(() => {
        this.getInfo()
      }, 1000)
      this.$swal("載入中", "請稍候");


    },
    beforeDestroy() {
      clearInterval(this.firstLoadID)
      clearInterval(this.logIntervalTimer)

    },
    watch: {
      '$route'(to, from) { // change id
        this.app = null;
        this.log = null;
        this.isFinish = false;
        this.screen = null;
        this.id = to.params.id;
        if (this.firstLoadID) {
          window.clearInterval(this.firstLoadID);
        }
        this.firstLoadID = setInterval(() => {
          this.getInfo()
        }, 1000)
        this.$swal("載入中", "請稍候");
      }
    },
    methods: {
      ...mapActions([
        'actionSetLoginInfo',
      ]),
      logSearchFun(row, col, cellValue, searchTerm) {
        console.log(row)
        return JSON.stringify(cellValue).toLowerCase().includes(searchTerm.toLowerCase());

      },
      getScreenFullpath(path) {
        return this.$HOST + 'app/uploads/screenshot/' + path
      },
      convertUnixTime(time) {
        let milliseconds = time * 1000
        let dateObject = new Date(milliseconds)
        return dateObject.toLocaleString()
      },
      reStartApp() {
        var RESTART_API = this.$HOST + "app/" + this.id + "/restart";
        this.reStartAppDisabled = true;
        this.$http.get(RESTART_API)
          .then((response) => {
            if (response.status == 200) {
              if (this.firstLoadID) {
                window.clearInterval(this.firstLoadID);
              }
              this.firstLoadID = setInterval(() => {
                this.getInfo()
              }, 1000)

            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      reRunTask() {
        var RERUN_API = this.$HOST + "app/" + this.id + "/rerun";
        this.reRunisDisabled = true;
        this.$http.get(RERUN_API)
          .then((response) => {
            if (response.status == 200) {
              this.$router.push("/task/" + response.body.id)
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      stopTask() {
        var STOP_API = this.$HOST + "app/" + this.id + "/stop";
        this.$http.get(STOP_API)
          .then((response) => {
            if (response.status == 200) {
              this.isFinish = true;
              this.remainTime = 0
              this.$swal("成功!", "已停止 Sandbox", "success");
              this.getScreen();
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      addTime() {
        this.addTimeisDisabled = true;
        var ADDTIME_API = this.$HOST + "app/" + this.id + "/addtime";
        this.$http.get(ADDTIME_API)
          .then((response) => {
            if (response.body.status == 200) {
              this.app = response.body.msg;
              this.loadPage();
              this.$swal("成功!", "以增加三十秒", "success");
              this.addTimeisDisabled = false;
            } else {
              this.$swal("錯誤!", JSON.stringify(response.body.msg), "error");
              addTimeisDisabled = true;
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body.msg), "error");

          })
          .finally(() => {});
      },
      reloadiframe() {
        var now = Math.round((new Date()).getTime() / 1000);
        if (now - this.reload_last_time < 1) {
          return;
        }
        this.reload_last_time = now
        
        this.tmurl = ""
        setTimeout(() => {
          this.tmurl = this.tmurl_org
        }, 100)
      },
      getInfo() {
        var INFO_API = this.$HOST + "app/" + this.id + "/status";
        this.$http.get(INFO_API)
          .then((response) => {
            if (response.status == 200) {
              if (!this.app) {
                this.$swal.close()
              }
              this.app = response.body.msg;
              this.loadPage();
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      getLog() {
        var LOG_API = this.$HOST + "app/" + this.id + "/log";
        this.$http.get(LOG_API)
          .then((response) => {
            if (response.status == 200) {
              this.log = response.body.msg;
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      getScreen() {
        var LOG_API = this.$HOST + "app/" + this.id + "/screen";
        this.$http.get(LOG_API)
          .then((response) => {
            if (response.status == 200) {
              this.screen = response.body.msg;
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }
          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});
      },
      loadPage() {
        this.appicon = this.$HOST + "app/uploads/icon/" + this.app.uuid + ".png"
        if (this.app.status > 2 && this.app.status < 100) {
          if (this.app.status != 4) {
            this.reStartAppDisabled = false;
            window.clearInterval(this.firstLoadID);
            this.tmurl = ""
            this.screenurl = ""
            this.fsystemurl = ""
            setTimeout(() => {
              this.baseurl = this.app.scrcpy_url;
              const url = new URL(this.baseurl);
              this.screenurl =
                `${url}#!action=stream&udid=android%3A5555&player=mse&ws=ws%3A%2F%2F${url.host}%2F%3Faction%3Dproxy-adb%26remote%3Dtcp%253A8886%26udid%3Dandroid%253A5555`
              this.fsystemurl = `${url}#!action=list-files&udid=android%3A5555&path=%2F`;
              this.tmurl_org = `${url}#!action=shell&udid=android%3A5555`;
              this.tmurl = this.tmurl_org;
            }, 100)
          }

          this.$swal.close()
          this.baseurl = this.app.scrcpy_url;
          const url = new URL(this.baseurl);

          this.remainTime = this.app.job_start_time - Math.floor(Date.now() / 1000) + this.app.job_alive_time
          //start log Timer
          if (this.logIntervalTimer) {
            window.clearInterval(this.logIntervalTimer);
          }
          this.logIntervalTimer = setInterval(() => {
            this.getLog();
            this.remainTime -= 1
            if (this.remainTime < 0) {
              this.getInfo()
              this.remainTime = 0
            }
          }, 1000)
        } else if (this.app.status < 3) {
          this.$swal({
            title: "Android Docker 初始化中",
            text: this.app.status_msg,
          });
        } else {
          window.clearInterval(this.firstLoadID);
          if (this.logIntervalTimer) {
            window.clearInterval(this.logIntervalTimer);
          }
          this.isFinish = true;
          this.remainTime = 0;
          this.getLog();
          this.getScreen();
        }

      },
    }
  }

</script>

<style type="text/css" media="screen">
  .wrap {
    overflow: hidden;
  }

  .frame {
    width: 101% !important;
    height: 115% !important;
    border: 0;
    transform: scale(1);

    -ms-transform-origin: 0 0;
    -moz-transform-origin: 0 0;
    -o-transform-origin: 0 0;
    -webkit-transform-origin: 0 0;
    transform-origin: 0 0;
  }

  .resize-wrapper {
    position: relative;
  }

  .resize-wrapper .resize-box {
    width: inherit;
    height: 30em;
    /* 條初始高度 越多越低 */
    resize: vertical;
    cursor: row-resize;
    opacity: 0;
    overflow: scroll;
  }

  .resize-wrapper .resize-real-content {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 4px;
    left: 0;
    overflow: scroll;
  }

  .resize-box::-webkit-scrollbar {
    width: 100vw;
    height: 4px;
  }

  .resize-wrapper .resize-line {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 4px;
    background-color: #ffffffA0;
    transition: all 0.3s ease;
    pointer-events: none;
  }

  .resize-box:hover~.resize-line {
    background-color: #ffffff;
    box-shadow: 1px 1px 3px 1px rgba(0, 0, 0, 0.2);
  }

  /* 幹來的 */
  .tab-group {
    width: 100%;
    height: 100%;
    font-size: 0;
    overflow: hidden;
    position: relative;
  }

  .tab-group input {
    display: none;
  }

  .tab-group input:checked+label {
    background: #eee;
  }

  .tab-group input#tab1:checked~.line {
    left: 0%;
  }

  .tab-group input#tab2:checked~.line {
    left: 25%;
  }

  .tab-group input#tab3:checked~.line {
    left: 50%;
  }

  .tab-group input#tab4:checked~.line {
    left: 75%;
  }

  .tab-group input#tab1:checked~.content-container #c1,
  .tab-group input#tab2:checked~.content-container #c2,
  .tab-group input#tab3:checked~.content-container #c3,
  .tab-group input#tab4:checked~.content-container #c4 {
    opacity: 1;
    visibility: visible;
  }

  .tab-group label {
    display: inline-block;
    font-size: 16px;
    height: 36px;
    line-height: 36px;
    width: 25%;
    text-align: center;
    background: #f4f4f4;
    color: #555;
    position: relative;
    transition: 0.25s background ease;
    cursor: pointer;
    margin: 0;
  }

  .tab-group label::after {
    content: "";
    height: 2px;
    width: 100%;
    position: absolute;
    display: block;
    background: #ccc;
    bottom: 0;
    opacity: 0;
    left: 0;
    transition: 0.25s ease;
  }

  .tab-group label:hover::after {
    opacity: 1;
  }

  .tab-group .line {
    position: absolute;
    height: 2px;
    background: #1E88E5;
    width: 25%;
    top: 34px;
    left: 0;
    transition: 0.25s ease;
  }

  .tab-group .content-container {
    background: #eee;
    position: relative;
    height: calc(100% - 36px);
    font-size: 16px;
  }

  .tab-group .content-container .content {
    position: absolute;
    padding: 0px;
    width: 100%;
    height: 100%;
    top: 0;
    opacity: 0;
    transition: 0.25s ease;
    visibility: hidden;
    overflow: scroll;
  }

  .vgt-wrap {
    word-break: break-all;
  }

  .finishcover {
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    display: flex;
    z-index: 1000;
    background-color: var(--controls-bg-color);
  }

  .finishcover-message {
    font-size: 30px;
    color: rgb(153, 153, 153);
    display: flex;
    justify-content: center;
    align-items: center;
    pointer-events: none;
    flex: 1 1 auto;
    margin: 20px;
  }

  .vueperslides__inner,
  .vueperslides,
  .vueperslides__parallax-wrapper {
    height: 99.5%;
  }

  .vueperslide__content-wrapper {
    justify-content: flex-start !important;
    align-items: flex-end !important;
    padding-top: 0.5em;
    padding-right: 1em;
    font-size: 1.3em;
    line-height: 1.3;

  }

  .vueperslide__title {
    padding: 0.2em 1em;
    border: 1px solid hsla(0, 0%, 100%, .5);
    border-radius: 2em;
    background: hsla(0, 0%, 100%, .2);
    color: #fff;
  }

  .vueperslide {
    background-size: contain;
    background-repeat: no-repeat;
  }

</style>
