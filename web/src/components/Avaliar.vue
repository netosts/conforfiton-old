<script setup>
import { ref, onMounted } from 'vue';
import { Form, Field } from 'vee-validate';

import { useRouter } from 'vue-router/auto';

// VARIABLES
const bodyElement = ref(null);
const router = useRouter();

// Emits
const emit = defineEmits(['isAvaliarActive']);

// Props
const props = defineProps({
  studentId: Number,
  studentName: String,
});

// FUNCTIONS
function closeAvaliar() {
  emit('isAvaliarActive', false);
  bodyElement.value.style.overflow = 'auto';
};

function onSubmit(values) {
  console.log(values);
  router.push(`/avaliar/${props.studentId}`);
};

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeAvaliar">
    <Form @submit="onSubmit">
      <div class="container">
        <div class="container__title">
          <div class="container__title__text">
            <h1>Avaliar</h1>
            <strong>{{ studentName }}</strong>
          </div>
          <div class="container__title__buttons">
            <button type="button" @click="closeAvaliar">
              <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
            </button>
          </div>
        </div>
        <div class="container__content">
          <div class="container__content__checkbox">
            <label for="neuromuscular">Neuromuscular</label>
            <Field name="avaliar" id="neuromuscular" type="checkbox" value="Neuromuscular" />
          </div>
          <div class="container__content__checkbox">
            <label for="antropometria">Antropometria</label>
            <Field name="avaliar" id="antropometria" type="checkbox" value="Antropometria" />
          </div>
          <div class="container__content__checkbox">
            <label for="cardio">Cardio</label>
            <Field name="avaliar" id="cardio" type="checkbox" value="Cardio" />
          </div>
        </div>
        <div class="container__submit">
          <button class="submit">Avaliar</button>
        </div>
      </div>
    </Form>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';


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
    border-radius: $border-radius;
    background-color: rgb(245, 245, 245);

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
          font-size: 1rem;
          font-weight: 600;
          color: $txt-title;
        }

        strong {
          font-size: 1.2rem;
          font-weight: 800;
          color: $logo-color;
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
          transition: .2s;

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
      padding: 20px 20px 10px 20px;

      &__checkbox {
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        border-radius: $border-radius;
        background-color: $buttons;

        label {
          flex: 1;
          color: white;
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
        flex: 1;
        @include submitButtons($validation, white);
      }
    }
  }
}
</style>