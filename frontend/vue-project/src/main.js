import 'mdb-vue-ui-kit/css/mdb.min.css'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueResource from 'vue-resource';
import VueSwal from 'vue-swal'
import Vuex from 'vuex'
import store from './store'
import VueGoodTablePlugin from 'vue-good-table';

import 'vue-good-table/dist/vue-good-table.css'

Vue.use(VueGoodTablePlugin);
Vue.use(Vuex)
Vue.use(VueSwal);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueResource);
Vue.config.productionTip = false
Vue.prototype.$HOST = '/api/'
Vue.http.interceptors.push((request, next) => {
  if (localStorage.getItem("token")){
    request.headers.set('Authorization', 'token ' + localStorage.getItem("token"))
  }
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
