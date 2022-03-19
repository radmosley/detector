<template>
  <NavBar></NavBar>
  <ContentArea></ContentArea>
</template>
<script>
  import NavBar from '@/components/NavBar.vue';
  import ContentArea from '@/components/ContentArea.vue';

  export default {
    name: 'App',
    components: { NavBar, ContentArea },
  };
</script>
<style></style>
