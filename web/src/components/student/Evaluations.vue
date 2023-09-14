<script setup>
defineProps({
  get: Object,
  show: Boolean,
});
</script>

<template>
  <section v-if="show">
    <h2>Avaliações</h2>
    <h3>Antropometria</h3>
    <div v-for="(item, id) in get.antropometria" :key="id">
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
    <h3>Neuromuscular</h3>
    <div v-for="(item, id) in get.neuromuscular" :key="id">
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
    <h3>Cardiorrespiratório</h3>
    <div v-for="(item, id) in get.cardio" :key="id">
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
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
