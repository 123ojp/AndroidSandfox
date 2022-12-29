<template>
  <div class="vh-100 d-flex flex-column">
    <header class="app-header">
      <navbar></navbar>
    </header>
    <main role="main" class="flex-fill">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import navbar from '@/components/shared/navbar.vue';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/js/bootstrap.js'

export default {
  name: 'App',
  components: {
      navbar: navbar,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
