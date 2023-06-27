<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <aside>
    <div class="logo">
      <RouterLink to="/">
        <div class="logo__image">
          <img src="../assets/images/temp-logo.png" alt="logo temporaria">
        </div>
        <div class="logo__title">
          <h1>Confor<span>Fit</span></h1>
        </div>
        <div class="logo__subtitle">
          Soluções Esportivas
        </div>
      </RouterLink>

    </div>
    <div class="menu">
      <h2>Menu</h2>
      <p>Calendar</p>
      <p>Chat</p>
      <p>Email</p>
      <p>Ecommerce</p>
    </div>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

aside {
  position: absolute;
  top: 0;
  left: 0;
  background-color: $sidebar;
  width: 227px;
  height: 100%;

  .logo {
    display: flex;
    flex-direction: column;
    margin: 20px;
    text-align: center;

    a {
      text-decoration: none;
    }

    &__image {
      margin-bottom: 5px;

      img {
        width: 40px;
      }
    }

    &__title {
      font-size: 1.2rem;
      color: white;
      text-transform: lowercase;

      span {
        color: $logo-color;
      }
    }

    &__subtitle {
      font-size: .5rem;
      color: $txt-subtitle;
      margin-top: -8px;
      text-transform: uppercase;
    }
  }

  .menu {
    padding: 20px;
    color: $txt-sidebar;

    h2 {
      font-size: .7rem;
      color: $menu-color;
      text-transform: uppercase;
    }

    p {
      font-size: .9rem;
      padding: 5px 10px;
    }
  }
}
</style>