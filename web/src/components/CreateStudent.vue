<script setup>
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';


// Variables
const bodyElement = ref(null);
// form variables
const nmPessoa = ref(null);
const cpfCnpj = ref(null);
const rg = ref(null);
const ufRG = ref(null);
const dtNascimento = ref(null);
const dsObs = ref(null);
const dsEmail = ref(null);
const telefone = ref(null);
const altura = ref(null);
const sexo = ref(null);
const peso = ref(null);
// emits
const emit = defineEmits(['isCreateStudentActive']);
// props
const props = defineProps({
  cpfCnpjList: Array
  // rg
  // ufRG
  // tratar erro de duplicada no rg e uf
})

// uf list
const ufList = [
  'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
  'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
];

// Watches

// capitalize first letter of each word in the name
// watch(nmPessoa, (newValue) => {
//   const cleannedValue = newValue.replace(/\b\w/g, (match) => match.toUpperCase());
//   nmPessoa.value = cleannedValue;
// })

watch(cpfCnpj, (newValue) => {
  const cleanedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleanedValue.substring(0, 11);
  cpfCnpj.value = restrictedValue;
});

watch(rg, (newValue) => {
  const cleanedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleanedValue.substring(0, 20);
  rg.value = restrictedValue;
});

watch(ufRG, (newValue) => {
  const cleanedValue = newValue.replace(/[^A-Za-z]/g, ''); // only allow letters (uppercase and lowercase)
  const restrictedValue = cleanedValue.substring(0, 2).toUpperCase(); // restrict to the first two characters and convert to uppercase
  ufRG.value = restrictedValue;
});

watch(telefone, (newValue) => {
  const cleannedValue = newValue.replace(/\D/g, '');
  const formattedValue = formatTelefone(cleannedValue);
  telefone.value = formattedValue;
});

watch(altura, (newValue) => {
  const cleannedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleannedValue.substring(0, 3);
  const formattedValue = formatAltura(restrictedValue);
  altura.value = formattedValue;
});

watch(peso, (newValue) => { // transform peso in 0-3 int numbers and 0-2 decimals
  const cleanedValue = newValue.replace(/[^0-9.]/g, '');
  const parts = cleanedValue.split('.');

  parts[0] = parts[0].substring(0, 3);

  if (parts.length > 1) {
    parts[1] = parts[1].substring(0, 2);
    peso.value = `${parts.join('.')}kg`; // add kg at the end when it has decimals
  } else {
    peso.value = parts.join('.');
  }
});

// !NO KG AT THE END!
// watch(peso, (newValue) => {
//   const cleanedValue = newValue.replace(/[^0-9.]/g, '');
//   const parts = cleanedValue.split('.');

//   parts[0] = parts[0].substring(0, 3);

//   if (parts.length > 1) {
//     parts[1] = parts[1].substring(0, 2);
//   }

//   const restrictedValue = parts.join('.');
//   peso.value = restrictedValue;
// });

// Functions
// close the create tab
function closeCreate() {
  // emit('isCreateStudentActive', false);
  // bodyElement.value.style.overflow = 'auto';
  location.reload();
};

// create a new student
function createStudent() {
  // transform the values that can break the db
  let telefoneTransformed = null;
  let alturaTransformed = null;
  let pesoTransformed = null;
  if (telefone.value !== null) {
    const cleannedTelefone = telefone.value.replace(/\D/g, '');
    telefoneTransformed = cleannedTelefone;
  }
  if (altura.value !== null) {
    const cleannedAltura = altura.value.replace(/\D/g, '');
    const alturaInteger = parseInt(cleannedAltura, 10);
    alturaTransformed = alturaInteger;
  }
  if (peso.value !== null) {
    const cleannedPeso = peso.value.replace(/[^\d.]/g, '');
    const pesoFloat = parseFloat(cleannedPeso);
    pesoTransformed = pesoFloat;
  }

  // get the current date and time
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();

  // axios post the form
  console.log('CRIANDO ALUNO...');
  if (!props.cpfCnpjList.includes(cpfCnpj.value)) { // check for cpf duplicates
    axios.post('/student', {
      "nmPessoa": nmPessoa.value,
      "ativo": true, // default: true
      "ser": "AL", // default: Aluno (AL)
      "tipoPessoa": "F", // default: Pessoa Física (F)
      "cpfCnpj": cpfCnpj.value,
      "rg": rg.value,
      "ufRG": ufRG.value,
      "dtNascimento": dtNascimento.value,
      "dsObs": dsObs.value,
      "dsEmail": dsEmail.value,
      "telefone": telefoneTransformed,
      "altura": alturaTransformed,
      "sexo": sexo.value,
      "fotoAluno": null,
      "peso": pesoTransformed,
      "dtData": formattedDate // current date and time
    }).then((res) => {
      alert(res.data);
      console.log('ALUNO CRIADO COM SUCESSO..');
      location.reload();
    }).catch((err) => {
      console.error(err);
    });
  } else {
    console.error('ERRO: ESTE CPF JÁ EXISTE NO BANCO DE DADOS!');
  }
};

