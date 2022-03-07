<template>
  <div>
    <Menu></Menu>
    <div class="container">
      <div class="column is-3"><SubMenu></SubMenu></div>
      <div class="column is-6"><Member></Member></div>
    </div>
  </div>
</template>

<script>
import Menu from "./components/main_menu.vue";
import Member from "./components/member_icon.vue";
import SubMenu from "./components/sub_nav.vue";
export default {
  components: { Menu, Member, SubMenu },
};
</script>

<style>
.content {
  display: flex;
}
</style>
