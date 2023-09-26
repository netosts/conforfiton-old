<script setup>
import { getCardioStudentPage } from "@/services/api/get";

import { formatEvaluatedAt } from "@/services/formats";
import { protocolsList } from "@/services/avaliar/cardio/lists";

import { onMounted, ref } from "vue";

import { useStudentStore } from "@/stores/student";
import { useRoute, definePage } from "vue-router/auto";
import DeleteConfirmation from "@/components/DeleteConfirmation.vue";

definePage({
  meta: { requiresAuth: true },
});

const props = defineProps({
  student: Object,
});

const route = useRoute();
const store = useStudentStore();
const evaluationResult = ref(null);
const isDeleteActive = ref(false);
const evaluationToDelete = ref(null);

function handleDelete(emittedValue) {
  isDeleteActive.value = emittedValue;
}

async function initEvaluation() {
  try {
    if (store.cardio.id !== route.params.id) {
      store.cardio.value = await getCardioStudentPage(route.params.id);
      store.cardio.id = route.params.id;
    }
  } catch {}
}

function deleteEvaluation(protocol, date, id) {
  date = formatEvaluatedAt(date);
  evaluationToDelete.value = {
    type: "cardio",
    id,
    name: `${protocol} (${date})`,
  };
  isDeleteActive.value = true;
}

function renameProtocol(value) {
  if (!value) return "Sem protocolo";
  const findProtocol = protocolsList.value.find((item) => item.value === value);
  return findProtocol ? findProtocol.name : null;
}

onMounted(() => {
  initEvaluation();
});
</script>

