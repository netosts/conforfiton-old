<script setup>
import http from '../../services/api/http';
import { getStudentAvaliar } from '../../services/api/get';

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
  rm: computed(() => {
    if (supino.pesoLevantado === undefined || supino.reps === undefined) {
      return;
    }
    return calcular1RM(supino.pesoLevantado, supino.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(supino.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.5) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.9)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.85)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.3) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.8)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.2) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.7)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.1) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.65)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.6)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.9) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.55)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.8) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.5)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.7) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.45)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.35)) {
        return 1;
      }
    }
  }),
});

const roscaDireta = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => {
    if (roscaDireta.pesoLevantado === undefined || roscaDireta.reps === undefined) {
      return;
    }
    return calcular1RM(roscaDireta.pesoLevantado, roscaDireta.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(roscaDireta.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.7) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.5)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.65) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.45)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.42)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.55) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.38)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.5) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.35)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.45) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.32)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.28)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.35) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.25)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.3) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.21)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.25) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.18)) {
        return 1;
      }
    }
  }),
});

const puxadaPelaFrente = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => {
    if (puxadaPelaFrente.pesoLevantado === undefined || puxadaPelaFrente.reps === undefined) {
      return;
    }
    return calcular1RM(puxadaPelaFrente.pesoLevantado, puxadaPelaFrente.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(puxadaPelaFrente.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.2) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.85)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.15) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.8)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.1) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.75)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.05) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.73)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.7)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.95) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.65)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.9) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.63)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.85) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.6)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.8) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.55)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.75) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.5)) {
        return 1;
      }
    }
  }),
});

const legPress = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => {
    if (legPress.pesoLevantado === undefined || legPress.reps === undefined) {
      return;
    }
    return calcular1RM(legPress.pesoLevantado, legPress.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(legPress.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 3) || (student.value.sexo === 'Feminino' && forcaRelativa >= 2.7)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 2.8) || (student.value.sexo === 'Feminino' && forcaRelativa >= 2.5)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 2.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 2.3)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 2.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 2.1)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 2.2) || (student.value.sexo === 'Feminino' && forcaRelativa >= 2)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 2) || (student.value.sexo === 'Feminino' && forcaRelativa >= 1.8)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.8) || (student.value.sexo === 'Feminino' && forcaRelativa >= 1.6)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 1.4)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 1.2)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 1.2) || (student.value.sexo === 'Feminino' && forcaRelativa >= 1)) {
        return 1;
      }
    }
  }),
});

const extensaoDeJoelhos = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => {
    if (extensaoDeJoelhos.pesoLevantado === undefined || extensaoDeJoelhos.reps === undefined) {
      return;
    }
    return calcular1RM(extensaoDeJoelhos.pesoLevantado, extensaoDeJoelhos.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(extensaoDeJoelhos.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.8) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.7)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.75) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.65)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.7) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.6)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.65) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.55)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.52)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.55) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.5)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.5) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.45)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.45) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.4)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.35)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.35) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.3)) {
        return 1;
      }
    }
  }),
});

const flexaoDeJoelhos = reactive({
  pesoLevantado: undefined,
  reps: undefined,
  rm: computed(() => {
    if (flexaoDeJoelhos.pesoLevantado === undefined || flexaoDeJoelhos.reps === undefined) {
      return;
    }
    return calcular1RM(flexaoDeJoelhos.pesoLevantado, flexaoDeJoelhos.reps)
  }),
  pontos: computed(() => {
    if (student.value) {
      const forcaRelativa = calcularForcaRelativa(flexaoDeJoelhos.rm, student.value.peso)
      if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.7) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.6)) {
        return 10;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.65) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.55)) {
        return 9;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.6) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.52)) {
        return 8;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.55) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.5)) {
        return 7;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.5) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.45)) {
        return 6;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.45) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.4)) {
        return 5;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.4) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.35)) {
        return 4;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.35) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.3)) {
        return 3;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.3) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.25)) {
        return 2;
      } else if ((student.value.sexo === 'Masculino' && forcaRelativa >= 0.25) || (student.value.sexo === 'Feminino' && forcaRelativa >= 0.2)) {
        return 1;
      }
    }
  }),
});

const pontosTotal = computed(() => {
  if (!(supino.pontos + roscaDireta.pontos + puxadaPelaFrente.pontos + legPress.pontos + extensaoDeJoelhos.pontos + flexaoDeJoelhos.pontos)) {
    return;
  }
  return supino.pontos + roscaDireta.pontos + puxadaPelaFrente.pontos + legPress.pontos + extensaoDeJoelhos.pontos + flexaoDeJoelhos.pontos;
});


// FUNCTIONS
function calcular1RM(pesoLevantado, reps) {
  const table = {
    1: 100,
    2: 95,
    3: 93,
    4: 90,
    5: 87,
    6: 85,
    7: 83,
    8: 80,
    9: 77,
    10: 75,
    11: 70,
    12: 67,
    15: 65,
  }

  return Number((pesoLevantado * 100 / table[reps]).toFixed(1));
};

function calcularForcaRelativa(RM, pesoCorporal) {
  return RM / pesoCorporal;
};

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
        gap: 20px;
        padding: 0 10px;

        @include mq(m) {
          display: grid;
          grid-template-columns: 1fr 1fr;
        }

        .register-field {
          flex: 1;
        }

        &__result {
          @include inputContainers();

          input {
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