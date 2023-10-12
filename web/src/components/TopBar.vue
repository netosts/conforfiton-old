<script setup>
import { ref } from "vue";
import { onClickOutside } from "@vueuse/core";

const personal = ref(JSON.parse(localStorage.getItem("credentials")));
const userPopup = ref(false);
const tooltip = ref();

function logout() {
  localStorage.removeItem("user");
  localStorage.removeItem("u:u");
  location.reload();
}

function closePopup() {
  userPopup.value = false;
}

onClickOutside(tooltip, closePopup);
</script>

<template>
  <header>
    <div class="topbar">
      <div ref="tooltip" class="user" @click="userPopup = !userPopup">
        <div class="user__image"></div>
        <div class="user__info">
          <p class="user__info-name">{{ personal?.name }}</p>
          <p class="user__info-credential">{{ personal?.role }}</p>
        </div>
        <Transition name="slide-fade">
          <div class="user__tooltip" v-show="userPopup">
            <span>Bem vindo {{ personal?.name }}!</span>
            <button @click="logout">
              <font-awesome-icon icon="fa-solid fa-arrow-right-to-bracket" />
              Sair
            </button>
          </div>
        </Transition>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

header {
  display: flex;
  justify-content: flex-end;
  height: 69px;
  background-color: white;
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.103);

  .topbar {
    display: flex;
    align-items: center;
    gap: 20px;

    .user {
      display: flex;
      align-items: center;
      position: absolute;
      top: 0;
      right: 20px;
      gap: 10px;
      padding: 15px 10px;
      background-color: $background;
      cursor: pointer;

      &__image {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        background-color: gray;
      }

      &__info-name {
        color: $txt-title;
      }

      &__info-credential {
        font-size: 0.6rem;
        color: $txt-subtitle;
      }

      &__tooltip {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 70px;
        right: 82%;
        transform: translateX(50%);
        width: 200px;
        padding: 10px 0;
        border-radius: $border-radius;
        background-color: white;
        cursor: default;
        transition: 0.35s;

        span {
          font-weight: 600;
          font-size: 11px;
          color: $txt-subtitle;
          padding: 5px 20px;
        }

        a {
          display: flex;
          align-items: center;
          gap: 15px;
          padding: 8px 24px;
          text-decoration: none;
          color: $txt-title;
          font-size: 16px;
          transition: 0.2s;
          &:hover {
            background-color: $background;
          }
        }

        button {
          display: flex;
          align-items: center;
          gap: 15px;
          padding: 8px 24px;
          border: none;
          background-color: transparent;
          text-align: start;
          color: $txt-title;
          font-size: 16px;
          cursor: pointer;
          transition: 0.2s;
          &:hover {
            background-color: $background;
          }
        }
      }
    }
  }
}
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(20px);
  opacity: 0;
}
</style>
