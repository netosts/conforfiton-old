<script setup>
import { ref } from "vue";

const personal = ref(JSON.parse(localStorage.getItem("credentials")));
const userPopup = ref(false);
</script>

<template>
  <header>
    <div class="topbar">
      <div class="user" @click="userPopup = !userPopup">
        <div class="user__image"></div>
        <div class="user__info">
          <p class="user__info-name">{{ personal?.name }}</p>
          <p class="user__info-credential">{{ personal?.role }}</p>
        </div>
        <Transition name="slide-fade">
          <div class="user__tooltip" v-show="userPopup">
            <span>Bem vindo {{ personal?.name }}!</span>
            <RouterLink to="/profile"
              ><font-awesome-icon icon="fa-solid fa-user" /> Perfil</RouterLink
            >
            <RouterLink to="/profile"
              ><font-awesome-icon icon="fa-solid fa-user" /> Perfil</RouterLink
            >
            <RouterLink to="/profile"
              ><font-awesome-icon icon="fa-solid fa-user" /> Perfil</RouterLink
            >
            <RouterLink to="/profile"
              ><font-awesome-icon icon="fa-solid fa-user" /> Perfil</RouterLink
            >
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
        right: 77%;
        transform: translateX(50%);
        width: 170px;
        padding: 10px 0;
        border-radius: $border-radius;
        background-color: white;
        transition: 0.35s;

        span {
          font-weight: 600;
          font-size: 11px;
          color: $txt-subtitle;
          padding: 5px 20px;
        }

        a {
          padding: 5px 20px;
          text-decoration: none;
          color: $txt-title;
          font-size: 14px;
          transition: 0.2s;
          &:hover {
            background-color: $background;
          }
        }

        &::before {
          content: "";
          position: absolute;
          top: -8px;
          right: 50%;
          transform: translateX(50%) rotate(45deg);
          width: 15px;
          height: 15px;
          background-color: white;
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
