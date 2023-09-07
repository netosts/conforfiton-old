<script setup>
import { postStudent, postAnamnese } from "../../services/api/post";
import { q4Radio, YesOrNoRadio, days } from "../../services/register/lists";

import { getUserIdSession } from "@/services/api/token";
import { translateGender, translateDays } from "@/services/helpers";

import { ref, onMounted } from "vue";
import { definePage, useRouter } from "vue-router/auto";

import { schema } from "../../services/register/schemas/anamnese";
import { form } from "../../services/register/forms/anamnese";

import { Form } from "vee-validate";
import TextField from "../../components/TextField.vue";
import SubmitButton from "../../components/SubmitButton.vue";

definePage({
  meta: { requiresAuth: true },
});

const router = useRouter();
// VARIABLES
const q4Calc = ref(null);
const transformTime = ref("dia");

// FUNCTIONS
async function onSubmit(_, { setFieldError }) {
  let errors = 0;

  // ANAMNESE FORM
  // q21 is required if q20 answer was Yes
  if (
    form.q20 &&
    (!form.q21 ||
      (typeof form.q21 === "string" && form.q21.trim().length === 0))
  ) {
    setFieldError("q21", "Se sim, este campo precisa ser preenchido.");
    errors++;
  }

  // q21 can't have value if q20 answer is No
  if (
    !form.q20 &&
    typeof form.q21 === "string" &&
    form.q21.trim().length !== 0
  ) {
    form.q21 = undefined;
  }

  // q11 and table(q12) is related
  if (form.q13.length < form.q12) {
    setFieldError("q12", "Dia(s) da semana não preenchido(s). ↓");
    errors++;
  }

  if (errors > 0) {
    return;
  }

  // Post new student
  try {
    const studentForm = JSON.parse(sessionStorage.getItem("registerStudent"));

    const userId = getUserIdSession();

    const currentDate = new Date();
    const formattedDate = currentDate.toISOString();

    studentForm.cpf = studentForm.cpf.replace(/\D/g, "");
    studentForm.phone_number = studentForm.phone_number.replace(/\D/g, "");
    studentForm.gender = translateGender(studentForm.gender); // from pt to en
    studentForm.created_at = formattedDate;
    studentForm.personal_id = userId;

    console.log(studentForm);

    await postStudent(studentForm);
    await postAnamnese(form, studentForm.email);

    alert("Cadastro realizado com sucesso!");

    sessionStorage.removeItem("registerStudent");
    sessionStorage.setItem("submitted", true);
    router.push("/");
  } catch (err) {
    console.error(err);
    throw err;
  }
}

function pushToTable(value) {
  const formQ = form.q13;
  if (!formQ.length) {
    formQ.push({ day: translateDays(value.day), periods: [value.value] });
    return;
  }
  const hasDay = formQ.some((item) => item.day === value.day);
  if (hasDay) {
    const index = formQ.findIndex((item) => item.day === value.day);
    if (formQ[index].periods.some((item) => item === value.value)) {
      const indexValue = formQ[index].periods.findIndex(
        (item) => item === value.value
      );
      formQ[index].periods.splice(indexValue, 1);
      if (!formQ[index].periods.length) {
        formQ.splice(index, 1);
      }
    } else {
      formQ[index].periods.push(value.value);
    }
  } else {
    formQ.push({ day: translateDays(value.day), periods: [value.value] });
  }
}

function disableCheckbox(value) {
  const formQ = form.q13;
  const hasDay = formQ.some((item) => item.day === value);
  if (formQ.length >= form.q12 && !hasDay) {
    return true;
  }
}

function pushToTime() {
  if (transformTime.value === "dia") {
    form.q4.tempo = q4Calc.value;
  }
  if (transformTime.value === "mes") {
    form.q4.tempo = q4Calc.value * 30;
  }
  if (transformTime.value === "ano") {
    form.q4.tempo = q4Calc.value * 365;
  }
}

onMounted(() => {
  form.q13 = [];
});
</script>

