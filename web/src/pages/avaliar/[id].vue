<script setup>
import { getStudentAvaliar, getRmConfig } from '../../services/api/get';
import { repsList, exerciseList, pontosTotal } from '../../services/configs/lists';

import { useAvaliarStore } from '../../stores/avaliar';

import { onMounted, ref } from 'vue';
import { useRoute, useRouter, definePage } from 'vue-router/auto';

import { Form } from 'vee-validate';
import TextField from '../../components/TextField.vue';


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
  // router.push('/print');
};

async function initRequests() {
  try {
    student.value = await getStudentAvaliar(route.params.id);
    store.student = student.value;
    if (store.types.includes('Neuromuscular')) {
      rmConfig.value = await getRmConfig(student.value.sexo);
      store.rmConfig = rmConfig.value;
    }
  } catch {
    alert('Houve um erro, o aluno não pôde ser encontrado.');
    router.push('/');
  }
};

// DOM Mount
onMounted(() => {
  initRequests();
});
</script>

<template>
  <main>
    <div class="top">
      <RouterLink to="/" class="voltar">
        <font-awesome-icon icon="fa-solid fa-arrow-left" />
        voltar
      </RouterLink>

      <h1>{{ student?.nm_pessoa }}</h1>
    </div>

    <Form @submit="onSubmit" id="myForm">
      <section class="student-details">
        <p>Peso corporal atual: {{ student?.peso }}</p>
      </section>

      <section v-if="store.types?.includes('Neuromuscular')">
        <h2>Neuromuscular</h2>

        <table>
          <thead>
            <tr>
              <th>Exercício</th>
              <th>Peso Levantado</th>
              <th>Repetições</th>
              <th>1RM</th>
              <th>Pontos</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="exercise in exerciseList" :key="exercise">
              <td>{{ exercise.title }}</td>
              <td>
                <TextField v-model="exercise.pesoLevantado" :name="`${exercise.name}PesoLevantado`" type="number" />
              </td>
              <td>
                <TextField v-model="exercise.reps" :name="`${exercise.name}Reps`" type="select" :options="repsList" />
              </td>
              <td>{{ exercise.rm }}</td>
              <td>{{ exercise.pontos }}</td>
            </tr>
          </tbody>
        </table>

        <div class="neurobox">
          <h4>Total: <span class="p-total">{{ pontosTotal }}</span></h4>
        </div>
      </section>

      <section v-if="store.types?.includes('Antropometria')">
        <h2>Antropometria</h2>
      </section>

      <section v-if="store.types?.includes('Cardio')">
        <h2>Cardio</h2>
      </section>

      <button class="submit">Salvar</button>
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import '../../assets/styles/variables';
@import '../../assets/styles/mixins';


main {
  display: flex;
  flex-direction: column;
  gap: 10px;

  .top {
    display: flex;
    justify-content: space-between;

    h1 {
      text-align: center;
      flex: 1;
    }

    .voltar {
      position: absolute;
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 600;
      text-decoration: none;
      color: $logo-color;
    }
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 20px;

    .student-details {
      padding: 20px;
      background-color: $readonly;
      font-weight: 500;
      text-transform: uppercase;
      pointer-events: none;
    }

    section {
      display: flex;
      flex-direction: column;
      gap: 20px;
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

      table {
        margin: 0px 10px 10px 10px;
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
        }

        td:not(:nth-child(1)) {
          width: 130px;
        }
      }
    }

    .submit {
      @include submitButtons($validation, white);
    }
  }
}
</style>