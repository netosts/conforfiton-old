<script setup>
import http from "../services/api/http";

import { getSecondUserIdLocal } from "@/services/api/token";

import { definePage } from "vue-router/auto";
import { ref, onMounted, watch } from "vue";
import Pagination from "../components/home/Pagination.vue";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const bodyElement = ref(null);
const students = ref([]);
const studentsFilter = ref("ativos");
const inputBar = ref("");
const inputFilter = ref("inputName");

// FUNCTIONS

// Axios Functions
// Get students from database
function getActiveStudents(value, limit) {
  if (inputBar.value === "") {
    value = "*";
  }
  const personal_id = getSecondUserIdLocal();
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
    value = "*";
  }
  const personal_id = getSecondUserIdLocal();
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
    value = "*";
  }
  const personal_id = getSecondUserIdLocal();
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
    getActiveStudents("*", 100);
  } else if (studentsFilter.value === "desativados") {
    getInactiveStudents("*", 100);
  } else if (studentsFilter.value === "todos") {
    getAllStudents("*", 100);
  }
}

watch(inputBar, (newValue) => {
  // Show students based on input bar + filter
  if (studentsFilter.value === "ativos" && newValue !== "") {
    getActiveStudents(newValue, 100);
  } else if (studentsFilter.value === "ativos" && newValue === "") {
    getActiveStudents("*", 100);
  }
  if (studentsFilter.value === "desativados" && newValue !== "") {
    getInactiveStudents(newValue, 100);
  } else if (studentsFilter.value === "desativados" && newValue === "") {
    getInactiveStudents("*", 100);
  }
  if (studentsFilter.value === "todos" && newValue !== "") {
    getAllStudents(newValue, 100);
  } else if (studentsFilter.value === "todos" && newValue === "") {
    getAllStudents("*", 100);
  }
});

// DOM Mounted
onMounted(() => {
  if (sessionStorage.getItem("submitted")) {
    sessionStorage.removeItem("submitted");
    location.reload();
  }
  getActiveStudents("*", 100);
  bodyElement.value = document.body;
});
</script>

<template>
  <main>
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
        <div class="searchbox__input__filter">
          <select v-model="inputFilter">
            <option value="inputName">Nome</option>
            <option value="inputCpf">CPF</option>
          </select>
        </div>
      </div>
    </div>

    <div class="filter">
      <select v-model="studentsFilter" @change="filterNget">
        <option value="ativos">Ativos</option>
        <option value="desativados">Desativados</option>
        <option value="todos">Todos</option>
      </select>
    </div>

    <Pagination :students="students" />
  </main>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

select,
input {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

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

      &__filter {
        position: relative;

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

        &::after {
          content: "\0025BC";
          font: normal normal normal 12px/1 FontAwesome;
          position: absolute;
          right: 10px;
          top: 50%;
          transform: translateY(-50%);
          color: $txt-title;
          pointer-events: none;
        }
      }
    }
  }

  .filter {
    position: relative;
    display: flex;
    justify-content: flex-end;

    select {
      padding: 8px 40px 8px 10px;
      outline: none;
      border: none;
      border-radius: $border-radius;
      background-color: white;
      cursor: pointer;
      color: $txt-title;
    }

    &::after {
      content: "\0025BC";
      font: normal normal normal 12px/1 FontAwesome;
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      color: $txt-title;
      pointer-events: none;
    }
  }
}
</style>
