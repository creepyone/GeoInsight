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
import AnalysisInfo from '../views/AnalysisInfoView.vue';

import NotFoundView from '../views/NotFoundView.vue';

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
      path: '/authorized/:id/analysis',
      component: Analysis,
      name: 'analysis',
    },
    {
      path: '/authorized/:id/history',
      component: History,
      name: 'history',
    },
    {
      path: '/authorized/:id',
      component: MainScreenAuth,
      name: 'main-screen-auth',
    },
    {
      path: '/authorized/:id/aboutus',
      component: AboutUsAuth,
      name: 'about-us-auth',
    },
    {
      path: '/authorized/:id/history/:id_analysis',
      component: AnalysisInfo,
      name: 'history-analysis-info',
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: NotFoundView
    }
  ],
  history: createWebHistory(),
});

const app = createApp(App);
app.use(router);
app.mount('#app');
