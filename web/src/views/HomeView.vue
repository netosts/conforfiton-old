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
        <div class="searchbox__input__db">
          <font-awesome-icon class="searchbox__input__db__icon" icon="fa-solid fa-magnifying-glass" size="sm" />
          <input type="text" name="searchDb" id="searchDb" placeholder="Procurar alunos no banco de dados...">
        </div>
        <select>
          <option value="#" selected>Novos</option>
          <option value="#">Nome</option>
          <option value="#">CPF</option>
        </select>
      </div>
    </div>

    <div class="box" v-motion-slide-right></div>
    <div class="box" v-motion-slide-right></div>
    <div class="box" v-motion-slide-right></div>
    <div class="box" v-motion-slide-visible-once-right></div>
    <div class="box" v-motion-slide-visible-once-right></div>
    <div class="box" v-motion-slide-visible-once-right></div>
    <div class="box" v-motion-slide-visible-once-right></div>
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
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.103);

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

  .box {
    width: 100%;
    height: 200px;
    border-radius: $border-radius;
    background: white;
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.103);
  }
}
</style>