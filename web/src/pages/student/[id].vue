<script setup>
import { getStudent } from '../../services/api/get';

import { onMounted, ref } from 'vue';
import { useRoute, definePage } from 'vue-router/auto'


definePage({
  meta: { isStudent: true, requiresAuth: true },
});


// VARIABLES
const route = useRoute();
const student = ref({});

// FUNCTIONS
async function initStudent() {
  student.value = await getStudent(route.params.id);
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
    <p>aluno: {{ student.nm_pessoa }}</p>
    <p>cpf: {{ student.cpf_cnpj }}</p>
  </main>
</template>

<style lang="scss" scoped></style>