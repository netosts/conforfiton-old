<script setup>
defineProps({
  get: Object,
  show: Boolean,
});
</script>

<template>
  <section v-if="show">
    <h2>Anamnese</h2>
    <p>{{ get }}</p>
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