// function to format the telefone number
function formatTelefone(value) {
  const match = value.match(/^(\d{2})(\d{5})(\d{4})$/);
  if (match) {
    return `(${match[1]})${match[2]}-${match[3]}`;
  }
  return value;
};

// function to format the altura value
function formatAltura(value) {
  const match = value.match(/^(\d{3})$/)
  if (match) {
    return `${match[0]}cm`;
  }
  return value;
}

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside id="createScroll" class="create">
    <form @submit.prevent="createStudent" class="create__form" v-motion-slide-visible-top>
      <div class="create__form__bg"></div>

      <div class="form__container">

        <div class="form__container__title">
          <h1 class="form__container__title__text">Cadastrar Novo Aluno</h1>
          <button type="button" @click="closeCreate" class="form__container__title__button">
            <font-awesome-icon icon="fa-solid fa-xmark" size="2xl" />
          </button>
        </div>

        <div class="form__container__fotoAluno">
          <img src="../assets/images/default-profile-picture2.jpg" alt="#" class="form__container__fotoAluno__image">
          <p class="form__container__fotoAluno__text">Foto do Aluno</p>
        </div>

        <!-- Início do cadastro -->
        <div class="form__container__nmPessoa">
          <label for="nmPessoa">Nome completo <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
          <input v-model="nmPessoa" type="text" id="nmPessoa" maxlength="60" placeholder="Digite o nome do aluno"
            required>
        </div>


        <div class="form__container__cpf-rg">
          <div class="form__container__cpf-rg__cpfCnpj">
            <label for="cpfCnpj">CPF <abbr title="VALOR NECESSÁRIO | Apenas números" class="required">*</abbr> </label>
            <input v-model="cpfCnpj" type="text" id="cpfCnpj" minlength="11" placeholder="Digite o CPF do aluno" required>
          </div>
          <div class="form__container__cpf-rg__rg">
            <label for="rg">RG</label>
            <input v-model="rg" type="text" id="rg" placeholder="Digite o RG do aluno">
          </div>
        </div>

        <div class="form__container__tel-email">
          <div class="form__container__tel-email__telefone">
            <label for="telefone">Telefone</label>
            <input v-model="telefone" type="tel" id="telefone" minlength="11" maxlength="11" placeholder="(79)99999-9999">
          </div>

          <div class="form__container__tel-email__dsEmail">
            <label for="dsEmail">E-mail</label>
            <input v-model="dsEmail" type="email" id="dsEmail" maxlength="80" placeholder="Digite o Email do aluno">
          </div>
        </div>

        <div class="form__container__uf-data-sexo">
          <div class="form__container__uf-data-sexo__ufRG">
            <label for="ufRG">UF</label>
            <!-- <input v-model="ufRG" type="text" id="ufRG" minlength="2" placeholder="SE"> -->
            <select v-model="ufRG" id="ufRG">
              <option v-for="uf in ufList" :value="uf">{{ uf }}</option>
            </select>
          </div>

          <div class="form__container__uf-data-sexo__dtNascimento">
            <label for="dtNascimento">Data Nascimento</label>
            <input v-model="dtNascimento" type="date" id="dtNascimento">
          </div>

          <div class="form__container__uf-data-sexo__sexo">
            <label for="sexo">Sexo Biológico <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
            <select v-model="sexo" id="sexo" required>
              <option value="Masculino">Masculino</option>
              <option value="Feminino">Feminino</option>
            </select>
          </div>
        </div>

        <div class="form__container__altura-peso">
          <div class="form__container__altura-peso__altura">
            <label for="altura">Altura(cm) <abbr
                title="VALOR NECESSÁRIO | Digite pelo menos 3 números. A altura será representada em centímetros"
                class="required">*</abbr> </label>
            <input v-model="altura" type="text" id="altura" minlength="3" placeholder="180cm" required>
          </div>

          <div class="form__container__altura-peso__peso">
            <label for="peso">Peso(kg)</label>
            <input v-model="peso" type="text" id="peso" placeholder="90.30kg">
          </div>
        </div>

        <div class="form__container__dsObs">
          <label for="dsObs">Observação</label>
          <textarea v-model="dsObs" id="dsObs" placeholder="Digite aqui se tiver alguma observação"></textarea>
        </div>

        <!-- SUBMIT -->
        <div class="form__container__submit">
          <input type="submit" value="Cadastrar Aluno">

          <button type="button" @click="closeCreate" class="form__container__submit__button">Cancelar</button>
        </div>
      </div>
    </form>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

