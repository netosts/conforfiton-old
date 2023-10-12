<script setup>
import { updateMorphofunctional } from "@/services/api/put";
import {
  q4Radio,
  YesOrNoRadio,
  updateMenstruationAnswers,
} from "@/services/register/lists";
import { fcMaxFormulas } from "@/services/student/lists";

import { fcmax } from "@/services/register/helpers";

import {
  updateTranslateMenstruation,
  translateFcMaxFormula,
  untranslateFcMaxFormula,
  untranslateMenstruation,
} from "@/services/helpers";

import { reactive, onMounted } from "vue";
import { useStudentStore } from "@/stores/student";
import { definePage, useRoute, useRouter } from "vue-router/auto";

import { schema } from "@/services/student/update-morphofunctional/schema";
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
  q1: store.overview.value?.q1,
  q2: store.overview.value?.q2,
  q4: {
    training: store.overview.value?.q4.training,
    time: store.overview.value?.q4.time,
  },
  q21: store.overview.value?.q21,
  q20: store.overview.value?.q20,
  diabetes: store.overview.value?.diabetes,
  hypertension: store.overview.value?.hypertension,
  q22: store.overview.value?.q22,
  alcohol_ingestion: store.overview.value?.alcohol_ingestion,
  physical_limitation: store.overview.value?.physical_limitation,
  iud: store.overview.value?.iud,
  menstruation: untranslateMenstruation(store.overview.value?.menstruation),
  fc_max_formula: untranslateFcMaxFormula(store.overview.value?.fc_max_formula),
  fc_max: store.overview.value?.fc_max,
  fc_repouso: store.overview.value?.fc_repouso,
  l1: store.overview.value?.l1,
  l2: store.overview.value?.l2,
});

async function onSubmit(_, { setFieldError }) {
  let errors = 0;

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

  // alcohol_ingestion and fc_max_formula can't be None
  if (!form.fc_max_formula) {
    if (form.diabetes) {
      form.fc_max_formula = "Diabetes";
    } else if (form.hypertension) {
      form.fc_max_formula = "Hypertension";
    } else {
      form.fc_max_formula = "Default";
    }
  }

  if (!form.alcohol_ingestion) {
    setFieldError("alcohol_ingestion", "Este campo é obrigatório.");
    errors++;
  }

  if (errors > 0) {
    return;
  }

  try {
    form.menstruation = updateTranslateMenstruation(form.menstruation);
    form.fc_max_formula = translateFcMaxFormula(form.fc_max_formula);
    form.fc_max = fcmax(props.student.birth_date, form.fc_max_formula);

    await updateMorphofunctional(route.params.id, form);

    alert(`Atualizado com sucesso!`);

    location.reload();
  } catch (err) {
    console.error(err);
    throw err;
  }
}

