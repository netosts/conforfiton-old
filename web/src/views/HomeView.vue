<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const msg = ref('');
const userId = ref(1);

function getMessage() {
  axios.get(`/user/${userId.value}`).then((res) => {
    msg.value = res.data;
  }).catch((err) => {
    console.error(err);
  })
};

onMounted(getMessage);
</script>

<template>
  <main>
    <div class="searchbox">
      <div class="searchbox__title">
        <h3>Procurar Alunos</h3>
        <button class="create-button">+ Criar Cadastro</button>
      </div>
      <div class="searchbox__input">
        <input type="text" name="searchDb" id="searchDb" placeholder="Procurar alunos no banco de dados...">
        <select id="searchFilter">
          <option value="#" selected>Novos</option>
          <option value="#">Nome</option>
          <option value="#">CPF</option>
        </select>
      </div>
    </div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
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
    width: 100%;
    padding: 16px;
    border-radius: $border-radius;
    background: white;
    box-shadow: 0px 2px 2px rgba(0 0 0 / 0.1);

    &__title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 30px;

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
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 25px;

      input {
        padding: 8px 15px 8px 40px;
        @include inputBar();

        &::placeholder {
          color: $txt-subtitle;
        }
      }

      select {
        padding-left: 10px;
        @include inputBar();
        cursor: pointer;
      }
    }
  }

  .box {
    width: 100%;
    height: 200px;
    border-radius: $border-radius;
    background: white;
    box-shadow: 0px 2px 4px rgba(0 0 0 / 0.1);
  }
}
</style>