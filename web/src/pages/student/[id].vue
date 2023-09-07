<script setup>
import { getStudent } from "../../services/api/get";

import { studentButtons, studentComponents } from "@/services/student/lists";
import { translateRole } from "@/services/helpers";

import { useStudentStore } from "@/stores/student";

import { onMounted, ref } from "vue";
import { useRoute, definePage } from "vue-router/auto";

definePage({
  meta: { isStudent: true, requiresAuth: true },
});

// VARIABLES
const route = useRoute();
const store = useStudentStore();
const student = ref({});

// FUNCTIONS
async function initStudent() {
  student.value = await getStudent(route.params.id);
}

function showContent(id) {
  store.show.fill(false);
  store.show[id] = true;
}

// DOM Mount
onMounted(() => {
  initStudent();
});
</script>

<template>
  <main>
    <div class="profile">
      <div class="profile__picture"></div>
      <div class="profile__info">
        <div class="profile__info__credentials">
          <p>{{ student.name }}</p>
          <span>{{ translateRole(student.role) }}</span>
        </div>
        <div class="profile__info__address">
          <span>
            <font-awesome-icon icon="fa-solid fa-location-dot" />
            California, United States</span
          >
        </div>
      </div>
    </div>
    <div class="content">
      <div class="content__buttons">
        <div class="content__buttons--buttons">
          <button
            v-for="(item, id) in studentButtons"
            :key="id"
            @click="showContent(id)"
            :class="{ 'button--active': store.show[id] }"
          >
            {{ item }}
          </button>
        </div>
        <button class="profile__edit">Editar Perfil</button>
      </div>
      <div class="content__components">
        <component
          v-for="(item, id) in studentComponents"
          :key="id"
          :is="item"
          :show="store.show[id]"
          :student="student"
        />
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

.profile {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 20px;
  padding: 30px;
  border-radius: 4px 4px 0 0;
  background-color: $buttons;

  &__picture {
    width: 90px;
    height: 90px;
    border: 4px solid #e9e9e9;
    background-color: black;
    border-radius: 50%;
  }

  &__info {
    display: flex;
    flex-direction: column;
    gap: 10px;

    &__credentials {
      p {
        font-size: 1.5rem;
        font-weight: 500;
        color: white;
      }
      span {
        font-size: 0.9rem;
        font-weight: 300;
        color: rgba(255, 255, 255, 0.857);
      }
    }

    &__address {
      font-size: 0.8rem;
      font-weight: 300;
      color: rgba(255, 255, 255, 0.678);
    }
  }
}
.content {
  display: flex;
  flex-direction: column;
  gap: 16px;

  &__buttons {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 10px 150px 10px 20px;
    border-radius: 0 0 4px 4px;
    box-shadow: $box-shadow;
    background-color: $buttons;

    &--buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      .button--active {
        background-color: rgba(255, 255, 255, 0.12);
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: $border-radius;
        background-color: transparent;
        cursor: pointer;
        color: rgba(255, 255, 255, 0.84);
        font-size: 0.9rem;
        font-weight: 500;
        transition: 0.3s;

        &:hover {
          background-color: rgba(255, 255, 255, 0.12);
        }
      }
    }

    .profile__edit {
      position: absolute;
      right: 20px;
      @include submitButtons($validation, white);
    }
  }
}
</style>
