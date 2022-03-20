import { createRouter, createWebHistory } from 'vue-router';
//Import HomeView Component
import HomeView from '../views/HomeView.vue';

const routes = [
  {
    // Home Page
    path: '/',
    name: 'home',
    component: HomeView,
  },
  // Member Profile
];

//Export routers
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
