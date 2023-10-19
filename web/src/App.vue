<script setup>
import SideBar from "./components/SideBar.vue";
import TopBar from "./components/TopBar.vue";

import { ref, watch } from "vue";
import { useRoute } from "vue-router/auto";

// VARIABLES
const route = useRoute();
const hideBars = ref(false);

// Get Emits
const sidebarIsActive = ref(null);
// Handle Emits
const handleSidebar = (emittedValue) => {
  return (sidebarIsActive.value = emittedValue);
};

const hiders = [
  "/login",
  "/login/register",
  "/login/demo",
  "/print",
  /\/register\/(?!anamnese$)(?!anamnese\/\d+)(?!student$)[A-Za-z0-9]+/,
  /\/register\/[A-Za-z0-9]+\/anamnese\//,
  "/successful-register",
  "/invalid-link",
  "/welcome",
];

watch(route, () => {
  if (hiders.some((item) => route.path.match(item))) {
    hideBars.value = true;
  } else {
    hideBars.value = false;
  }
});
</script>

<template>
  <SideBar v-show="!hideBars" @sidebarIsActive="handleSidebar" />
  <TopBar
    v-show="!hideBars"
    :class="sidebarIsActive ? 'header__sidebar-active' : null"
  />
  <RouterView
    :class="{
      'main__sidebar-active': sidebarIsActive && !hideBars,
      main: !hideBars,
    }"
  />
</template>

<style lang="scss" scoped>
@import "./assets/styles/variables";
@import "./assets/styles/mixins";

header {
  position: fixed;
  top: 0;
  right: 0;
  left: 75px;
  z-index: 10;
  transition: 0.2s;

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

.main {
  position: relative;
  top: 69px;
  left: 75px;

  margin: {
    top: 25px;
    right: calc(25px + 75px);
    bottom: calc(25px + 69px);
    left: 25px;
  }

  transition: 0.2s;

  @include mq(m) {
    margin: {
      top: 15px;
      right: calc(15px + 75px);
      bottom: calc(15px + 69px);
      left: 15px;
    }
  }

  @include mq(s) {
    left: 0px;
    margin-right: 15px;
    transition: none;
  }

  @include mq(xs-s) {
    margin-left: 10px;
    margin-right: 10px;
  }
}

.main__sidebar-active {
  left: 250px;
  margin-right: calc(25px + 250px);

  @include mq(m) {
    margin-right: calc(15px + 250px);
  }

  @include mq(s) {
    left: 0;
    margin-right: 25px;
  }
}
</style>
