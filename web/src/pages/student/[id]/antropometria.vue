<script setup>
import {
  getNeuromuscularStudentPage,
  getAntropometriaStudentPage,
  getCardioStudentPage,
} from "@/services/api/get";

import { formatCreatedAt } from "@/services/formats";
import { protocolsList } from "@/services/avaliar/neuromuscular/lists";

import { onMounted } from "vue";

import { useStudentStore } from "@/stores/student";
import { useRoute } from "vue-router/auto";

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

function renameProtocol(value) {
  if (!value) return "Sem protocolo";
  const findProtocol = protocolsList.value.find((item) => item.value === value);
  return findProtocol.name;
}

onMounted(() => {
  initEvaluation();
});
</script>

<template>
  <section>
    <h2>Neuromuscular</h2>
    <div class="evaluation">
      <div
        v-for="(item, id) in store.evaluations.neuromuscular"
        :key="id"
        class="evaluation__items"
      >
        <p>{{ renameProtocol(item.neuromuscular_protocol) }}</p>
        <p>{{ formatCreatedAt(item.created_at) }}</p>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped></style>
