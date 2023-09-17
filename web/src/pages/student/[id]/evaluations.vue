<script setup>
import {
  getNeuromuscularStudentPage,
  getAntropometriaStudentPage,
  getCardioStudentPage,
} from "@/services/api/get";

import { onMounted } from "vue";
import { useRoute } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";

const route = useRoute();
const store = useStudentStore();

async function initEvaluations() {
  try {
    if (store.evaluations.id !== route.params.id) {
      const [neuromuscular, antropometria, cardio] = await Promise.all([
        getNeuromuscularStudentPage(route.params.id),
        getAntropometriaStudentPage(route.params.id),
        getCardioStudentPage(route.params.id),
      ]);
      store.evaluations.neuromuscular = neuromuscular;
      store.evaluations.antropometria = antropometria;
      store.evaluations.cardio = cardio;
      store.evaluations.id = route.params.id;
    }
  } catch {}
}

onMounted(() => {
  initEvaluations();
});
</script>

<template>
  <section>
    <h2>Avaliações</h2>
    <h3>Neuromuscular</h3>
    <div v-for="(item, id) in store.evaluations.neuromuscular" :key="id">
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
    <h3>Antropometria</h3>
    <div v-for="(item, id) in store.evaluations.antropometria" :key="id">
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>

    <h3>Cardiorrespiratório</h3>
    <div v-for="(item, id) in store.evaluations.cardio" :key="id">
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
