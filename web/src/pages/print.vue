<script setup>
import { onMounted } from "vue";

onMounted(() => {
  window.print();
});
</script>

<template>
  <aside>
    <section class="presentation">
      <div class="presentation__background"></div>
      <div class="presentation__content">
        <div class="presentation__content__page">
          <div class="presentation__content__page--bar"></div>
          <div class="presentation__content__page--number">01</div>
        </div>
        <div class="presentation__content__title">
          <h1>Avaliação</h1>
          <h1>Física</h1>
        </div>
      </div>
    </section>
    <section class="presentation">
      <div class="presentation__background"></div>
      <div class="presentation__content">
        <div class="presentation__content__page">
          <div class="presentation__content__page--bar"></div>
          <div class="presentation__content__page--number">01</div>
        </div>
        <div class="presentation__content__title">
          <h1>Avaliação</h1>
          <h1>Física</h1>
        </div>
      </div>
    </section>
  </aside>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

section {
  height: 1100px;
  width: 1600px;

  .presentation {
    &__background {
      position: absolute;
      right: -500px;
      z-index: 1;
      height: 100%;
      width: 100%;
      background-color: $logo-color;
    }

    &__content {
      position: relative;
      z-index: 10;
      padding: 100px;

      &__page {
        display: flex;
        align-items: center;
        gap: 50px;

        &--bar {
          width: 60px;
          height: 5px;
          background-color: $sidebar;
        }

        &--number {
          color: $logo-color;
          font-weight: 900;
          font-size: 2rem;
        }
      }

      &__title {
        display: flex;
        flex-direction: column;
        margin-top: 150px;
        font-size: 11rem;
        color: $sidebar;

        h1:nth-child(2) {
          margin-top: -100px;
          margin-left: 187px;
        }
      }
    }
  }
}

@media print {
  section {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
</style>
