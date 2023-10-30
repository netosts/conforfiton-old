<script setup>
import {
  fcmaxList,
  l1l2List,
  vo2maxList,
} from "@/services/avaliar/cardio/lists";

import { Form, Field } from "vee-validate";
</script>

<template>
  <Form v-slot="{ values, meta }">
    <div class="radio">
      <div class="radio__1">
        <h3>FCMAX</h3>
        <div v-for="(item, id) in fcmaxList" :key="id">
          <Field
            type="radio"
            name="fcmax"
            :id="item.id"
            :value="item.value"
            :meta="meta"
            rules="required"
          />
          <label :for="item.id">{{ item.label }}</label>
        </div>
      </div>
      <div class="radio__1">
        <h3>VO2MAX</h3>
        <div v-for="(item, id) in vo2maxList" :key="id">
          <Field
            type="radio"
            name="vo2max"
            :id="item.id"
            :value="item.value"
            :meta="meta"
            rules="required"
          />
          <label :for="item.id">{{ item.label }}</label>
        </div>
      </div>
      <div class="radio__1">
        <h3>L1 & L2</h3>
        <div v-for="(item, id) in l1l2List" :key="id">
          <Field
            type="radio"
            name="l1l2"
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
        <button
          type="button"
          class="submitbox__submit__btn"
          @click="
            $emit('confirmProtocol', values.fcmax + values.l1l2 + values.vo2max)
          "
        >
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
  gap: 10px;
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
