<script setup>
import { useRoute } from 'vue-router';
import { ref, reactive } from 'vue';

import { Form } from 'vee-validate';
import RegisterField from '../../components/RegisterField.vue';

// VARIABLES
const count = ref(0);
const radioDisabled = ref(false);

// Form variables
const form = reactive({
  peso: '', q1: '', q2: '', q3: '', q4: '', q5: '', q6: '', q7: '',
  q8: '', q9: '', q10: '', q11: '', q12: '', q13: '', q14: '', q15: '',
  q16: '', q17: '', q18: '', q19: '', q20: '', q21: '', q22: '',
  q23: '', q24: '', q25: '', q26: '', q27: '', q28: '', q29: '',
  q30: '', q31: '', q32: '', q33: '', q34: '', q35: ''
});

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
  q22: 'required|maxLength:100|asymbol',
  q23: 'required|maxLength:100|asymbol',
  q24: 'required|maxLength:100|asymbol',
  q25: 'required|between:0,10',
  q26: 'required|maxLength:100|asymbol',
  q27: 'required|maxLength:100|asymbol',
};

// Lists
const q3Radio = [{ label: 'Parado', value: 'Parado' }, { label: 'Treinando', value: 'Treinando' }];
const days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];

// FUNCTIONS
function onSubmit() {
  console.log("form submitted");
  console.log(form);
};

function onReset() {
  location.reload();
};

function plus() {
  console.log('count', count.value);
  console.log('form', form.q14);
  if (count.value >= form.q14) {
    count.value = form.q14 - 1;
  } else {
    count.value++;
  }
};

function isRadioDisabled(q14Value) {
  if (q14Value !== '' && count.value >= q14Value) {
    radioDisabled.value = true;
    return true;
  } else {
    radioDisabled.value = false;
    return false;
  }
};
</script>

<template>
  <main>
    <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ meta }" class="form">

      <RegisterField v-model="form.peso" name="peso" type="number" :meta="meta" label="Qual seu peso?"
        placeholder="Ex: 90.30" />

      <RegisterField v-model="form.q1" name="q1" type="textarea" :meta="meta" rows="2"
        label="Quais são seus objetivos com o início de um programa de treinamento físico?" />

      <RegisterField v-model="form.q2" name="q2" type="text" :meta="meta" label="Desses, qual o principal?"
        :class="{ 'input--disabled': !form.q1 }" :tabindex="!form.q1 ? '1' : null" />

      <RegisterField v-model="form.q3" name="q3" type="radio" :radios="q3Radio" :meta="meta"
        label="Você está parado(a) ou treinando?" />

      <RegisterField v-model="form.q4" name="q4" type="text" :meta="meta" label="Há quanto tempo?"
        :class="{ 'input--disabled': !form.q3 }" :tabindex="!form.q3 ? '1' : null" />

      <RegisterField v-model="form.q5" name="q5" type="textarea" :meta="meta" rows="2"
        label="Como é ou era o seu último treino" />

      <RegisterField v-model="form.q6" name="q6" type="text" :meta="meta"
        label="Existe algum exercício que você não gosta de fazer?" />

      <RegisterField v-model="form.q7" name="q7" type="text" :meta="meta" label="Por que?"
        :class="{ 'input--disabled': !form.q6 }" :tabindex="!form.q6 ? '1' : null" />

      <RegisterField v-model="form.q8" name="q8" type="text" :meta="meta" label="Qual exercício você ama fazer?" />

      <RegisterField v-model="form.q9" name="q9" type="text" :meta="meta" label="Por que?"
        :class="{ 'input--disabled': !form.q8 }" :tabindex="!form.q8 ? '1' : null" />

      <RegisterField v-model="form.q10" name="q10" type="text" :meta="meta"
        label="Em quanto tempo você concluía seu treino?" />

      <RegisterField v-model="form.q11" name="q11" type="text" :meta="meta" label="Tem restrição de tempo para treinar?"
        span="Um treino de 30 a 50 minutos seria suficiente!" />

      <RegisterField v-model="form.q12" name="q12" type="text" :meta="meta"
        label="Quanto tempo de treino você tem disponível por dia?" />

      <RegisterField v-model="form.q13" name="q13" type="text" :meta="meta" label="Qual será o local de treino?"
        span="(Academia; academia do prédio; casa; parque; etc)" />

      <RegisterField v-model="form.q14" name="q14" type="number" :meta="meta"
        label="Quantos dias da semana você tem disponibilidade para treinar?" />

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
          <tr v-for="day, index in days" :key="day">
            <td>{{ day }}</td>
            <td>
              <input v-model="form[`q${index + 15}`]" :name="`q${index + 15}`" value="Manhã" type="radio" @click="plus"
                :disabled="isRadioDisabled(form.q14)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
            <td>
              <input v-model="form[`q${index + 15}`]" :name="`q${index + 15}`" value="Tarde" type="radio" @click="plus"
                :disabled="isRadioDisabled(form.q14)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
            <td>
              <input v-model="form[`q${index + 15}`]" :name="`q${index + 15}`" value="Noite" type="radio" @click="plus"
                :disabled="isRadioDisabled(form.q14)" :tabindex="!form.q14 ? '-1' : null" />
            </td>
          </tr>
        </tbody>
      </table>

      <RegisterField v-model="form.q22" name="q22" type="text" :meta="meta"
        label="Você está fazendo dieta orientado(a) por nutricionista?" />

      <RegisterField v-model="form.q23" name="q23" type="text" :meta="meta"
        label="Está sendo acompanhado(a) por nutrologista ou endocrinologista?" />

      <RegisterField v-model="form.q24" name="q24" type="text" :meta="meta"
        label="Descreva rapidamente sua rotina alimentar!" />

      <RegisterField v-model="form.q25" name="q25" type="text" :meta="meta"
        label="De 0 a 10 como você classifica seu sono." span="sendo 0 para..." />

      <RegisterField v-model="form.q26" name="q26" type="text" :meta="meta" label="Qual sua profissão?" />

      <RegisterField v-model="form.q27" name="q27" type="text" :meta="meta"
        label="Em sua profissão você fica muito tempo sentado(a), em movimento ou realiza trabalho braçal?" />

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
  background-color: white;
  border-radius: $border-radius;
  box-shadow: $box-shadow;

  .form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 16px;

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