<script setup>
import CreateStudent from '../components/CreateStudent.vue';
import StudentDetails from '../components/StudentDetails.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';


// Variables
const bodyElement = ref(null);
const students = ref([]);
const studentsCpfCnpj = ref([]);
const isCreateStudentActive = ref(false);
const studentDetails = ref(null);
const studentsFilter = ref('ativos');
const isStudentDetailsActive = ref(false);

// Handle emits
const handleCreate = (emittedValue) => {
  return isCreateStudentActive.value = emittedValue;
};

const handleDetails = (emittedValue) => {
  return isStudentDetailsActive.value = emittedValue;
}

// Functions
// toggle the create student form
function toggleCreate() {
  isCreateStudentActive.value = !isCreateStudentActive.value;
  bodyElement.value.style.overflow = isCreateStudentActive.value ? 'hidden' : 'auto';
};

// axios functions
// get students from database
function getActiveStudents() {
  axios.get(`/students/active`).then((res) => {
    students.value = res.data;
    studentDetails.value = students.value[0];
  }).catch((err) => {
    console.error(err);
  });
};

function getInactiveStudents() {
  axios.get(`/students/inactive`).then((res) => {
    students.value = res.data;
    studentDetails.value = students.value[0];
  }).catch((err) => {
    console.error(err);
  });
};

function getAllStudents() {
  axios.get(`/students`).then((res) => {
    students.value = res.data;
    studentDetails.value = students.value[0];
  });
};

// get all cpf/cnpj in database
function getCpfCnpj() {
  axios.get(`/cpfCnpj`).then((res) => {
    studentsCpfCnpj.value = res.data;
  }).catch((err) => {
    console.error(err);
  });
};

// get student by id from database
function getStudent(ID_Pessoa) {
  axios.get(`/student/${ID_Pessoa}`).then((res) => {
    studentDetails.value = res.data;
    isStudentDetailsActive.value = true;
    bodyElement.value.style.overflow = isStudentDetailsActive.value ? 'hidden' : 'auto';
  }).catch((err) => {
    console.error(err);
  });
};

// format functions
function formatTelefone(phoneNumber) {
  const tel = phoneNumber;

  // extract the different parts of the phone number
  const ddd = tel.slice(0, 2);
  const firstPart = tel.slice(2, 7);
  const secondPart = tel.slice(7, 11);

  // create the formatted phone number string
  const formattedPhoneNumber = `(${ddd})${firstPart}-${secondPart}`;

  return formattedPhoneNumber;
};

function formatCpf(cpf) {

  // extract the different parts of the cpf number
  const firstPart = cpf.slice(0, 3);
  const secondPart = cpf.slice(3, 6);
  const thirdPart = cpf.slice(6, 9);
  const lastPart = cpf.slice(9, 11);

  // create the formatted cpf number string
  const formattedCpfNumber = `${firstPart}.${secondPart}.${thirdPart}-${lastPart}`;

  return formattedCpfNumber;
};

// transform dtNascimento YYYY-MM-DD into person's age
function formatAge(value) {
  const birthdate = value;
  const today = new Date();

  // extract the birthdate parts
  const birthdateParts = birthdate.split('-');
  const birthYear = parseInt(birthdateParts[0]);
  const birthMonth = parseInt(birthdateParts[1]);
  const birthDay = parseInt(birthdateParts[2]);

  // calculate the person's age
  let age = today.getFullYear() - birthYear;

  // check if the current month and day are before the birth month and day
  if (
    today.getMonth() < birthMonth - 1 ||
    (today.getMonth() === birthMonth - 1 && today.getDate() < birthDay)
  ) {
    age--;
  }

  return age;
};

// Watch
function filterNget() {
  if (studentsFilter.value === 'ativos') {
    getActiveStudents();
  } else if (studentsFilter.value === 'desativados') {
    getInactiveStudents();
  } else if (studentsFilter.value === 'todos') {
    getAllStudents();
  }
};

// DOM Mounted
onMounted(() => {
  getActiveStudents();
  getCpfCnpj();
  bodyElement.value = document.body;
});
</script>

