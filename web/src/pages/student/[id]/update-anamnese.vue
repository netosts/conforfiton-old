<script setup>
import { updateAnamnese } from "@/services/api/put";
import {
  q4Radio,
  YesOrNoRadio,
  days,
  updateMenstruationAnswers,
} from "@/services/register/lists";
import { fcMaxFormulas } from "@/services/student/lists";

import { fcmax, calculateL1, calculateL2 } from "@/services/register/helpers";
import {
  transformQ13,
  createAnamneseForm,
} from "@/services/student/update-anamnese/helpers";

import {
  updateTranslateMenstruation,
  translateFcMaxFormula,
  untranslateFcMaxFormula,
  untranslateMenstruation,
  translateDays,
} from "@/services/helpers";

import { reactive, onMounted } from "vue";
import { useStudentStore } from "@/stores/student";
import { definePage, useRoute, useRouter } from "vue-router/auto";

import { schema } from "@/services/register/schemas/anamnese";
import { Form, Field } from "vee-validate";
import TextField from "@/components/TextField.vue";

definePage({
  meta: { requiresAuth: true },
});

const props = defineProps({
  student: Object,
});

const store = useStudentStore();
const route = useRoute();
const router = useRouter();

const form = reactive({
  q1: {
    value: store.anamnese.value?.q1,
    name: "q1",
    type: "textarea",
    rows: "2",
    label:
      "Principal objetivo com o início de um programa de treinamento físico",
    gender: ["Male", "Female"],
  },
  q2: {
    value: store.anamnese.value?.q2,
    name: "q2",
    type: "text",
    label: "Objetivo secundário",
    gender: ["Male", "Female"],
  },
  q3: {
    value: store.anamnese.value?.q3,
    name: "q3",
    type: "text",
    label: "Em quanto tempo espera atingir esses objetivos",
    gender: ["Male", "Female"],
  },
  q4a: {
    value: store.anamnese.value?.q4.training,
    name: "q4a",
    type: "radio",
    radios: q4Radio,
    label: "Está parado ou ativo",
    gender: ["Male", "Female"],
  },
  q4b: {
    value: store.anamnese.value?.q4.time,
    name: "q4b",
    type: "text",
    label: "Há quanto tempo está parado ou ativo",
    gender: ["Male", "Female"],
  },
  q5: {
    value: store.anamnese.value?.q5,
    name: "q5",
    type: "textarea",
    rows: "2",
    label: "Como é ou era o último treino",
    gender: ["Male", "Female"],
  },
  q6: {
    value: store.anamnese.value?.q6,
    name: "q6",
    type: "textarea",
    rows: "2",
    label: "Exercício que não gosta de fazer",
    gender: ["Male", "Female"],
  },
  q7: {
    value: store.anamnese.value?.q7,
    name: "q7",
    type: "textarea",
    rows: "2",
    label: "Exercício que ama fazer",
    gender: ["Male", "Female"],
  },
  q8: {
    value: store.anamnese.value?.q8,
    name: "q8",
    type: "text",
    label: "Em quanto tempo costumava concluir o treino",
    gender: ["Male", "Female"],
  },
  q9: {
    value: store.anamnese.value?.q9,
    name: "q9",
    type: "text",
    label: "Restrição de tempo para treinar",
    gender: ["Male", "Female"],
  },
  q10: {
    value: store.anamnese.value?.q10,
    name: "q10",
    type: "text",
    label: "Tempo de treino disponível por dia",
    gender: ["Male", "Female"],
  },
  q11: {
    value: store.anamnese.value?.q11,
    name: "q11",
    type: "text",
    label: "Local de treino",
    gender: ["Male", "Female"],
  },
  q12: {
    value: store.anamnese.value?.q12,
    name: "q12",
    type: "number",
    label: "Disponibilidade para treinar durante a semana",
    gender: ["Male", "Female"],
  },
  q13: {
    value: transformQ13(store.anamnese.value?.q13),
    name: "q13",
    gender: ["Male", "Female"],
  },
  q14: {
    value: store.anamnese.value?.q14,
    name: "q14",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Está fazendo dieta orientado(a) por nutricionista",
    gender: ["Male", "Female"],
  },
  q15: {
    value: store.anamnese.value?.q15,
    name: "q15",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Está sendo acompanhado(a) por nutrologista ou endocrinologista",
    gender: ["Male", "Female"],
  },
  q16: {
    value: store.anamnese.value?.q16,
    name: "q16",
    type: "textarea",
    rows: "2",
    label: "Rotina alimentar",
    gender: ["Male", "Female"],
  },
  q17: {
    value: store.anamnese.value?.q17,
    name: "q17",
    type: "number",
    label: "Qualidade do sono, de 1 a 10",
    span: "(Sendo 1 para péssimo e 10 para excelente)",
    gender: ["Male", "Female"],
  },
  q18: {
    value: store.anamnese.value?.q18,
    name: "q18",
    type: "text",
    label: "Profissão",
    gender: ["Male", "Female"],
  },
  q19: {
    value: store.anamnese.value?.q19,
    name: "q19",
    type: "text",
    label:
      "No trabalho, permanece muito tempo sentado(a), em movimento ou realiza trabalho braçal",
    gender: ["Male", "Female"],
  },
  q20: {
    value: store.anamnese.value?.q20,
    name: "q20",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Dores ou desconfortos",
    gender: ["Male", "Female"],
  },
  q21: {
    value: store.anamnese.value?.q21,
    name: "q21",
    type: "textarea",
    rows: "2",
    label:
      "Se sim, onde? Leve ou aguda? Esporádica ou crônica? Qual a intensidade dessa(s) dor(es) de 0 a 10?",
    gender: ["Male", "Female"],
  },
  physical_limitation: {
    value: store.anamnese.value?.physical_limitation,
    name: "physical_limitation",
    type: "textarea",
    rows: "2",
    label: "Limitação física",
    gender: ["Male", "Female"],
  },
  diabetes: {
    value: store.anamnese.value?.diabetes,
    name: "diabetes",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Tem Diabetes",
    gender: ["Male", "Female"],
  },
  hypertension: {
    value: store.anamnese.value?.hypertension,
    name: "hypertension",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Tem Hipertensão",
    gender: ["Male", "Female"],
  },
  q22: {
    value: store.anamnese.value?.q22,
    name: "q22",
    type: "text",
    label: "Patologia (doença) diagnosticada por algum médico",
    gender: ["Male", "Female"],
  },
  q23: {
    value: store.anamnese.value?.q23,
    name: "q23",
    type: "textarea",
    rows: "2",
    label: "Uso de medicamentos de forma rotineira",
    gender: ["Male", "Female"],
  },
  iud: {
    value: store.anamnese.value?.iud,
    name: "iud",
    type: "radio",
    radios: YesOrNoRadio,
    label: "Faz uso de Dispositivos intrauterinos (DIU)",
    gender: ["Female"],
  },
  menstruation: {
    value: untranslateMenstruation(store.anamnese.value?.menstruation),
    name: "menstruation",
    type: "select",
    options: updateMenstruationAnswers,
    label: "Menstrua regularmente",
    gender: ["Female"],
  },
  alcohol_ingestion: {
    value: store.anamnese.value?.alcohol_ingestion,
    name: "alcohol_ingestion",
    type: "text",
    label: "Regularidade no consumo de álcool",
    gender: ["Male", "Female"],
  },
  q24: {
    value: store.anamnese.value?.q24,
    name: "q24",
    type: "radio",
    radios: YesOrNoRadio,
    label:
      "O médico já mencionou condição cardíaca e só deve realizar atividade física recomendada por um médico",
    gender: ["Male", "Female"],
  },
  fc_max_formula: {
    value: untranslateFcMaxFormula(store.anamnese.value?.fc_max_formula),
    name: "fc_max_formula",
    type: "select",
    options: fcMaxFormulas,
    label: "Formula para calcular frequência cardíaca máxima",
    gender: ["Male", "Female"],
  },
  fc_repouso: {
    value: store.anamnese.value?.fc_repouso,
    name: "fc_repouso",
    type: "number",
    label: "Frequência cardíaca em repouso",
    gender: ["Male", "Female"],
  },
  q25: {
    value: store.anamnese.value?.q25,
    name: "q25",
    type: "radio",
    radios: YesOrNoRadio,
    label:
      "O médico sabe que ele(a) está ingressando em um programa de treinamento físico",
    gender: ["Male", "Female"],
  },
  q26: {
    value: store.anamnese.value?.q26,
    name: "q26",
    type: "text",
    label: "Meta a atingir",
    gender: ["Male", "Female"],
  },
  q27: {
    value: store.anamnese.value?.q27,
    name: "q27",
    type: "textarea",
    label: "Algo relevante para personalizar o treino",
    gender: ["Male", "Female"],
  },
});

