<script setup>
import axios from 'axios';
import { getCpfCnpj, getRgUF } from '../services/students/get';
import { postStudent } from '../services/students/post';

import { formatTelefone, formatAltura } from '../services/validators/formats';
import { cpfValidator, dateValidator } from '../services/validators/validators';

import { ref, reactive, watch, onMounted } from 'vue';

import RegisterField from './RegisterField.vue';
import * as yup from 'yup';
import { Form } from 'vee-validate';

const schema = yup.object({
  name: yup.string().required('Por favor digite o nome do aluno.'),
  cpf: yup.string().required('Por favor digite o CPF do aluno.')
    .matches(/^[0-9]{11}$/, 'O CPF precisa ter 11 números.')
    .test('cpf-validation', 'O CPF não é válido.', cpfValidator)
    .test('cpf-unique', 'O CPF já foi cadastrado.', async function (value) {
      const studentsCpfCnpj = await getCpfCnpj(axios);
      return !studentsCpfCnpj.includes(value);
    }),

});

// Variables
const bodyElement = ref(null);
const submitted = ref(false);
// form variables
const form = reactive({
  nmPessoa: '',
  ser: 'Aluno',
  tipoPessoa: 'PF',
  cpfCnpj: '',
  rg: '',
  ufRG: '',
  empPersonal: false,
  dtNascimento: '',
  dsObs: '',
  dsEmail: '',
  telefone: '',
  altura: '',
  sexo: '',
  tmCamisa: '',
  fotoAluno: null,
  ID_Empresa: 1,
  ID_Personal: 2,
  peso: '',
  dtData: '',
  bpmRepouso: '',
  bpmMaximo: '',
});
const nmPessoa = ref('');
const cpfCnpj = ref('');
const rg = ref('');
const ufRG = ref('');
const telefone = ref('');
const dsEmail = ref('');
const dtNascimento = ref('');
const sexo = ref('');
const tmCamisa = ref('');
const altura = ref('');
const peso = ref('');
const bpmMaximo = ref('');
const bpmRepouso = ref('');
const dsObs = ref('');

// emits
const emit = defineEmits(['isCreateStudentActive']);

// Lists
const ufList = [
  'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
  'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
];
const sexoList = [
  'Masculino', 'Feminino'
];
const tmCamisaList = [
  'PP', 'P', 'M', 'G', 'GG', 'XG'
];

// Functions
// close the create tab
function closeCreate() {
  location.reload();
};

// create a new student
async function onSubmit(values) {
  // get the current date and time
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  form.dtData = formattedDate;
  console.log(values)
  console.log(form)
  submitted.value = true;
  console.log('CRIANDO ALUNO...');
  postStudent(axios, form);
  // validators
  // rg/uf
  if (rg.value !== '' || ufRG.value !== '') {
    if (ufRG.value === '') {
      input_ufRG.value = 'input--invalid';
      invalidInputs['ufRG'] = true;
      ufMsg.value = 'Não nulo.';
    } else if (rg.value === '') {
      input_rg.value = 'input--invalid';
      invalidInputs['rg'] = true;
      rgMsg.value = 'O RG não pode ser nulo.';
    } else {  // look if rg is duplicated based on UF
      const studentsRgUFs = await getRgUF(axios, ufRG.value);
      if (studentsRgUFs.includes(rg.value)) {
        input_rg.value = 'input--invalid';
        invalidInputs['rg'] = true;
        rgMsg.value = `O RG já foi cadastrado em ${ufRG.value}.`;
      }
    }
  }
  // telefone
  if (telefone.value !== '' && telefone.value.length < 11) {  // nullable + minlength 11
    input_telefone.value = 'input--invalid';
    invalidInputs['telefone'] = true;
    telefoneMsg.value = 'O telefone está incompleto.';
  }
  // email
  if (dsEmail.value === '') { // required
    input_dsEmail.value = 'input--invalid';
    invalidInputs['dsEmail'] = true;
    dsEmailMsg.value = 'Por favor digite o Email do aluno.';
  }
  // data nascimento
  if (dtNascimento.value !== '' && !dateValidator(dtNascimento.value)) {  // nullable + validate
    input_dtNascimento.value = 'input--invalid';
    invalidInputs['dtNascimento'] = true;
    dtNascimentoMsg.value = 'Data inválida.';
  }
  // sexo
  if (sexo.value === '') {  // required
    input_sexo.value = 'input--invalid';
    invalidInputs['sexo'] = true;
    sexoMsg.value = 'Por favor informe um sexo.';
  }
  // camisa
  if (tmCamisa.value === '') {  // required
    input_tmCamisa.value = 'input--invalid';
    invalidInputs['tmCamisa'] = true;
    tmCamisaMsg.value = 'Não nulo.';
  }
  // altura
  if (altura.value.length < 3) {  // required
    input_altura.value = 'input--invalid';
    invalidInputs['altura'] = true;
    alturaMsg.value = 'Por favor informe uma altura.';
  }
  // peso
  if (peso.value !== '' && peso.value.length < 2) {  // nullable + minlength 11
    input_peso.value = 'input--invalid';
    invalidInputs['peso'] = true;
    pesoMsg.value = 'O peso está incompleto.';
  }
};

