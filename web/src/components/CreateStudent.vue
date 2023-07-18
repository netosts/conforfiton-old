<script setup>
import { formatTelefone, formatAltura, cpfValidator, dateValidator } from '../assets/js/formatFunctions';
import { getCpfCnpj, getRgUF } from '../assets/js/axiosGets';
import { postStudent } from '../assets/js/axiosPost';
import { ref, reactive, watch, onMounted } from 'vue';
import axios from 'axios';


const model = ref('')
const reset = () => {
  model.value = '';
}

// Variables
const bodyElement = ref(null);
const submitted = ref(false);
// form variables
const form = reactive({
  nmPessoa: '',
  cpfCnpj: '',
  rg: '',
  ufRG: '',
  telefone: '',
  dsEmail: '',
  dtNascimento: '',
  sexo: '',
  nCamisa: '',
  altura: '',
  peso: '',
  fcMaxima: '',
  fcRepouso: '',
  dsObs: '',
});
const nmPessoa = ref('');
const cpfCnpj = ref('');
const rg = ref('');
const ufRG = ref('');
const telefone = ref('');
const dsEmail = ref('');
const dtNascimento = ref('');
const sexo = ref('');
const nCamisa = ref('');
const altura = ref('');
const peso = ref('');
const fcMaxima = ref('');
const fcRepouso = ref('');
const dsObs = ref('');
// form classess
const invalidInputs = {};
const input = ref({
  nmPessoa: { classInput: 'input--null', msg: '' },
  cpfCnpj: { classInput: 'input--null', msg: '' },
  rg: { classInput: 'input--null', msg: '' },
  ufRG: { classInput: 'input--null', msg: '' },
  telefone: { classInput: 'input--null', msg: '' },
  dsEmail: { classInput: 'input--null', msg: '' },
  dtNascimento: { classInput: 'input--null', msg: '' },
  sexo: { classInput: 'input--null', msg: '' },
  nCamisa: { classInput: 'input--null', msg: '' },
  altura: { classInput: 'input--null', msg: '' },
  peso: { classInput: 'input--null', msg: '' },
  fcMaxima: { classInput: 'input--null', msg: '' },
  fcRepouso: { classInput: 'input--null', msg: '' },
  dsObs: { classInput: 'input--null', msg: '' },
});
const input_nmPessoa = ref('input--null');
const input_cpfCnpj = ref('input--null');
const input_rg = ref('input--null');
const input_ufRG = ref('input--null');
const input_telefone = ref('input--null');
const input_dsEmail = ref('input--null');
const input_dtNascimento = ref('input--null');
const input_sexo = ref('input--null');
const input_nCamisa = ref('input--null');
const input_altura = ref('input--null');
const input_peso = ref('input--null');
const input_fcMaxima = ref('input--null');
const input_fcRepouso = ref('input--null');
const input_dsObs = ref('input--null');
// validation msgs
const nmPessoaMsg = ref(null);
const cpfCnpjMsg = ref(null);
const rgMsg = ref(null);
const ufMsg = ref(null);
const telefoneMsg = ref(null);
const dsEmailMsg = ref(null);
const dtNascimentoMsg = ref(null);
const sexoMsg = ref(null);
const nCamisaMsg = ref(null);
const alturaMsg = ref(null);
const pesoMsg = ref(null);

// emits
const emit = defineEmits(['isCreateStudentActive']);

// Lists
// uf list
const ufList = [
  '', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
  'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
];
// nCamisa list
const nCamisaList = [
  'PP', 'P', 'M', 'G', 'GG', 'XG'
];

// Functions
// close the create tab
function closeCreate() {
  location.reload();
};

