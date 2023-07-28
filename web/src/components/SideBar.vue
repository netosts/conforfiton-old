<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';

// Get the refs
const sidebar = ref('');
const sidebarIsActive = ref(null);
// define the emit
const emit = defineEmits(['sidebarIsActive']);

// Functions
function toggleSidebar() {
  if (sidebar.value.classList.contains('sidebar-active')) {
    sidebarIsActive.value = false;
  } else {
    sidebarIsActive.value = true;
  }
};
// toggle sidebar when window resize
function windowResizeSidebar() {
  if (window.innerWidth >= 1050) {
    sidebarIsActive.value = true;
  } else {
    sidebarIsActive.value = false;
  }
};

function logout() {
  localStorage.removeItem('user');
  location.reload();
};

// DOM Mount Functions
onMounted(() => {
  window.addEventListener('resize', windowResizeSidebar);
  windowResizeSidebar();
});
onUnmounted(() => {
  window.removeEventListener('resize', windowResizeSidebar);
});

// Watch for changes and then send emit
watch(sidebarIsActive, (newValue) => {
  emit('sidebarIsActive', newValue);
});
</script>

<template>
  <aside class="sidebar" :class="sidebarIsActive ? 'sidebar-active' : null" ref="sidebar">
    <div class="menu-button" @click="toggleSidebar">
      <div class="line__1"></div>
      <div class="line__2"></div>
      <div class="line__3"></div>
    </div>
    <div class="sidebar__1">
      <div class="logo" v-show="sidebarIsActive">
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
      <div class="menu" v-show="sidebarIsActive">
        <h2>Menu</h2>
        <ul>
          <li>Alunos</li>
          <ul>
            <li>Visualizar todos</li>
            <li>Avaliar aluno</li>
            <li>Adicionar peso</li>
            <li>
              <RouterLink to="/login">Login</RouterLink>
            </li>
            <li>
              <button @click="logout">Logout</button>
            </li>
          </ul>
        </ul>
      </div>
    </div>
    <div class="sidebar__2" @click="toggleSidebar"></div>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

.sidebar {
  display: grid;
  grid-template-columns: 250px 1fr;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 2;
  width: 250px;
  height: 100%;
  transition: .2s;
  transform: translateX(-70%);

  @include mq(s) {
    transform: translateX(-100%);
    transition: none;
  }

  &__1 {
    background-color: $sidebar;
  }

  &__2 {
    background-color: rgba(0, 0, 0, 0.205);
  }

  .menu-button {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 4px;
    position: absolute;
    top: 10px;
    right: -65px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    transition: .3s;

    &:hover {
      gap: 5px;
    }

    div {
      height: 2px;
      border-radius: 10px;
      background-color: $txt-subtitle;
    }

    .line__1 {
      margin-left: -4px;
      width: 22px;
    }

    .line__2 {
      width: 26px;
    }

    .line__3 {
      margin-left: -11px;
      width: 15px;
    }
  }

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

.sidebar-active {
  transform: translateX(0);

  @include mq(s) {
    width: 100%;
  }
}
</style>