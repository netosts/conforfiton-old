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
  emit('isCreateStudentActive', false);
  bodyElement.value.style.overflow = 'auto';
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
    <form @submit.prevent="createStudent" class="create__form">
      <button type="button" @click="closeCreate">CLOSE</button>

      <div class="create__form__title">
        <h1>Cadastrar Novo Aluno</h1>
      </div>

      <div class="create__form__fotoAluno">
        <img src="#" alt="#">
        <p>Adicionar Foto</p>
      </div>

      <!-- Início do cadastro -->
      <div class="create__form__nmPessoa">
        <label for="nmPessoa">Nome completo</label>
        <input v-model="nmPessoa" type="text" id="nmPessoa" maxlength="60" placeholder="Digite o nome do aluno" required>
      </div>

      <div class="create__form__cpfCnpj">
        <label for="cpfCnpj">CPF</label>
        <input v-model="cpfCnpj" type="text" id="cpfCnpj" placeholder="Digite o CPF do aluno" required>
      </div>

      <div class="create__form__rg">
        <label for="rg">RG</label>
        <input v-model="rg" type="text" id="rg" placeholder="Digite o RG do aluno">
      </div>

      <div class="create__form__ufRG">
        <label for="ufRG">UF</label>
        <input v-model="ufRG" type="text" id="ufRG" placeholder="SE">
      </div>

      <div class="create__form__dtNascimento">
        <label for="dtNascimento">Data Nascimento</label>
        <input v-model="dtNascimento" type="date" id="dtNascimento">
      </div>

      <div class="create__form__dsObs">
        <label for="dsObs">Observação</label>
        <textarea v-model="dsObs" id="dsObs" cols="30" rows="10"></textarea>
      </div>

      <div class="create__form__dsEmail">
        <label for="dsEmail">E-mail</label>
        <input v-model="dsEmail" type="email" id="dsEmail" maxlength="80" placeholder="Digite o Email do aluno">
      </div>

      <div class="create__form__telefone">
        <label for="telefone">Telefone</label>
        <input v-model="telefone" type="tel" id="telefone" minlength="11" maxlength="11" placeholder="(79)99999-9999">
      </div>

      <div class="create__form__altura">
        <label for="altura">Altura (cm)</label>
        <input v-model="altura" type="text" id="altura" minlength="3" placeholder="180cm" required>
      </div>

      <div class="create__form__sexo">
        <label for="masculino">Masculino</label>
        <input v-model="sexo" type="radio" id="masculino" name="sexo" value="Masculino" required>

        <label for="feminino">Feminino</label>
        <input v-model="sexo" type="radio" id="feminino" name="sexo" value="Feminino" required>
      </div>

      <div class="create__form__peso">
        <label for="peso">Peso (kg)</label>
        <input v-model="peso" type="text" id="peso" placeholder="90.30kg">
      </div>

      <!-- SUBMIT -->
      <div class="create__form__submit">
        <input type="submit" value="Cadastrar Aluno">
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
  padding: 50px;
  background-color: rgba(79, 79, 79, 0.442);

  &__form {
    position: relative;
    z-index: 999;
    margin: auto;
    border-radius: $border-radius;
    background-color: white;

    button {
      position: absolute;
      top: 0;
      right: -60px;
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