// create a new student
async function createStudent() {
  console.log(form);
  console.log(form.nmPessoa);
  submitted.value = true;
  console.log('CRIANDO ALUNO...');
  // validators
  // name
  if (form.nmPessoa === '') { // required
    input_nmPessoa.value = 'input--invalid';
    invalidInputs['nmPessoa'] = true;
    nmPessoaMsg.value = 'Por favor digite o nome do aluno.';
  }
  // cpf
  if (cpfCnpj.value === '' || cpfCnpj.value.length < 11) { // required + minlength 11
    input_cpfCnpj.value = 'input--invalid';
    invalidInputs['cpfCnpj'] = true;
    cpfCnpjMsg.value = 'Por favor digite o CPF do aluno.';
  } else if (!cpfValidator(cpfCnpj.value)) {  // real cpf validation
    input_cpfCnpj.value = 'input--invalid';
    invalidInputs['cpfCnpj'] = true;
    cpfCnpjMsg.value = 'O CPF digitado não é válido.';
  } else {  // look if cpf is duplicated
    const studentsCpfCnpj = await getCpfCnpj(axios);
    if (studentsCpfCnpj.includes(cpfCnpj.value)) {
      input_cpfCnpj.value = 'input--invalid';
      invalidInputs['cpfCnpj'] = true;
      cpfCnpjMsg.value = 'O CPF digitado já foi cadastrado.';
    }
  }
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
  if (nCamisa.value === '') {  // required
    input_nCamisa.value = 'input--invalid';
    invalidInputs['nCamisa'] = true;
    nCamisaMsg.value = 'Não nulo.';
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

  // verify if there is any input error, then continues if not
  if (Object.keys(invalidInputs).length > 0) {
    console.log('tem erro na tela');
    console.log(Object.keys(invalidInputs).length);
    return;  // AQUI ELE PARA
  }
  // PAROU NO RETURN ACIMA, SÓ CONTINUA SE N TIVER ERRO
  console.log('SE NÃO TEM ERRO ENTÃO EU GRITO!');
  // transform the values that can break the db
  let telefoneTransformed = null;
  let alturaTransformed = null;
  let pesoTransformed = null;

  if (telefone.value !== '') {
    const cleannedTelefone = telefone.value.replace(/\D/g, '');
    telefoneTransformed = cleannedTelefone; // telefone only digits
    form.telefone = telefoneTransformed;
  }

  const cleannedAltura = altura.value.replace(/\D/g, '');
  const alturaInteger = parseInt(cleannedAltura, 10);
  alturaTransformed = alturaInteger; // altura as INT

  if (peso.value !== '') {
    const cleannedPeso = peso.value.replace(/[^\d.]/g, '');
    const pesoFloat = parseFloat(cleannedPeso);
    pesoTransformed = pesoFloat; // peso as FLOAT
  }
  // get the current date and time
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  // axios post the form
  postStudent(axios, telefoneTransformed, alturaTransformed, pesoTransformed, formattedDate);
};

// Watches
watch(nmPessoa, (newValue) => {  // validate nmPessoa input
  if (input_nmPessoa.value === 'input--invalid') {
    input_nmPessoa.value = 'input--valid';
    delete invalidInputs.nmPessoa;
  } else if (input_nmPessoa.value === 'input--valid' && newValue === '') {
    input_nmPessoa.value = 'input--invalid';
    invalidInputs['nmPessoa'] = true;
  }
  // capitalize first letter of each word in the name
  const cleannedValue = newValue.replace(/\b\w/g, (match) => match.toUpperCase());
  nmPessoa.value = cleannedValue;
});

watch(cpfCnpj, (newValue) => {  // validate cpfCnpj input
  if (cpfCnpj.value.length === 11 && input_cpfCnpj.value === 'input--invalid') {  // validator
    input_cpfCnpj.value = 'input--valid';
    delete invalidInputs.cpfCnpj;
  } else if (input_cpfCnpj.value !== 'input--null' && cpfCnpj.value.length < 11) {
    input_cpfCnpj.value = 'input--invalid';
    invalidInputs['cpfCnpj'] = true;
    cpfCnpjMsg.value = 'O CPF precisa ter 11 números.';
  }
  // only numbers and maxlength 11
  const cleanedValue = newValue.replace(/[^0-9]/g, '');
  const restrictedValue = cleanedValue.substring(0, 11);
  cpfCnpj.value = restrictedValue;
});

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

watch(nCamisa, () => {  // validate nCamisa input
  if (input_nCamisa.value === 'input--invalid') {
    input_nCamisa.value = 'input--valid';
    delete invalidInputs.nCamisa;
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
          <img src="../assets/images/default-profile-picture2.jpg" alt="default profile picture"
            class="form__container__fotoAluno__image">
          <p class="form__container__fotoAluno__text">Foto do Aluno</p>
        </div>

        <!-- Início do cadastro -->
        <div class="form__container__nmPessoa">
          <label for="nmPessoa">Nome completo <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
          <!-- <input v-model="form.nmPessoa" :class="input_nmPessoa" type="text" id="nmPessoa" maxlength="60"
            placeholder="Digite o nome do aluno">
          <span v-show="input_nmPessoa === 'input--invalid'" class="invalid--msg">{{ nmPessoaMsg }}</span> -->
        </div>


        <div class="form__container__cpf-rg-uf">
          <div class="form__container__cpf-rg-uf__cpfCnpj">
            <label for="cpfCnpj">CPF <abbr title="VALOR NECESSÁRIO | Apenas números" class="required">*</abbr> </label>
            <input v-model.number="form.cpfCnpj" :class="input_cpfCnpj" type="text" id="cpfCnpj"
              placeholder="Digite o CPF do aluno">
            <span v-show="input_cpfCnpj === 'input--invalid'" class="invalid--msg">{{ cpfCnpjMsg }}</span>
          </div>
          <div class="form__container__cpf-rg-uf__rg-uf">
            <div class="form__container__cpf-rg-uf__rg-uf__rg">
              <label for="rg">RG</label>
              <input v-model="form.rg" :class="input_rg" type="text" id="rg" placeholder="Digite o RG do aluno">
              <span v-show="input_rg === 'input--invalid'" class="invalid--msg">{{ rgMsg }}</span>
            </div>

            <div class="form__container__cpf-rg-uf__rg-uf__ufRG">
              <label for="ufRG">UF</label>
              <select v-model="form.ufRG" :class="input_ufRG" id="ufRG">
                <option v-for="uf in ufList" :value="uf">{{ uf }}</option>
              </select>
              <span v-show="input_ufRG === 'input--invalid'" class="invalid--msg">{{ ufMsg }}</span>
            </div>
          </div>
        </div>

        <div class="form__container__tel-email">
          <div class="form__container__tel-email__telefone">
            <label for="telefone">Telefone</label>
            <input v-model="form.telefone" :class="input_telefone" type="tel" id="telefone" maxlength="11"
              placeholder="(79)99999-9999">
            <span v-show="input_telefone === 'input--invalid'" class="invalid--msg">{{ telefoneMsg }}</span>
          </div>

          <div class="form__container__tel-email__dsEmail">
            <label for="dsEmail">E-mail <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
            <input v-model="form.dsEmail" :class="input_dsEmail" type="text" id="dsEmail" maxlength="80"
              placeholder="Digite o Email do aluno">
            <span v-show="input_dsEmail === 'input--invalid'" class="invalid--msg">{{ dsEmailMsg }}</span>
          </div>
        </div>

        <div class="form__container__data-sexo-camisa">
          <div class="form__container__data-sexo-camisa__dtNascimento">
            <label for="dtNascimento">Data Nascimento</label>
            <input v-model="form.dtNascimento" :class="input_dtNascimento" type="date" id="dtNascimento">
            <span v-show="input_dtNascimento === 'input--invalid'" class="invalid--msg">{{ dtNascimentoMsg }}</span>
          </div>

          <div class="form__container__data-sexo-camisa__sexo">
            <label for="sexo">Sexo Biológico <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
            <select v-model="form.sexo" :class="input_sexo" id="sexo">
              <option value="Masculino">Masculino</option>
              <option value="Feminino">Feminino</option>
            </select>
            <span v-show="input_sexo === 'input--invalid'" class="invalid--msg">{{ sexoMsg }}</span>
          </div>

          <div class="form__container__data-sexo-camisa__nCamisa">
            <label for="nCamisa">Nº Camisa <abbr title="VALOR NECESSÁRIO" class="required">*</abbr> </label>
            <select v-model="form.nCamisa" :class="input_nCamisa" id="nCamisa">
              <option v-for="nCamisa in nCamisaList" :value="nCamisa">{{ nCamisa }}</option>
            </select>
            <span v-show="input_nCamisa === 'input--invalid'" class="invalid--msg">{{ nCamisaMsg }}</span>
          </div>
        </div>

        <div class="form__container__altura-peso">
          <div class="form__container__altura-peso__altura">
            <label for="altura">Altura(cm) <abbr
                title="VALOR NECESSÁRIO | Digite pelo menos 3 números. A altura será representada em centímetros"
                class="required">*</abbr> </label>
            <input v-model="form.altura" :class="input_altura" type="text" id="altura" placeholder="180cm">
            <p v-show="input_altura === 'input--invalid'" class="invalid--msg">{{ alturaMsg }}</p>
          </div>

          <div class="form__container__altura-peso__peso">
            <label for="peso">Peso(kg)</label>
            <input v-model="form.peso" :class="input_peso" type="text" id="peso" placeholder="90.30kg">
            <p v-show="input_peso === 'input--invalid'" class="invalid--msg">{{ pesoMsg }}</p>
          </div>
        </div>

        <div class="form__container__freqCardio">
          <div class="form__container__freqCardio__maxima">
            <label for="fcMaxima">Freq. C. Máxima</label>
            <input v-model="form.fcMaxima" :class="input_fcMaxima" type="text" id="fcRepouso"
              placeholder="Frequência Cardíaca">
          </div>

          <div class="form__container__freqCardio__repouso">
            <label for="fcRepouso">Freq. C. Repouso</label>
            <input v-model="form.fcRepouso" :class="input_fcRepouso" type="text" id="fcRepouso"
              placeholder="Frequência Cardíaca">
          </div>
        </div>

        <div class="form__container__dsObs">
          <label for="dsObs">Observação</label>
          <textarea v-model="form.dsObs" :class="input_dsObs" id="dsObs"
            placeholder="Digite aqui se tiver alguma observação"></textarea>
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

      &__nmPessoa {
        @include inputContainers();
      }

      &__cpf-rg-uf {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;

        @include mq(s) {
          display: flex;
          flex-direction: column;
        }

        &__cpfCnpj {
          @include inputContainers();
        }

        &__rg-uf {
          display: grid;
          grid-template-columns: 1fr 80px;
          gap: 20px;

          @include mq(xs-s) {
            display: flex;
            flex-direction: column;
          }

          &__rg {
            @include inputContainers();
          }

          &__ufRG {
            @include inputContainers();
          }
        }
      }

      &__tel-email {
        display: grid;
        grid-template-columns: 200px 400px;
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
        }

        &__dsEmail {
          @include inputContainers();
        }
      }

      &__data-sexo-camisa {
        display: grid;
        grid-template-columns: 150px 200px 80px;
        gap: 20px;

        @include mq(s) {
          grid-template-columns: 150px 150px 80px;
        }

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        &__dtNascimento {
          @include inputContainers();
        }

        &__sexo {
          @include inputContainers();
        }

        &__nCamisa {
          @include inputContainers();
        }
      }

      &__altura-peso {
        display: grid;
        grid-template-columns: 200px 200px;
        gap: 20px;

        @include mq(xs-s) {
          display: flex;
          flex-direction: column;
        }

        &__altura {
          @include inputContainers();
        }

        &__peso {
          @include inputContainers();
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

        &__maxima {
          @include inputContainers();
        }

        &__repouso {
          @include inputContainers();
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
        flex-wrap: wrap;
        gap: 20px;

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

.input--valid {
  border: 1px solid green;
}

.input--invalid {
  border: 1px solid #F06548;
}

.input--null {
  border: 1px solid $input-border;

  &:focus {
    border: 1px solid #7a85ac;
  }
}

.invalid--msg {
  color: #F06548;
  font-size: .75rem;
}
</style>