async function onSubmit(_, { setFieldError }) {
  let errors = 0;

  // q21 is required if q20 answer was Yes
  if (
    form.q20.value &&
    (!form.q21.value ||
      (typeof form.q21.value === "string" &&
        form.q21.value.trim().length === 0))
  ) {
    setFieldError("q21", "Se sim, este campo precisa ser preenchido.");
    errors++;
  }

  // q21 can't have value if q20 answer is No
  if (
    !form.q20.value &&
    typeof form.q21.value === "string" &&
    form.q21.value.trim().length !== 0
  ) {
    form.q21.value = undefined;
  }

  // q11 and table(q12) is related
  if (form.q13.value.length < form.q12.value) {
    setFieldError("q12", "Dia(s) da semana não preenchido(s). ↓");
    errors++;
  }

  // alcohol_ingestion and fc_max_formula can't be None
  if (!form.fc_max_formula.value) {
    if (form.diabetes.value) {
      form.fc_max_formula.value = "Diabetes";
    } else if (form.hypertension.value) {
      form.fc_max_formula.value = "Hypertension";
    } else {
      form.fc_max_formula.value = "Default";
    }
  }

  if (!form.alcohol_ingestion.value) {
    setFieldError("alcohol_ingestion", "Este campo é obrigatório.");
    errors++;
  }

  if (errors > 0) {
    return;
  }

  try {
    form.menstruation.value = updateTranslateMenstruation(
      form.menstruation.value
    );
    form.fc_max_formula.value = translateFcMaxFormula(
      form.fc_max_formula.value
    );
    const anamneseForm = createAnamneseForm(form);
    anamneseForm["fc_max"] = fcmax(
      props.student.birth_date,
      form.fc_max_formula.value
    );
    anamneseForm["l1"] = calculateL1(
      anamneseForm.fc_max,
      form.fc_repouso.value
    );
    anamneseForm["l2"] = calculateL2(
      anamneseForm.fc_max,
      form.fc_repouso.value
    );

    await updateAnamnese(route.params.id, anamneseForm);

    alert(`Atualizado com sucesso!`);

    location.reload();
  } catch (err) {
    console.error(err);
    throw err;
  }
}

