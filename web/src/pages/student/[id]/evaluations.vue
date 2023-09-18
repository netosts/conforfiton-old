<script setup>
import {
  getNeuromuscularStudentPage,
  getAntropometriaStudentPage,
  getCardioStudentPage,
} from "@/services/api/get";

import { onMounted, ref } from "vue";
import { useRoute } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";

import Avaliar from "@/components/Avaliar.vue";

const route = useRoute();
const store = useStudentStore();

const bodyElement = ref(null);
const activeEvaluation = ref(null);
const isAvaliarActive = ref(false);

const props = defineProps({
  student: Object,
});

// Send Props
const studentId = ref(null);
const studentName = ref(null);

// Handle Emits
const handleAvaliar = (emittedValue) => {
  return (isAvaliarActive.value = emittedValue);
};

function toggleAvaliar(id, name) {
  isAvaliarActive.value = !isAvaliarActive.value;
  bodyElement.value.style.overflow = isAvaliarActive.value ? "hidden" : "auto";
  studentId.value = id;
  studentName.value = name;
}

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
  bodyElement.value = document.body;
});
</script>

<template>
  <Avaliar
    :studentName="studentName"
    :studentId="studentId"
    @isAvaliarActive="handleAvaliar"
    v-show="isAvaliarActive"
  />

  <div class="evaluation-button">
    <button @click="toggleAvaliar(student?.person_id, student?.name)">
      Nova Avaliação
    </button>
  </div>

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

.evaluation-button {
  display: flex;
  justify-content: flex-end;
  button {
    margin-top: -10px;
    margin-bottom: 10px;
    font-weight: 500;
    @include submitButtons($validation, white);
  }
}
</style>
