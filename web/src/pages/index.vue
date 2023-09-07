<script setup>
import http from "../services/api/http";
import Avaliar from "../components/Avaliar.vue";

import { getUserIdSession } from "@/services/api/token";
import { translateGender } from "@/services/helpers";

import { definePage } from "vue-router/auto";
import { ref, onMounted, watch } from "vue";
import { formatAge } from "../services/validators/formats";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const bodyElement = ref(null);
const students = ref([]);
const isAvaliarActive = ref(false);
const studentsFilter = ref("ativos");
const inputBar = ref("");
const inputFilter = ref("inputName");

// Send Props
const studentId = ref(null);
const studentName = ref(null);

// Handle Emits
const handleAvaliar = (emittedValue) => {
  return (isAvaliarActive.value = emittedValue);
};

// FUNCTIONS
function toggleAvaliar(id, name) {
  isAvaliarActive.value = !isAvaliarActive.value;
  bodyElement.value.style.overflow = isAvaliarActive.value ? "hidden" : "auto";
  studentId.value = id;
  studentName.value = name;
}

// Axios Functions
// Get students from database
function getActiveStudents(value, limit) {
  if (inputBar.value === "") {
    value = "%";
  }
  const personal_id = getUserIdSession();
  http
    .get(
      `/student/active/${inputFilter.value}/${value}/${limit}/${personal_id}`
    )
    .then((res) => {
      students.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
}

function getInactiveStudents(value, limit) {
  if (inputBar.value === "") {
    value = "%";
  }
  const personal_id = getUserIdSession();
  http
    .get(
      `/student/inactive/${inputFilter.value}/${value}/${limit}/${personal_id}`
    )
    .then((res) => {
      students.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
}

function getAllStudents(value, limit) {
  if (inputBar.value === "") {
    value = "%";
  }
  const personal_id = getUserIdSession();
  http
    .get(`/student/${inputFilter.value}/${value}/${limit}/${personal_id}`)
    .then((res) => {
      students.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
}

// WATCHES
function filterNget() {
  // Show students based on filter
  if (studentsFilter.value === "ativos") {
    getActiveStudents("%", 5);
  } else if (studentsFilter.value === "desativados") {
    getInactiveStudents("%", 5);
  } else if (studentsFilter.value === "todos") {
    getAllStudents("%", 5);
  }
}

watch(inputBar, (newValue) => {
  // Show students based on input bar + filter
  if (studentsFilter.value === "ativos" && newValue !== "") {
    getActiveStudents(newValue, 100);
  } else if (studentsFilter.value === "ativos" && newValue === "") {
    getActiveStudents("%", 5);
  }
  if (studentsFilter.value === "desativados" && newValue !== "") {
    getInactiveStudents(newValue, 100);
  } else if (studentsFilter.value === "desativados" && newValue === "") {
    getInactiveStudents("%", 5);
  }
  if (studentsFilter.value === "todos" && newValue !== "") {
    getAllStudents(newValue, 100);
  } else if (studentsFilter.value === "todos" && newValue === "") {
    getAllStudents("%", 5);
  }
});

// DOM Mounted
onMounted(() => {
  if (sessionStorage.getItem("submitted")) {
    sessionStorage.removeItem("submitted");
    location.reload();
  }
  getActiveStudents("%", 100);
  bodyElement.value = document.body;
});
</script>

<template>
  <main>
    <Avaliar
      :studentName="studentName"
      :studentId="studentId"
      @isAvaliarActive="handleAvaliar"
      v-show="isAvaliarActive"
    />

    <div class="searchbox">
      <div class="searchbox__title">
        <h3>Procurar Alunos</h3>
        <RouterLink to="/register">
          <button>+ Novo Aluno</button>
        </RouterLink>
      </div>

      <div class="searchbox__input">
        <div class="searchbox__input__db">
          <font-awesome-icon
            class="searchbox__input__db__icon"
            icon="fa-solid fa-magnifying-glass"
            size="sm"
          />
          <input
            v-model="inputBar"
            type="text"
            id="searchDb"
            placeholder="Procurar alunos no banco de dados..."
          />
        </div>
        <select v-model="inputFilter">
          <option value="inputName">Nome</option>
          <option value="inputCpf">CPF</option>
        </select>
      </div>
    </div>

    <div class="filter">
      <select v-model="studentsFilter" @change="filterNget">
        <option value="ativos">Ativos</option>
        <option value="desativados">Desativados</option>
        <option value="todos">Todos</option>
      </select>
    </div>

    <div class="students">
      <section v-for="student in students" :key="student" class="student">
        <div class="student__container">
          <RouterLink :to="`/student/${student.id}`">
            <div class="student__container__profile">
              <div class="student__container__profile__picture">
                <!-- <img src="../assets/images/default-profile-picture2.jpg" alt="default profile picture"> -->
              </div>
              <div class="student__container__profile__info">
                <div class="student__container__profile__info__name">
                  <p>{{ student.name }}</p>
                </div>
                <div class="student__container__profile__info__content">
                  <p>
                    Sexo:
                    <strong>{{ translateGender(student.gender) }}</strong> |
                  </p>
                  <p>
                    Idade:
                    <strong>{{ formatAge(student.birth_date) }}</strong>
                    |
                  </p>
                  <p>
                    Altura: <strong>{{ student.height }}cm</strong> |
                  </p>
                  <p>
                    Peso:
                    <strong>{{ student.weight + "kg" }}</strong>
                  </p>
                  |
                  <p>Desempenho: Bom</p>
                </div>
              </div>
            </div>
          </RouterLink>
          <div class="student__container__button">
            <div class="student__container__button__box">
              <button @click="toggleAvaliar(student.id, student.name)">
                Avaliar
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 25px;

  .searchbox {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
    padding: 16px;
    border-radius: $border-radius;
    background: white;
    box-shadow: $box-shadow;

    &__title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding-bottom: 16px;

      h3 {
        font-size: 1rem;
        font-weight: 500;
        color: $txt-title;
      }

      button {
        @include submitButtons($buttons, white);
      }
    }

    &__input {
      display: flex;
      gap: 25px;

      @include mq(m) {
        flex-direction: column;
        gap: 15px;
      }

      &__db {
        position: relative;
        width: 100%;

        &__icon {
          position: absolute;
          top: 50%;
          left: 14px;
          transform: translateY(-50%);
          color: $txt-subtitle;
        }

        input {
          padding: 8px 15px 8px 40px;
          width: 100%;
          @include inputBar();

          &::placeholder {
            color: $txt-subtitle;
          }
        }
      }

      select {
        padding: 8px 15px 8px 10px;
        width: 250px;
        @include inputBar();
        cursor: pointer;
        color: $txt-title;

        @include mq(m) {
          width: 100%;
        }
      }
    }
  }

  .filter {
    display: flex;
    justify-content: flex-end;

    select {
      padding: 8px 15px 8px 10px;
      outline: none;
      border: none;
      border-radius: $border-radius;
      cursor: pointer;
      color: $txt-title;
    }
  }

  .students {
    display: flex;
    flex-direction: column;
    gap: 25px;
    width: 100%;

    .student {
      border-radius: $border-radius;
      box-shadow: $box-shadow;
      background-color: white;

      &__container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;

        a {
          flex: 1;
          padding: 16px;
          text-decoration: none;
          transition: 0.2s;

          &:hover {
            filter: brightness(0.8);
          }
        }

        &__profile {
          display: flex;
          flex-wrap: wrap;
          gap: 14px;

          &__picture {
            width: 60px;
            height: 60px;
            border-radius: $border-radius;
            background-image: url("../assets/images/default-profile-picture2.jpg");
            background-size: cover;
          }

          &__info {
            display: flex;
            flex-direction: column;
            justify-content: space-around;

            &__name {
              font-size: 1.2rem;
              font-weight: 600;
              color: $txt-title;
            }

            &__content {
              display: flex;
              flex-wrap: wrap;
              gap: 5px;
              font-size: 0.9rem;
              color: $txt-subtitle;

              @include mq(l) {
                display: none;
              }
            }
          }
        }

        &__button {
          margin-right: 16px;
          button {
            padding: 14px 20px;
            border: none;
            border-radius: $border-radius;
            background-color: $validation;
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
      }
    }
  }
}
</style>
