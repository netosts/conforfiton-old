<script setup>
defineProps({
  student: Object,
  show: Boolean,
});
</script>

<template>
  <section v-if="show">
    <h2>Informações Gerais</h2>
    <p>Altura: {{ student.height }}</p>
    <p>T. Camisa: {{ student.shirt_size }}</p>
    <p>T. Shorts: {{ student.shorts_size }}</p>
    <p>Registrado em: {{ student.created_at }}</p>
    <p>Ativo: {{ student.deleted_at ? "Não" : "Sim" }}</p>
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
