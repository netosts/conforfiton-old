<script setup>
const props = defineProps({
  reset: Boolean,
  meta: Object,
  msg: String,
});

function onReset() {
  location.reload();
}
</script>

<template>
  <div class="submitbox" :tabindex="!meta.valid ? '-1' : null">
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
</style>
