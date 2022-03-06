<template>
  <div id="app">
    <Menu></Menu>
    <Member></Member>
    <!-- <router-view>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </router-view> -->
  </div>
</template>

<script>
import Menu from "./components/main_menu.vue";
import Member from "./components/member_icon.vue";
export default {
  components: { Menu, Member },
};
</script>

<style>
body {
  margin: 0;
}
</style>
