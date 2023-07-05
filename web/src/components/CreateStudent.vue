<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';


// Variables
const bodyElement = ref(null);
// emits
const emit = defineEmits(['isCreateStudentActive'])

// Functions
// close the create tab
function closeCreate() {
  emit('isCreateStudentActive', false);
  bodyElement.value.style.overflow = 'auto';
}

// create a new student
// function createStudent() {
//   if (!studentsCpfCnpj.includes('1281739181')) {
//     console.log('CRIANDO ALUNO...');
//     axios.post('/student', {
//       "nmPessoa": "None man 2",
//       "ativo": "",
//       "ser": "f",
//       "tipoPessoa": "f",
//       "cpfCnpj": "1281739181",
//       "rg": "",
//       "ufRG": "SE",
//       "dsRazaoSocial": "",
//       "dsInscricaoEstadual": "",
//       "dsInscricaoMunicipal": "",
//       "isentoIE": "",
//       "dtNascimento": "2023-07-04",
//       "dsObs": "",
//       "dsEmail": "",
//       "telefone": ""
//     }).then((res) => {
//       alert(res.data);
//       console.log('...PESSOA CRIADA COM SUCESSO!')
//     }).catch((err) => {
//       console.error(err);
//     });
//   } else {
//     console.error('ERRO: Esse CPF já está em uso.');
//   }
// };

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
})
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
        <p>Foto do aluno</p>
      </div>

      <div class="create__form__nmPessoa">
        <label for="nmPessoa">Nome completo</label>
        <input type="text" id="nmPessoa" name="nmPessoa" maxlength="10" placeholder="Digite o nome do aluno" required>
      </div>

      <!-- <div class="create__form__ser">
        <label for="aluno">Aluno</label>
        <input type="radio" id="aluno" name="ser" value="A" required checked>

        <label for="funcionario">Funcionário</label>
        <input type="radio" id="funcionario" name="ser" value="F" required>

        <label for="fornecedor">Fornecedor</label>
        <input type="radio" id="fornecedor" name="ser" value="FO" required>
      </div> -->

      <!-- <div class="create__form__tipoPessoa">
        <label for="pf">Pessoa física</label>
        <input type="radio" id="pf" name="tipoPessoa" value="F" required checked>

        <label for="pj">Pessoa Jurídica</label>
        <input type="radio" id="pj" name="tipoPessoa" value="J" required>
      </div> -->

      <div class="create__form__cpfCnpj">
        <label for="cpfCnpj">CPF</label>
        <input type="text" id="cpfCnpj" name="cpfCnpj" minlength="11" maxlength="11" placeholder="Digite o CPF do aluno">
      </div>

      <div class="create__form__dsEmail">
        <label for="dsEmail">E-mail</label>
        <input type="text" id="dsEmail" name="dsEmail" maxlength="80" placeholder="Digite o Email do aluno">
      </div>

      <div class="create__form__telefone">
        <label for="telefone">Telefone</label>
        <input type="tel" id="telefone" name="telefone" minlength="11" maxlength="11" placeholder="(79)99999-9999">
      </div>

      <div class="create__form__altura">
        <label for="altura">Altura (cm)</label>
        <input type="number" id="altura" name="altura" minlength="3" placeholder="180cm">
      </div>

      <div class="create__form__sexo">
        <label for="masculino">Masculino</label>
        <input type="radio" id="masculino" name="sexo" value="Masculino" required checked>

        <label for="feminino">Feminino</label>
        <input type="radio" id="feminino" name="sexo" value="Feminino" required>
      </div>

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