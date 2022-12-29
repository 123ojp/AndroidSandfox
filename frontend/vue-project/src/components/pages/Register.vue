<template>
  <div>
    <div class="jumbotron">
      <div class="container">
        <h1>註冊</h1>
      </div>
    </div>
    <div class="col-md-6 offset-md-3">

      <div class="form-group">
        <label for="name-input">
          名稱
        </label>
        <input v-model="data.username" class="form-control input-filled-valid" type="text" name="name" id="name-input">
      </div>
      <div class="form-group">
        <label for="email-input">
          Email
        </label>
        <input v-model="data.email" class="form-control" type="text" name="email" id="email-input">
      </div>
      <div class="row pt-3">
        <div class="col-md-12">
          <button onclick="" type="primary" @click="handleRegister" tabindex="5"
            class="btn btn-md btn-primary btn-outlined float-right">註冊</button>
        </div>
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
        data: {
          username: '',
          email: '',
        }


      }
    },
    methods: {
      ...mapActions([
        'actionSetLoginInfo',
      ]),
      handleRegister() {
        let username = this.data.username
        let email = this.data.email
        // 帳號密碼需驗證不能為空
        if (username == '' || email == '') {
          this.$swal('錯誤！', '每個欄位不能為空', 'error');
          return
        }
        const re =
          /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re.test(email)) {
          this.$swal('錯誤！', 'email格式不正確', 'error');
          return
        }
        var payload = {
          username:username,
          email:email
        }
        var REG_API  = this.$HOST  + "user/register" ;
        this.$http.post(REG_API, payload)
          .then((response) => {
            if (response.status == 200) {
              this.$swal("Email 發送成功", "請去 "+email+ " 領取驗證碼，在進行密碼設定", "success")
              this.$router.push("/register_next/")

            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
            }

          })
          .catch((response) => {
            this.$swal("錯誤!",JSON.stringify(response.body), "error");

          })
          .finally(() => {});

      },
    }
  }

</script>