// Watches

watch(rg, (newValue) => {  // validate rg input
  // validators rg-uf
  if ((ufRG.value !== '' && input_rg.value === 'input--valid') && rg.value === '') {
    input_rg.value = 'input--invalid';
    invalidInputs['rg'] = true;
    rgMsg.value = 'O RG não pode ser nulo.';
  }
  if (input_rg.value === 'input--invalid' && rg.value !== '') {
    input_rg.value = 'input--valid';
    delete invalidInputs.rg;
  }
  if (input_rg.value === 'input--null' && input_ufRG.value === 'input--invalid') {
    input_ufRG.value = 'input--null';
    delete invalidInputs.ufRG;
  }
  if (input_ufRG.value === 'input--null' && (rg.value === '' && input_rg.value === 'input--valid')) {
    input_rg.value = 'input--null';
  }
  // only numbers and maxlength 20
  const cleanedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleanedValue.substring(0, 20);
  rg.value = restrictedValue;
});

watch(ufRG, (oldValue, newValue) => {  // validate ufRG input
  // validators uf-rg
  if (ufRG.value !== '' && input_ufRG.value === 'input--invalid') {
    input_ufRG.value = 'input--valid';
    delete invalidInputs.ufRG;
  }
  if (ufRG.value === '' && input_rg.value === 'input--invalid') {
    input_rg.value = 'input--null';
    delete invalidInputs.rg;
  }
  if ((ufRG.value === '' && input_ufRG.value === 'input--valid') && (input_rg.value === 'input--valid' || input_rg.value === 'input--null')) {
    input_ufRG.value = 'input--null';
  }
  if (newValue !== oldValue && input_rg.value === 'input--invalid') {
    input_rg.value = 'input--valid';
    delete invalidInputs.rg;
  }
});

watch(telefone, (newValue) => {  // validate telefone input
  if (telefone.value.length === 14 && input_telefone.value === 'input--invalid') {
    input_telefone.value = 'input--valid';
    delete invalidInputs.telefone;
  } else if (input_telefone.value === 'input--valid' && telefone.value !== '') {
    input_telefone.value = 'input--invalid';
    invalidInputs['telefone'] = true;
  } else if (input_telefone.value === 'input--invalid' && newValue === '') {
    input_telefone.value = 'input--null';
    delete invalidInputs.telefone;
  }
  // only numbers + format ()-
  const cleannedValue = newValue.replace(/\D/g, '');
  const formattedValue = formatTelefone(cleannedValue);
  telefone.value = formattedValue;
});

