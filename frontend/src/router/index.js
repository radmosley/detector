import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Member from '../components/Member.vue';
import NavBar from '../components/NavBar.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    Member,
    NavBar,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
