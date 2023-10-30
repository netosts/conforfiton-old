import { createRouter, createWebHistory } from "vue-router/auto";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior: () => ({ left: 0, top: 0 }),
});

router.beforeEach((to, from) => {
  if (to.meta.requiresAuth) {
    const logged = localStorage.getItem("user");
    if (!logged) return { path: "/login" };
  }
});

export default router;
