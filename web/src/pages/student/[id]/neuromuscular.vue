<script setup>
import { getNeuromuscularStudentPage } from "@/services/api/get";

import { formatEvaluatedAt } from "@/services/formats";
import { protocolsList } from "@/services/avaliar/neuromuscular/lists";

import { onMounted, ref } from "vue";

import { useStudentStore } from "@/stores/student";
import { useRoute, definePage } from "vue-router/auto";

definePage({
  meta: { requiresAuth: true },
});

const route = useRoute();
const store = useStudentStore();
const evaluationResult = ref(null);

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
        v-for="(item, id) in store.neuromuscular?.value"
        :key="id"
        class="evaluation__items"
        :class="{
          'evaluation__items--active':
            evaluationResult?.created_at === item.created_at,
        }"
        @click="evaluationResult = item"
      >
        <p>{{ renameProtocol(item.neuromuscular_protocol) }}</p>
        <p>{{ formatEvaluatedAt(item.created_at) }}</p>
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
              <th>Exercício</th>
              <th>Peso L.</th>
              <th>Reps</th>
              <th>1RM</th>
              <th>Pontos</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Supino</td>
              <td>{{ evaluationResult.bench_press_lifted }}</td>
              <td>{{ evaluationResult.bench_press_reps }}</td>
              <td>{{ evaluationResult.bench_press_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.bench_press_points }}
              </td>
            </tr>
            <tr>
              <td>Rosca Direta</td>
              <td>{{ evaluationResult.barbell_curl_lifted }}</td>
              <td>{{ evaluationResult.barbell_curl_reps }}</td>
              <td>{{ evaluationResult.barbell_curl_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.barbell_curl_points }}
              </td>
            </tr>
            <tr>
              <td>Puxada Pela Frente</td>
              <td>{{ evaluationResult.pull_down_lifted }}</td>
              <td>{{ evaluationResult.pull_down_reps }}</td>
              <td>{{ evaluationResult.pull_down_rm }}</td>
              <td class="emphasize">{{ evaluationResult.pull_down_points }}</td>
            </tr>
            <tr>
              <td>Leg Press</td>
              <td>{{ evaluationResult.leg_press_lifted }}</td>
              <td>{{ evaluationResult.leg_press_reps }}</td>
              <td>{{ evaluationResult.leg_press_rm }}</td>
              <td class="emphasize">{{ evaluationResult.leg_press_points }}</td>
            </tr>
            <tr>
              <td>Extenção de Joelhos</td>
              <td>{{ evaluationResult.leg_extension_lifted }}</td>
              <td>{{ evaluationResult.leg_extension_reps }}</td>
              <td>{{ evaluationResult.leg_extension_rm }}</td>
              <td class="emphasize">
                {{ evaluationResult.leg_extension_points }}
              </td>
            </tr>
            <tr>
              <td>Flexão de Joelhos</td>
              <td>{{ evaluationResult.leg_curl_lifted }}</td>
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
      </div>

      <div
        class="rmlfp"
        v-if="evaluationResult.neuromuscular_protocol === 'RMLFP'"
      >
        <h3>Teste de Força/Resistência</h3>
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
              <td>Abdominal</td>
              <td>{{ evaluationResult.sit_up }} reps</td>
              <td class="emphasize">{{ evaluationResult.sit_up_result }}</td>
            </tr>
            <tr>
              <td>Flexão de Braço</td>
              <td>{{ evaluationResult.push_up }} reps</td>
              <td class="emphasize">{{ evaluationResult.push_up_result }}</td>
            </tr>
            <tr>
              <td>Salto Horizontal</td>
              <td>{{ evaluationResult.jump }} cm</td>
              <td class="emphasize">{{ evaluationResult.jump_result }}</td>
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
    width: 150px;
    padding: 10px 20px;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: rgb(246, 246, 246);
    text-align: center;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: 0.2s;

    &:hover {
      background-color: rgb(228, 228, 228);
    }

    &:active {
      filter: brightness(0.7);
    }

    &--active {
      background-color: $logo-color;
      color: white;
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
      margin-bottom: 10px;
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

    .emphasize {
      font-weight: 800;
      color: $logo-color;
    }
  }
}
</style>
