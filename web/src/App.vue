<script setup>
import SideBar from './components/SideBar.vue';
import TopBar from './components/TopBar.vue';
import { RouterView } from 'vue-router';
import { ref } from 'vue';


// get sidebar element with emit
const sidebarIsActive = ref(null);
const handleSidebarIsActive = (emittedValue) => {
  return sidebarIsActive.value = emittedValue;
};
</script>

<template>
  <SideBar @sidebarIsActive="handleSidebarIsActive" />
  <TopBar :class="sidebarIsActive ? 'header__sidebar-active' : null" />
  <RouterView :class="sidebarIsActive ? 'main__sidebar-active' : null" />
</template>

<style lang="scss" scoped>
@import './assets/styles/variables';
@import './assets/styles/mixins';

header {
  position: fixed;
  top: 0;
  right: 0;
  left: 75px;
  z-index: 1;
  transition: .2s;

  @include mq(l-xl) {
    left: 75px;
  }

  @include mq(s) {
    left: 0;
    transition: none;
  }
}

.header__sidebar-active {
  left: 250px;
}

main {
  position: relative;
  top: 69px;
  left: 75px;
  transition: .2s;

  @include mq(s) {
    left: 0;
    transition: none;
  }
}

.main__sidebar-active {
  left: 250px;

  @include mq(s) {
    left: 0;
  }
}
</style>