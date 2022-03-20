<template>
  <nav>
    <div class="nav-container">
      <div class="branding">
        <a href="/"><h1>GovDB</h1></a>
      </div>
      <MobileSearch></MobileSearch>
    </div>
  </nav>
</template>

<script>
  import MobileSearch from '@/components/MobileSearch.vue';
  export default {
    name: 'MobileNavBar',
    components: { MobileSearch },
  };
</script>

<style lang="css"></style>
