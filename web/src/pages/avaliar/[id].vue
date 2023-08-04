<script setup>
import http from '../../services/api/http';
import { getStudentCredentials } from '../../services/api/get';

import { onMounted, ref } from 'vue';
import { useRoute, definePage } from 'vue-router/auto'


definePage({
  meta: { isStudent: true, requiresAuth: true },
});

const route = useRoute()
const student = ref(null);

// FUNCTIONS
async function initStudent() {
  student.value = await getStudentCredentials(http, route.params.id);
}

// DOM Mount
onMounted(() => {
  initStudent();
})
</script>

<template>
  <main>
    <RouterLink to="/">
      <p>home</p>
    </RouterLink>
    <p v-if="student">aluno: {{ student.nmPessoa }}</p>
  </main>
</template>

<style lang="scss" scoped></style>