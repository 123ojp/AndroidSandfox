<template>
  <div>
    <div class="jumbotron">
      <div class="container">
        <h1>登入</h1>
      </div>
    </div>
    <div class="col-md-6 offset-md-3">

      <div class="form-group">
        <label for="name-input">
          E-mail
        </label>
        <input v-model="data.username" class="form-control input-filled-valid" type="text" name="name" id="name-input" />
      </div>
      <div class="form-group">
        <label for="password-input">
          密碼
        </label>
        <input v-model="data.password" class="form-control input-filled-valid" type="password" name="password"
          id="password-input" />
      </div>
      <div class="row pt-3">
        <div class="col-md-12">
          <button onclick="" type="primary" @click="handleLogin" tabindex="5"
            class="btn btn-md btn-primary btn-outlined float-right">登入</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

  export default {
    data() {
      return {
        data :{
          username: 'admin',
          password: 'admin',
        }
     }
    },
    methods: {
    ...mapActions([
      'actionSetLoginInfo',
    ]),
      handleLogin() {
        let password = this.data.password
        let username = this.data.username
        // 帳號密碼需驗證不能為空
        if (password == '' || username == '') {
          this.$swal('錯誤！', '每個欄位不能為空', 'error');
          return
        }

        var payload = {
           username : username,
           password : password
        }
        var LOGIN_API = this.$HOST  + "user/login"
        this.$http.post(LOGIN_API, payload)
          .then((response) => {
            if (response.status == 200) {
              this.$swal("成功!", "登入成功!", "success").then((value) => {
                this.$router.push("/")
              });
              var login_info = {
                  username : username,
                  islogin : true,
                  token : response.body.token
              }
              this.actionSetLoginInfo(login_info)
              localStorage.setItem('token', response.body.token);
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
    }
  }

</script>
