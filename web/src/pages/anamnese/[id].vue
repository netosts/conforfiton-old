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
const q3Calc = ref(null);
const transformTime = ref('dia');

for (let i = 1; i < 27; i++) {
  Object.defineProperty(form.value, `q${i}`, {
    value: i === 12 ? [] : undefined,
    writable: true,
  });
};

Object.defineProperty(form.value, 'q3', {
  value: {
    treinando: undefined,
    tempo: undefined,
  },
  writable: true,
});

// Validation schema
const schema = {
  peso: 'required|between:0,600|maxDecimal:2',
  q1: 'required|maxLength:255|asymbol',
  q2: 'required|maxLength:100|asymbol',
  q3a: 'required',
  q3b: 'required|between:0,100',
  q4: 'required|maxLength:255|asymbol',
  q5: 'required|maxLength:100|asymbol',
  q6: 'required|maxLength:100|asymbol',
  q7: 'required|maxLength:100|asymbol',
  q8: 'required|maxLength:100|asymbol',
  q9: 'required|maxLength:100|asymbol',
  q10: 'required|maxLength:100|asymbol',
  q11: 'required|between:0,7',
  q13: 'required',
  q14: 'required',
  q15: 'required|maxLength:100|asymbol',
  q16: 'required|between:1,10',
  q17: 'required|maxLength:100|asymbol',
  q18: 'required|maxLength:100|asymbol',
  q19: 'required',
  q20: 'maxLength:255|asymbol',
  q21: 'required|maxLength:100|asymbol',
  q22: 'required|maxLength:100|asymbol',
  q23: 'required|maxLength:100|asymbol',
  q24: 'required|maxLength:100|asymbol',
  q25: 'required|maxLength:100|asymbol',
  q26: 'maxLength:255|asymbol',
};

// Lists
const q3Radio = [{ label: 'Parado', value: false }, { label: 'Treinando', value: true }];
const YesOrNoRadio = [{ label: 'Sim', value: true }, { label: 'Não', value: false }];

const days = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

