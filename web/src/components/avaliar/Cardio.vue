<script setup>
import {
  cardioList,
  results,
  protocolsList,
} from "@/services/avaliar/cardio/lists";
import { createCardioForm } from "@/services/avaliar/cardio/helpers";

import { postCardio } from "@/services/api/post";
import { updateCardioProtocol } from "@/services/api/put";

import { useRoute } from "vue-router/auto";
import { useAvaliarStore } from "@/stores/avaliar";

import { ref } from "vue";

import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const route = useRoute();
const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

async function onSubmit() {
  try {
    const error = cardioList.value.some((object) => !object.value);
    if (error)
      return alert(
        "Por favor preencha a avaliação cardiorrespiratória corretamente."
      );

    const form = await createCardioForm(
      store.student?.weight,
      store.evaluatedAt,
      store.cardio_protocol,
      cardioList.value,
      results
    );
    await postCardio(form, route.params.id);

    sessionStorage.setItem("submitted", true);

    alert("Cardio salvo com sucesso");

    // Remove Cardio from the screen
    const indexToRemove = store.types.indexOf("cardio");
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
  if (
    (store.cardio_protocol === "EllestadActive" ||
      store.cardio_protocol === "EllestadInactive") &&
    !store.student?.fc_max
  ) {
    store.cardio_protocol = null;
    return alert(
      "Para o protocolo de Ellestad é necessário fazer Anamnese antes."
    );
  }
  const data = { cardio_protocol: store.cardio_protocol };
  await updateCardioProtocol(store.student?.id, data);
  selectProtocol.value = false;
}
</script>

<template>
  <section>
    <Form @submit="onSubmit">
      <h2 class="avaliar--title">Cardiorrespiratório</h2>

      <div class="protocol">
        <p>
          Protocolo:
          <span>{{ renameProtocol(store.cardio_protocol) }}</span>
        </p>
        <div class="protocol__update" v-if="store.cardio_protocol !== 'Elder'">
          <button type="button" @click="openSelect" v-show="protocolButton">
            Novo protocolo
          </button>
          <select
            v-model="store.cardio_protocol"
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

      <div class="cardio" v-if="!!store.cardio_protocol">
        <div class="cardio__inputs">
          <div v-for="(item, id) in cardioList" :key="id">
            <TextField
              v-model="item.value"
              :name="item.name"
              type="number"
              :label="item.label"
              :span="item.span"
              :rules="{
                required: true,
                bpm:
                  item.name === 'l1_ellestad_conconi' ||
                  item.name === 'l2_ellestad_conconi' ||
                  item.name === 'fc_5min',
                distance: item.name === 'distance',
                time: item.name === 'time',
              }"
            />
          </div>
        </div>

        <p v-if="results.elder_aerobic_power">
          Classificação: {{ results.elder_aerobic_power }}
        </p>

        <p v-if="results.weekly_caloric_expenditure">
          Gasto Calórico - Semanal:
          {{ results.weekly_caloric_expenditure }} kcal
        </p>
        <p v-if="results.daily_caloric_expenditure">
          Gasto Calórico - Diário: {{ results.daily_caloric_expenditure }} kcal
        </p>

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
    }

    .cardio {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 20px;
      &__inputs {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
      }
    }
  }
}

.submitbox {
  margin-top: 10px;
}
</style>
