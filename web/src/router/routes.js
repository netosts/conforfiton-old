
const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/student/:id/',
    name: 'student',
    component: () => import('../views/StudentView.vue'),
    beforeEnter(to, from) {

    },
  }
]

export default routes