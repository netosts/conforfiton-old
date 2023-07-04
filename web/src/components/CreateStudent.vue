<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';


// Variables
const bodyElement = ref(null);
// emits
const emit = defineEmits(['isCreateStudentActive'])

function closeCreate() {
  emit('isCreateStudentActive', false);
  bodyElement.value.style.overflow = 'auto';
}

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
})
</script>

<template>
  <aside id="createScroll" class="create">
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    <div class="create__form">
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
      <h1>AAAAAAAAAAAAAAAAAAAAAAAA</h1>
    </div>
    <div class="create__close" @click="closeCreate"></div>
  </aside>
</template>

<style lang="scss" scoped>
.create {
  color: red;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 999;
  overflow: auto;

  &__form {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 888;
    background-color: white;
    color: red;
  }

  &__close {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 777;
    width: 100%;
    height: 100%;
    background-color: rgba(79, 79, 79, 0.442);
  }
}
</style>