<script setup>
import {
  getNeuromuscularStudentPage,
  getAntropometriaStudentPage,
  getCardioStudentPage,
} from "@/services/api/get";

import { onMounted, ref } from "vue";
import { useRoute } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";

const route = useRoute();
const store = useStudentStore();

const activeEvaluation = ref(null);

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
    <h2>Neuromuscular</h2>
    <div
      v-for="(item, id) in store.evaluations.neuromuscular"
      :key="id"
      class="evaluation"
    >
      <button class="evaluation__item" @click="activeEvaluation = id">
        {{ id + 1 }}
      </button>
      <div class="evaluation__show" v-if="activeEvaluation === id">
        Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
      </div>
    </div>
  </section>
  <section>
    <h2>Antropometria</h2>
    <div
      v-for="(item, id) in store.evaluations.antropometria"
      :key="id"
      class="evaluation"
    >
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
  </section>
  <section>
    <h2>Cardiorrespiratório</h2>
    <div
      v-for="(item, id) in store.evaluations.cardio"
      :key="id"
      class="evaluation"
    >
      Avaliação[{{ id + 1 }}] <span>{{ item }}</span>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
  padding: 20px;
  margin-bottom: 20px;
  width: 100%;
  border-radius: $border-radius;
  box-shadow: $box-shadow;
  background-color: white;

  h2 {
    padding-bottom: 20px;
    color: $txt-title;
  }

  .evaluation {
    &__item {
      width: 50px;
      height: 50px;
      background-color: black;
      border-radius: 50%;
      color: red;
    }
  }
}
</style>
