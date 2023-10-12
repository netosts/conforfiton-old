<script setup>
import { getOverviewInformation } from "@/services/api/get";

import {
  weeklyCaloricExpenditure,
  dailyCaloricExpenditure,
} from "@/services/avaliar/cardio/helpers";

import { onMounted, onUnmounted } from "vue";
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

async function initOverview() {
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
  await initOverview();
  store.overview.initiated = true;
});

onUnmounted(() => {
  store.overview.initiated = false;
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
          <RouterLink
            :to="`/student/${route.params.id}/update-morphofunctional`"
            class="morphofunctional__content__edit"
          >
            <font-awesome-icon icon="fa-solid fa-gear" size="lg" />
          </RouterLink>
          <p>
            {{ student?.name }} está
            {{
              store.overview.value?.q4.training
                ? "em atividade"
                : "em sedentarismo"
            }}
            há "<strong>{{ store.overview.value?.q4.time }}</strong
            >"; tem como objetivo principal "<strong>{{
              store.overview.value?.q1
            }}</strong
            >" e secundário "<strong>{{ store.overview.value?.q2 }}</strong
            >"; consome álcool "<strong>{{
              store.overview.value?.alcohol_ingestion
            }}</strong
            >" por semana; e tem como limitação física "<strong>{{
              store.overview.value?.physical_limitation
            }}</strong
            >".
          </p>
          <p v-if="student?.gender === 'Female'">
            {{
              store.overview.value?.iud
                ? "Faz uso de Dispositivos intrauterinos (DIU)"
                : "Não faz uso de Dispositivos intrauterinos (DIU)"
            }}. <br />
            {{
              store.overview.value?.menstruation === true
                ? "Menstrua normalmente"
                : store.overview.value?.menstruation === false
                ? "Não menstrua"
                : "Prefere não informar"
            }}.
          </p>
          <p>
            {{
              store.overview.value?.q20
                ? `Apresenta dor/desconforto muscular: "${store.overview.value?.q21}".`
                : "Não apresenta dor/desconforto muscular."
            }}
            <br />
            {{
              store.overview.value?.diabetes
                ? "Tem diabetes."
                : "Não tem diabetes."
            }}
            <br />
            {{
              store.overview.value?.hypertension
                ? "Tem hipertensão."
                : "Não tem hipertensão."
            }}
            <br />
            Suas patologias são: "<strong>{{
              store.overview.value?.q22
            }}</strong
            >".
          </p>
          <p>
            Sua frequência cardíaca máxima é
            <strong>{{ store.overview.value?.fc_max }}bpm</strong> e a de
            repouso é
            <strong>{{
              store.overview.value?.fc_repouso
                ? `${store.overview.value?.fc_repouso}bpm`
                : "[NÃO INCLUÍDO]"
            }}</strong
            >. <br />
            Sua zona alvo é: <br />
            L1:
            <strong>{{
              store.overview.value?.l1
                ? `${store.overview.value?.l1}bpm`
                : "[NÃO INCLUÍDO]"
            }}</strong
            >. <br />
            L2:
            <strong>{{
              store.overview.value?.l2
                ? `${store.overview.value?.l2}bpm`
                : "[NÃO INCLUÍDO]"
            }}</strong
            >. <br />
          </p>
          <p>
            Gastos Calóricos &#8595; <br />
            DIÁRIO:
            <strong>{{ dailyCaloricExpenditure(student?.weight) }}kcal</strong>.
            <br />
            SEMANAL:
            <strong>{{ weeklyCaloricExpenditure(student?.weight) }}kcal</strong
            >.
          </p>
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
    text-align: center;
  }

  .overview-container {
    display: flex;
    flex-direction: column;
    gap: 20px;

    .morphofunctional,
    .training-zone {
      &__content {
        position: relative;
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 20px 50px 20px 20px;
        border: 1px solid $input-border;
        border-radius: $border-radius;
        box-shadow: $box-shadow;
        p::before {
          content: "• ";
          color: black;
        }
        &__edit {
          position: absolute;
          top: 5px;
          right: 5px;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 40px;
          height: 40px;
          border-radius: 50%;
          padding: 10px;
          color: $txt-aside;
          cursor: pointer;
          transition: 0.2s;
          &:hover {
            background-color: rgba(0, 0, 0, 0.08);
          }
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
