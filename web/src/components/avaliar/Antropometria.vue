<script setup>
import { antropometria } from "@/services/avaliar/antropometria/lists";

import { updateAntropometriaProtocol } from "@/services/api/put";

import { useAvaliarStore } from "@/stores/avaliar";

import { ref } from "vue";

import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

function onSubmit(values) {
  console.log(values);
  console.log(antropometria);
}

const protocols = {
  Default: "Padrão",
  Weltman: "Weltman",
  JacksonPollock3Siri: "Jackson e Pollock 3 [Siri]",
  JacksonPollock3Brozek: "Jackson e Pollock 3 [Brozek]",
  Falkner: "Falkner",
  JacksonPollock7Siri: "JacksonPollock 7 [Siri]",
  JacksonPollock7Brozek: "JacksonPollock 7 [Brozek]",
};

function renameProtocol(value) {
  if (!value) return "Sem protocolo";
  return protocols[value];
}

function openSelect() {
  selectProtocol.value = !selectProtocol.value;
  protocolButton.value = false;
}

async function updateProtocol() {
  const data = { antropometria_protocol: store.antropometria_protocol };
  await updateAntropometriaProtocol(store.student?.id, data);
  selectProtocol.value = false;
}
</script>

<template>
  <section>
    <Form @submit="onSubmit">
      <h2 class="avaliar--title">Antropometria</h2>

      <div class="protocol">
        <p>
          Protocolo:
          <span>{{ renameProtocol(store.antropometria_protocol) }}</span>
        </p>
        <div class="protocol__update">
          <button type="button" @click="openSelect" v-show="protocolButton">
            Mudar protocolo
            <font-awesome-icon icon="fa-solid fa-plus" />
          </button>
          <select
            v-model="store.antropometria_protocol"
            v-show="selectProtocol"
            @change="updateProtocol"
          >
            <option value="Default">Padrão</option>
            <option value="Weltman">Weltman</option>
            <option value="JacksonPollock3Siri">
              Jackson e Pollock 3 [Siri]
            </option>
            <option value="JacksonPollock3Brozek">
              Jackson e Pollock 3 [Brozek]
            </option>
            <option value="Falkner">Falkner</option>
            <option value="JacksonPollock7Siri">JacksonPollock 7 [Siri]</option>
            <option value="JacksonPollock7Brozek">
              JacksonPollock 7 [Brozek]
            </option>
          </select>
        </div>
      </div>

      <div class="antropometria">
        <div class="antropometria__containers">
          <h3 class="antropometria__containers--cm">
            Circunferências (centímetros)
          </h3>
          <div class="antropometria__containers--grid">
            <TextField
              v-model="antropometria.abs"
              type="number"
              name="abs"
              label="Abdominal"
            />
            <TextField
              v-model="antropometria.waist"
              type="number"
              name="waist"
              label="Cintura"
            />
            <TextField
              v-model="antropometria.hip"
              type="number"
              name="hip"
              label="Quadril"
            />
            <TextField
              v-model="antropometria.thighs"
              type="number"
              name="thighs"
              label="Coxa"
            />
            <TextField
              v-model="antropometria.rightForearm"
              type="number"
              name="rightForearm"
              label="Antebraço Direito"
            />
            <TextField
              v-model="antropometria.chest"
              type="number"
              name="chest"
              label="Peitoral"
            />
            <TextField
              v-model="antropometria.triceps"
              type="number"
              name="triceps"
              label="Tríceps"
            />
            <TextField
              v-model="antropometria.suprailiac"
              type="number"
              name="suprailiac"
              label="Suprailíaca"
            />
            <TextField
              v-model="antropometria.subscapularis"
              type="number"
              name="subscapularis"
              label="Subescapular"
            />
            <TextField
              v-model="antropometria.midaxiallry"
              type="number"
              name="midaxiallry"
              label="Axilar Média"
            />
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Índice de Massa Corporal</h3>
            <p>IMC: {{ antropometria.imc }}</p>
            <p>Classificação: {{ antropometria.imcClass }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Circunferência Abdominal</h3>
            <p>Classificação: {{ antropometria.caClass }}</p>
            <pre>{{ antropometria.caRisk }}</pre>
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Relação Cintura Quadril</h3>
            <p>RCQ: {{ antropometria.rcq }}</p>
            <p>Classificação: {{ antropometria.rcqClass }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Relação Circunferência Abdominal Estatura</h3>
            <p>Classificação: {{ antropometria.rcaeClass }}</p>
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Índice de Adposidade Corporal</h3>
            <p>IAC: {{ antropometria.iac }}</p>
            <p>Classificação: {{ antropometria.iacClass }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Porcentagem de Gordura</h3>
            <p>Gordura: {{ antropometria.pg }}%</p>
            <p>Classificação: {{ antropometria.pgClass }}</p>
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
@import "@/assets/styles/mixins";

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

    .protocol {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 20px;
      margin: 0 20px;
      @include mq(m) {
        gap: 10px;
        flex-direction: column;
        align-items: center;
      }

      p {
        display: flex;
        align-items: center;
        gap: 8px;
        span {
          font-weight: 600;
        }
      }

      &__update {
        button {
          display: flex;
          align-items: center;
          gap: 4px;
          border: none;
          border-radius: $border-radius;
          background-color: $buttons;
          color: white;
          padding: 2px 8px;
          transition: 0.2s;
          cursor: pointer;

          &:hover {
            filter: brightness(0.9);
          }
        }
      }
      select {
        padding: 8px 15px 8px 10px;
        width: 250px;
        outline: none;
        border: none;
        border-radius: $border-radius;
        background-color: $buttons;
        cursor: pointer;
        color: white;

        @include mq(m) {
          width: 100%;
        }
      }
    }

    .antropometria {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 0 20px 20px 20px;

      &__1-1 {
        display: flex;
        gap: 10px;
        div {
          flex: 1;
        }
      }

      &__containers {
        padding: 10px;
        border: 1px solid $input-border;

        &--cm {
          text-align: center;
          margin-bottom: 10px;
        }

        h3 {
          font-weight: 600;
          color: $txt-aside;
        }

        p {
          color: $txt-aside;
        }

        &--grid {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr;
          gap: 10px;

          @include mq(l-xl) {
            grid-template-columns: 1fr 1fr;
          }

          @include mq(m) {
            grid-template-columns: 1fr;
          }

          .register-field {
            flex: 1;
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
