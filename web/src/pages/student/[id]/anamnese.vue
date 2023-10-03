<script setup>
import { getAnamnese } from "@/services/api/get";

import { translateDays, translatePeriods } from "@/services/helpers";

import { reactive, onMounted, onUnmounted, computed } from "vue";
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

const labelsList = reactive([
  {
    label:
      "Principal objetivo com o início de um programa de treinamento físico",
    value: computed(() => store.anamnese.value?.q1),
    show: false,
  },
  {
    label: "Objetivo secundário",
    value: computed(() => store.anamnese.value?.q2),
    show: false,
  },
  {
    label: "Em quanto tempo espera atingir esses objetivos",
    value: computed(() => store.anamnese.value?.q3),
    show: false,
  },
  {
    label: "Está ativo/sedentário há quanto tempo",
    value: computed(() => {
      if (store.anamnese.value?.q4.training) {
        return `Em atividade há ${store.anamnese.value?.q4.time}`;
      } else {
        return `Está sedentário(a) há ${store.anamnese.value?.q4.time}`;
      }
    }),
    show: false,
  },
  {
    label: "Como é ou era o último treino",
    value: computed(() => store.anamnese.value?.q5),
    show: false,
  },
  {
    label: "Exercício que não gosta de fazer",
    value: computed(() => store.anamnese.value?.q6),
    show: false,
  },
  {
    label: "Exercício que ama fazer",
    value: computed(() => store.anamnese.value?.q7),
    show: false,
  },
  {
    label: "Em quanto tempo costumava concluir o treino",
    value: computed(() => store.anamnese.value?.q8),
    show: false,
  },
  {
    label: "Restrição de tempo para treinar",
    value: computed(() => store.anamnese.value?.q9),
    show: false,
  },
  {
    label: "Tempo de treino disponível por dia",
    value: computed(() => store.anamnese.value?.q10),
    show: false,
  },
  {
    label: "Local de treino",
    value: computed(() => store.anamnese.value?.q11),
    show: false,
  },
  {
    label: "Disponibilidade para treinar durante a semana",
    value: computed(() => store.anamnese.value?.q13),
    show: false,
  },
  {
    label: "Está fazendo dieta orientado(a) por nutricionista",
    value: computed(() => (store.anamnese.value?.q14 ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Está sendo acompanhado(a) por nutrologista ou endocrinologista",
    value: computed(() => (store.anamnese.value?.q15 ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Rotina alimentar",
    value: computed(() => store.anamnese.value?.q16),
    show: false,
  },
  {
    label: "Qualidade do sono, de 1 a 10",
    value: computed(() => store.anamnese.value?.q17),
    show: false,
  },
  {
    label: "Profissão",
    value: computed(() => store.anamnese.value?.q18),
    show: false,
  },
  {
    label:
      "No trabalho, permanece muito tempo sentado(a), em movimento ou realiza trabalho braçal",
    value: computed(() => store.anamnese.value?.q19),
    show: false,
  },
  {
    label: "Dores ou desconfortos",
    value: computed(() => store.anamnese.value?.q21),
    show: false,
  },
  {
    label: "Tem Diabetes",
    value: computed(() => (store.anamnese.value?.diabetes ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Tem Hipertensão",
    value: computed(() => (store.anamnese.value?.hypertension ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Patologia (doença) diagnosticada por algum médico",
    value: computed(() => store.anamnese.value?.q22),
    show: false,
  },
  {
    label: "Uso de medicamentos de forma rotineira",
    value: computed(() => store.anamnese.value?.q23),
    show: false,
  },
  {
    label:
      "Tem alguma condição cardíaca e só deve realizar atividade física recomendada por um médico",
    value: computed(() => (store.anamnese.value?.q24 ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Frequência cardíaca em repouso",
    value: computed(() => store.anamnese.value?.fc_repouso),
    show: false,
  },
  {
    label:
      "O médico sabe que ele(a) está ingressando em um programa de treinamento físico",
    value: computed(() => (store.anamnese.value?.q25 ? "Sim" : "Não")),
    show: false,
  },
  {
    label: "Meta a atingir",
    value: computed(() => store.anamnese.value?.q26),
    show: false,
  },
  {
    label: "Algo relevante para personalizar o treino",
    value: computed(() => store.anamnese.value?.q27),
    show: false,
  },
]);

function openDiv(id) {
  if (labelsList[id].show) {
    labelsList[id].show = false;
    return;
  }
  // Set the 'show' property to false for all items
  labelsList.forEach((item) => {
    item.show = false;
  });

  labelsList[id].show = true;
}

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

onMounted(async () => {
  await initAnamnese();
  store.anamnese.initiated = true;
});

onUnmounted(() => {
  store.anamnese.initiated = false;
});
</script>

<template>
  <section>
    <h2>Anamnese</h2>
    <div
      class="content"
      v-if="store.anamnese.value && store.anamnese.initiated"
    >
      <div
        v-for="(item, id) in labelsList"
        :key="id"
        class="content__container"
        @click="openDiv(id)"
      >
        <div class="content__container__title">
          <h3>
            {{ item.label }}
          </h3>
          <font-awesome-icon
            v-show="!item.show"
            icon="fa-solid fa-circle-plus"
            size="lg"
          />
          <font-awesome-icon
            v-show="item.show"
            icon="fa-solid fa-circle-minus"
            size="lg"
          />
        </div>
        <div v-if="id === 11" class="content__container__response">
          <h4
            v-show="item.show"
            v-for="(subItem, subId) in item.value"
            :key="subId"
          >
            {{ translateDays(subItem.day) }}:
            <span
              v-for="(period, periodId) in subItem.periods"
              :key="periodId"
              >{{
                periodId !== 0
                  ? `, ${translatePeriods(period)}`
                  : translatePeriods(period)
              }}</span
            >
          </h4>
        </div>
        <div v-else class="content__container__response">
          <h4 v-show="item.show">{{ item.value }}</h4>
        </div>
      </div>
    </div>
    <div
      class="no-anamnese"
      v-if="!store.anamnese.value && store.anamnese.initiated"
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

  .content {
    display: flex;
    flex-direction: column;
    gap: 16px;

    &__container {
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 10px 20px;
      border-bottom: 1px solid $input-border;
      border-radius: $border-radius;
      box-shadow: $box-shadow;
      cursor: pointer;
      transition: 0.1s;

      &:hover {
        box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.14);
      }

      &__title {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        color: $txt-aside;
      }
      h3 {
        font-weight: 500;
      }

      h4 {
        font-weight: 400;
        color: $logo-color;
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
