<script setup>
import { onMounted } from "vue";
import { definePage } from "vue-router/auto";

definePage({
  meta: { requiresAuth: true },
});

function print() {
  window.print();
}

// onMounted(() => {
//   window.print();
// });
</script>

<template>
  <aside>
    <section>
      <div class="teste" @click="print"></div>
      <div class="teste" @click="print">
        <p class="teste__name">Thiago</p>
        <p class="teste__age">31 anos</p>
        <p class="teste__gender">Masculino</p>
        <p class="teste__weight">75kg</p>
        <p class="teste__height">1.79m</p>
        <p class="teste__imc">22.1</p>
      </div>
    </section>
  </aside>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

section {
  display: flex;
  flex-direction: column;

  .teste {
    width: 798px;
    height: 1128px;
    background-size: cover;

    &:nth-child(1) {
      background-image: url("../assets/images/print-evaluation-cover.jpg");
    }
    &:nth-child(2) {
      background-image: url("../assets/images/print-evaluation-presentation.jpg");
    }

    &__name {
      position: absolute;
      top: 1263px;
      left: 293px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
    &__age {
      position: absolute;
      top: 1294px;
      left: 187px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
    &__gender {
      position: absolute;
      top: 1325px;
      left: 182px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
    &__weight {
      position: absolute;
      top: 1263px;
      left: 623px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
    &__height {
      position: absolute;
      top: 1292px;
      left: 668px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
    &__imc {
      position: absolute;
      top: 1325px;
      left: 614px;
      font-size: 1.8rem;
      font-weight: 600;
      color: $txt-aside;
    }
  }
}

@media print {
  .teste {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
</style>
