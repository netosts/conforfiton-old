<script setup>
import http from '../../services/api/http';
import { getStudentCredentials } from '../../services/api/get';

import { ref, onMounted } from 'vue';
import { useRoute, definePage } from 'vue-router/auto'

import { Form } from 'vee-validate';
import TextField from '../../components/TextField.vue';


definePage({
  meta: { isStudent: true, requiresAuth: true }
});

// VARIABLES
const route = useRoute();
const student = ref(null);

// Form variables
const form = ref({ peso: null })
for (let i = 1; i < 30; i++) {
  Object.defineProperty(form.value, `q${i}`, {
    value: i === 15 ? [] : undefined,
    writable: true,
  });
};

// Validation schema
const schema = {
  peso: 'required|between:0,600|maxDecimal:2',
  q1: 'required|maxLength:255|asymbol',
  q2: 'required|maxLength:100|asymbol',
  q3: 'required',
  q4: 'required|maxLength:100|asymbol',
  q5: 'required|maxLength:255|asymbol',
  q6: 'required|maxLength:100|asymbol',
  q7: 'required|maxLength:100|asymbol',
  q8: 'required|maxLength:100|asymbol',
  q9: 'required|maxLength:100|asymbol',
  q10: 'required|maxLength:100|asymbol',
  q11: 'required|maxLength:100|asymbol',
  q12: 'required|maxLength:100|asymbol',
  q13: 'required|maxLength:100|asymbol',
  q14: 'required|between:0,7',
  q16: 'required|maxLength:100|asymbol',
  q17: 'required|maxLength:100|asymbol',
  q18: 'required|maxLength:100|asymbol',
  q19: 'required|between:0,10',
  q20: 'required|maxLength:100|asymbol',
  q21: 'required|maxLength:100|asymbol',
  q22: 'required',
  q23: 'maxLength:100|asymbol',
  q24: 'required|maxLength:100|asymbol',
  q25: 'required|maxLength:100|asymbol',
  q26: 'required|maxLength:100|asymbol',
  q27: 'required|maxLength:100|asymbol',
  q28: 'required|maxLength:100|asymbol',
  q29: 'maxLength:255|asymbol',
};

// Lists
const q3Radio = [{ label: 'Parado', value: 'Parado' }, { label: 'Treinando', value: 'Treinando' }];
const q22Radio = [{ label: 'Sim', value: 'Sim' }, { label: 'Não', value: 'Não' }];
const days = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

// FUNCTIONS
function onSubmit(values, { setFieldError }) {
  let errors = 0
  // q29 is required if q28 answer was Yes
  if (form.q28 === 'Sim' && form.q29 === '') {
    setFieldError('q29', 'Se sim, este campo precisa ser preenchido.');
    errors++;
  }

  if (errors === 0) {
    console.log("form submitted");
  }
  console.log(form);
};

function onReset() {
  location.reload();
};

function pushToForm(value) {
  const formQ = form.value.q15;
  if (!formQ.length) {
    formQ.push({ day: value.day, periods: [value.value] });
    return;
  }
  const hasDay = formQ.some(item => item.day === value.day)
  if (hasDay) {
    const index = formQ.findIndex(item => item.day === value.day)
    if (formQ[index].periods.some(item => item === value.value)) {
      const indexValue = formQ[index].periods.findIndex(item => item === value.value)
      formQ[index].periods.splice(indexValue, 1)
      if (!formQ[index].periods.length) {
        formQ.splice(index, 1);
      }
    } else {
      formQ[index].periods.push(value.value)
    }
  } else {
    formQ.push({ day: value.day, periods: [value.value] });
  }
};

function disableCheckbox(value) {
  console.log('Big O Alert!');
  const formQ = form.value.q15;
  const hasDay = formQ.some(item => item.day === value);
  if (formQ.length >= form.value.q14 && !hasDay) {
    return true;
  }
};

async function initStudent() {
  student.value = await getStudentCredentials(http, route.params.id);
  console.log(student.value)
};

