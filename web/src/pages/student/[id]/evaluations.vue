<script setup>
import { evaluationsButtons } from "@/services/student/lists";

import { onMounted, ref } from "vue";
import { definePage } from "vue-router/auto";

import Avaliar from "@/components/Avaliar.vue";

definePage({
  meta: { requiresAuth: true },
});

const bodyElement = ref(null);
const isAvaliarActive = ref(false);

const props = defineProps({
  student: Object,
});

// Send Props
const studentId = ref(null);
const studentName = ref(null);

// Handle Emits
const handleAvaliar = (emittedValue) => {
  return (isAvaliarActive.value = emittedValue);
};

function toggleAvaliar(id, name) {
  isAvaliarActive.value = !isAvaliarActive.value;
  bodyElement.value.style.overflow = isAvaliarActive.value ? "hidden" : "auto";
  studentId.value = id;
  studentName.value = name;
}

onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <Avaliar
    :studentName="studentName"
    :studentId="studentId"
    @isAvaliarActive="handleAvaliar"
    v-show="isAvaliarActive"
  />

  <section class="view-container">
    <h2>Visualizar avaliação</h2>
    <div class="view-evaluationbox">
      <div v-for="(item, id) in evaluationsButtons" :key="id">
        <RouterLink :to="`/student/${student?.person_id}/${item.link}`">
          <button class="view-evaluationbox__button">
            <div class="view-evaluationbox__button__text">
              <h3>{{ item.name }}</h3>
              <p>{{ item.description }}</p>
            </div>
            <img :src="item.img" />
          </button>
        </RouterLink>
      </div>
    </div>
  </section>

  <aside class="new-evaluation">
    <button @click="toggleAvaliar(student?.person_id, student?.name)">
      <font-awesome-icon icon="fa-solid fa-plus" />
      Iniciar Nova Avaliação
    </button>
  </aside>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
  padding: 20px;
  padding-bottom: 40px;
  margin-bottom: 20px;
  width: 100%;
  border-radius: $border-radius;
  box-shadow: $box-shadow;
  background-color: white;

  h2 {
    text-align: center;
    padding-bottom: 20px;
    color: $txt-title;
    transition: 0.2s;
    @include mq(xs) {
      font-size: 1.3rem;
    }
  }
}
.view-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  .view-evaluationbox {
    display: grid;
    grid-template-columns: 1fr 1fr;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;

    @include mq(l-xl) {
      display: flex;
    }

    a {
      text-decoration: none;
    }
    &__button {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      height: 120px;
      width: 300px;
      padding: 20px;
      border: none;
      border-radius: $border-radius;
      box-shadow: $box-shadow;
      background-color: rgb(246, 246, 246);
      text-align: start;
      cursor: pointer;
      transition: 0.2s;

      @include mq(xs) {
        width: 265px;
      }

      &:hover {
        filter: brightness(0.9);
      }

      &:active {
        filter: brightness(0.7);
      }

      &__text {
        h3 {
          font-size: 1.2rem;
          font-weight: 700;
          color: rgb(43, 43, 43);
          @include mq(xs) {
            font-size: 1.1rem;
          }
        }
        p {
          font-size: 1rem;
          color: $txt-subtitle;
          @include mq(xs) {
            font-size: 0.9rem;
          }
        }
      }
      img {
        height: 90px;
        width: 90px;
        transition: 0.2s;
        @include mq(xs) {
          height: 65px;
          width: 65px;
        }
      }
    }
  }
}
.new-evaluation {
  display: flex;
  justify-content: flex-end;
  button {
    flex: 1;
    margin-top: -7px;
    margin-bottom: 10px;
    font-weight: 500;
    font-size: 1rem;
    padding: 16px 20px;
    border: none;
    border-radius: $border-radius;
    background-color: $buttons;
    color: white;
    cursor: pointer;
    transition: 0.2s;

    &:hover {
      filter: brightness(0.9);
    }

    &:active {
      filter: brightness(0.7);
    }
  }
}
</style>
