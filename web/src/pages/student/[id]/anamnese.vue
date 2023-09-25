<script setup>
import { getAnamnese } from "@/services/api/get";

import { onMounted } from "vue";
import { useRoute } from "vue-router/auto";

import { useStudentStore } from "@/stores/student";

import { definePage } from "vue-router/auto";

definePage({
  meta: { requiresAuth: true },
});

defineProps({
  student: Object,
});

const route = useRoute();
const store = useStudentStore();

async function initAnamnese() {
  try {
    if (store.anamnese.id !== route.params.id) {
      store.anamnese.value = await getAnamnese(route.params.id);
      store.anamnese.id = route.params.id;
    }
  } catch (err) {
    if (err.response.data.msg === "Anamnese not found.") {
      store.anamnese.value = null;
      store.anamnese.id = route.params.id;
    }
  }
}

onMounted(() => {
  initAnamnese();
});
</script>

<template>
  <section>
    <h2>Anamnese</h2>
    <div class="content" v-if="store.anamnese.value">
      <pre>{{ store.anamnese.value }}</pre>
    </div>
    <div class="no-anamnese" v-else>
      <h3>Anamnese não foi cadastrada</h3>
      <RouterLink :to="`/register/anamnese/${student?.person_id}`">
        <button>
          <font-awesome-icon icon="fa-solid fa-plus" /> Adicionar Anamnese
        </button>
      </RouterLink>
    </div>
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

  .content {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 10px 20px;
    border: 1px solid $input-border;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    p {
      color: $buttons;
      font-weight: 600;
    }
    p::before {
      content: "- ";
      color: black;
    }
  }

  .no-anamnese {
    display: flex;
    flex-direction: column;
    gap: 10px;
    h3 {
      padding: 10px;
      text-align: center;
      font-weight: 600;
      color: $error-msg;
      border: 1px solid $error-msg;
      margin-bottom: 10px;
    }
    a {
      display: flex;
      text-decoration: none;
      button {
        flex: 1;
        padding: 10px;
        background: none;
        text-align: center;
        font-weight: 600;
        color: $validation;
        border: 1px solid $validation;
        cursor: pointer;
        transition: 0.4s;
        &:hover {
          background-color: $validation;
          color: white;
        }
      }
    }
  }
}
</style>
