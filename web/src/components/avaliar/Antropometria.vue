<script setup>
import {
  antropometriaList,
  results,
  protocolsList,
} from "@/services/avaliar/antropometria/lists";
import { createAntropometriaForm } from "@/services/avaliar/antropometria/helpers";

import { postAntropometria } from "@/services/api/post";
import { updateAntropometriaProtocol } from "@/services/api/put";

import { useRoute } from "vue-router/auto";
import { useAvaliarStore } from "@/stores/avaliar";

import { ref } from "vue";

import { Form, Field } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const route = useRoute();
const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

async function onSubmit(values) {
  try {
    const error = Object.values(values).some(
      (value) => value === null || value === undefined || value === ""
    );
    if (error) return alert("Por favor preencha a avaliação corretamente.");
    if (values.pg_result > 100)
      return alert("Porcentagem de gordura acima de 100%");

    const form = await createAntropometriaForm(
      store.student?.weight,
      store.antropometria_protocol,
      antropometriaList.value,
      results
    );
    await postAntropometria(form, route.params.id);

    sessionStorage.setItem("submitted", true);

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
  return findProtocol.name;
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
          </select>
        </div>
      </div>

      <div class="antropometria" v-show="!!store.antropometria_protocol">
        <div class="antropometria__containers">
          <h3 class="antropometria__containers--cm">Medidas</h3>
          <div class="antropometria__containers--grid">
            <div v-for="(item, id) in antropometriaList" :key="id">
              <TextField
                v-model="item.value"
                type="number"
                :name="item.name"
                :label="item.label"
                :span="item.span"
                rules="required|between:0,999"
              />
            </div>
          </div>
        </div>

        <table class="antropometria__table">
          <thead>
            <tr>
              <th>Fórmulas</th>
              <th>Resultado</th>
              <th>Classificação</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>IMC</td>
              <td>
                <Field
                  v-model="results.imc_result"
                  name="imc_result"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
              <td>
                <Field
                  v-model="results.imc_class"
                  name="imc_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>
            <tr>
              <td>CA</td>
              <td>N/A</td>
              <td>
                <Field
                  v-model="results.ca_class"
                  name="ca_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>
            <tr>
              <td>RCQ</td>
              <td>
                <Field
                  v-model="results.rcq_result"
                  name="rcq_result"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
              <td>
                <Field
                  v-model="results.rcq_class"
                  name="rcq_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>

            <tr>
              <td>RCAE</td>
              <td>N/A</td>
              <td>
                <Field
                  v-model="results.rcae_class"
                  name="rcae_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>

            <tr>
              <td>IAC</td>
              <td>
                <Field
                  v-model="results.iac_result"
                  name="iac_result"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
              <td>
                <Field
                  v-model="results.iac_class"
                  name="iac_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>

            <tr>
              <td>%G</td>
              <td>
                <Field
                  v-model="results.pg_result"
                  name="pg_result"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
              <td>
                <Field
                  v-model="results.pg_class"
                  name="pg_class"
                  v-slot="{ field }"
                >
                  <input v-bind="field" type="text" tabindex="-1" />
                </Field>
              </td>
            </tr>
          </tbody>
        </table>
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
      flex-direction: column;
      align-items: center;
      gap: 10px;
      margin: 0 20px 10px 20px;

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

      &__table {
        border-collapse: collapse;
        border: 1px solid $input-border;
        color: $txt-aside;
        text-align: center;

        th,
        td {
          border: 1px solid $input-border;
          padding: 8px;
        }

        td {
          font-weight: 500;

          input {
            width: 100%;
            border: none;
            text-align: center;
            pointer-events: none;
          }

          &:not(:nth-child(1)) {
            min-width: 50px;
            max-width: 100px;
          }
        }
      }

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
  }
}

.submitbox {
  margin-top: 10px;
}
</style>
