import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import MainScreenNotAuth from '../views/MainScreenNotAuthView.vue';
import AboutUsNotAuth from '../views/AboutUsNotAuthView.vue';
import LogIn from '../views/LogInView.vue';
import SignUp from '../views/SignUpView.vue';

import Analysis from '../views/AnalysisView.vue';
import History from '../views/HistoryView.vue';
import MainScreenAuth from '../views/MainScreenView.vue';
import AboutUsAuth from '../views/AboutUsAuthView.vue';

const router = createRouter({
  routes: [
    {
      path: '/',
      component: MainScreenNotAuth,
      name: 'main-screen-not-auth',
    },
    {
      path: '/aboutus',
      component: AboutUsNotAuth,
      name: 'about-us-not-auth',
    },
    {
      path: '/login',
      component: LogIn,
      name: 'log-in',
    },
    {
      path: '/signup',
      component: SignUp,
      name: 'sign-up',
    },
    {
      path: '/authorized/analysis',
      component: Analysis,
      name: 'analysis',
    },
    {
      path: '/authorized/history',
      component: History,
      name: 'history',
    },
    {
      path: '/authorized',
      component: MainScreenAuth,
      name: 'main-screen-auth',
    },
    {
      path: '/authorized/aboutus',
      component: AboutUsAuth,
      name: 'about-us-auth',
    },
  ],
  history: createWebHistory(),
});

const app = createApp(App);
app.use(router);
app.mount('#app');
