import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueAxios from 'vue-axios';
import axios from 'axios';

// import HelloWorld from '@/components/HelloWorld';

createApp(App).use(VueAxios, axios).use(store).use(router).mount('#app');
