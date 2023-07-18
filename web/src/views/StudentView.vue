<script setup>
import { useRoute } from 'vue-router';
import { onMounted } from 'vue';
import axios from 'axios';

const route = useRoute();

function getStudent() {
  axios.get(`/student/${route.params.id}`).then((res) => {
    // studentDetails.value = res.data;
    // isStudentDetailsActive.value = true;
    // bodyElement.value.style.overflow = isStudentDetailsActive.value ? 'hidden' : 'auto';
    console.log(res.data);
  }).catch((err) => {
    console.error(err);
  });
};

onMounted(() => {
  getStudent();
})
</script>

<template>
  <main>
    <button @click="getStudent">{{ route.params.id }}</button>
  </main>
</template>

<style lang="scss" scoped></style>