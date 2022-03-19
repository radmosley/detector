<template>
  <nav>
    <div class="nav-container">
      <div class="branding"><h1>GovDB</h1></div>
      <div class="searchbox">search</div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar',
  };
</script>

<style lang="css">
  @media screen and (max-width: 600px) {
    nav {
      width: 100%;
      background: #f7f7f7;
    }
    .nav-container {
      display: flex;
      flex-flow: row nowrap;
      align-items: center;
      justify-content: space-between;
      padding: 0.3rem 1.5rem 0.3rem 1.5rem;
    }
    .branding > h1 {
      font-weight: 700;
    }
  }
</style>
