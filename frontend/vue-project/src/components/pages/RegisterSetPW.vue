<template>
  <div>
    <div class="jumbotron">
      <div class="container">
        <h1>驗證信箱 & 設定密碼</h1>
      </div>
    </div>
    <div class="col-md-6 offset-md-3">

      <div class="form-group">
        <label for="name-input">
          信箱收到的 Token
        </label>
        <input v-model="data.token" class="form-control input-filled-valid" type="text" name="name" id="name-input">
      </div>
      <div class="form-group">
        <label for="password-input">
          Password
        </label>
        <input v-model="data.password" class="form-control input-filled-valid" type="password" name="password"
          id="password-input">
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
          token: '',
          password: '',
          email: '',
        }


      }
    },
    created: function (){
        this.data.token = this.$route.params.token;
    },
    methods: {
      ...mapActions([
        'actionSetLoginInfo',
      ]),
      handleRegister() {
        let token = this.data.token
        let password = this.data.password
        let email = this.data.email
        // 帳號密碼需驗證不能為空
        if (token == '' || password == '') {
          this.$swal('錯誤！', '每個欄位不能為空', 'error');
          return
        }

        var payload = {
          token : token,
          password: password
        }
        var SETPW_API  = this.$HOST  + "user/create" ;        
        this.$http.post(SETPW_API, payload)
          .then((response) => {
            if (response.status == 200) {
              this.$swal("成功!", "註冊成功!", "success")
              var login_info = {
                  islogin : true,
                  username: response.body.username,
                  token : response.body.token

              }
              this.actionSetLoginInfo(login_info)
              localStorage.setItem('token', response.body.token);
              this.$router.push("/")

            } else {
              console.log(response.body)
              this.$swal("錯誤!", response.body, "error");
            }

          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");

          })
          .finally(() => {});

      },
    }
  }

</script>
