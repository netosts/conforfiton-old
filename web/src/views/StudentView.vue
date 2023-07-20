<script setup>
import axios from 'axios';
import { getStudent } from '../services/students/get';

import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';

// Variables
const route = useRoute();
const student = ref({});

// Functions
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