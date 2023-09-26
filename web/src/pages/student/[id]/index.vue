<script setup>
import { getOverviewInformation } from "@/services/api/get";

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
    if (store.overview.id !== route.params.id) {
      store.overview.value = await getOverviewInformation(route.params.id);
      store.overview.id = route.params.id;
    }
  } catch (err) {
    if (err.response.data.msg === "Anamnese not found.") {
      store.overview.value = null;
      store.overview.id = route.params.id;
    }
  }
}

onMounted(async () => {
  await initAnamnese();
  store.overview.initiated = true;
});
</script>

<template>
  <section>
    <h2>Avaliação Morfofuncional</h2>
    <div
      class="overview-container"
      v-if="store.overview.value && store.overview.initiated"
    >
      <div class="morphofunctional">
        <div class="morphofunctional__content">
          <p>
            {{ student?.name }} está
            {{
              store.overview.value?.q4.training
                ? "em atividade"
                : "em sedentarismo"
            }}
            há {{ store.overview.value?.q4.time }}
          </p>
          <p>Seu principal objetivo é: "{{ store.overview.value?.q1 }}"</p>
          <p>
            E tem como objetivo secundário: "{{ store.overview.value?.q2 }}"
          </p>
          <p>
            Dores/Desconfortos: "{{
              store.overview.value?.q20 ? store.overview.value?.q21 : "Nenhum"
            }}"
          </p>
          <p>Diabetes: {{ store.overview.value?.diabetes ? "Sim" : "Não" }}</p>
          <p>
            Hipertensão:
            {{ store.overview.value?.hypertension ? "Sim" : "Não" }}
          </p>
          <p>Patologias: {{ store.overview.value?.q22 }}</p>
        </div>
      </div>
      <div class="training-zone">
        <h2>Zonas de Treino</h2>
        <div class="training-zone__content">
          <p>FC Max: {{ store.overview.value?.fc_max }}</p>
          <p>FC Repouso: {{ store.overview.value?.fc_repouso }}</p>
          <p>L1: {{ store.overview.value?.l1 }}</p>
          <p>L2: {{ store.overview.value?.l2 }}</p>
        </div>
      </div>
    </div>

    <div
      class="no-anamnese"
      v-if="!store.overview.value && store.overview.initiated"
    >
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

  .overview-container {
    display: flex;
    flex-direction: column;
    gap: 20px;

    .morphofunctional,
    .training-zone {
      &__content {
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