watch(dsEmail, () => {  // validate dsEmail input
  const emailRegex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
  if (submitted.value) {
    if (!emailRegex.test(dsEmail.value) && dsEmail.value !== '') {
      invalidInputs['dsEmail'] = true;
      input_dsEmail.value = 'input--invalid';
      dsEmailMsg.value = 'Email digitado incorretamente.'
    } else {
      delete invalidInputs.dsEmail;
      input_dsEmail.value = 'input--valid';
    }
  }
});

watch(dtNascimento, () => {  // validate date of birth
  if (input_dtNascimento.value === 'input--invalid' && dateValidator(dtNascimento.value)) {
    input_dtNascimento.value = 'input--valid';
    delete invalidInputs.dtNascimento;
  } else if (input_dtNascimento.value === 'input--invalid' && dtNascimento.value === '') {
    input_dtNascimento.value = 'input--null';
    delete invalidInputs.dtNascimento;
  } else if (input_dtNascimento.value === 'input--valid' && dtNascimento.value === '') {
    input_dtNascimento.value = 'input--null';
  }
});

watch(sexo, () => {  // validate sexo input
  if (input_sexo.value === 'input--invalid') {
    input_sexo.value = 'input--valid';
    delete invalidInputs.sexo;
  }
});

watch(tmCamisa, () => {  // validate tmCamisa input
  if (input_tmCamisa.value === 'input--invalid') {
    input_tmCamisa.value = 'input--valid';
    delete invalidInputs.tmCamisa;
  }
});

watch(altura, (newValue) => {  // validate altura input
  if (input_altura.value === 'input--invalid' && altura.value.length === 3) {
    input_altura.value = 'input--valid';
    delete invalidInputs.altura;
  } else if (input_altura.value === 'input--valid' && altura.value.length < 3) {
    input_altura.value = 'input--invalid';
    invalidInputs['altura'] = true;
  }
  // only numbers and maxlength 3 + format altura
  const cleannedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleannedValue.substring(0, 3);
  const formattedValue = formatAltura(restrictedValue);
  altura.value = formattedValue;
});

