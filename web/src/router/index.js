import { createRouter, createWebHistory } from 'vue-router/auto'

import { getStudentCredentials } from '../services/api/get';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior: () => ({ left: 0, top: 0 }),
})


router.beforeEach((to, from) => {
  if (to.meta.requiresAuth) {
    const logged = localStorage.getItem('user')
    if (!logged) return { path: '/login' }
  }
})

router.beforeResolve(async (to, from) => {
  if (to.meta.isStudent) {
    try {
      await getStudentCredentials(to.params.id)
    } catch {
      return {
        name: 'NotFound',
        // allows keeping the URL while rendering a different page
        params: { pathMatch: to.path.split('/').slice(1) },
        query: to.query,
        hash: to.hash,
      } 
    }
  }
})

export default router
