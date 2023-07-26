<script setup>
import { ref, onMounted } from 'vue';

// VARIABLES
const bodyElement = ref(null);

// Emits
const emit = defineEmits(['isAvaliarActive']);

// Props
const props = defineProps({
  studentId: Number
})

function closeAvaliar() {
  emit('isAvaliarActive', false);
  bodyElement.value.style.overflow = 'auto';
  console.log(props.studentId)
};

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
})
</script>

<template>
  <aside>
    <div class="container">
      <div class="close">
        <button @click="closeAvaliar">
          <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
        </button>
      </div>
      <div class="content">
        <div class="content__item">
          <RouterLink :to="'/anamnese/' + studentId">
            <button>Anamnese</button>
          </RouterLink>
        </div>
        <div class="content__item">
          <RouterLink to="/neuromuscular">
            <button>Neuromuscular</button>
          </RouterLink>
        </div>
        <div class="content__item">
          <RouterLink to="/antropometria">
            <button>Antropometria</button>
          </RouterLink>
        </div>
        <div class="content__item">
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

  @include mq(s) {
    padding: 10px;
  }

  .container {

    .close {
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;

      button {
        margin-right: -40px;
        width: 40px;
        height: 40px;
        border: none;
        border-radius: 50%;
        background-color: rgba(0, 0, 0, 0.267);
        color: white;
        cursor: pointer;
      }
    }

    .content {
      display: flex;
      gap: 20px;
      padding: 10px;
      background-color: $validation;
      border-radius: $border-radius;
    }
  }
}
</style>