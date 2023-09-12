<script setup>
import { formatDate } from "@/services/helpers";
defineProps({
  get: Object,
  show: Boolean,
});
</script>

<template>
  <section v-if="show">
    <h2>Informações Gerais</h2>
    <p>CPF: {{ get?.cpf }}</p>
    <p>Sexo: {{ get?.gender }}</p>
    <p>Email: {{ get?.email }}</p>
    <p>Telefone: {{ get?.phone_number }}</p>
    <p>Altura: {{ get?.height }}</p>
    <p>T. Camisa: {{ get?.shirt_size }}</p>
    <p>T. Shorts: {{ get?.shorts_size }}</p>
    <p>Registrado em: {{ formatDate(get?.created_at) }}</p>
    <p>Ativo: {{ get?.deleted_at ? "Não" : "Sim" }}</p>
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
