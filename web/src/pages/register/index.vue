<script setup>
import {
  countCpfDuplicate,
  countRgUfDuplicate,
  countEmailDuplicate,
} from "../../services/api/get";
import { postStudent, postAnamnese } from "../../services/api/post";
import {
  ufList,
  sexoList,
  camisaList,
  shortsList,
  q4Radio,
  YesOrNoRadio,
  days,
} from "../../services/configs/lists";
import { registerSchema } from "../../services/configs/schemas";

import { ref } from "vue";
import { definePage } from "vue-router/auto";

import { form } from "../../services/configs/forms/register";
import { Form } from "vee-validate";
import TextField from "../../components/TextField.vue";
import SubmitButton from "../../components/SubmitButton.vue";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const q4Calc = ref(null);
const transformTime = ref("dia");

// FUNCTIONS
async function onSubmit(values, { setFieldError, setErrors }) {
  let errors = 0;

  // REGISTER
  // CPF and Email Duplicate validation
  form.cpf_cnpj = form.cpf_cnpj.replace(/\D/g, ""); // only digits
  const [countedCpf, countedEmail] = await Promise.all([
    countCpfDuplicate(form.cpf_cnpj),
    countEmailDuplicate(form.ds_email),
  ]);

  if (countedCpf > 0) {
    setFieldError("cpf", "O CPF já foi cadastrado.");
    errors++;
  }

  if (countedEmail > 0) {
    setFieldError("email", "Este email já foi cadastrado.");
    errors++;
  }

  // RG and UF must be together
  if (
    (form.rg !== "" && form.uf_rg === "") ||
    (form.uf_rg !== "" && form.rg === "")
  ) {
    setErrors({
      rg: "O RG e UF precisam ser cadastrados juntos.",
      uf: " ",
    });
    errors++;
  } else if (form.rg !== "" && form.uf_rg !== "") {
    // RG in UF Duplicate validation
    const countedRgUf = await countRgUfDuplicate(form.rg, form.uf_rg);
    if (countedRgUf > 0) {
      setFieldError("rg", `O RG já foi cadastrado em ${form.uf_rg}.`);
      errors++;
    }
  }

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
    // only proceed without errors
    return;
  }

  // SUBMIT
  // Get the current date and time and use as dtData
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  // Format problematic values before posting
  form.dt_data = formattedDate;
  form.rg = form.rg.replace(/\D/g, ""); // only digits
  form.telefone = form.telefone.replace(/\D/g, ""); // only digits

  // Post new student
  try {
    console.log(form);
    postStudent(form);
    await delay(2000);
    postAnamnese(form);
    console.log("form submitted");
  } catch (e) {
    console.error(e);
  }
}

function pushToTable(value) {
  const formQ = form.q13;
  if (!formQ.length) {
    formQ.push({ day: value.day, periods: [value.value] });
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
    formQ.push({ day: value.day, periods: [value.value] });
  }
}

function disableCheckbox(value) {
  // console.log('Big O Alert!');
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

async function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
</script>

<template>
  <main>
    <div class="top">
      <RouterLink to="/" class="voltar">
        <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
      </RouterLink>
      <h1>Bem-Vindo</h1>
    </div>

    <Form
      @submit="onSubmit"
      :validation-schema="registerSchema"
      v-slot="{ meta }"
      class="form"
    >
      <section class="form__section">
        <div class="form__section__title">
          <h2>Informações de Cadastro</h2>
        </div>
        <TextField
          v-model="form.nm_pessoa"
          :meta="meta"
          name="name"
          type="text"
          label="Nome completo"
          required="*"
          placeholder="Digite seu nome completo"
        />
        <div class="form__section__1-1sm">
          <TextField
            v-model="form.cpf_cnpj"
            :meta="meta"
            name="cpf"
            type="text"
            label="CPF"
            required="*"
            placeholder="Digite seu CPF"
          />
          <div class="form__section__1-1sm__1sm">
            <TextField
              v-model="form.rg"
              :meta="meta"
              name="rg"
              type="text"
              label="RG"
              placeholder="Digite seu RG"
            />
            <TextField
              v-model="form.uf_rg"
              :meta="meta"
              name="uf"
              type="select"
              label="UF"
              :options="ufList"
            />
          </div>
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.telefone"
            :meta="meta"
            name="telefone"
            type="text"
            label="Telefone"
            required="*"
            placeholder="(00)00000-0000"
          />
          <TextField
            v-model="form.ds_email"
            :meta="meta"
            name="email"
            type="text"
            label="E-mail"
            required="*"
            placeholder="Digite seu Email"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.dt_nascimento"
            :meta="meta"
            type="date"
            name="date"
            label="Data Nascimento"
            required="*"
          />
          <TextField
            v-model="form.sexo"
            :meta="meta"
            name="sexo"
            type="select"
            label="Sexo Biológico"
            required="*"
            :options="sexoList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.tm_camisa"
            :meta="meta"
            name="camisa"
            type="select"
            label="T. Camisa"
            required="*"
            :options="camisaList"
          />
          <TextField
            v-model="form.tm_shorts"
            :meta="meta"
            name="shorts"
            type="select"
            label="T. Shorts"
            required="*"
            :options="shortsList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.altura"
            :meta="meta"
            name="altura"
            type="number"
            label="Altura(cm)"
            required="*"
            placeholder="Ex: 180"
          />
          <TextField
            v-model="form.peso"
            :meta="meta"
            name="peso"
            type="number"
            label="Peso(kg)"
            required="*"
            placeholder="Ex: 90,30"
          />
        </div>
        <TextField
          v-model="form.ds_obs"
          :meta="meta"
          name="dsObs"
          type="textarea"
          label="Observação"
          placeholder="Digite aqui se tiver alguma observação"
        />
      </section>

      <section class="form__section">
        <div class="form__section__title">
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
      </section>

      <div class="form__section">
        <SubmitButton msg="Concluir" :reset="true" :meta="meta" />
      </div>
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
  margin: 10px;

  .top {
    display: flex;
    flex-direction: column;
    padding: 10px;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;
    box-shadow: $box-shadow;

    .voltar {
      position: absolute;
      top: 21px;
      @include tool();
      color: $buttons;
    }

    h1 {
      text-align: center;
      text-transform: uppercase;
    }
  }

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
        margin-bottom: 10px;
        text-align: center;
        border-bottom: 3px dotted $background;

        h2 {
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
