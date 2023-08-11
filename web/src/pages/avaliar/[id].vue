<script setup>
import { getStudentAvaliar, getRmConfig } from "../../services/api/get";
import {
  repsList,
  exerciseList,
  pontosTotal,
} from "../../services/configs/lists";

import { useAvaliarStore } from "../../stores/avaliar";

import { onMounted, ref } from "vue";
import { useRoute, useRouter, definePage } from "vue-router/auto";

import { Form } from "vee-validate";
import TextField from "../../components/TextField.vue";
import SubmitButton from "../../components/SubmitButton.vue";

definePage({
  meta: { isStudent: true, requiresAuth: true },
});

// VARIABLES
const router = useRouter();
const route = useRoute();
const student = ref(null);
const rmConfig = ref(null);
const store = useAvaliarStore();

// Form variables

// FUNCTIONS
function onSubmit(values) {
  console.log(values);
  router.push("/print");
}

async function initRequests() {
  try {
    student.value = await getStudentAvaliar(route.params.id);
    store.student = student.value;
    if (store.types.includes("Neuromuscular")) {
      rmConfig.value = await getRmConfig(student.value.sexo);
      store.rmConfig = rmConfig.value;
    }
  } catch {
    alert("Houve um erro, o aluno não pôde ser encontrado.");
    router.push("/");
  }
}

// DOM Mount
onMounted(() => {
  initRequests();
});
</script>

<template>
  <main>
    <section class="student">
      <div class="top">
        <RouterLink to="/" class="voltar">
          <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
        </RouterLink>
        <h1>{{ student?.nm_pessoa }}</h1>
      </div>

      <div class="student__details">
        <p>Peso: {{ student?.peso }}kg</p>
        <p>Sexo: {{ student?.sexo }}</p>
      </div>
    </section>

    <Form @submit="onSubmit">
      <section v-if="store.types?.includes('Neuromuscular')">
        <h2>Neuromuscular</h2>
        <table class="neuro-table">
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
            <tr v-for="exercise in exerciseList" :key="exercise">
              <td>{{ exercise.title }}</td>
              <td>
                <TextField
                  v-model="exercise.pesoLevantado"
                  :name="`${exercise.name}PesoLevantado`"
                  type="number"
                />
              </td>
              <td>
                <TextField
                  v-model="exercise.reps"
                  :name="`${exercise.name}Reps`"
                  type="select"
                  :options="repsList"
                />
              </td>
              <td>{{ exercise.rm }}</td>
              <td>{{ exercise.pontos }}</td>
            </tr>
          </tbody>
        </table>

        <div class="neuro-total">
          <h3>Total:</h3>
          <span>{{ pontosTotal }}</span>
        </div>
      </section>

      <section v-if="store.types?.includes('Antropometria')">
        <h2>Antropometria</h2>
      </section>

      <section v-if="store.types?.includes('Cardio')">
        <h2>Cardio</h2>
      </section>

      <SubmitButton msg="Salvar" />
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import "../../assets/styles/variables";
@import "../../assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 10px;

  .student {
    display: flex;
    flex-direction: column;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;

    .top {
      padding: 10px;
      box-shadow: $box-shadow;

      .voltar {
        position: absolute;
        top: 5px;
        @include tool();
        color: $buttons;
      }

      h1 {
        text-align: center;
        padding: 0 40px;
      }
    }

    &__details {
      display: flex;
      justify-content: space-evenly;
      gap: 5px;
      background-color: $readonly;
      font-weight: 600;
      pointer-events: none;

      p {
        flex: 1;
        padding: 20px;
        text-align: center;
      }

      p:nth-child(1) {
        border-right: 2px solid $background;
      }
    }
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 20px;

    section {
      display: flex;
      flex-direction: column;
      gap: 10px;
      border-radius: $border-radius;
      box-shadow: $box-shadow;
      background-color: white;
      color: $txt-aside;

      h2 {
        padding: 10px;
        border-bottom: 1px solid $input-border;
        text-align: center;
        color: $txt-title;
      }

      .neuro-table {
        margin: 0px 10px;
        border-collapse: collapse;
        border: 1px solid $input-border;

        th,
        td {
          border: 1px solid $input-border;
          padding: 8px;
          text-align: center;
        }

        th {
          color: $txt-aside;
        }

        td {
          font-weight: 500;
          color: $txt-aside;

          &:not(:nth-child(1)) {
            min-width: 50px;
            max-width: 100px;

            .register-field {
              min-width: 50px;
            }
          }
        }
      }

      .neuro-total {
        display: flex;
        margin: 0 10px 10px 10px;
        border: 1px solid $input-border;

        h3 {
          padding: 0 10px;
          font-size: 1.2rem;
        }

        span {
          flex: 1;
          font-size: 1.2rem;
          font-weight: 800;
          color: $logo-color;
        }
      }
    }
  }
}
</style>
