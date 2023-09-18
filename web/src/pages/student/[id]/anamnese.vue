<script setup>
import { getAnamnese } from "@/services/api/get";

import { onMounted } from "vue";
import { useRoute } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";

const route = useRoute();
const store = useStudentStore();

async function initAnamnese() {
  try {
    if (store.anamnese.id !== route.params.id) {
      store.anamnese.value = await getAnamnese(route.params.id);
      store.anamnese.id = route.params.id;
    }
  } catch {}
}

onMounted(() => {
  initAnamnese();
});
</script>

<template>
  <section>
    <h2>Anamnese</h2>
    <p>{{ store.anamnese.value }}</p>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

section {
  padding: 20px;
  margin-bottom: 20px;
  width: 100%;
  border-radius: $border-radius;
  box-shadow: $box-shadow;
  background-color: white;

  h2 {
    padding-bottom: 20px;
    color: $txt-title;
  }
}
</style>