function pushToTable(value) {
  value.day = translateDays(value.day);
  const formQ = form.q13.value;
  if (!formQ?.length) {
    formQ?.push({ day: value.day, periods: [value.value] });
    return;
  }
  const hasDay = formQ?.some((item) => item.day === value.day);
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
  value = translateDays(value);
  const formQ = form.q13.value;
  const form12 = form.q12.value;
  const hasDay = formQ?.some((item) => item.day === value);
  if (formQ?.length >= form12 && !hasDay) {
    return true;
  }
}

function checkTheBox(day, value) {
  day = translateDays(day);
  const formQ = form.q13.value;
  const currentDay = formQ?.filter((item) => item.day === day);
  return currentDay?.some((item) => item.periods.includes(value));
}

onMounted(() => {
  if (!store.anamnese.value) {
    router.push(`/student/${route.params.id}`);
  }
});
</script>

<template>
  <section>
    <Form
      @submit="onSubmit"
      class="form"
      :validation-schema="schema"
      v-slot="{ meta }"
    >
      <div class="form__section">
        <div
          v-for="(item, _, id) in form"
          :key="id"
          class="form__section__fields"
        >
          <TextField
            v-if="
              id !== 13 &&
              item.gender.includes(student?.gender) &&
              item.type !== 'radio'
            "
            v-model="item.value"
            :name="item.name"
            :meta="meta"
            :type="item.type"
            :label="item.label"
            :span="item.span ? item.span : null"
            :rows="item.rows ? item.rows : null"
            :radios="item.radios ? item.radios : null"
            :options="item.options ? item.options : null"
          />

          <div
            v-if="
              item.type === 'radio' && item.gender.includes(student?.gender)
            "
            class="radio-field"
          >
            <label>{{ item.label }}</label>
            <div
              v-for="(radio, id) in item.radios"
              :key="id"
              class="radio-container"
            >
              <Field
                v-model="item.value"
                :name="item.name"
                :meta="meta"
                v-slot="{ field }"
              >
                <input
                  v-bind="field"
                  :value="radio.value"
                  type="radio"
                  :id="item.name + radio.label"
                  :checked="radio.value === item.value"
                />
              </Field>
              <label :for="item.name + radio.label">{{ radio.label }}</label>
            </div>
          </div>

          <table v-if="id === 13">
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
                    :checked="checkTheBox(day, 1)"
                  />
                </td>
                <td>
                  <input
                    :name="`${day}`"
                    :value="{ day, value: 2 }"
                    type="checkbox"
                    @change="pushToTable({ day, value: 2 })"
                    :disabled="disableCheckbox(day)"
                    :checked="checkTheBox(day, 2)"
                  />
                </td>
                <td>
                  <input
                    :name="`${day}`"
                    :value="{ day, value: 3 }"
                    type="checkbox"
                    @change="pushToTable({ day, value: 3 })"
                    :disabled="disableCheckbox(day)"
                    :checked="checkTheBox(day, 3)"
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="submit">
          <button>Atualizar anamnese</button>
        </div>
      </div>
    </Form>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

.form {
  display: flex;
  flex-direction: column;
  gap: 16px;

  &__section {
    display: flex;
    flex-direction: column;
    padding: 16px;
    background-color: white;
    border-radius: $border-radius;
    box-shadow: $box-shadow;

    &__fields {
      display: flex;
      flex-direction: column;

      .register-field {
        margin-bottom: 16px;
      }

      .radio-field {
        @include inputContainers();
        margin-bottom: 16px;

        p {
          color: $error-msg;
        }

        .radio-container {
          display: flex;
          gap: 5px;
          padding: 0 10px;

          label {
            font-size: 0.95rem;
            font-weight: 600;
            color: $txt-aside;
          }
        }
      }

      table {
        margin-bottom: 16px;
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
    }

    .submit {
      display: flex;
      justify-content: flex-end;
      button {
        @include submitButtons($buttons, white);
      }
    }
  }
}
</style>