watch(peso, (newValue) => {  // validate peso input
  if (input_peso.value === 'input--invalid' && peso.value.length > 1) {
    input_peso.value = 'input--valid';
    delete invalidInputs.peso;
  } else if (input_peso.value === 'input--valid' && peso.value.length === 1) {
    input_peso.value = 'input--invalid';
    invalidInputs['peso'] = true;
  }
  if (peso.value === '') {
    if (input_peso.value === 'input--invalid') {
      delete invalidInputs.peso;
    }
    input_peso.value = 'input--null';
  }
  // transform peso in 0-3 int numbers and 0-2 decimals
  const cleanedValue = newValue.replace(/[^0-9.]/g, '');
  const parts = cleanedValue.split('.');

  parts[0] = parts[0].substring(0, 3);

  if (parts.length > 1) {
    parts[1] = parts[1].substring(0, 2);
    peso.value = `${parts.join('.')}kg`;  // add kg at the end when it has decimals
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
// function validate

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside>
    <Form @submit="onSubmit" v-slot="{ meta }" class="form" v-motion-slide-visible-top>
      <div class="form__bg"></div>

      <div class="form__container">

        <div class="form__container__title">
          <h1 class="form__container__title__text">Cadastrar Novo Aluno</h1>
          <button type="button" @click="closeCreate" class="form__container__title__button">
            <font-awesome-icon icon="fa-solid fa-xmark" size="2xl" />
          </button>
        </div>

        <div class="form__container__fotoAluno">
          <img src="../assets/images/default-profile-picture2.jpg" alt="default profile picture"
            class="form__container__fotoAluno__image">
          <p class="form__container__fotoAluno__text">Foto do Aluno</p>
        </div>

        <!-- Início do cadastro -->
        <RegisterField v-model="form.nmPessoa" :meta="meta" rules="required" name="nome" type="text" label="Nome completo"
          required="*" placeholder="Digite o nome do aluno" />

        <div class="form__container__cpf-rg-uf">
          <RegisterField v-model="form.cpfCnpj" :meta="meta" rules="required" name="cpf" type="text" label="CPF"
            required="*" placeholder="Digite o CPF do aluno" />
          <div class="form__container__cpf-rg-uf__rg-uf">
            <RegisterField v-model="form.rg" :meta="meta" name="rg" type="text" label="RG"
              placeholder="Digite o RG do aluno" />

            <RegisterField v-model="form.ufRG" :meta="meta" name="uf" type="select" label="UF" :options="ufList" />
          </div>
        </div>

        <div class="form__container__tel-email">
          <RegisterField v-model="form.telefone" :meta="meta" name="telefone" type="text" label="Telefone"
            placeholder="(00)00000-0000" />

          <RegisterField v-model="form.dsEmail" :meta="meta" rules="required|email" name="email" type="text"
            label="E-mail" required="*" placeholder="Digite o Email do aluno" />
        </div>

        <div class="form__container__data-sexo-camisa">
          <div class="form__container__data-sexo-camisa__dtNascimento">
            <label for="date">Data Nascimento</label>
            <input v-model="form.dtNascimento" type="date" id="date">
          </div>

          <RegisterField v-model="form.sexo" :meta="meta" rules="required" name="sexo" type="select"
            label="Sexo Biológico" required="*" :options="sexoList" />

          <RegisterField v-model="form.tmCamisa" :meta="meta" rules="required" name="camisa" type="select" label="Camisa"
            required="*" :options="tmCamisaList" />
        </div>

        <div class="form__container__altura-peso">
          <RegisterField v-model="form.altura" :meta="meta" rules="required" name="altura" type="number"
            label="Altura(cm)" required="*" placeholder="180cm" />

          <RegisterField v-model="form.peso" :meta="meta" name="peso" type="number" label="Peso(kg)"
            placeholder="90.30kg" />
        </div>

        <div class="form__container__freqCardio">
          <RegisterField v-model="form.bpmMaximo" :meta="meta" name="bpmMaximo" type="number" label="Freq. C. Máxima"
            placeholder="BPM" />

          <RegisterField v-model="form.bpmRepouso" :meta="meta" name="bpmRepouso" type="number" label="Freq. C. Repouso"
            placeholder="BPM" />
        </div>

        <RegisterField v-model="form.dsObs" :meta="meta" name="obs" type="textarea" label="Observação"
          placeholder="Digite aqui se tiver alguma observação" />

        <!-- SUBMIT -->
        <div class="form__container__submit">
          <div class="submit" :class="{ 'submit--disabled': !meta.valid }">
            <button type="submit" class="submit__btn">Cadastrar Aluno</button>
          </div>
          <button type="button" class="cancel" @click="closeCreate">Cancelar</button>
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

  .form {
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

    &__container {
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
        width: 600px;
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

      &__cpf-rg-uf {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;

        @include mq(s) {
          display: flex;
          flex-direction: column;
        }

        &__rg-uf {
          display: grid;
          grid-template-columns: 1fr 80px;
          gap: 20px;

          @include mq(xs-s) {
            display: flex;
            flex-direction: column;
          }
        }
      }

      &__tel-email {
        display: flex;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        .register-field {
          flex: 1;
        }
      }

      &__data-sexo-camisa {
        display: flex;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        .register-field {
          flex: 1;
        }

        &__dtNascimento {
          @include inputContainers();
        }
      }

      &__altura-peso {
        display: flex;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        .register-field {
          flex: 1;
        }
      }

      &__freqCardio {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }
      }

      &__submit {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 20px;

        .submit {
          &__btn {
            @include submitButtons($validation, white);
          }

          &--disabled {
            opacity: 0.5;
            cursor: not-allowed;

            .submit__btn {
              pointer-events: none;
            }
          }
        }

        .cancel {
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
</style>