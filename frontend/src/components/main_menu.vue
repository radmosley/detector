<template>
  <!-- <div class="wrapper">
    <nav class="container navbar is-transparent">
      <div class="navbar-brand">
        <SiteBranding></SiteBranding>
      </div>
      <div>
        <Search></Search>
      </div>
    </nav>
  </div> -->

  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <h1 class="title is-1">website</h1>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <input type="search" name="" id="" />
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
// import SiteBranding from "@/components/site_branding.vue";
// import Search from "@/components/search.vue";
export default {
  // components: { SiteBranding, Search },
  name: "Menu",
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  background: red;
  min-height: 75px;
}

.container {
  background: transparent;
}

.navbar.container {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}
</style>
