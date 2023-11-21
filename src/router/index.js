import { createRouter, createWebHistory } from 'vue-router';


export const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import(/* webpackChunkName: "home" */ '../views/HomeView.vue')
    },
    {
        path: '/shark',
        name: 'shark',
        component: () => import(/* webpackChunkName: "shark" */ '../views/SharkView.vue')
    }
];
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })

export default router;

