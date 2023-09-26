<script setup>
import { getAntropometriaStudentPage } from "@/services/api/get";

import { formatEvaluatedAt } from "@/services/formats";
import { protocolsList } from "@/services/avaliar/antropometria/lists";

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
    if (store.antropometria.id !== route.params.id) {
      store.antropometria.value = await getAntropometriaStudentPage(
        route.params.id
      );
      store.antropometria.id = route.params.id;
    }
  } catch {}
}

function deleteEvaluation(protocol, date, id) {
  date = formatEvaluatedAt(date);
  evaluationToDelete.value = {
    type: "antropometria",
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
    <h2>Antropométrica</h2>
    <div class="evaluation">
      <div
        v-for="(item, id) in store.antropometria?.value"
        :key="id"
        class="evaluation__items"
        :class="{
          'evaluation__items--active': evaluationResult?.id === item.id,
        }"
      >
        <button
          @click="
            deleteEvaluation(
              item.antropometria_protocol,
              item.created_at,
              item.id
            )
          "
          class="evaluation__items__delete"
        >
          <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
        </button>
        <div @click="evaluationResult = item" class="evaluation__items__text">
          <p>{{ renameProtocol(item.antropometria_protocol) }}</p>
          <p>{{ formatEvaluatedAt(item.created_at) }}</p>
        </div>
      </div>
    </div>
    <div class="indicators" v-if="evaluationResult">
      <div class="circumference">
        <h3>Indicadores Circunferências</h3>
        <table>
          <thead>
            <tr>
              <th>Indicador</th>
              <th>Avaliação</th>
              <th>Classificação</th>
              <th>Meta</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>IMC</td>
              <td>{{ evaluationResult.imc_result }} kg/m²</td>
              <td class="emphasize">{{ evaluationResult.imc_class }}</td>
            </tr>
            <tr>
              <td>CA</td>
              <td>{{ evaluationResult.abdominal_circumference }} cm</td>
              <td class="emphasize">{{ evaluationResult.ca_class }}</td>
            </tr>
            <tr>
              <td>RCQ</td>
              <td>{{ evaluationResult.rcq_result }}</td>
              <td class="emphasize">{{ evaluationResult.rcq_class }}</td>
            </tr>
            <tr>
              <td>RCAE</td>
              <td>{{ evaluationResult.rcae_result }}</td>
              <td class="emphasize">{{ evaluationResult.rcae_class }}</td>
            </tr>
            <tr>
              <td>IAC</td>
              <td>{{ evaluationResult.iac_result }}</td>
              <td class="emphasize">{{ evaluationResult.iac_class }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="fat-percentage">
        <h3>Indicadores %Gordura</h3>
        <table>
          <thead>
            <tr>
              <th>Indicador</th>
              <th>Avaliação</th>
              <th>Meta</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Peso</td>
              <td>{{ evaluationResult.weight }} kg</td>
              <td class="emphasize">{{ evaluationResult.weight_goal }} kg</td>
            </tr>
            <tr>
              <td>Gordura</td>
              <td>{{ evaluationResult.pg_result }}%</td>
              <td class="emphasize">{{ evaluationResult.pg_goal }}%</td>
            </tr>
            <tr>
              <td>MIG (Massa isenta de gordura)</td>
              <td>{{ evaluationResult.mig_result }}%</td>
              <td class="emphasize">{{ evaluationResult.mig_goal }}%</td>
            </tr>
            <tr>
              <td>Peso Gordura</td>
              <td>{{ evaluationResult.fat_weight_result }} kg</td>
              <td class="emphasize">
                {{ evaluationResult.fat_weight_goal }} kg
              </td>
            </tr>
            <tr>
              <td>Peso MIG</td>
              <td>{{ evaluationResult.mig_weight_result }} kg</td>
              <td class="emphasize">
                {{ evaluationResult.mig_weight_goal }} kg
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="evaluation-values">
        <h3>Medidas da Avaliação</h3>
        <table>
          <thead>
            <tr>
              <th>Medida</th>
              <th>Valor</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Circunferência Abdominal</td>
              <td>{{ evaluationResult.abdominal_circumference }}</td>
            </tr>
            <tr>
              <td>Circunferência Cintura</td>
              <td>{{ evaluationResult.waist_circumference }}</td>
            </tr>
            <tr>
              <td>Circunferência Quadril</td>
              <td>{{ evaluationResult.hip_circumference }}</td>
            </tr>
            <tr>
              <td>Circunferência Coxa</td>
              <td>{{ evaluationResult.thighs_circumference }}</td>
            </tr>
            <tr>
              <td>Circunferência Biceps D.</td>
              <td>{{ evaluationResult.right_biceps_circumference }}</td>
            </tr>
            <tr>
              <td>Circunferência Antebraço D.</td>
              <td>{{ evaluationResult.right_forearm_circumference }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Peitoral</td>
              <td>{{ evaluationResult.chest_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Abdominal</td>
              <td>{{ evaluationResult.abdominal_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Coxa</td>
              <td>{{ evaluationResult.thighs_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Triceps</td>
              <td>{{ evaluationResult.triceps_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Suprailíaca</td>
              <td>{{ evaluationResult.suprailiac_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Subescapular</td>
              <td>{{ evaluationResult.subscapularis_skin_fold }}</td>
            </tr>
            <tr>
              <td>Dobra Cutânea Axilar Média</td>
              <td>{{ evaluationResult.midaxillary_skin_fold }}</td>
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
@import "@/assets/styles/animations";

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

  .circumference,
  .fat-percentage,
  .evaluation-values {
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
