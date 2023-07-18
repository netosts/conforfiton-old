
const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/student/:id/',
    name: 'student',
    component: () => import('../views/StudentView.vue')
  }
]

export default routes