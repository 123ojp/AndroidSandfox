import Vue from 'vue'
import Router from 'vue-router'
import store from '../store';
import Home from '../components/pages/Home'
import Register from '../components/pages/Register'
import RegisterSetPW from '../components/pages/RegisterSetPW'
import Login from '../components/pages/Login'
import Profile from '../components/pages/Profile'
import Error404 from '../components/pages/Error404'
import NewApp from '../components/pages/NewApp'
import Task from '../components/pages/Task'
import ListTask from '../components/pages/ListTask'
Vue.use(Router)


let routes = [
  {
    path: '/',
    component: Home,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: '/register',
    component: Register,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: '/register_next/:token*',
    component: RegisterSetPW,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: '/login',
    component: Login,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: '/new',
    component: NewApp,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: '/list',
    component: ListTask,
    meta: {
      requiresAuth: false
    },
  },
  {
    path: '/task/:id',
    component: Task,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: '/profile',
    component: Profile,
    meta: {
      requiresAuth: true
    },
  },
  {
    path: '/*',
    component: Error404,
    meta: {
      requiresAuth: false
    },
  },
];
var router = new Router({
//mode: 'history',
routes
});
router.beforeEach((to, from, next) => {
// 如果 router 轉跳的頁面需要驗證 requiresAuth: true
if (to.matched.some(record => {
    console.log(record.name, record.meta.requiresAuth);
    return record.meta.requiresAuth;
  })) {
  // 如果沒有 islogin
  if (!store.state.login_info.islogin && !localStorage.getItem("token")) {
    // 轉跳到 login page
    Vue.prototype.$swal("未登入!", "請先登入才能查看此頁面!", "error").then((value) => {
      next({
        path: '/login'
      })
    });

  } else {
    next(); // 往下繼續執行
  }
} else {
  next(); // 往下繼續執行
}
});
export default router;

