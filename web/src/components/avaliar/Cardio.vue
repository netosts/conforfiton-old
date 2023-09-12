<script setup>
import {
  cardioList,
  results,
  renameProtocol,
} from "@/services/avaliar/cardio/lists";
import { createAntropometriaForm } from "@/services/avaliar/antropometria/helpers";

// import { postAntropometria } from "@/services/api/post";
// import { updateAntropometriaProtocol } from "@/services/api/put";

import { useRoute } from "vue-router/auto";
import { useAvaliarStore } from "@/stores/avaliar";

import { ref } from "vue";

import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";
import Checkbox from "./cardio/Checkbox.vue";

const route = useRoute();
const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

async function onSubmit() {
  try {
    // const form = await createAntropometriaForm(
    //   store.student?.weight,
    //   store.cardio_protocol,
    //   antropometriaList.value,
    //   results
    // );
    // await postAntropometria(form, route.params.id);

    sessionStorage.setItem("submitted", true);

    alert("Antropometria salvo com sucesso");

    // Remove Antropometria from the screen
    const indexToRemove = store.types.indexOf("Antropometria");
    // store.types.splice(indexToRemove, 1);
  } catch (err) {
    console.error(err);
    throw err;
  }
}

function openSelect() {
  selectProtocol.value = !selectProtocol.value;
  protocolButton.value = false;
}

async function updateProtocol(value) {
  console.log(value);
  const data = { cardio_protocol: value };
  console.log(data);
  // await updateAntropometriaProtocol(store.student?.id, data);
  // selectProtocol.value = false;
}
</script>

<template>
  <section>
    <Form @submit="onSubmit" v-slot="meta">
      <h2 class="avaliar--title">Cardiorrespiratório</h2>

      <div class="protocol">
        <p>
          Protocolo:
          <span>{{ renameProtocol }}</span>
        </p>
        <div class="protocol__update" v-if="store.cardio_protocol !== 'Elder'">
          <button type="button" @click="openSelect" v-show="protocolButton">
            Novo protocolo
          </button>
        </div>
      </div>

      <Checkbox v-show="selectProtocol" @confirmProtocol="updateProtocol" />

      <div class="cardio">
        <div class="cardio__inputs">
          <div v-for="(item, id) in cardioList" :key="id">
            <TextField
              v-model="item.value"
              :name="item.name"
              type="number"
              :label="item.label"
              :span="item.span"
              :meta="meta"
              rules="required"
            />
          </div>
        </div>

        <p v-if="results.fcmax">FCMAX: {{ results.fcmax }}</p>
        <p v-if="results.l1">L1: {{ results.l1 }}</p>
        <p v-if="results.l2">L2: {{ results.l2 }}</p>
        <p v-if="results.l1_fcmax_percentage">
          L1 (% FC Max): {{ results.l1_fcmax_percentage }}
        </p>
        <p v-if="results.l2_fcmax_percentage">
          L2 (% FC Max): {{ results.l2_fcmax_percentage }}
        </p>
        <p v-if="results.vo2max">VO2MAX: {{ results.vo2max }} ml/kg/min</p>
        <p v-if="results.vo2max">vVO2MAX: {{ results.vvo2max }} Km/h</p>
        <p v-if="results.vo2max_pace">Pace: {{ results.vo2max_pace }} min/km</p>
        <p v-if="results.vl1">VL1: {{ results.vl1 }} Km/h</p>
        <p v-if="results.vl1_pace">Pace: {{ results.vl1_pace }} min/km</p>
        <p v-if="results.vl2">VL2: {{ results.vl2 }} Km/h</p>
        <p v-if="results.vl2_pace">Pace: {{ results.vl2_pace }} min/km</p>
        <p v-if="results.elder_aerobic_power">
          Classificação: {{ results.elder_aerobic_power }}
        </p>

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
