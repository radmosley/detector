<template>
  <MobileNavBar v-if="$isMobile()"></MobileNavBar>
  <NavBar v-else></NavBar>
  <ContentArea></ContentArea>
</template>

<script>
  import NavBar from '@/components/NavBar.vue';
  import ContentArea from '@/components/ContentArea.vue';
  import MobileNavBar from '@/components/MobileNavBar.vue';

  export default {
    name: 'HomeView',
    components: { NavBar, MobileNavBar, ContentArea },
  };
</script>
