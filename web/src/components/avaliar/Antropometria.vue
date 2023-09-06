<script setup>
import {
  antropometria,
  antropometriaList,
  protocolsList,
} from "@/services/avaliar/antropometria/lists";

import { updateAntropometriaProtocol } from "@/services/api/put";

import { useAvaliarStore } from "@/stores/avaliar";

import { ref, computed } from "vue";

import { schema } from "@/services/avaliar/antropometria/schema";
import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

function onSubmit(values) {
  try {
    console.log(values);
    console.log(antropometria);

    alert("Antropometria salvo com sucesso");

    // Remove Antropometria from the screen
    const indexToRemove = store.types.indexOf("Antropometria");
    store.types.splice(indexToRemove, 1);
  } catch (err) {
    console.error(err);
    throw err;
  }
}

function renameProtocol(value) {
  if (!value) return "Sem protocolo";
  const findProtocol = protocolsList.value.find((item) => item.value === value);
  return findProtocol.value;
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
    <Form @submit="onSubmit" :validation-schema="schema" v-slot="meta">
      <h2 class="avaliar--title">Antropometria</h2>

      <div class="protocol">
        <p>
          Protocolo:
          <span>{{ renameProtocol(store.antropometria_protocol) }}</span>
        </p>
        <div class="protocol__update">
          <button type="button" @click="openSelect" v-show="protocolButton">
            Novo protocolo
          </button>
          <select
            v-model="store.antropometria_protocol"
            v-show="selectProtocol"
            @change="updateProtocol"
          >
            <option
              v-for="(protocol, id) in protocolsList"
              :key="id"
              :value="protocol.value"
            >
              {{ protocol.name }}
            </option>
            <!-- <option value="Weltman">Weltman</option>
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
            <option value="Idoso3Dobras">
              JacksonPollock 7 [Brozek]
            </option>
            <option value="IdosoTranWeltman">
              JacksonPollock 7 [Brozek]
            </option> -->
          </select>
        </div>
      </div>

      <div class="antropometria" v-show="!!store.antropometria_protocol">
        <div class="antropometria__containers">
          <h3 class="antropometria__containers--cm">
            Circunferências (centímetros)
          </h3>
          <div class="antropometria__containers--grid">
            <div v-for="(item, id) in antropometriaList" :key="id">
              <TextField
                v-model="item.value"
                type="number"
                :name="item.name"
                :label="item.label"
                :meta="meta"
              />
            </div>
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Índice de Massa Corporal</h3>
            <p>IMC: {{ antropometria.imc_result }}</p>
            <p>Classificação: {{ antropometria.imc_class }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Circunferência Abdominal</h3>
            <p>Classificação: {{ antropometria.ca_class }}</p>
            <pre>{{ antropometria.ca_risk }}</pre>
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Relação Cintura Quadril</h3>
            <p>RCQ: {{ antropometria.rcq_result }}</p>
            <p>Classificação: {{ antropometria.rcq_class }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Relação Circunferência Abdominal Estatura</h3>
            <p>Classificação: {{ antropometria.rcae_class }}</p>
          </div>
        </div>

        <div class="antropometria__1-1">
          <div class="antropometria__containers">
            <h3>Índice de Adposidade Corporal</h3>
            <p>IAC: {{ antropometria.iac_result }}</p>
            <p>Classificação: {{ antropometria.iac_class }}</p>
          </div>
          <div class="antropometria__containers">
            <h3>Porcentagem de Gordura</h3>
            <p>Gordura: {{ antropometria.pg_result }}%</p>
            <p>Classificação: {{ antropometria.pg_class }}</p>
          </div>
        </div>
        <SubmitButton msg="Salvar" :meta="meta.meta" />
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
      margin: 0 20px 10px 20px;
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