onMounted(() => {
  if (!store.overview.value) {
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
        <TextField
          v-model="form.q1"
          name="q1"
          :meta="meta"
          type="textarea"
          rows="2"
          label="O aluno(a) tem como principal objetivo:"
        />
        <TextField
          v-model="form.q2"
          name="q2"
          :meta="meta"
          type="text"
          label="E como objetivo secundário:"
        />
        <TextField
          v-model="form.q4.training"
          name="q4a"
          :meta="meta"
          type="radio"
          :radios="q4Radio"
          label="O aluno(a) está parado(a) ou treinando:"
        />
        <TextField
          v-model="form.q4.time"
          name="q4b"
          :meta="meta"
          type="text"
          label="Há quanto tempo:"
        />
        <div class="register-field">
          <label
            >O aluno(a) tem algum tipo de dor ou desconforto (muscular ou
            articular):</label
          >
          <div
            v-for="(radio, id) in YesOrNoRadio"
            :key="id"
            class="radio-container"
          >
            <Field
              v-model="form.q20"
              name="q20"
              :meta="meta"
              v-slot="{ field }"
            >
              <input
                v-bind="field"
                :value="radio.value"
                type="radio"
                :id="'q20' + radio.label"
                :checked="radio.value === form.q20"
              />
            </Field>
            <label :for="'q20' + radio.label">{{ radio.label }}</label>
          </div>
        </div>
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
          v-model="form.physical_limitation"
          name="physical_limitation"
          :meta="meta"
          type="textarea"
          rows="2"
          label="O aluno(a) tem algum tipo de limitação física?"
        />
        <div class="register-field">
          <label>O aluno(a) é diagnosticado com Diabetes?</label>
          <div
            v-for="(radio, id) in YesOrNoRadio"
            :key="id"
            class="radio-container"
          >
            <Field
              v-model="form.diabetes"
              name="diabetes"
              :meta="meta"
              v-slot="{ field }"
            >
              <input
                v-bind="field"
                :value="radio.value"
                type="radio"
                :id="'diabetes' + radio.label"
                :checked="radio.value === form.diabetes"
              />
            </Field>
            <label :for="'diabetes' + radio.label">{{ radio.label }}</label>
          </div>
        </div>
        <div class="register-field">
          <label>O aluno(a) é diagnosticado com Hipertensão?</label>
          <div
            v-for="(radio, id) in YesOrNoRadio"
            :key="id"
            class="radio-container"
          >
            <Field
              v-model="form.hypertension"
              name="hypertension"
              :meta="meta"
              v-slot="{ field }"
            >
              <input
                v-bind="field"
                :value="radio.value"
                type="radio"
                :id="'hypertension' + radio.label"
                :checked="radio.value === form.hypertension"
              />
            </Field>
            <label :for="'hypertension' + radio.label">{{ radio.label }}</label>
          </div>
        </div>
        <TextField
          v-model="form.q22"
          name="q22"
          :meta="meta"
          type="text"
          label="O aluno(a) tem alguma patologia (doença) diagnosticada por algum médico?"
          span="(Alergias; doenças cardíacas; doenças fúngicas; etc)"
        />
        <div class="register-field" v-if="student?.gender === 'Female'">
          <label>A aluna faz uso de Dispositivos intrauterinos (DIU)?</label>
          <div
            v-for="(radio, id) in YesOrNoRadio"
            :key="id"
            class="radio-container"
          >
            <Field
              v-model="form.iud"
              name="iud"
              :meta="meta"
              v-slot="{ field }"
            >
              <input
                v-bind="field"
                :value="radio.value"
                type="radio"
                :id="'iud' + radio.label"
                :checked="radio.value === form.iud"
              />
            </Field>
            <label :for="'iud' + radio.label">{{ radio.label }}</label>
          </div>
        </div>
        <TextField
          v-if="student?.gender === 'Female'"
          v-model="form.menstruation"
          name="menstruation"
          :meta="meta"
          type="select"
          :options="updateMenstruationAnswers"
          label="A aluna menstrua regularmente?"
        />
        <TextField
          v-model="form.alcohol_ingestion"
          name="alcohol_ingestion"
          :meta="meta"
          type="text"
          label="O aluno(a) consome álcool? Se sim, quantas vezes por semana?"
        />
        <TextField
          v-model="form.fc_max_formula"
          name="fc_max_formula"
          :meta="meta"
          type="select"
          :options="fcMaxFormulas"
          label="Formula para calcular frequência cardíaca máxima:"
        />
        <TextField
          v-model="form.fc_repouso"
          name="fc_repouso"
          :meta="meta"
          type="number"
          label="Frequência cardíaca em repouso do aluno(a):"
        />
        <TextField
          v-model="form.l1"
          name="l1"
          :meta="meta"
          type="number"
          label="L1"
          span="(bpm)"
        />
        <TextField
          v-model="form.l2"
          name="l2"
          :meta="meta"
          type="number"
          label="L2"
          span="(bpm)"
        />
        <div class="submit">
          <button>Atualizar informações</button>
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

    .register-field {
      @include inputContainers();

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
