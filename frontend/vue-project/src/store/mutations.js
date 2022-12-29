import * as types from './mutations_type.js'
import Vue from 'vue'

// state
export const state = {
  login_info: {}
}

// mutations
export const mutations = {
  // action 發出 commit 會對應到 mutation 使用的是 Object key 方式
  [types.SET_USER_INFO] (state,data) {
    // 在 mutation 改變 state（只有 mutation 可以改變！）
    state.login_info =data;
  }
}