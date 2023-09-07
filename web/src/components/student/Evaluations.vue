<script setup>
defineProps({
  student: Object,
  show: Boolean,
});
</script>

<template>
  <section v-if="show">
    <h2>Informações Gerais</h2>
    <p>CPF: {{ student.cpf }}</p>
    <p>Sexo: {{ student.gender }}</p>
    <p>Email: {{ student.email }}</p>
    <p>Telefone: {{ student.phone_number }}</p>
    <p>Altura: {{ student.height }}</p>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
  padding: 20px;
  width: 100%;
  border-radius: $border-radius;
  box-shadow: $box-shadow;
  background-color: white;
}
</style>
