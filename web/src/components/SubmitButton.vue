<script setup>
const props = defineProps({
  reset: Boolean,
  meta: Object,
  msg: String,
  isSubmitting: Boolean,
});

function onReset() {
  location.reload();
}
</script>

<template>
  <div
    class="submitbox"
    :tabindex="!meta?.valid ? '-1' : null"
    v-if="!isSubmitting"
  >
    <div
      class="submitbox__submit"
      :class="{ 'submitbox__submit--disabled': meta ? !meta.valid : null }"
    >
      <button type="submit" class="submitbox__submit__btn">{{ msg }}</button>
    </div>
    <button v-if="reset" type="button" class="reset" @click="onReset">
      Reiniciar
    </button>
  </div>

  <div class="spinnerbox" v-else>
    <font-awesome-icon
      icon="fa-solid fa-spinner"
      size="2xl"
      spin
      class="spinner"
    />
  </div>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

.submitbox {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;

  &__submit {
    display: flex;
    flex: 1;

    &__btn {
      flex: 1;
      @include submitButtons($validation, white);
    }

    &--disabled {
      opacity: 0.5;
      cursor: not-allowed;

      .submitbox__submit__btn {
        pointer-events: none;
      }
    }
  }

  .reset {
    @include submitButtons($profile-pic, $txt-title);
  }
}

.spinnerbox {
  display: flex;
  justify-content: center;
  color: $buttons;
}
</style>
