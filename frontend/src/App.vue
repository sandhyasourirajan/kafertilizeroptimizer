<template>

  <v-app>
    <page-header> </page-header>
    <div id="app">
      <router-view />
    </div>
    <page-footer></page-footer>

  </v-app>
</template>

<script>

  import { webAuth, isLoggedIn, login, logout }  from './auth0-service'

  export default {
      name:'app',
      mounted(){
          if ( ! isLoggedIn() ) {
              login();
          }
      },
      methods: {
          handleLogout() {
              logout();
          }
      }
  }

</script>

<style scoped>
@import '../node_modules/bootstrap/dist/css/bootstrap.css';
</style>
