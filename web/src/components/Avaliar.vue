<script setup>
import { ref, onMounted } from 'vue';

// VARIABLES
const bodyElement = ref(null);

// Emits
const emit = defineEmits(['isAvaliarActive']);

// Props
const props = defineProps({
  studentId: Number,
  studentName: String,
});

function closeAvaliar() {
  emit('isAvaliarActive', false);
  bodyElement.value.style.overflow = 'auto';
};

function autoScroll() {
  bodyElement.value.style.overflow = 'auto';
};

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeAvaliar">
    <div class="container">
      <div class="container__title">
        <div class="container__title__text">
          <h1>Avaliar</h1>
          <strong>{{ studentName }}</strong>
        </div>
        <div class="container__title__buttons">
          <button @click="closeAvaliar">
            <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
          </button>
        </div>
      </div>
      <div class="container__content">
        <div class="container__content__item">
          <RouterLink :to="'/anamnese/' + studentId" @click="autoScroll">
            <button>Anamnese</button>
          </RouterLink>
        </div>
        <div class="container__content__item">
          <RouterLink to="/neuromuscular">
            <button>Neuromuscular</button>
          </RouterLink>
        </div>
        <div class="container__content__item">
          <RouterLink to="/antropometria">
            <button>Antropometria</button>
          </RouterLink>
        </div>
        <div class="container__content__item">
          <RouterLink to="/cardio">
            <button>Cardio</button>
          </RouterLink>
        </div>
      </div>
    </div>
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
            background-color: rgba(133, 133, 133, 0.267);
          }
        }
      }
    }

    &__content {
      display: flex;
      gap: 25px;
      padding: 20px;

      @include mq(s-m) {
        display: grid;
        grid-template-columns: 1fr 1fr;
        text-align: center;
        gap: 15px;
        padding: 20px 15px;
      }

      &__item {
        &:nth-child(1) {
          button {
            @include submitButtons($validation, white);
          }
        }

        &:nth-child(2) {
          button {
            @include submitButtons($validation, white);
          }
        }

        &:nth-child(3) {
          button {
            @include submitButtons($validation, white);
          }
        }

        &:nth-child(4) {
          button {
            @include submitButtons($validation, white);
          }
        }
      }
    }
  }
}
</style>