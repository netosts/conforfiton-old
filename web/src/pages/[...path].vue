<script setup>
import { definePage } from 'vue-router/auto'

definePage({
  path: '/:pathMatch(.*)*',
  name: 'NotFound',
  meta: { requiresAuth: true },
});
</script>

<template>
  <main>
    <h1>Página não encontrada</h1>
    <div class="ops">
      <p>Ops... Você tentou acessar uma página que não existe.</p>
      <RouterLink to="/"><strong>Voltar ao início</strong></RouterLink>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';

h1 {
  margin-bottom: 20px;
  font-size: 3rem;
  color: $buttons;
}

.ops {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;

  p {
    color: $txt-aside;
  }

  a {
    color: $logo-color;
    text-decoration: none;
  }
}
</style>