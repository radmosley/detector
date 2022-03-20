<template>
  <div class="container">
    <ul id="example-1">
      <MemberIcon></MemberIcon>
    </ul>
  </div>
</template>

<script>
  import MemberIcon from '@/components/Member.vue';
  export default {
    name: 'ContentArea',
    components: { MemberIcon },
  };
</script>

<style scoped>
  .container {
  }
</style>
