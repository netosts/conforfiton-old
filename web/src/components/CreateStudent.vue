<script setup>
import http from '../services/api/http';
import { countCpfDuplicate, countRgUfDuplicate, countEmailDuplicate } from '../services/api/get';
import { postStudent } from '../services/api/post';

import { ref, reactive, onMounted } from 'vue';

import TextField from './TextField.vue';
import { Form } from 'vee-validate';


// VARIABLES
const bodyElement = ref(null);

// Form Variables
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

// Emits
const emit = defineEmits(['isCreateStudentActive']);

// Lists
const ufList = [
  '', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
  'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
];
const sexoList = [
  'Masculino', 'Feminino'
];
const tmCamisaList = [
  'PP', 'P', 'M', 'G', 'GG', 'XG'
];

// Form-level Validation Schema
const schema = {
  name: 'required|maxLength:60',
  cpf: 'required|cpf|maxLength:11',
  rg: 'maxLength:20',
  telefone: 'minLength:11|maxLength:11',
  email: 'required|email|maxLength:80',
  sexo: 'required',
  altura: 'required|between:0,250|maxDecimal:1',
  peso: 'between:0,600|maxDecimal:2',
  bpmMaximo: 'between:0,220',
  bpmRepouso: 'between:0,220',
  dsObs: 'maxLength:300'
};

// FUNCTIONS
// Close the create tab
function closeCreate() {
  location.reload();
};

// Create a new student
async function onSubmit(values, { setFieldError, setErrors }) {
  console.log('CRIANDO ALUNO...');

  let errors = 0;  // track errors

  // CPF Duplicate validation
  form.cpfCnpj = form.cpfCnpj.replace(/\D/g, '');  // only digits
  const countedCpf = await countCpfDuplicate(http, form.cpfCnpj);
  if (countedCpf > 0) {
    setFieldError('cpf', 'O CPF já foi cadastrado.');
    errors++;
  }

  // RG and UF must be together
  if ((form.rg !== '' && form.ufRG === '') || (form.ufRG !== '' && form.rg === '')) {
    setErrors({
      rg: 'O RG e UF precisam ser cadastrados juntos.',
      uf: ' ',
    });
    errors++;
  } else if (form.rg !== '' && form.ufRG !== '') {
    // RG in UF Duplicate validation
    const countedRgUf = await countRgUfDuplicate(http, form.rg, form.ufRG);
    if (countedRgUf > 0) {
      setFieldError('rg', `O RG já foi cadastrado em ${form.ufRG}.`);
      errors++;
    }
  }

  // Email duplicate validation
  const countedEmail = await countEmailDuplicate(http, form.dsEmail);
  if (countedEmail > 0) {
    setFieldError('email', 'Este email já foi cadastrado.')
    errors++;
  }

  // BPM Maximo and Repouso must be together
  if ((form.bpmMaximo !== '' && form.bpmRepouso === '') || (form.bpmMaximo === '' && form.bpmRepouso !== '')) {
    setErrors({
      bpmMaximo: 'As frequências cardíacas precisam ser cadastradas juntas.',
      bpmRepouso: 'As frequências cardíacas precisam ser cadastradas juntas.'
    });
    errors++;
  }

  if (errors > 0) {  // only proceed without errors
    return;
  }

  // Get the current date and time and use as dtData
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  // Format problematic values before posting
  form.dtData = formattedDate;
  form.rg = form.rg.replace(/\D/g, '');  // only digits
  form.telefone = form.telefone.replace(/\D/g, '');  // only digits

  // Post new student
  postStudent(http, form);
};

// DOM Mounted
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeCreate">
    <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ meta }" class="form" v-motion-slide-visible-top>
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
        <TextField v-model="form.nmPessoa" :meta="meta" name="name" type="text" label="Nome completo" required="*"
          placeholder="Digite o nome do aluno" />

        <div class="form__container__cpf-rg-uf">
          <TextField v-model="form.cpfCnpj" :meta="meta" name="cpf" type="text" label="CPF" required="*"
            placeholder="Digite o CPF do aluno" />

          <div class="form__container__cpf-rg-uf__rg-uf">
            <TextField v-model="form.rg" :meta="meta" name="rg" type="text" label="RG"
              placeholder="Digite o RG do aluno" />

            <TextField v-model="form.ufRG" :meta="meta" name="uf" type="select" label="UF" :options="ufList" />
          </div>
        </div>

        <div class="form__container__tel-email">
          <TextField v-model="form.telefone" :meta="meta" name="telefone" type="text" label="Telefone"
            placeholder="(00)00000-0000" />

          <TextField v-model="form.dsEmail" :meta="meta" name="email" type="text" label="E-mail" required="*"
            placeholder="Digite o Email do aluno" />
        </div>

        <div class="form__container__data-sexo-camisa">
          <div class="form__container__data-sexo-camisa__dtNascimento">
            <label for="date">Data Nascimento</label>
            <input v-model="form.dtNascimento" type="date" id="date">
          </div>

          <TextField v-model="form.sexo" :meta="meta" name="sexo" type="select" label="Sexo Biológico" required="*"
            :options="sexoList" />

          <TextField v-model="form.tmCamisa" :meta="meta" name="camisa" type="select" label="Camisa"
            :options="tmCamisaList" />
        </div>

        <div class="form__container__altura-peso">
          <TextField v-model="form.altura" :meta="meta" name="altura" type="number" label="Altura(cm)" required="*"
            placeholder="Ex: 180" />

          <TextField v-model="form.peso" :meta="meta" name="peso" type="number" label="Peso(kg)"
            placeholder="Ex: 90,30" />
        </div>

        <div class="form__container__freqCardio">
          <TextField v-model="form.bpmMaximo" :meta="meta" name="bpmMaximo" type="number" label="Freq. C. Máxima"
            placeholder="BPM" />

          <TextField v-model="form.bpmRepouso" :meta="meta" name="bpmRepouso" type="number" label="Freq. C. Repouso"
            placeholder="BPM" />
        </div>

        <TextField v-model="form.dsObs" :meta="meta" name="dsObs" type="textarea" label="Observação"
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