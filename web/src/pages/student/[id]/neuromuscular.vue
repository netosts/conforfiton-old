<script setup>
import { getNeuromuscularStudentPage } from "@/services/api/get";

import { formatEvaluatedAt } from "@/services/formats";
import { protocolsList } from "@/services/avaliar/neuromuscular/lists";

import { onMounted, ref } from "vue";
import { useWindowSize } from "@vueuse/core";

import { useStudentStore } from "@/stores/student";
import { useRoute, definePage } from "vue-router/auto";
import DeleteEvaluationConfirmation from "@/components/DeleteEvaluationConfirmation.vue";

definePage({
  meta: { requiresAuth: true },
});

defineProps({
  student: Object,
});

const route = useRoute();
const store = useStudentStore();
const evaluationResult = ref(null);
const isDeleteActive = ref(false);
const evaluationToDelete = ref(null);
const { width, height } = useWindowSize();

function handleDelete(emittedValue) {
  if (evaluationResult.value?.id === emittedValue) {
    evaluationResult.value = null;
  }
  isDeleteActive.value = false;
}

function handleCloseButton(_) {
  isDeleteActive.value = false;
}

async function initEvaluation() {
  try {
    if (store.neuromuscular.id !== route.params.id) {
      store.neuromuscular.value = await getNeuromuscularStudentPage(
        route.params.id
      );
      store.neuromuscular.id = route.params.id;
    }
  } catch {}
}

