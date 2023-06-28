<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const msg = ref('');
const userId = ref(1);

function getMessage() {
  axios.get(`/user/${userId.value}`).then((res) => {
    msg.value = res.data;
  }).catch((err) => {
    console.error(err);
  })
};

onMounted(getMessage);
</script>

<template>
  <main>
    <h1>HOME</h1>
    <RouterLink to="/about">About</RouterLink>
    <p>{{ msg.name }}</p>
  </main>
</template>

<style lang="scss" scoped></style>