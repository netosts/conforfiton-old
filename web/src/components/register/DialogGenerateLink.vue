<script setup>
import { ref, onMounted } from "vue";

// VARIABLES
const bodyElement = ref(null);

// Emits
const emit = defineEmits(["isDialogActive"]);

// Props
const props = defineProps({
  link: String,
});

// FUNCTIONS
function closeDialog() {
  emit("isDialogActive", false);
  bodyElement.value.style.overflow = "auto";
}

function copyLink() {
  navigator.clipboard.writeText(props.link);
  alert("Link copiado!");
}

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeDialog">
    <div class="container">
      <div @click="copyLink" class="container__link">
        <span>{{ link }}</span>
        <font-awesome-icon icon="fa-solid fa-copy" size="lg" />
      </div>
      <div class="container__button">
        <button type="button" @click="closeDialog">Fechar</button>
      </div>
    </div>
  </aside>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

aside {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;
  background-color: rgba(79, 79, 79, 0.442);

  @include mq(s) {
    padding: 10px;
  }

  .container {
    position: relative;
    display: flex;
    flex-direction: column;
    border-radius: $border-radius;
    background-color: rgb(245, 245, 245);
    color: $txt-title;

    &__link {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 10px 10px 0 10px;
      padding: 10px;
      border-radius: $border-radius;

      cursor: pointer;
      transition: 0.2s;

      &:hover {
        background-color: rgb(234, 234, 241);
      }
      span {
        text-align: center;
        font-size: 18px;
        font-weight: 500;
      }
    }

    &__button {
      display: flex;
      justify-content: flex-end;
      margin: 10px;

      button {
        @include submitButtons(rgb(223, 223, 223), black);
      }
    }
  }
}
</style>
