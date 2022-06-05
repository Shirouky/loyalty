<template>
  <div id="app">
    <nav>
      <router-link to="/">Главная</router-link> |
      <router-link to="/cashier">Касса</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",

};
</script>

<style scoped>
#app {
  padding: 0 10vw;
}
</style>
