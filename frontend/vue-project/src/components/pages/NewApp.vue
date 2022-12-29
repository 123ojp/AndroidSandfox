<template>
  <div>
    <div class="jumbotron">
      <div class="container">
        <h1>開始一個新任務</h1>
      </div>
    </div>
    <div class="col-md-6 offset-md-3">

      <div class="form-group">
        <label for="name-input">
          上傳
        </label>
        <b-form-group label="檔案：" label-cols-sm="2" label-size="lg">
          <b-form-file id="file-large" accept=".apk" v-model="file" placeholder="Choose a file or drop it here..."
            size="lg">
          </b-form-file>

        </b-form-group>
        <b-form-group label="Hooks：" label-cols-sm="2" label-size="lg">
          <b-form-checkbox-group size="lg" id="checkbox-group-1" v-model="feature" :options="options"
            :aria-describedby="ariaDescribedby" name="flavour-1"></b-form-checkbox-group>

        </b-form-group>
        <b-button variant="info" class="float-right" @click="submitFile">開始任務</b-button>
      </div>

    </div>
  </div>
</template>
<script>
  import {
    mapGetters,
    mapActions
  } from 'vuex'

  export default {

    data() {
      return {
        file: null,
        data: {
          username: '',
          email: '',
        },
        options: [{
            text: 'IPC',
            value: 'IPC'
          },
          {
            text: 'Syscall',
            value: 'Syscall'
          },
          {
            text: 'SharedPreferences',
            value: 'SharedPreferences'
          },
          {
            text: 'SQLiteDatabase',
            value: 'SQLiteDatabase'
          },
          {
            text: 'Native',
            value: 'Native'
          },
          {
            text:"Bypass Root",
            value:"BypassRoot"
          },
            {
            text:"Http MITM",
            value:"mitm"
          },
        ],
        feature: ['IPC', 'Syscall', 'SQLiteDatabase','BypassRoot','mitm','Native'],
      }
    },
    methods: {
      ...mapActions([
        'actionSetLoginInfo',
      ]),
      submitFile() {
        let fileToUpload = this.file;
        if (fileToUpload) {
          let formData = new FormData();
          var NEW_API = this.$HOST + "app/new";
          formData.append('file', fileToUpload);
          formData.append('feature', this.feature);
          this.$swal("上傳中", "請稍候");
          this.$http.post(NEW_API, formData).then((response) => {
            // success actions
            this.$swal.close()
            this.$router.push("/task/" + response.body.id)

          }).catch((response) => {
            this.$swal.close()
            this.$swal("錯誤!", JSON.stringify(response.body), "error");
          });
        } else {
          this.$swal.close()
          this.$swal("錯誤!", "沒有選擇檔案", "error");
        }



      },
    }
  }

</script>
