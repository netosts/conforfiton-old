<script setup>
import SideBar from './components/SideBar.vue';
import TopBar from './components/TopBar.vue';
import { RouterView } from 'vue-router';
import { ref, watch } from 'vue';


// get sidebar element with emit
const sidebarIsActive = ref(null);
const handleSidebarIsActive = (emittedValue) => {
  return sidebarIsActive.value = emittedValue.classList;
};

// Functions
// is side bar active?
watch(sidebarIsActive, (newValue) => {
  if (newValue === true) {
    console.log("sidebar is active");
  } else {
    console.log("sidebar is not active");
  }
})
</script>

<template>
  <SideBar @sidebarIsActive="handleSidebarIsActive" />
  <TopBar :class="sidebarIsActive ? 'header__sidebar-active' : null" />
  <RouterView :class="sidebarIsActive ? 'main__sidebar-active' : null" />
  <h1 v-show="sidebarIsActive">TESTEEEEEEEEEEEEEEEEEEEEEE</h1>
</template>

<style lang="scss" scoped>
@import './assets/styles/variables';
@import './assets/styles/mixins';

header {
  position: fixed;
  top: 0;
  right: 0;
  left: 250px;
  z-index: 1;
  transition: .2s;

  @include mq(l-xl) {
    left: 75px;
  }
}

.header__sidebar-active {
  left: 250px;
}

main {
  position: relative;
  top: 69px;
  left: 250px;
  transition: .2s;

  @include mq(l-xl) {
    left: 75px;
  }
}

.main__sidebar-active {
  left: 250px;
}
</style>