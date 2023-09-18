import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ErrorView from '@/views/ErrorView.vue';

import RegisterView from '@/views/Users/RegisterView.vue';
import LoginView from '@/views/Users/LoginView.vue';
import ProfileView from '@/views/Users/ProfileView.vue';

import DatasetView from '@/views/Datasets/DatasetView.vue';
import DatasetListView from '@/views/Datasets/DatasetListView.vue';
import CreateDatasetView from '@/views/Datasets/CreateDatasetView.vue';

import ModelView from '@/views/Models/ModelView.vue';
import ModelListView from '@/views/Models/ModelListView.vue';
import CreateModelView from '@/views/Models/CreateModelView.vue';

import TrainingView from '@/views/Trainings/TrainingView.vue';
import TrainingListView from '@/views/Trainings/TrainingListView.vue';

import store from '@/store/index';

const routes = [
  {
    path: '/',
    name: "Home",
    component: HomeView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/error',
    name: 'Error',
    component: ErrorView,
  },
  {
    path: '/datasets',
    name: 'Datasets',
    component: DatasetListView,
    meta: { requiresAuth: true },
  },
  {
    path: '/datasets/:id',
    name: 'Dataset',
    component: DatasetView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/datasets/create',
    name: 'Create Dataset',
    component: CreateDatasetView,
    meta: { requiresAuth: true },
  },
  {
    path: '/models',
    name: 'Models',
    component: ModelListView,
    meta: { requiresAuth: true },
  },
  {
    path: '/models/create',
    name: 'Create Model',
    component: CreateModelView,
    meta: { requiresAuth: true },
  },
  {
    path: '/models/:id',
    name: 'Model',
    component: ModelView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/trainings',
    name: 'Tranings',
    component: TrainingListView,
    meta: { requiresAuth: true },
  },
  {
    path: '/trainings/:id',
    name: 'Training',
    component:  TrainingView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth) && !store.getters.isAuthenticated) {
    next({ path: '/login' });
  } else {
    next();
  }
});

export default router