<template>
  <div id="app">
    <div>
      <div class="row content">
        <Menu></Menu>
        <Member></Member>
      </div>

      <footer>
        <p>Footer Text</p>
      </footer>
      <!-- <Menu></Menu>
    <Member></Member> -->
      <!-- <router-view>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </router-view> -->
    </div>
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
/* Set black background color, white text and some padding */
footer {
  background-color: #555;
  color: white;
  padding: 15px;
}
</style>