<template>
  <main>
    <CreateStudent :cpfCnpjList="studentsCpfCnpj" @isCreateStudentActive="handleCreate" v-show="isCreateStudentActive" />

    <div class="searchbox">
      <div class="searchbox__title">
        <h3>Procurar Alunos</h3>
        <button class="create-button" @click="toggleCreate">+ Cadastrar Aluno</button>
      </div>

      <div class="searchbox__input">
        <div class="searchbox__input__db">
          <font-awesome-icon class="searchbox__input__db__icon" icon="fa-solid fa-magnifying-glass" size="sm" />
          <input type="text" name="searchDb" id="searchDb" placeholder="Procurar alunos no banco de dados...">
        </div>
        <select>
          <option value="#" selected>Nome</option>
          <option value="#">CPF</option>
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

    <div class="sections">
      <div class="sections__students">
        <section v-for="student in students" :key="student" class="student">
          <div class="student__if">
            <div class="student__if__container1">
              <div class="student__if__container1__identity">
                <div class="student__if__container1__identity__profile">
                  <div class="student__if__container1__identity__profile__picture">
                    <!-- <img src="../assets/images/default-profile-picture2.jpg" alt="default profile picture"> -->
                  </div>
                  <div class="student__if__container1__identity__profile__info">
                    <div class="student__if__container1__identity__profile__info__name">
                      <p>{{ student.nmPessoa }}</p>
                    </div>
                    <div class="student__if__container1__identity__profile__info__desempenho">
                      <p>Desempenho: Bom</p>
                    </div>
                  </div>
                </div>
                <div class="student__if__container1__identity__button">
                  <button>Avaliar</button>
                </div>
              </div>
              <div class="student__if__container1__info">
                <p>Sexo: <strong>{{ student.sexo }}</strong> | </p>
                <p>Idade: <strong>{{ student.dtNascimento ? formatAge(student.dtNascimento) : '' }}</strong> | </p>
                <p>Altura: <strong>{{ student.altura }}cm</strong> | </p>
                <p>Peso: <strong>{{ student.peso ? student.peso + 'kg' : '' }}</strong></p>
              </div>
              <div class="student__if__container1__dsObs">
                <p>{{ student.dsObs ? student.dsObs : '' }}</p>
              </div>
            </div>
            <div class="student__if__container2">
              <div class="student__if__container2__details">
                <p v-if="!student.deleted_at">
                  <font-awesome-icon icon="fa-solid fa-check" />
                  Ativo
                </p>
                <p v-if="student.deleted_at">
                  <font-awesome-icon icon="fa-solid fa-x" size="sm" />
                  Desativado
                </p>
                <p v-if="student.ufRG">
                  <font-awesome-icon icon="fa-solid fa-location-dot" />
                  {{ student.ufRG }}
                </p>
                <p v-if="student.telefone">
                  <font-awesome-icon icon="fa-solid fa-phone-flip" />
                  {{ formatTelefone(student.telefone) }}
                </p>
                <p v-if="student.dsEmail">
                  <font-awesome-icon icon="fa-solid fa-envelope" />
                  {{ student.dsEmail }}
                </p>
                <button @click="getStudent(student.ID_Pessoa)">Mais Detalhes</button>
              </div>
            </div>
          </div>
        </section>
      </div>

      <StudentDetails :studentDetails="studentDetails" @isStudentDetailsActive="handleDetails"
        v-show="isStudentDetailsActive" />
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';


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
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.103);

    &__title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 16px;

      h3 {
        font-size: 1rem;
        font-weight: 500;
        color: $txt-title;
      }

      button {
        padding: 10px 20px;
        border: none;
        border-radius: $border-radius;
        background-color: $buttons;
        color: white;
        cursor: pointer;
        transition: .3s;

        &:hover {
          filter: brightness(.85);
        }

        &:active {
          filter: brightness(.5);
        }
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

      @include mq(m) {
        width: 100%;
      }
    }
  }

  .sections {
    display: flex;
    gap: 25px;

    @include mq(l) {
      flex-direction: column;
    }

    &__students {
      display: flex;
      flex-direction: column;
      gap: 25px;
      width: 100%;

      .student {
        display: flex;
        flex-direction: column;
        width: 100%;
        border-radius: $border-radius;
        box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.103);
        background-color: white;

        &__if {
          &__container1 {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 16px 16px 10px 16px;
            border-bottom: 2px dotted $background;

            &__identity {
              display: flex;
              justify-content: space-between;
              gap: 20px;

              &__profile {
                display: flex;
                flex-wrap: wrap;
                gap: 14px;

                &__picture {
                  width: 50px;
                  height: 50px;
                  border-radius: $border-radius;
                  background-image: url('../assets/images/default-profile-picture2.jpg');
                  background-size: cover;
                }

                &__info {
                  display: flex;
                  flex-direction: column;

                  &__name {
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: $txt-title;
                  }

                  &__desempenho {
                    font-size: 0.85rem;
                    color: $txt-subtitle;
                  }
                }
              }

              &__button {
                button {
                  @include submitButtons($validation, white);
                }
              }
            }

            &__info {
              display: flex;
              gap: 5px;
              font-size: .9rem;
              color: $txt-aside;
            }

            &__dsObs {
              font-size: .85rem;
              color: $txt-subtitle;
            }
          }

          &__container2 {
            padding: 10px 16px;

            &__details {
              display: flex;
              align-items: center;
              justify-content: space-between;
              flex-wrap: wrap;
              gap: 16px;

              p {
                font-size: 0.85rem;
                color: $txt-aside;
              }

              button {
                padding: 8px 16px;
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
          }
        }
      }
    }
  }
}
</style>