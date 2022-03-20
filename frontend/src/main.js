import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// Configure Axios to retrieve Django db
import VueAxios from 'vue-axios';
import axios from 'axios';
// Import CSS
import '@/assets/css/main.css';
// Is Mobile Detection
import VueMobileDetection from 'vue-mobile-detection';

createApp(App)
  .use(VueMobileDetection) //Provides .isMoble() method
  .use(VueAxios, axios) // API Calls
  .use(store)
  .use(router)
  .mount('#app');