function deleteEvaluation(protocol, date, id) {
  date = formatEvaluatedAt(date);
  evaluationToDelete.value = {
    type: protocol !== "RMLFP" ? "neuromuscular" : "neuromuscular/rml",
    id,
    name: `${protocol} (${date})`,
  };
  isDeleteActive.value = true;
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
  <DeleteEvaluationConfirmation
    :evaluation="evaluationToDelete"
    @deactivateDelete="handleDelete"
    @closeDeleteButton="handleCloseButton"
    v-if="isDeleteActive"
  />
  <section>
    <h2>Neuromuscular</h2>
    <div class="evaluation">
      <div
        v-for="(item, id) in store.neuromuscular?.value"
        :key="id"
        class="evaluation__items"
        :class="{
          'evaluation__items--active':
            evaluationResult?.id === item.id &&
            evaluationResult?.neuromuscular_protocol ===
              item.neuromuscular_protocol,
        }"
      >
        <button
          @click="
            deleteEvaluation(
              item.neuromuscular_protocol,
              item.created_at,
              item.id
            )
          "
          class="evaluation__items__delete"
        >
          <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
        </button>
        <div @click="evaluationResult = item" class="evaluation__items__text">
          <p>{{ renameProtocol(item.neuromuscular_protocol) }}</p>
          <p>{{ formatEvaluatedAt(item.created_at) }}</p>
        </div>
      </div>
    </div>
    <div class="indicators" v-if="evaluationResult">
      <div
        class="rmzona"
        v-if="
          evaluationResult.neuromuscular_protocol === '1RMZona' ||
          evaluationResult.neuromuscular_protocol === 'RMEpley'
        "
      >
        <h3>Teste de 1RM Zona</h3>
        <table>
          <thead>
            <tr>
              <th>{{ width < 410 ? "Exc." : "Exercício" }}</th>
              <th>{{ width < 410 ? "P.L." : "Peso L." }}</th>
              <th>{{ width < 410 ? "R." : "Reps." }}</th>
              <th>1RM</th>
              <th>{{ width < 410 ? "Pts." : "Pontos" }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ width < 410 ? "Spn." : "Supino" }}</td>
              <td>{{ evaluationResult.bench_press_lifted }} kg</td>
              <td>{{ evaluationResult.bench_press_reps }}</td>
              <td>{{ evaluationResult.bench_press_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.bench_press_points }}
              </td>
            </tr>
            <tr>
              <td>{{ width < 410 ? "R. D." : "Rosca Direta" }}</td>
              <td>{{ evaluationResult.barbell_curl_lifted }} kg</td>
              <td>{{ evaluationResult.barbell_curl_reps }}</td>
              <td>{{ evaluationResult.barbell_curl_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.barbell_curl_points }}
              </td>
            </tr>
            <tr>
              <td>{{ width < 410 ? "P. P. F." : "Puxada Pela Frente" }}</td>
              <td>{{ evaluationResult.pull_down_lifted }} kg</td>
              <td>{{ evaluationResult.pull_down_reps }}</td>
              <td>{{ evaluationResult.pull_down_rm }}</td>
              <td class="emphasize">{{ evaluationResult.pull_down_points }}</td>
            </tr>
            <tr>
              <td>{{ width < 410 ? "L. P." : "Leg Press" }}</td>
              <td>{{ evaluationResult.leg_press_lifted }} kg</td>
              <td>{{ evaluationResult.leg_press_reps }}</td>
              <td>{{ evaluationResult.leg_press_rm }}</td>
              <td class="emphasize">{{ evaluationResult.leg_press_points }}</td>
            </tr>
            <tr>
              <td>{{ width < 410 ? "E. J." : "Extensão de Joelhos" }}</td>
              <td>{{ evaluationResult.leg_extension_lifted }} kg</td>
              <td>{{ evaluationResult.leg_extension_reps }}</td>
              <td>{{ evaluationResult.leg_extension_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.leg_extension_points }}
              </td>
            </tr>
            <tr>
              <td>{{ width < 410 ? "F. J." : "Flexão de Joelhos" }}</td>
              <td>{{ evaluationResult.leg_curl_lifted }} kg</td>
              <td>{{ evaluationResult.leg_curl_reps }}</td>
              <td>{{ evaluationResult.leg_curl_rm }}</td>
              <td class="emphasize">{{ evaluationResult.leg_curl_points }}</td>
            </tr>
          </tbody>
        </table>
        <div class="total">
          <h4>Total:</h4>
          <span>{{ evaluationResult.total_points }}</span>
        </div>
        <div class="total">
          <h4>
            Desempenho: <span>{{ evaluationResult.classification }}</span>
          </h4>
        </div>
        <div class="legenda" v-if="width < 410">
          <h4>Legenda</h4>
          <p>Spn. > Supino</p>
          <p>R. D. > Rosca Direta</p>
          <p>P. P. F. > Puxada Pela Frente</p>
          <p>L. P. > Leg Press</p>
          <p>E. J. > Extensão de Joelhos</p>
          <p>F. J. > Flexão de Joelhos</p>
        </div>
      </div>

      <div
        class="rmlfp"
        v-if="evaluationResult.neuromuscular_protocol === 'RMLFP'"
      >
        <h3>Teste de Força/Resistência</h3>
        <table>
          <thead>
            <tr>
              <th>{{ width < 415 ? "Ind." : "Indicador" }}</th>
              <th>{{ width < 415 ? "Aval." : "Avaliação" }}</th>
              <th>{{ width < 415 ? "Class." : "Classificação" }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ width < 415 ? "Abd." : "Abdominal" }}</td>
              <td>{{ evaluationResult.sit_up }} reps</td>
              <td class="emphasize">{{ evaluationResult.sit_up_result }}</td>
            </tr>
            <tr>
              <td>{{ width < 415 ? "F. B." : "Flexão de Braço" }}</td>
              <td>{{ evaluationResult.push_up }} reps</td>
              <td class="emphasize">{{ evaluationResult.push_up_result }}</td>
            </tr>
            <tr>
              <td>{{ width < 415 ? "S. H." : "Salto Horizontal" }}</td>
              <td>{{ evaluationResult.jump }} cm</td>
              <td class="emphasize">{{ evaluationResult.jump_result }}</td>
            </tr>
          </tbody>
        </table>
        <div class="legenda" v-if="width < 415">
          <h4>Legenda</h4>
          <p>Ind. > Indicador</p>
          <p>Aval. > Avaliação</p>
          <p>Class. > Classificação</p>
          <p>Abd. > Abdominal</p>
          <p>F. B. > Flexão de Braço</p>
          <p>S. H. > Salto Horizontal</p>
        </div>
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
    z-index: 1;
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

  .rmzona,
  .rmlfp {
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
    .total {
      display: flex;
      border: 1px solid $input-border;

      h4 {
        padding: 0 10px;
        font-size: 1.2rem;
        color: $txt-aside;
      }

      span {
        flex: 1;
        font-size: 1.2rem;
        font-weight: 800;
        color: $logo-color;
      }
    }

    .legenda {
      display: flex;
      flex-direction: column;
      padding: 0 10px;
      border: 1px solid $input-border;
      color: $txt-aside;

      h4 {
        font-size: 1.2rem;
      }
    }

    .emphasize {
      font-weight: 800;
      color: $logo-color;
    }
  }
}
</style>
