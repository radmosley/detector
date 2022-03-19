<template>
  <li v-for="s in senator" :key="s.id">
    <div class="member-container">
      <div class="member-image">
        <img src="https://via.placeholder.com/150" />
      </div>
      <div class="member-content">
        <h3>{{ s.title }}</h3>
        <h4>{{ s.first_name }} {{ s.last_name }}</h4>
        <input class="contact-button" type="button" value="contact" />
      </div>
    </div>
  </li>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'MemberIcon',
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

<style scoped>
  .member-container {
    margin: 1rem;
    display: flex;
  }
  .member-content {
    padding: 0 1rem;
  }
  .member-content > h3 {
    font-size: 0.9rem;
  }
  .member-content > h4 {
    font-size: 1rem;
    font-weight: 600;
  }
  .contact-button {
    margin-top: 2rem;
    background: #d6d6d6;
    color: inherit;
    border: none;
    padding: 0.25rem 0.5rem;
    font: inherit;
    cursor: pointer;
    outline: inherit;
    bottom: 0;
  }
</style>
