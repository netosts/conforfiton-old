<script setup>
import { updateNeuromuscularProtocol } from "@/services/api/put";

import {
  protocolsList,
  neuroComponents,
} from "@/services/avaliar/neuromuscular/lists";

import { ref } from "vue";

import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

const selectProtocol = ref(false);
const protocolButton = ref(true);

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
  const data = { neuromuscular_protocol: store.neuromuscular_protocol };
  await updateNeuromuscularProtocol(store.student?.id, data);
  selectProtocol.value = false;
}
</script>

<template>
  <section>
    <h2 class="avaliar--title">Neuromuscular</h2>

    <div class="protocol">
      <p>
        Protocolo:
        <span>{{ renameProtocol(store.neuromuscular_protocol) }}</span>
      </p>
      <div class="protocol__update">
        <button type="button" @click="openSelect" v-show="protocolButton">
          Novo protocolo
        </button>
        <select
          v-model="store.neuromuscular_protocol"
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

    <div
      v-for="(item, id) in neuroComponents"
      :key="id"
      class="neuromuscular"
      v-show="!!store.neuromuscular_protocol"
    >
      <component
        v-if="item.protocol === store.neuromuscular_protocol"
        :is="item.component"
      />
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
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
}
</style>
