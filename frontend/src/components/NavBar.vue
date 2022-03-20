<template>
  <nav>
    <div class="nav-container">
      <div class="branding"><h1>GovDB</h1></div>
      <div class="searchbox">
        <input type="search" id="site-search" name="q" />
        <button>Search</button>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar',
  };
</script>

<style lang="css">
  @media screen and (min-width: 800px) {
    #site-search {
      display: inline;
    }
  }
</style>