// DOM Mount
onMounted(() => {
  initStudent();
});
</script>

<template>
  <main>

    <RouterLink to="/" class="voltar">
      <font-awesome-icon icon="fa-solid fa-arrow-left" />
      voltar
    </RouterLink>

    <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ meta }" class="form">

      <div class="form__title">
        <h1>Formulário Anamnese</h1>
        <h2>{{ student ? student.nmPessoa : '' }}</h2>
      </div>

      <TextField v-model="form.peso" name="peso" type="number" :meta="meta" label="Qual seu peso?"
        placeholder="Ex: 90.30" />

      <TextField v-model="form.q1" name="q1" type="textarea" :meta="meta" rows="2"
        label="Quais são seus objetivos com o início de um programa de treinamento físico?" />

      <TextField v-model="form.q2" name="q2" type="text" :meta="meta" label="Desses, qual o principal?"
        :class="{ 'input--disabled': !form.q1 }" :tabindex="!form.q1 ? '1' : null" />

      <TextField v-model="form.q3" name="q3" type="radio" :radios="q3Radio" :meta="meta"
        label="Você está parado(a) ou treinando?" />

      <TextField v-model="form.q4" name="q4" type="text" :meta="meta" label="Há quanto tempo?"
        :class="{ 'input--disabled': !form.q3 }" :tabindex="!form.q3 ? '1' : null" />

      <TextField v-model="form.q5" name="q5" type="textarea" :meta="meta" rows="2"
        label="Como é ou era o seu último treino" />

      <TextField v-model="form.q6" name="q6" type="text" :meta="meta"
        label="Existe algum exercício que você não gosta de fazer?" />

      <TextField v-model="form.q7" name="q7" type="text" :meta="meta" label="Por que?"
        :class="{ 'input--disabled': !form.q6 }" :tabindex="!form.q6 ? '1' : null" />

      <TextField v-model="form.q8" name="q8" type="text" :meta="meta" label="Qual exercício você ama fazer?" />

      <TextField v-model="form.q9" name="q9" type="text" :meta="meta" label="Por que?"
        :class="{ 'input--disabled': !form.q8 }" :tabindex="!form.q8 ? '1' : null" />

      <TextField v-model="form.q10" name="q10" type="text" :meta="meta"
        label="Em quanto tempo você concluía seu treino?" />

      <TextField v-model="form.q11" name="q11" type="text" :meta="meta" label="Tem restrição de tempo para treinar?"
        span="Um treino de 30 a 50 minutos seria suficiente!" />

      <TextField v-model="form.q12" name="q12" type="text" :meta="meta"
        label="Quanto tempo de treino você tem disponível por dia?" />

      <TextField v-model="form.q13" name="q13" type="text" :meta="meta" label="Qual será o local de treino?"
        span="(Academia; academia do prédio; casa; parque; etc)" />

      <TextField v-model="form.q14" name="q14" type="number" :meta="meta"
        label="Quantos dias da semana você tem disponibilidade para treinar?" />

      <!-- :class="{ 'input--disabled': !form.q14 }" -->
      <table :class="{ 'input--disabled': !form.q14 }">
        <thead>
          <tr>
            <th></th>
            <th>Manhã</th>
            <th>Tarde</th>
            <th>Noite</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="day in days" :key="day">
            <td>{{ day }}</td>
            <td>
              <input :name="`${day}`" :value="{ day, value: 1 }" type="checkbox" @change="pushToForm({ day, value: 1 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
            <td>
              <input :name="`${day}`" :value="{ day, value: 2 }" type="checkbox" @change="pushToForm({ day, value: 2 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
            <td>
              <input :name="`${day}`" :value="{ day, value: 3 }" type="checkbox" @change="pushToForm({ day, value: 3 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
          </tr>
        </tbody>
      </table>

      <TextField v-model="form.q16" name="q16" type="text" :meta="meta"
        label="Você está fazendo dieta orientado(a) por nutricionista?" />

      <TextField v-model="form.q17" name="q17" type="text" :meta="meta"
        label="Está sendo acompanhado(a) por nutrologista ou endocrinologista?" />

      <TextField v-model="form.q18" name="q18" type="text" :meta="meta"
        label="Descreva rapidamente sua rotina alimentar!" />

      <TextField v-model="form.q19" name="q19" type="text" :meta="meta" label="De 0 a 10 como você classifica seu sono."
        span="(Sendo 0 para péssimo e 10 para excelente)" />

      <TextField v-model="form.q20" name="q20" type="text" :meta="meta" label="Qual sua profissão?" />

      <TextField v-model="form.q21" name="q21" type="text" :meta="meta"
        label="Em sua profissão você fica muito tempo sentado(a), em movimento ou realiza trabalho braçal?" />

      <TextField v-model="form.q22" name="q22" type="radio" :meta="meta" :radios="q22Radio"
        label="Você tem algum tipo de dor ou desconforto (muscular ou articular)?" />

      <TextField v-model="form.q23" name="q23" type="text" :meta="meta" rows="2" v-show="form.q22 === 'Sim'"
        label="Se sim, onde? Leve ou aguda? Esporádica ou crônica? Qual a intensidade dessa(s) dor(es) de 0 a 10?" />

      <TextField v-model="form.q24" name="q24" type="text" :meta="meta" rows="2"
        label="Alguma patologia (doença) diagnosticada por algum médico?"
        span="(Hipertensão; doenças cardíacas; diabetes; etc)" />

      <TextField v-model="form.q25" name="q25" type="text" :meta="meta"
        label="Faz uso de medicamentos de forma rotineira? Se sim, quais?" />

      <TextField v-model="form.q26" name="q26" type="text" :meta="meta"
        label="Seu médico já mencionou alguma vez que você tem alguma condição cardíaca e que você só deve realizar atividade física recomendada por um médico?" />

      <TextField v-model="form.q27" name="q27" type="text" :meta="meta"
        label="Seu médico sabe que você está ingressando em um programa de treinamento físico?" />

      <TextField v-model="form.q28" name="q28" type="text" :meta="meta" label="Você tem alguma meta para atingir?"
        span="Ex: uma data; uma festa ou evento; uma roupa; etc." />

      <TextField v-model="form.q29" name="q29" type="textarea" :meta="meta"
        label="Existe algo que você acredita ser relevante me contar para personalizar ainda mais o seu treino? Essa é a hora!!! Vamos que vamos, pois juntos e com compromisso somos mais fortes! Obrigado pela confiança." />

      <div class="form__submit">
        <div class="submit" :class="{ 'submit--disabled': !meta.valid }">
          <button type="submit" class="submit__btn">Concluir</button>
        </div>
        <button type="button" class="reset" @click="onReset">Reiniciar</button>
      </div>
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

  .voltar {
    font-weight: 600;
    text-decoration: none;
    color: $logo-color;
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 16px;
    background-color: white;
    border-radius: $border-radius;
    box-shadow: $box-shadow;

    &__title {
      padding: 10px;
      margin-bottom: 10px;
      text-align: center;
      border-bottom: 3px dotted $background;

      h1 {
        color: $buttons;
      }

      h2 {
        color: $txt-subtitle;
      }
    }

    table {
      border-collapse: collapse;
      border: 1px solid $input-border;

      th,
      td {
        border: 1px solid $input-border;
        padding: 8px;
        text-align: center;
      }

      th {
        background-color: $buttons;
        color: white;
      }

      td {
        font-weight: 500;
        color: $txt-aside;
      }
    }

    &__submit {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 20px;

      .submit {
        display: flex;
        flex: 1;

        &__btn {
          flex: 1;
          @include submitButtons($validation, white);
        }

        &--disabled {
          opacity: 0.5;
          cursor: not-allowed;

          .submit__btn {
            pointer-events: none;
          }
        }
      }

      .reset {
        @include submitButtons($profile-pic, $txt-title);
      }

    }
  }
}

.input--disabled {
  opacity: 0.5;
  pointer-events: none;
}
</style>