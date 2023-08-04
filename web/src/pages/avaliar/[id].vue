<script setup>
import http from '../../services/api/http';
import { getStudentAvaliar } from '../../services/api/get';

import { calcular1RM, calcularPontos, supinoConfig, roscaDiretaConfig, puxadaPelaFrenteConfig, legPressConfig, extensaoDeJoelhosConfig, flexaoDeJoelhosConfig } from '../../services/configs/neuromuscular';

import { useAvaliarStore } from '../../stores/avaliar';

import { onMounted, ref, reactive, computed } from 'vue';
import { useRoute, definePage } from 'vue-router/auto';

import { Form } from 'vee-validate';
import TextField from '../../components/TextField.vue';


definePage({
  meta: { isStudent: true, requiresAuth: true },
});

// VARIABLES
const route = useRoute();
const student = ref(null);
const store = useAvaliarStore();

// Form variables
const supino = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(supino.pesoLevantado, supino.reps)),
  pontos: computed(() => calcularPontos(student.value, supino.rm, supinoConfig)),
});

const roscaDireta = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(roscaDireta.pesoLevantado, roscaDireta.reps)),
  pontos: computed(() => calcularPontos(student.value, roscaDireta.rm, roscaDiretaConfig)),
});

const puxadaPelaFrente = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(puxadaPelaFrente.pesoLevantado, puxadaPelaFrente.reps)),
  pontos: computed(() => calcularPontos(student.value, puxadaPelaFrente.rm, puxadaPelaFrenteConfig)),
});

const legPress = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(legPress.pesoLevantado, legPress.reps)),
  pontos: computed(() => calcularPontos(student.value, legPress.rm, legPressConfig)),
});

const extensaoDeJoelhos = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(extensaoDeJoelhos.pesoLevantado, extensaoDeJoelhos.reps)),
  pontos: computed(() => calcularPontos(student.value, extensaoDeJoelhos.rm, extensaoDeJoelhosConfig)),
});

const flexaoDeJoelhos = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => calcular1RM(flexaoDeJoelhos.pesoLevantado, flexaoDeJoelhos.reps)),
  pontos: computed(() => calcularPontos(student.value, flexaoDeJoelhos.rm, flexaoDeJoelhosConfig)),
});

const pontosTotal = computed(() => {
  if (!(supino.pontos + roscaDireta.pontos + puxadaPelaFrente.pontos + legPress.pontos + extensaoDeJoelhos.pontos + flexaoDeJoelhos.pontos)) {
    return;
  }
  return supino.pontos + roscaDireta.pontos + puxadaPelaFrente.pontos + legPress.pontos + extensaoDeJoelhos.pontos + flexaoDeJoelhos.pontos;
});


// FUNCTIONS
function onSubmit(values) {
  console.log(values);
};

async function initStudent() {
  student.value = await getStudentAvaliar(http, route.params.id);
};

// DOM Mount
onMounted(() => {
  initStudent();
});
</script>

<template>
  <main>
    <div class="top">
      <RouterLink to="/" class="voltar">
        <font-awesome-icon icon="fa-solid fa-arrow-left" />
        voltar
      </RouterLink>

      <h1>{{ student?.nmPessoa }}</h1>
    </div>

    <Form @submit="onSubmit">
      <section>
        <p>Peso corporal atual: {{ student?.peso }}</p>
      </section>

      <button type="button" @click="calcularForcaRelativa(57.1, student.peso)">click</button>

      <section v-if="store.types?.includes('Neuromuscular')">
        <h2>Neuromuscular</h2>

        <div class="neurobox">
          <h3>Supino</h3>
          <div class="neuro">
            <TextField v-model="supino.pesoLevantado" name="supinoPesoLevantado" type="number" label="peso levantado" />
            <TextField v-model="supino.reps" name="supinoReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="supino.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="supino.pontos" type="number" readonly>
            </div>
          </div>
        </div>

        <div class="neurobox">
          <h3>Rosca Direta</h3>
          <div class="neuro">
            <TextField v-model="roscaDireta.pesoLevantado" name="roscaDiretaPesoLevantado" type="number"
              label="peso levantado" />
            <TextField v-model="roscaDireta.reps" name="roscaDiretaReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="roscaDireta.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="roscaDireta.pontos" type="number" readonly>
            </div>
          </div>
        </div>

        <div class="neurobox">
          <h3>Puxada pela frente</h3>
          <div class="neuro">
            <TextField v-model="puxadaPelaFrente.pesoLevantado" name="puxadaPelaFrentePesoLevantado" type="number"
              label="peso levantado" />
            <TextField v-model="puxadaPelaFrente.reps" name="puxadaPelaFrenteReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="puxadaPelaFrente.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="puxadaPelaFrente.pontos" type="number" readonly>
            </div>
          </div>
        </div>

        <div class="neurobox">
          <h3>Leg Press</h3>
          <div class="neuro">
            <TextField v-model="legPress.pesoLevantado" name="legPressPesoLevantado" type="number"
              label="peso levantado" />
            <TextField v-model="legPress.reps" name="legPressReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="legPress.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="legPress.pontos" type="number" readonly>
            </div>
          </div>
        </div>

        <div class="neurobox">
          <h3>Extensão de joelhos</h3>
          <div class="neuro">
            <TextField v-model="extensaoDeJoelhos.pesoLevantado" name="extensaoDeJoelhosPesoLevantado" type="number"
              label="peso levantado" />
            <TextField v-model="extensaoDeJoelhos.reps" name="extensaoDeJoelhosReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="extensaoDeJoelhos.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="extensaoDeJoelhos.pontos" type="number" readonly>
            </div>
          </div>
        </div>

        <div class="neurobox">
          <h3>Flexão de joelhos</h3>
          <div class="neuro">
            <TextField v-model="flexaoDeJoelhos.pesoLevantado" name="flexaoDeJoelhosPesoLevantado" type="number"
              label="peso levantado" />
            <TextField v-model="flexaoDeJoelhos.reps" name="flexaoDeJoelhosReps" type="number" label="repetições" />
            <div class="neuro__result">
              <label>1RM</label>
              <input v-model="flexaoDeJoelhos.rm" type="number" readonly>
            </div>
            <div class="neuro__result">
              <label>Pontos</label>
              <input v-model="flexaoDeJoelhos.pontos" type="number" readonly>
            </div>
          </div>
        </div>

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
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import '../../assets/styles/variables';
@import '../../assets/styles/mixins';


main {
  display: flex;
  flex-direction: column;
  gap: 16px;

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

    .neurobox {
      display: flex;
      flex-direction: column;

      h3 {
        padding: 5px 10px 0 10px;
        color: $txt-aside;
      }

      h4 {
        padding: 10px;

        .p-total {
          color: $logo-color;
        }
      }

      .neuro {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0 10px;

        @include mq(m) {
          display: grid;
          grid-template-columns: 1fr 1fr;
        }

        .register-field {
          gap: 2px;
          flex: 1;
          color: $txt-title;
        }

        &__result {
          display: flex;
          flex-direction: column;
          gap: 2px;
          font-weight: 500;

          input {
            @include createInput();
            font-weight: 500;
          }

          input {
            background-color: rgb(232, 241, 243);
            width: 80px;

            @include mq(m) {
              width: 100%;
            }
          }
        }
      }
    }
  }
}
</style>