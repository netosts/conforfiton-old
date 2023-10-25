<script setup>
import { ref } from "vue";

const photoTooltip = ref(false);
const buttonsHover = ref(false);
const fileInput = ref(null);
const photoSrc = ref(null);

const emit = defineEmits(["formData"]);

function fileChange(event) {
  if (!event.target.files[0]) {
    return;
  }
  fileInput.value = event.target.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(fileInput.value);
  reader.onload = (e) => {
    photoSrc.value = e.target.result;
  };
  emit("formData", fileInput.value);
}

function removePicture() {
  photoSrc.value = null;
  emit("formData", null);
}
</script>

<template>
  <div class="photo">
    <div class="photo__input">
      <div class="photo__input__image">
        <img
          @mouseover="buttonsHover = true"
          @mouseleave="buttonsHover = false"
          :src="photoSrc ? photoSrc : '/img/default-profile-picture.jpg'"
        />
        <input
          type="file"
          accept="image/*"
          ref="fileInput"
          class="hidden"
          @change="fileChange"
        />
        <Transition name="fade">
          <div
            @mouseover="buttonsHover = true"
            @mouseleave="buttonsHover = false"
            class="photo__input__image__buttons"
            v-show="buttonsHover"
          >
            <button type="button" @click="removePicture">X</button>
            <button
              type="button"
              @click="fileInput.click()"
              @mouseover="photoTooltip = true"
              @mouseleave="photoTooltip = false"
            >
              O
            </button>
          </div>
        </Transition>
        <Transition name="fade">
          <div class="photo__input__image--tooltip" v-show="photoTooltip">
            <span>Selecionar Imagem</span>
          </div>
        </Transition>
      </div>
      <span class="photo__input--text">Foto do Aluno</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

.photo {
  &__input {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    &__image {
      position: relative;
      img {
        border: 8px solid $profile-pic;
        border-radius: 50%;
        width: 120px;
        height: 120px;
      }
      &__buttons {
        position: absolute;
        top: 50%;
        right: 50%;
        transform: translate(50%, -50%);
        display: flex;
        gap: 10px;

        button {
          background-color: rgba(255, 255, 255, 0.224);
          border: none;
          border-radius: 50%;
          width: 40px;
          height: 40px;
          color: white;
          cursor: pointer;
          transition: 0.2s;

          &:hover {
            background-color: rgba(255, 255, 255, 0.44);
          }
        }
      }
      &--tooltip {
        position: absolute;
        z-index: 2;
        top: 50px;
        right: -150px;
        height: 30px;
        border-radius: $border-radius;
        background-color: rgb(80, 80, 80);
        span {
          position: relative;
          z-index: 2;
          padding: 10px;
          font-size: 12px;
          color: rgb(240, 240, 240);
        }
        &::before {
          content: "";
          position: absolute;
          z-index: 1;
          top: 5px;
          left: -2px;
          width: 20px;
          height: 20px;
          background-color: rgb(80, 80, 80);
          transform: rotate(45deg);
        }
      }
    }
    &--text {
      font-size: 14px;
      font-weight: 500;
      color: $txt-title;
    }
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.hidden {
  visibility: hidden;
  position: absolute;
}
</style>
