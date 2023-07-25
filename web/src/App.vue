<script setup>
import SideBar from './components/SideBar.vue';
import TopBar from './components/TopBar.vue';

import { useRoute } from 'vue-router';
import { ref, watch } from 'vue';


// VARIABLES
const route = useRoute();
const logging = ref(false);

// Get Emits
const sidebarIsActive = ref(null);
// Handle Emits
const handleSidebar = (emittedValue) => {
  return sidebarIsActive.value = emittedValue;
};

watch(route, () => {
  if (route.path === '/login') {
    logging.value = true;
  }
})
</script>

<template>
  <SideBar v-show="!logging" @sidebarIsActive="handleSidebar" />
  <TopBar v-show="!logging" :class="sidebarIsActive ? 'header__sidebar-active' : null" />
  <RouterView :class="{ 'main__sidebar-active': sidebarIsActive && !logging }" />
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

  margin: {
    top: 25px;
    right: calc(25px + 75px);
    bottom: calc(25px + 69px);
    left: 25px;
  }

  ;
  transition: .2s;

  @include mq(s) {
    left: 0;
    margin-right: 25px;
    transition: none;
  }
}

.main__sidebar-active {
  left: 250px;
  margin-right: calc(25px + 250px);

  @include mq(s) {
    left: 0;
    margin-right: 25px;
  }
}
</style>