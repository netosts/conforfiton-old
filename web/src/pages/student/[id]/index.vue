<script setup>
import {
  formatDate,
  formatAge,
  cmToMeters,
  formatTelefone,
  formatCpf,
} from "@/services/formats";
import { translateGender } from "@/services/helpers";
defineProps({
  student: Object,
});
</script>

<template>
  <section>
    <h2>Informações Gerais</h2>

    <p>
      Idade: <span>{{ formatAge(student?.birth_date) }}</span>
    </p>
    <p>
      Sexo: <span>{{ translateGender(student?.gender) }}</span>
    </p>
    <p>
      CPF: <span>{{ formatCpf(student?.cpf) }}</span>
    </p>
    <p>
      Email: <span>{{ student?.email }}</span>
    </p>
    <p>
      Telefone: <span>{{ formatTelefone(student?.phone_number) }}</span>
    </p>
    <p>
      Altura: <span>{{ cmToMeters(student?.height) }}m</span>
    </p>
    <p>
      T. Camisa: <span>{{ student?.shirt_size }}</span>
    </p>
    <p>
      T. Shorts: <span>{{ student?.shorts_size }}</span>
    </p>
    <p>
      Registrado em: <span>{{ formatDate(student?.created_at) }}</span>
    </p>
    <p>
      Ativo: <span>{{ student?.deleted_at ? "Não" : "Sim" }}</span>
    </p>
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

  h2 {
    padding-bottom: 20px;
    color: $txt-title;
  }

  p {
    display: grid;
    grid-template-columns: 1fr 1fr;
    color: $txt-aside;
    font-size: 15px;
    font-weight: 600;

    span {
      font-weight: 400;
      color: $txt-subtitle;
    }
  }
}
</style>
