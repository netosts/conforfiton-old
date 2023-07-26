import Home from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { requiresAuth: true }, // This route requires authentication
  },
  {
    path: '/student/:id/',
    name: 'student',
    component: () => import('../views/StudentView.vue'),
    meta: { requiresAuth: true, isStudent: true },
  },
  {
    path: '/anamnese/:id/',
    name: 'anamnese',
    component: () => import('../views/Avaliar/AnamneseView.vue'),
    meta: { requiresAuth: true, isStudent: true }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue'),
    beforeEnter: () => {
      const isAuthenticated = false
      if (isAuthenticated) return { name: 'home' }
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFoundView.vue')
  }
]

export default routes