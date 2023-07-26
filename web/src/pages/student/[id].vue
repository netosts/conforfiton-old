<script setup>
import axios from 'axios';
import { getStudent } from '../../services/axios/get';

import { onMounted, ref } from 'vue';
import { useRoute, definePage } from 'vue-router/auto'


// definePage({
//   meta: { isStudent: true, },
// });


// VARIABLES
const route = useRoute();
const student = ref({});

// FUNCTIONS
async function initStudent() {
  student.value = await getStudent(axios, route.params.id);
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
    <p>aluno: {{ student.nmPessoa }}</p>
    <p>cpf: {{ student.cpfCnpj }}</p>
  </main>
</template>

<style lang="scss" scoped></style>