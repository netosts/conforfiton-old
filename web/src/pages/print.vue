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
      <div class="teste" @click="print">
        <p class="teste__student">EU SOU CARLOS</p>
      </div>
      <div class="teste" @click="print">
        <p class="teste__cleu">EU SOU JONAS</p>
      </div>
      <div class="teste" @click="print">
        <p class="teste__zeu">EU SOU LUCIO</p>
      </div>
      <!-- width="795" -->
      <!-- <img src="@/assets/images/teste.png" @click="print" alt="#" />
      <img src="@/assets/images/teste.png" @click="print" alt="#" />
      <img src="@/assets/images/teste.png" @click="print" alt="#" /> -->
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
    background-image: url("../assets/images/teste-798-2.jpg");
    background-size: cover;

    &__student {
      position: absolute;
      top: 310px;
      left: 200px;
      font-size: 3rem;
      font-weight: 900;
      color: red;
    }

    &__cleu {
      position: absolute;
      top: 1440px;
      left: 200px;
      font-size: 3rem;
      font-weight: 900;
      color: blue;
    }

    &__zeu {
      position: absolute;
      top: 2570px;
      left: 200px;
      font-size: 3rem;
      font-weight: 900;
      color: green;
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
