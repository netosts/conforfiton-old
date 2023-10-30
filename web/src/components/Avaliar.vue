<script setup>
import { ref, onMounted } from "vue";
import { Form, Field } from "vee-validate";
import { useAvaliarStore } from "../stores/avaliar";

import { useRouter } from "vue-router/auto";

// VARIABLES
const bodyElement = ref(null);
const router = useRouter();
const store = useAvaliarStore();
const date = ref(null);

// Emits
const emit = defineEmits(["isAvaliarActive"]);

// Props
const props = defineProps({
  studentId: Number,
  studentName: String,
});

// FUNCTIONS
function closeAvaliar() {
  emit("isAvaliarActive", false);
  bodyElement.value.style.overflow = "auto";
}

function onSubmit(values) {
  store.types = values.avaliar;
  store.evaluatedAt = values.date;
  bodyElement.value.style.overflow = "auto";
  router.push(`/avaliar/${props.studentId}`);
}

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeAvaliar">
    <Form @submit="onSubmit" v-slot="{ values }">
      <div class="container">
        <div class="container__title">
          <div class="container__title__text">
            <h1>{{ studentName }}</h1>
          </div>
          <div class="container__title__buttons">
            <button type="button" @click="closeAvaliar">
              <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
            </button>
          </div>
        </div>
        <div class="container__content">
          <div class="container__content__date">
            <label for="date">Data</label>
            <Field v-model="date" name="date" id="date" type="date" />
          </div>
          <div class="container__content__checkbox">
            <label for="neuromuscular">Neuromuscular</label>
            <Field
              name="avaliar"
              id="neuromuscular"
              type="checkbox"
              value="neuromuscular"
            />
          </div>
          <div class="container__content__checkbox">
            <label for="antropometria">Antropometria</label>
            <Field
              name="avaliar"
              id="antropometria"
              type="checkbox"
              value="antropometria"
            />
          </div>
          <div class="container__content__checkbox">
            <label for="cardio">Cardiorrespiratório</label>
            <Field name="avaliar" id="cardio" type="checkbox" value="cardio" />
          </div>
        </div>
        <div class="container__submit">
          <div
            class="submit"
            :class="{
              'submit--disabled':
                !values.avaliar?.length || !values.date ? true : false,
            }"
          >
            <button type="submit" class="submit__btn">Avaliar</button>
          </div>
        </div>
      </div>
    </Form>
  </aside>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

aside {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;
  background-color: rgba(79, 79, 79, 0.442);

  @include mq(s) {
    padding: 10px;
  }

  .container {
    width: 375px;
    border-radius: $border-radius;
    background-color: rgb(245, 245, 245);

    @include mq(xs) {
      width: 300px;
    }

    &__title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid $input-border;

      &__text {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 20px;

        h1 {
          font-size: 1.4rem;
          font-weight: 800;
          color: $txt-aside;
        }
      }

      &__buttons {
        button {
          margin-right: 10px;
          width: 40px;
          height: 40px;
          border: none;
          border-radius: 50%;
          background-color: transparent;
          color: rgba(85, 85, 85, 0.588);
          cursor: pointer;
          transition: 0.2s;

          &:hover {
            color: $txt-aside;
            background-color: rgba(186, 186, 186, 0.267);
          }
        }
      }
    }

    &__content {
      display: flex;
      flex-direction: column;
      gap: 5px;
      padding: 20px 10px 10px 10px;

      &__date {
        display: flex;
        justify-content: space-between;
        border: 1px solid $input-border;

        label {
          flex: 1;
          color: $txt-aside;
          padding: 5px 15px;
        }

        input {
          border: none;
          background-color: transparent;
          margin-right: 10px;
          outline: none;
        }
      }

      &__checkbox {
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        border-bottom: 1px solid $input-border;

        label {
          flex: 1;
          color: $txt-aside;
          padding: 5px 15px;
        }

        input {
          width: 15px;
          margin-right: 10px;
        }
      }
    }

    &__submit {
      display: flex;
      padding: 10px;

      .submit {
        display: flex;
        flex: 1;

        &__btn {
          flex: 1;
          @include submitButtons($validation, white);
        }

        &--disabled {
          opacity: 0.5;
          cursor: not-allowed;

          .submit__btn {
            pointer-events: none;
          }
        }
      }
    }
  }
}
</style>
