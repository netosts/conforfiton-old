<script setup>

</script>

<template>
  <header>
    <div class="topbar">
      <div class="tools">
        <div class="full-screen">
          <font-awesome-icon icon="fa-solid fa-expand" size="xl" />
        </div>
        <div class="dark-mode">
          <font-awesome-icon icon="fa-regular fa-moon" size="xl" />
        </div>
      </div>
      <div class="user">
        <div class="user__image">
        </div>
        <div class="user__info">
          <p class="user__info-name">Thiago</p>
          <p class="user__info-credential">Admin</p>
        </div>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

header {
  display: flex;
  justify-content: flex-end;
  padding: 0 20px;
  background-color: white;

  .topbar {
    display: flex;
    align-items: center;
    gap: 20px;

    .tools {
      display: flex;
      gap: 5px;

      .full-screen {
        @include tool();
      }

      .dark-mode {
        @include tool();
      }

      .fa-expand,
      .fa-moon {
        width: 18px
      }
    }

    .user {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 15px 10px;
      background-color: $background;

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
        font-size: .6rem;
        color: $txt-subtitle;
      }
    }
  }
}
</style>