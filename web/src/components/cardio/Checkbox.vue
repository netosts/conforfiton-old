<script setup>
import { formulaList, protocolsList } from "@/services/avaliar/cardio/lists";

import { Form, Field } from "vee-validate";

function onSubmit(values) {
  console.log(values.formula + values.protocol);
}
</script>

<template>
  <Form @submit="onSubmit" v-slot="{ values, meta }">
    <div class="radio">
      <div class="radio__1">
        <h3>Formulas FCMAX</h3>
        <div v-for="(item, id) in formulaList" :key="id">
          <Field
            type="radio"
            name="formula"
            :id="item.id"
            :value="item.value"
            :meta="meta"
            rules="required"
          />
          <label :for="item.id">{{ item.label }}</label>
        </div>
      </div>
      <div class="radio__1">
        <h3>Protocolos</h3>
        <div v-for="(item, id) in protocolsList" :key="id">
          <Field
            type="radio"
            name="protocol"
            :id="item.id"
            :value="item.value"
            :meta="meta"
            rules="required"
          />
          <label :for="item.id">{{ item.label }}</label>
        </div>
      </div>
    </div>

    <div class="submitbox">
      <div
        class="submitbox__submit"
        :class="{ 'submitbox__submit--disabled': meta ? !meta.valid : null }"
      >
        <button type="submit" class="submitbox__submit__btn">
          Confirmar protocolo
        </button>
      </div>
    </div>
  </Form>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

form {
  margin: 0 10px 10px 10px;
  border: 1px solid $input-border;
}
.radio {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 10px 20px 0 20px;

  &__1 {
    display: flex;
    flex-direction: column;
    div {
      display: flex;
      gap: 10px;
    }
  }
}

.submitbox {
  &__submit {
    display: flex;
    flex: 1;

    &__btn {
      flex: 1;
      border: none;
      padding: 2px 10px;
      background-color: $buttons;
      color: white;
      margin: 0 10px 10px 10px;
      cursor: pointer;
      transition: 0.2s;

      &:hover {
        filter: brightness(0.9);
      }

      &:active {
        filter: brightness(0.7);
      }
    }

    &--disabled {
      opacity: 0.5;
      cursor: not-allowed;

      .submitbox__submit__btn {
        pointer-events: none;
      }
    }
  }
}
</style>

<!-- border: none;
  padding: 2px 10px;
  background-color: $buttons;
  color: white;
  margin: 10px;
  cursor: pointer;
  transition: 0.2s;

  &:hover {
    filter: brightness(0.9);
  }

  &:active {
    filter: brightness(0.7);
  } -->