<template>
  <DeleteConfirmation
    :evaluation="evaluationToDelete"
    @isDeleteActive="handleDelete"
    v-if="isDeleteActive"
  />
  <section>
    <h2>Cardiorrespiratória</h2>
    <div class="evaluation">
      <div
        v-for="(item, id) in store.cardio?.value"
        :key="id"
        class="evaluation__items"
        :class="{
          'evaluation__items--active': evaluationResult?.id === item.id,
        }"
      >
        <button
          @click="
            deleteEvaluation(item.cardio_protocol, item.created_at, item.id)
          "
          class="evaluation__items__delete"
        >
          <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
        </button>
        <div @click="evaluationResult = item" class="evaluation__items__text">
          <p>{{ renameProtocol(item.cardio_protocol) }}</p>
          <p>{{ formatEvaluatedAt(item.created_at) }}</p>
        </div>
      </div>
    </div>
    <div class="indicators" v-if="evaluationResult">
      <div v-if="evaluationResult.cardio_protocol !== 'Elder'">
        <h3>{{ renameProtocol(evaluationResult.cardio_protocol) }}</h3>
        <table>
          <thead>
            <tr>
              <th>Indicador</th>
              <th>Avaliação</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="evaluationResult.distance">
              <td>Distância</td>
              <td>{{ evaluationResult.distance }} m</td>
            </tr>
            <tr v-if="evaluationResult.time">
              <td>Tempo</td>
              <td>{{ evaluationResult.time }} min</td>
            </tr>
            <tr v-if="evaluationResult.fc_5min">
              <td>FC 5º Min</td>
              <td>{{ evaluationResult.fc_5min }} bpm</td>
            </tr>
            <tr>
              <td>VO2Max</td>
              <td>{{ evaluationResult.vo2max }} ml/kg/min</td>
            </tr>
            <tr>
              <td>VO2Max Absoluto</td>
              <td>{{ evaluationResult.vo2max_absolute }} l/min</td>
            </tr>
            <tr>
              <td>VO2Max Mets</td>
              <td>{{ evaluationResult.vo2max_mets }} mets</td>
            </tr>
            <tr>
              <td>vVO2Max</td>
              <td>{{ evaluationResult.vvo2max }} Km/h</td>
            </tr>
            <tr>
              <td>VVO2Max Pace</td>
              <td>{{ evaluationResult.vvo2max_pace }} min/km</td>
            </tr>
            <tr v-if="evaluationResult.vl1">
              <td>vL1</td>
              <td>{{ evaluationResult.vl1 }} Km/h</td>
            </tr>
            <tr v-if="evaluationResult.vl2">
              <td>vL2</td>
              <td>{{ evaluationResult.vl2 }} Km/h</td>
            </tr>
            <tr v-if="evaluationResult.vl1_pace">
              <td>vL1 Pace</td>
              <td>{{ evaluationResult.vl1_pace }} min/km</td>
            </tr>
            <tr v-if="evaluationResult.vl2_pace">
              <td>vL2 Pace</td>
              <td>{{ evaluationResult.vl2_pace }} min/km</td>
            </tr>
            <tr>
              <td>Peso</td>
              <td>{{ evaluationResult.weight }} kg</td>
            </tr>
            <tr>
              <td>Gasto calórico semanal</td>
              <td>{{ evaluationResult.weekly_caloric_expenditure }} kcal</td>
            </tr>
            <tr>
              <td>Gasto calórico diário</td>
              <td>{{ evaluationResult.daily_caloric_expenditure }} kcal</td>
            </tr>
            <tr v-if="evaluationResult.l1_fc_max_percentage">
              <td>Limiar 1 (% FC Max)</td>
              <td>{{ evaluationResult.l1_fc_max_percentage }} bpm</td>
            </tr>
            <tr v-if="evaluationResult.l2_fc_max_percentage">
              <td>Limiar 2 (% FC Max)</td>
              <td>{{ evaluationResult.l2_fc_max_percentage }} bpm</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>
        <table>
          <thead>
            <tr>
              <th>Indicador</th>
              <th>Avaliação</th>
              <th>Classificação</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Distância</td>
              <td>{{ evaluationResult.distance }}m</td>
              <td class="emphasize">
                {{ evaluationResult.elder_aerobic_power }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding: 20px;
  margin-bottom: 20px;
  width: 100%;
  border-radius: $border-radius;
  box-shadow: $box-shadow;
  background-color: white;

  h2 {
    color: $txt-title;
  }
}
.evaluation {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;

  &__items {
    position: relative;
    text-align: center;
    font-size: 13px;
    font-weight: 500;

    &__text {
      position: relative;
      z-index: 10;
      width: 150px;
      padding: 10px 20px;
      border-radius: $border-radius;
      box-shadow: $box-shadow;
      background-color: rgb(246, 246, 246);
      cursor: pointer;
      transition: 0.2s;
      &:hover {
        background-color: rgb(228, 228, 228);
      }

      &:active {
        filter: brightness(0.7);
      }
    }

    &--active {
      .evaluation__items__text {
        background-color: $logo-color;
        color: white;
      }
    }

    &__delete {
      position: absolute;
      top: -20px;
      right: -20px;
      z-index: 100;
      width: 40px;
      height: 40px;
      border: none;
      border-radius: 50%;
      background-color: transparent;
      color: rgba(85, 85, 85, 0.588);
      cursor: pointer;
      transition: 0.2s;

      &:hover {
        color: $txt-aside;
        background-color: rgb(228, 228, 228);
      }
    }
  }
}

.indicators {
  display: flex;
  flex-direction: column;
  gap: 40px;

  div {
    display: flex;
    flex-direction: column;
    gap: 10px;

    h3 {
      text-align: center;
      font-weight: 600;
      color: $txt-title;
      border-bottom: 1px solid $input-border;
    }

    table {
      border-collapse: collapse;
      border: 1px solid $input-border;

      th {
        background-color: $buttons;
        color: white;
      }

      th,
      td {
        border: 1px solid $input-border;
        padding: 8px;
        text-align: center;
      }

      td {
        font-weight: 500;
        color: $txt-aside;

        &:nth-child(1) {
          font-weight: 700;
        }

        &:not(:nth-child(1)) {
          min-width: 50px;
          max-width: 100px;
        }
      }
    }

    .emphasize {
      font-weight: 800;
      color: $logo-color;
    }
  }
}
</style>
