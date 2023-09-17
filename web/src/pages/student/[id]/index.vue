<script setup>
import { formatDate } from "@/services/helpers";
defineProps({
  student: Object,
});
</script>

<template>
  <section>
    <h2>Informações Gerais</h2>
    <p>CPF: {{ student?.cpf }}</p>
    <p>Sexo: {{ student?.gender }}</p>
    <p>Email: {{ student?.email }}</p>
    <p>Telefone: {{ student?.phone_number }}</p>
    <p>Altura: {{ student?.height }}</p>
    <p>T. Camisa: {{ student?.shirt_size }}</p>
    <p>T. Shorts: {{ student?.shorts_size }}</p>
    <p>Registrado em: {{ formatDate(student?.created_at) }}</p>
    <p>Ativo: {{ student?.deleted_at ? "Não" : "Sim" }}</p>
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