.create {
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

  &__form {
    position: relative;
    z-index: 999;
    margin: auto;
    border-radius: $border-radius;
    background-color: white;
    transition: .5s ease-out;

    @include mq(s) {
      width: 100%;
    }

    &__bg {
      position: absolute;
      width: 100%;
      height: 140px;
      z-index: 0;
      border-radius: 4px 4px 0 0;
      background-color: #46578b;
    }

    .form__container {
      display: flex;
      flex-direction: column;
      gap: 20px;
      position: relative;
      padding: 10px 20px 20px 20px;
      width: 800px;
      font-size: .85rem;
      font-weight: 500;
      color: $txt-aside;

      @include mq(l) {
        width: 500px;
      }

      @include mq(s) {
        width: 100%;
      }

      &__title {
        display: flex;
        justify-content: space-between;
        align-items: center;

        &__text {
          font-size: 1rem;
          font-weight: 600;
          color: white;
        }

        &__button {
          margin-right: -10px;
          width: 40px;
          height: 40px;
          border: none;
          border-radius: 50%;
          background-color: transparent;
          color: rgba(255, 255, 255, 0.588);
          cursor: pointer;
          transition: .2s;

          &:hover {
            color: white;
            background-color: rgba(0, 0, 0, 0.267);
          }
        }
      }

      &__fotoAluno {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 29px 0 15px 0;

        &__image {
          width: 80px;
          height: 80px;
          border: 8px solid $profile-pic;
          border-radius: 50%;
        }

        &__text {
          padding-top: 10px;
          font-size: 0.8rem;
          font-weight: 500;
          color: $txt-title;
        }
      }

      &__nmPessoa {
        @include inputContainers();

        input {
          @include createInput();
        }
      }

      &__cpf-rg {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        &__cpfCnpj {
          @include inputContainers();

          input {
            @include createInput();
          }
        }

        &__rg {
          @include inputContainers();

          input {
            @include createInput();
          }
        }
      }

      &__tel-email {
        display: grid;
        grid-template-columns: 200px 1fr;
        gap: 20px;

        @include mq(l) {
          grid-template-columns: 1fr 1fr;
        }

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        &__telefone {
          @include inputContainers();

          input {
            @include createInput();
          }
        }

        &__dsEmail {
          @include inputContainers();

          input {
            @include createInput();
          }
        }
      }

      &__uf-data-sexo {
        display: grid;
        grid-template-columns: 80px 150px 200px;
        gap: 20px;

        @include mq(l) {
          grid-template-columns: 80px 1fr 1fr
        }

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        &__ufRG {
          @include inputContainers();

          select {
            @include createInput();
          }
        }

        &__dtNascimento {
          @include inputContainers();

          input {
            @include createInput();
          }
        }

        &__sexo {
          @include inputContainers();

          select {
            @include createInput();
          }
        }
      }

      &__altura-peso {
        display: grid;
        grid-template-columns: 200px 200px;
        gap: 20px;

        &__altura {
          @include inputContainers();

          input {
            @include createInput();
          }
        }

        &__peso {
          @include inputContainers();

          input {
            @include createInput();
          }
        }
      }

      &__dsObs {
        @include inputContainers();

        textarea {
          height: 80px;
          @include createInput();
          resize: none;
        }
      }

      &__submit {
        display: flex;
        justify-content: space-between;

        input {
          @include submitButtons($validation, white);
        }

        &__button {
          @include submitButtons($profile-pic, $txt-title);
        }
      }
    }
  }

  &__close {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.456);
  }
}

.required {
  position: absolute;
  color: red;
  font-size: 1.2rem;
  margin-left: 5px;
  text-decoration: none;
}
</style>