import Vue from "vue";
import VueRouter from "vue-router";
import Menu from "../components/main_menu.vue";
import Member from "../components/member_icon.vue";
// import Home from "../views/home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Menu,
    Member,
  },
];

export default routes;
