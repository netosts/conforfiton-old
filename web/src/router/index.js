import { createRouter, createWebHistory } from 'vue-router/auto'

import { getStudent } from '../services/axios/get';
import axios from 'axios';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior: () => ({ left: 0, top: 0 }),
})


router.beforeEach((to, from) => {
  const isAuthenticated = true

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isAuthenticated) return { path: '/login' }
  }
})

router.beforeResolve(async (to, from) => {
  if (to.meta.isStudent) {
    try {
      await getStudent(axios, to.params.id)
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
