<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#appnav" aria-controls="appnav"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

        <router-link to="/" class="navbar-brand" active-class="active" exact>
      <img class="img-responsive" height="25" src="@/assets/logo.png" alt="logo" /> Android Sandbox
        </router-link>

    <div class="collapse navbar-collapse" id="appnav">
      <ul class="nav navbar-nav  mr-auto">
        <router-link to="/new" class="nav-item nav-link" active-class="active" exact>
          新增任務
        </router-link>
        <router-link to="/list" class="nav-item nav-link" active-class="active" exact>
          任務列表
        </router-link>        
      </ul>
      <ul class="navbar-nav ml-md-auto d-block d-sm-flex d-md-flex">
        <hr class="d-sm-flex d-md-flex d-lg-none">
        <li v-show="isLogin" class="nav-item">
          <a v-show="isLogin" class="nav-item nav-link" active-class="active" exact>
            您好 {{ username }}
          </a>
        </li>
        <li class="nav-item">
          <router-link v-show="!isLogin" to="/register" class="nav-item nav-link" active-class="active" exact>
            註冊
          </router-link>
          <router-link v-show="isLogin" to="/profile" class="nav-item nav-link" active-class="active" exact>
            個人資料
          </router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link d-none d-md-block d-lg-block">|</a>
        </li>
        <li class="nav-item">
          <router-link to="/login" v-show="!isLogin" class="nav-item nav-link" active-class="active" exact>
            登入
          </router-link>
          <a @click="logout" v-show="isLogin" class="nav-item nav-link" active-class="active" exact>
            登出
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    data() {
      return {


      }
    },
    created: function () {
      var token = localStorage.getItem("token")
      if (token){
        this.getloginstate()
      }
    },
    computed: {
      // ...mapGetters 為 ES7 寫法
      ...mapGetters({
        // getCount return value 將會存在別名為 count 的 data 上
        isLogin: 'getIsLogin',
        username: 'getLoginUsername'
      }),
    },
    methods: {
      ...mapActions([
       'actionSetLoginInfo',
      ]),
      logout() {
        localStorage.removeItem("token");
        this.$swal("成功!", "登出成功!", "success").then((value) => {
                });
        var login_info = {
          email: null,
          islogin: false,
          username: null
        }
        this.actionSetLoginInfo(login_info)
      },
      getloginstate(){
        var PROFILE_API = this.$HOST  + "user/info"
        this.$http.get(PROFILE_API)
          .then((response) => {
            if (response.status == 200) {
              var login_info = {
                  username : response.body.username,
                  islogin : true,
              }
              this.actionSetLoginInfo(login_info)
            } else {
              console.log(response.body)
              this.$swal("錯誤!", "登入資料過期", "error");
              localStorage.removeItem("token");
            }

          })
          .catch((response) => {
            this.$swal("錯誤!", "登入資料過期", "error");
            this.$router.push("/login")
            localStorage.removeItem("token");
          })
          .finally(() => {});
      }
    }
  }
</script>
