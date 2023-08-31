<script setup>
import { antropometria } from "@/services/avaliar/antropometria/lists";

import { useAvaliarStore } from "@/stores/avaliar";

import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const store = useAvaliarStore();

function onSubmit(values) {
  console.log(values);
  console.log(antropometria);
}
</script>

<template>
  <section>
    <Form @submit="onSubmit">
      <h2 class="avaliar--title">Antropometria</h2>

      <div class="antropometria">
        <div class="antropometria__containers">
          <h3>Índice de Massa Corporal</h3>
          <p>IMC: {{ antropometria.imc }}</p>
          <p>Classificação: {{ antropometria.imcClass }}</p>
        </div>

        <div class="antropometria__containers">
          <h3>Circunferência Abdominal</h3>
          <div class="antropometria__containers__1-1">
            <div class="antropometria__containers__1-1--1">
              <TextField
                v-model="antropometria.ca"
                type="number"
                name="ca"
                label="Circunferência Abdominal"
                span="(cm)"
              />
            </div>
            <div class="antropometria__containers__1-1--2">
              <p>Classificação: {{ antropometria.caClass }}</p>
              <pre>{{ antropometria.caRisk }}</pre>
            </div>
          </div>
        </div>

        <div class="antropometria__containers">
          <h3>Relação Cintura Quadril</h3>
          <div class="antropometria__containers__1-1">
            <div class="antropometria__containers__1-1--1">
              <TextField
                v-model="antropometria.waist"
                type="number"
                name="waist"
                label="Circunferência de Cintura"
                span="(cm)"
              />
              <TextField
                v-model="antropometria.hip"
                type="number"
                name="hip"
                label="Circunferência de Quadril"
                span="(cm)"
              />
            </div>
            <div class="antropometria__containers__1-1--2">
              <p>RCQ: {{ antropometria.rcq }}</p>
              <p>Classificação: {{ antropometria.rcqClass }}</p>
            </div>
          </div>
        </div>

        <div class="antropometria__containers">
          <h3>Relação Circunferência Abdominal Estatura</h3>
          <p>Classificação: {{ antropometria.rcaeClass }}</p>
        </div>

        <div class="antropometria__containers">
          <h3>Índice de Adposidade Corporal</h3>
          <p>IAC: {{ antropometria.iac }}</p>
          <p>Classificação: {{ antropometria.iacClass }}</p>
        </div>

        <div class="antropometria__containers">
          <h3>Porcentagem de Gordura</h3>
          <div class="antropometria__containers__1-1">
            <div class="antropometria__containers__1-1--1">
              <TextField
                v-model="antropometria.pgA"
                type="number"
                name="pgA"
                :label="
                  store.student?.gender === 'Male'
                    ? 'Biceps Direito Relaxado'
                    : 'Abdominal'
                "
                span="(cm)"
              />
              <TextField
                v-model="antropometria.pgB"
                type="number"
                name="pgB"
                :label="store.student?.gender === 'Male' ? 'Abdominal' : 'Coxa'"
                span="(cm)"
              />
              <TextField
                v-model="antropometria.pgC"
                type="number"
                name="pgC"
                :label="
                  store.student?.gender === 'Male'
                    ? 'Antebraço Direito'
                    : 'Antebraço Direito'
                "
                span="(cm)"
              />
            </div>
            <div class="antropometria__containers__1-1--2">
              <p>%G: {{ antropometria.pg }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="submit--btn">
        <SubmitButton msg="Salvar" />
      </div>
    </Form>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";

section {
  display: flex;
  flex-direction: column;
  gap: 20px;

  form {
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

    .antropometria {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 20px;

      &__containers {
        padding: 10px;
        border: 1px solid $input-border;

        h3 {
          font-weight: 600;
          color: $txt-aside;
        }

        p {
          color: $txt-aside;
        }

        &__1-1 {
          display: flex;
          flex-direction: column;
          gap: 10px;
          &--1 {
            display: flex;
            gap: 20px;

            .register-field {
              flex: 1;
            }
          }
        }
      }
    }

    .submit--btn {
      margin: 10px;
      margin-top: -5px;
    }
  }
}
</style>
