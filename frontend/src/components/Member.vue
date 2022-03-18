<template>
  <ul id="example-1">
    <li v-for="s in senator" :key="s.id">
      {{ s.first_name }}
    </li>
  </ul>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'HelloWorld',
    data() {
      return {
        senator: [],
      };
    },
    methods: {
      async getData() {
        try {
          const response = await axios.get('http://localhost:8000/senators/');
          this.senator = response.data;
        } catch (error) {
          console.log(error);
        }
      },
    },
    created() {
      this.getData();
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