// FUNCTIONS
function onSubmit(values, { setFieldError }) {
  let errors = 0
  // q20 is required if q19 answer was Yes
  if (form.value.q19 && (form.value.q20 === undefined || typeof form.value.q20 === 'string' && form.value.q20.trim().length === 0)) {
    setFieldError('q20', 'Se sim, este campo precisa ser preenchido.');
    errors++;
  }

  // q11 and table(q12) is related
  if (form.value.q12.length < form.value.q11) {
    setFieldError('q11', 'Dia(s) da semana não preenchido(s). ↓');
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

function pushToTable(value) {
  const formQ = form.value.q12;
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
  // console.log('Big O Alert!');
  const formQ = form.value.q12;
  const hasDay = formQ.some(item => item.day === value);
  if (formQ.length >= form.value.q11 && !hasDay) {
    return true;
  }
};

function pushToTime() {
  if (transformTime.value === 'dia') {
    form.value.q3.tempo = q3Calc.value
  }
  if (transformTime.value === 'mes') {
    form.value.q3.tempo = q3Calc.value * 30
  }
  if (transformTime.value === 'ano') {
    form.value.q3.tempo = q3Calc.value * 365
  }
};

async function initStudent() {
  student.value = await getStudentCredentials(http, route.params.id);
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

      <TextField v-model="form.peso" name="peso" :meta="meta" type="number" label="Qual seu peso?"
        placeholder="Ex: 90.30" />

      <TextField v-model="form.q1" name="q1" :meta="meta" type="textarea" rows="2"
        label="Quais são seus objetivos com o início de um programa de treinamento físico?" />

      <TextField v-model="form.q2" name="q2" :meta="meta" type="text" label="Desses, qual o principal?"
        :class="{ 'input--disabled': !form.q1 }" :tabindex="!form.q1 ? '-1' : null" />

      <TextField v-model="form.q3.treinando" name="q3a" :meta="meta" type="radio" :radios="q3Radio"
        label="Você está parado(a) ou treinando?" />

      <div class="q3time" :class="{ 'input--disabled': form.q3.treinando === undefined }">
        <TextField v-model="q3Calc" @input="pushToTime" name="q3b" :meta="meta" type="number" label="Há quanto tempo?"
          :tabindex="form.q3.treinando === undefined ? '-1' : null" />

        <div class="q3time__select">
          <label for="q3c">Dia/Mês/Ano</label>
          <select v-model="transformTime" @change="pushToTime" id="q3c">
            <option value="dia">Dia(s)</option>
            <option value="mes">Mês</option>
            <option value="ano">Ano</option>
          </select>
        </div>
      </div>

      <TextField v-model="form.q4" name="q4" :meta="meta" type="textarea" rows="2"
        label="Como é ou era o seu último treino" />

      <TextField v-model="form.q5" name="q5" :meta="meta" type="text"
        label="Existe algum exercício que você não gosta de fazer? Por que?" />

      <TextField v-model="form.q6" name="q6" :meta="meta" type="text" label="E qual exercício você ama fazer? Por que?" />

      <TextField v-model="form.q7" name="q7" :meta="meta" type="text" label="Em quanto tempo você concluía seu treino?" />

      <TextField v-model="form.q8" name="q8" :meta="meta" type="text" label="Tem restrição de tempo para treinar?"
        span="Um treino de 30 a 50 minutos seria suficiente!" />

      <TextField v-model="form.q9" name="q9" :meta="meta" type="text"
        label="Quanto tempo de treino você tem disponível por dia?" />

      <TextField v-model="form.q10" name="q10" :meta="meta" type="text" label="Qual será o local de treino?"
        span="(Academia; academia do prédio; casa; parque; etc)" />

      <TextField v-model="form.q11" name="q11" :meta="meta" type="number"
        label="Quantos dias da semana você tem disponibilidade para treinar?" />

      <table :class="{ 'input--disabled': !form.q11 }">
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
              <input :name="`${day}`" :value="{ day, value: 1 }" type="checkbox" @change="pushToTable({ day, value: 1 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q11 ? '-1' : null" />
            </td>
            <td>
              <input :name="`${day}`" :value="{ day, value: 2 }" type="checkbox" @change="pushToTable({ day, value: 2 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q11 ? '-1' : null" />
            </td>
            <td>
              <input :name="`${day}`" :value="{ day, value: 3 }" type="checkbox" @change="pushToTable({ day, value: 3 })"
                :disabled="disableCheckbox(day)" :tabindex="!form.q11 ? '-1' : null" />
            </td>
          </tr>
        </tbody>
      </table>

      <TextField v-model="form.q13" name="q13" :meta="meta" type="radio" :radios="YesOrNoRadio"
        label="Você está fazendo dieta orientado(a) por nutricionista?" />

      <TextField v-model="form.q14" name="q14" :meta="meta" type="radio" :radios="YesOrNoRadio"
        label="Está sendo acompanhado(a) por nutrologista ou endocrinologista?" />

      <TextField v-model="form.q15" name="q15" :meta="meta" type="text"
        label="Descreva rapidamente sua rotina alimentar!" />

      <TextField v-model="form.q16" name="q16" :meta="meta" type="number" label="De 1 a 10 como você classifica seu sono."
        span="(Sendo 1 para péssimo e 10 para excelente)" />

      <TextField v-model="form.q17" name="q17" :meta="meta" type="text" label="Qual sua profissão?" />

      <TextField v-model="form.q18" name="q18" :meta="meta" type="text"
        label="Em sua profissão você fica muito tempo sentado(a), em movimento ou realiza trabalho braçal?" />

      <TextField v-model="form.q19" name="q19" :meta="meta" type="radio" :radios="YesOrNoRadio"
        label="Você tem algum tipo de dor ou desconforto (muscular ou articular)?" />

      <TextField v-model="form.q20" name="q20" :meta="meta" type="textarea" rows="2" v-show="form.q19"
        label="Se sim, onde? Leve ou aguda? Esporádica ou crônica? Qual a intensidade dessa(s) dor(es) de 0 a 10?" />

      <TextField v-model="form.q21" name="q21" :meta="meta" type="text" rows="2"
        label="Alguma patologia (doença) diagnosticada por algum médico?"
        span="(Hipertensão; doenças cardíacas; diabetes; etc)" />

      <TextField v-model="form.q22" name="q22" :meta="meta" type="text"
        label="Faz uso de medicamentos de forma rotineira? Se sim, quais?" />

      <TextField v-model="form.q23" name="q23" :meta="meta" type="text"
        label="Seu médico já mencionou alguma vez que você tem alguma condição cardíaca e que você só deve realizar atividade física recomendada por um médico?" />

      <TextField v-model="form.q24" name="q24" :meta="meta" type="text"
        label="Seu médico sabe que você está ingressando em um programa de treinamento físico?" />

      <TextField v-model="form.q25" name="q25" :meta="meta" type="text" label="Você tem alguma meta para atingir?"
        span="Ex: uma data; uma festa ou evento; uma roupa; etc." />

      <TextField v-model="form.q26" name="q26" :meta="meta" type="textarea"
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

    .q3time {
      display: flex;
      gap: 20px;

      .register-field {
        flex: 1;
      }

      &__select {
        display: flex;
        flex-direction: column;
        gap: 5px;
        flex: 1;

        select {
          @include createInput();
        }
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