<template>
  <main>
    <Form
      @submit="onSubmit"
      :validation-schema="schema"
      v-slot="{ meta }"
      class="form"
    >
      <section class="form__section">
        <div class="form__section__title">
          <RouterLink to="/register" class="back">
            <font-awesome-icon icon="fa-solid fa-chevron-left" size="xl" />
          </RouterLink>
          <h2>Formulário Anamnese</h2>
        </div>
        <TextField
          v-model="form.q1"
          name="q1"
          :meta="meta"
          type="textarea"
          rows="2"
          label="Quais são seus objetivos com o início de um programa de treinamento físico?"
        />
        <TextField
          v-model="form.q2"
          name="q2"
          :meta="meta"
          type="text"
          label="Desses, qual o principal?"
          :class="{ 'input--disabled': !form.q1 }"
          :tabindex="!form.q1 ? '-1' : null"
        />
        <TextField
          v-model="form.q3"
          name="q3"
          :meta="meta"
          type="text"
          label="Em quanto tempo espera atingir esses objetivos?"
        />
        <TextField
          v-model="form.q4.treinando"
          name="q4a"
          :meta="meta"
          type="radio"
          :radios="q4Radio"
          label="Você está parado(a) ou treinando?"
        />
        <div
          class="q4time"
          :class="{ 'input--disabled': form.q4.treinando === undefined }"
        >
          <TextField
            v-model="q4Calc"
            @input="pushToTime"
            name="q4b"
            :meta="meta"
            type="number"
            label="Há quanto tempo?"
            :tabindex="form.q4.treinando === undefined ? '-1' : null"
          />
          <div class="q4time__select">
            <label for="q4c">Dia/Mês/Ano</label>
            <select v-model="transformTime" @change="pushToTime" id="q4c">
              <option value="dia">Dia(s)</option>
              <option value="mes">Mês</option>
              <option value="ano">Ano</option>
            </select>
          </div>
        </div>
        <TextField
          v-model="form.q5"
          name="q5"
          :meta="meta"
          type="textarea"
          rows="2"
          label="Como é ou era o seu último treino?"
        />
        <TextField
          v-model="form.q6"
          name="q6"
          :meta="meta"
          type="textarea"
          rows="2"
          label="Existe algum exercício que você não gosta de fazer? Por que?"
        />
        <TextField
          v-model="form.q7"
          name="q7"
          :meta="meta"
          type="textarea"
          rows="2"
          label="E qual exercício você ama fazer? Por que?"
        />
        <TextField
          v-model="form.q8"
          name="q8"
          :meta="meta"
          type="text"
          label="Em quanto tempo você concluía seu treino?"
        />
        <TextField
          v-model="form.q9"
          name="q9"
          :meta="meta"
          type="text"
          label="Tem restrição de tempo para treinar?"
          span="Um treino de 30 a 50 minutos seria suficiente!"
        />
        <TextField
          v-model="form.q10"
          name="q10"
          :meta="meta"
          type="text"
          label="Quanto tempo de treino você tem disponível por dia?"
        />
        <TextField
          v-model="form.q11"
          name="q11"
          :meta="meta"
          type="text"
          label="Qual será o local de treino?"
          span="(Academia; academia do prédio; casa; parque; etc)"
        />
        <TextField
          v-model="form.q12"
          name="q12"
          :meta="meta"
          type="number"
          label="Quantos dias da semana você tem disponibilidade para treinar?"
        />
        <table :class="{ 'input--disabled': !form.q12 }">
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
                <input
                  :name="`${day}`"
                  :value="{ day, value: 1 }"
                  type="checkbox"
                  @change="pushToTable({ day, value: 1 })"
                  :disabled="disableCheckbox(day)"
                  :tabindex="!form.q12 ? '-1' : null"
                />
              </td>
              <td>
                <input
                  :name="`${day}`"
                  :value="{ day, value: 2 }"
                  type="checkbox"
                  @change="pushToTable({ day, value: 2 })"
                  :disabled="disableCheckbox(day)"
                  :tabindex="!form.q12 ? '-1' : null"
                />
              </td>
              <td>
                <input
                  :name="`${day}`"
                  :value="{ day, value: 3 }"
                  type="checkbox"
                  @change="pushToTable({ day, value: 3 })"
                  :disabled="disableCheckbox(day)"
                  :tabindex="!form.q12 ? '-1' : null"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <TextField
          v-model="form.q14"
          name="q14"
          :meta="meta"
          type="radio"
          :radios="YesOrNoRadio"
          label="Você está fazendo dieta orientado(a) por nutricionista?"
        />
        <TextField
          v-model="form.q15"
          name="q15"
          :meta="meta"
          type="radio"
          :radios="YesOrNoRadio"
          label="Está sendo acompanhado(a) por nutrologista ou endocrinologista?"
        />
        <TextField
          v-model="form.q16"
          name="q16"
          :meta="meta"
          type="textarea"
          rows="2"
          label="Descreva rapidamente sua rotina alimentar!"
        />
        <TextField
          v-model="form.q17"
          name="q17"
          :meta="meta"
          type="number"
          label="De 1 a 10 como você classifica seu sono."
          span="(Sendo 1 para péssimo e 10 para excelente)"
        />
        <TextField
          v-model="form.q18"
          name="q18"
          :meta="meta"
          type="text"
          label="Qual sua profissão?"
        />
        <TextField
          v-model="form.q19"
          name="q19"
          :meta="meta"
          type="text"
          label="Em sua profissão você fica muito tempo sentado(a), em movimento ou realiza trabalho braçal?"
        />
        <TextField
          v-model="form.q20"
          name="q20"
          :meta="meta"
          type="radio"
          :radios="YesOrNoRadio"
          label="Você tem algum tipo de dor ou desconforto (muscular ou articular)?"
        />
        <TextField
          v-model="form.q21"
          name="q21"
          :meta="meta"
          type="textarea"
          rows="2"
          v-show="form.q20"
          label="Se sim, onde? Leve ou aguda? Esporádica ou crônica? Qual a intensidade dessa(s) dor(es) de 0 a 10?"
        />
        <TextField
          v-model="form.q22"
          name="q22"
          :meta="meta"
          type="text"
          label="Alguma patologia (doença) diagnosticada por algum médico?"
          span="(Hipertensão; doenças cardíacas; diabetes; etc)"
        />
        <TextField
          v-model="form.q23"
          name="q23"
          :meta="meta"
          type="textarea"
          rows="2"
          label="Faz uso de medicamentos de forma rotineira? Se sim, quais?"
        />
        <TextField
          v-model="form.q24"
          name="q24"
          :meta="meta"
          type="radio"
          :radios="YesOrNoRadio"
          label="Seu médico já mencionou alguma vez que você tem alguma condição cardíaca e que você só deve realizar atividade física recomendada por um médico?"
        />
        <TextField
          v-model="form.q25"
          name="q25"
          :meta="meta"
          type="radio"
          :radios="YesOrNoRadio"
          label="Seu médico sabe que você está ingressando em um programa de treinamento físico?"
        />
        <TextField
          v-model="form.q26"
          name="q26"
          :meta="meta"
          type="text"
          label="Você tem alguma meta para atingir?"
          span="Ex: uma data; uma festa ou evento; uma roupa; etc."
        />
        <TextField
          v-model="form.q27"
          name="q27"
          :meta="meta"
          type="textarea"
          label="Existe algo que você acredita ser relevante me contar para personalizar ainda mais o seu treino? Essa é a hora!!!"
        />
        <p class="final">
          Vamos que vamos, pois juntos e com compromisso somos mais fortes!
          Obrigado pela confiança.
        </p>

        <SubmitButton msg="Concluir" :meta="meta" />
      </section>
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import "../../assets/styles/variables";
@import "../../assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 30px;

  .form {
    display: flex;
    flex-direction: column;
    gap: 16px;

    &__section {
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding: 16px;
      background-color: white;
      border-radius: $border-radius;
      box-shadow: $box-shadow;

      &__title {
        padding: 10px;
        margin-top: -10px;
        margin-bottom: 20px;
        text-align: center;
        border-bottom: 3px dotted $background;

        .back {
          position: absolute;
          top: 40px;
          left: 35px;
          @include tool();
          color: $buttons;
        }

        h2 {
          padding: 0 20px;
          color: $buttons;
        }
      }

      &__1-1 {
        display: flex;
        gap: 20px;

        @include mq(xs-s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }
      }

      &__1-1sm {
        display: flex;
        gap: 20px;

        @include mq(s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }

        &__1sm {
          flex: 1;
          display: grid;
          gap: 20px;
          grid-template-columns: 1fr 80px;

          @include mq(xs) {
            display: flex;
            flex-direction: column;
          }
        }
      }

      &__1-1-1 {
        display: flex;
        gap: 20px;

        @include mq(s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }
      }

      .q4time {
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

      .final {
        margin: 10px;
        font-weight: 500;
        text-align: center;
      }
    }
  }
}

.input--disabled {
  opacity: 0.5;
  pointer-events: none;
}
</style>
