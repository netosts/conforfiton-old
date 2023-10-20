<script setup>
import { getStudent } from "@/services/api/get";

import { studentButtons } from "@/services/student/lists";
import { translateRole } from "@/services/helpers";
import { formatAge } from "@/services/formats";

import { onMounted } from "vue";
import { useRoute, useRouter, definePage } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";
import { useAvaliarStore } from "@/stores/avaliar";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const route = useRoute();
const router = useRouter();
const store = useStudentStore();
const avaliarStore = useAvaliarStore();

// FUNCTIONS
async function initStudent() {
  try {
    if (store.student.id !== route.params.id) {
      store.student.value = await getStudent(route.params.id);
      avaliarStore["student"] = {
        age: formatAge(store.student.value.birth_date),
      };
      store.student.id = route.params.id;
    }
  } catch (err) {
    if (err.response.data.msg === "Student not found.") {
      router.push("/NotFound");
    }
  }
}

// DOM Mount
onMounted(() => {
  if (sessionStorage.getItem("submitted")) {
    sessionStorage.removeItem("submitted");
    location.reload();
  }
  initStudent();
});
</script>

<template>
  <main>
    <div
      class="profile"
      :class="store.student.value?.deleted_at ? 'inactive' : null"
    >
      <div class="profile__picture"></div>
      <div class="profile__info">
        <div class="profile__info__credentials">
          <p>{{ store.student.value?.name }}</p>
          <span>{{ translateRole(store.student?.value?.role) }}</span>
        </div>
        <div class="profile__info__address">
          <span>
            <font-awesome-icon icon="fa-solid fa-location-dot" />
            California, United States</span
          >
        </div>
      </div>
      <RouterLink :to="`/student/${route.params.id}/update-profile`">
        <button class="profile__edit">
          <font-awesome-icon icon="fa-solid fa-pen-to-square" size="xl" />
        </button>
      </RouterLink>
    </div>

    <div class="content">
      <div
        class="content__buttons"
        :class="store.student.value?.deleted_at ? 'inactive' : null"
      >
        <div class="content__buttons--buttons">
          <RouterLink
            v-for="(item, id) in studentButtons"
            :key="id"
            :to="`/student/${route.params.id}/${item.link}`"
          >
            <button>
              {{ item.button }}
            </button>
          </RouterLink>
        </div>
      </div>
      <div class="content__components">
        <RouterView :student="store.student.value" />
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
      padding-right: 40px;
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

  &__edit {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 50px;
    height: 50px;
    border: none;
    border-radius: 50%;
    background-color: transparent;
    color: white;
    cursor: pointer;
    transition: 0.2s;

    &:hover {
      background-color: rgba(255, 255, 255, 0.12);
    }

    &:active {
      filter: brightness(0.7);
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
    padding: 10px 20px;
    border-radius: 0 0 4px 4px;
    box-shadow: $box-shadow;
    background-color: $buttons;

    &--buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;

      a {
        border-radius: $border-radius;
        transition: 0.3s;

        &:hover {
          background-color: rgba(255, 255, 255, 0.12);
        }

        button {
          padding: 10px 16px;
          border: none;
          background-color: transparent;
          cursor: pointer;
          color: rgba(255, 255, 255, 0.84);
          font-size: 0.9rem;
          font-weight: 500;
        }
      }

      .router-link-exact-active {
        background-color: rgba(255, 255, 255, 0.12);
      }
    }
  }
}

.inactive {
  background-color: rgb(251, 65, 65);
}
</style>
