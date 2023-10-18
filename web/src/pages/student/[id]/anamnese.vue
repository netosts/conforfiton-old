<script setup>
import { getAnamnese } from "@/services/api/get";

import {
  translateDays,
  translatePeriods,
  untranslateMenstruation,
} from "@/services/helpers";

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
    gender: ["Male", "Female"],
  },
  {
    label: "Objetivo secundário",
    value: computed(() => store.anamnese.value?.q2),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Em quanto tempo espera atingir esses objetivos",
    value: computed(() => store.anamnese.value?.q3),
    show: false,
    gender: ["Male", "Female"],
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
    gender: ["Male", "Female"],
  },
  {
    label: "Como é ou era o último treino",
    value: computed(() => store.anamnese.value?.q5),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Exercício que não gosta de fazer",
    value: computed(() => store.anamnese.value?.q6),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Exercício que ama fazer",
    value: computed(() => store.anamnese.value?.q7),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Em quanto tempo costumava concluir o treino",
    value: computed(() => store.anamnese.value?.q8),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Restrição de tempo para treinar",
    value: computed(() => store.anamnese.value?.q9),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Tempo de treino disponível por dia",
    value: computed(() => store.anamnese.value?.q10),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Local de treino",
    value: computed(() => store.anamnese.value?.q11),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Disponibilidade para treinar durante a semana",
    value: computed(() => store.anamnese.value?.q13),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Está fazendo dieta orientado(a) por nutricionista",
    value: computed(() => (store.anamnese.value?.q14 ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Está sendo acompanhado(a) por nutrologista ou endocrinologista",
    value: computed(() => (store.anamnese.value?.q15 ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Rotina alimentar",
    value: computed(() => store.anamnese.value?.q16),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Qualidade do sono, de 1 a 10",
    value: computed(() => store.anamnese.value?.q17),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Profissão",
    value: computed(() => store.anamnese.value?.q18),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label:
      "No trabalho, permanece muito tempo sentado(a), em movimento ou realiza trabalho braçal",
    value: computed(() => store.anamnese.value?.q19),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Dores ou desconfortos",
    value: computed(() =>
      store.anamnese.value?.q21 ? store.anamnese.value?.q21 : "Nenhum"
    ),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Limitação física",
    value: computed(() => store.anamnese.value?.physical_limitation),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Tem Diabetes",
    value: computed(() => (store.anamnese.value?.diabetes ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Tem Hipertensão",
    value: computed(() => (store.anamnese.value?.hypertension ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Patologia (doença) diagnosticada por algum médico",
    value: computed(() => store.anamnese.value?.q22),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Uso de medicamentos de forma rotineira",
    value: computed(() => store.anamnese.value?.q23),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Faz uso de Dispositivos intrauterinos (DIU)",
    value: computed(() => (store.anamnese.value?.iud ? "Sim" : "Não")),
    show: false,
    gender: ["Female"],
  },
  {
    label: "Menstrua regularmente",
    value: computed(() =>
      untranslateMenstruation(store.anamnese.value?.menstruation)
    ),
    show: false,
    gender: ["Female"],
  },
  {
    label: "Regularidade no consumo de álcool",
    value: computed(() => store.anamnese.value?.alcohol_ingestion),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label:
      "O médico já mencionou condição cardíaca e só deve realizar atividade física recomendada por um médico",
    value: computed(() => (store.anamnese.value?.q24 ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Frequência cardíaca em repouso",
    value: computed(() =>
      store.anamnese.value?.fc_repouso
        ? store.anamnese.value?.fc_repouso
        : "Não incluído"
    ),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label:
      "O médico sabe que ele(a) está ingressando em um programa de treinamento físico",
    value: computed(() => (store.anamnese.value?.q25 ? "Sim" : "Não")),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Meta a atingir",
    value: computed(() => store.anamnese.value?.q26),
    show: false,
    gender: ["Male", "Female"],
  },
  {
    label: "Algo relevante para personalizar o treino",
    value: computed(() =>
      store.anamnese.value?.q27 ? store.anamnese.value?.q27 : "Não incluído"
    ),
    show: false,
    gender: ["Male", "Female"],
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
    <RouterLink
      :to="`/student/${route.params.id}/update-anamnese`"
      class="update-anamnese"
      v-if="store.anamnese.value && store.anamnese.initiated"
    >
      <font-awesome-icon icon="fa-solid fa-gear" size="lg" />
    </RouterLink>
    <div
      class="content"
      v-if="store.anamnese.value && store.anamnese.initiated"
    >
      <div v-for="(item, id) in labelsList" :key="id" @click="openDiv(id)">
        <div
          :class="
            !item.gender.includes(student?.gender)
              ? 'content__loop__container--hidden'
              : 'content__loop__container'
          "
        >
          <div
            v-if="item.gender.includes(student?.gender)"
            class="content__loop__container__title"
          >
            <h3>
              {{ item.label }}
            </h3>
            <font-awesome-icon
              v-show="!item.show"
              icon="fa-solid fa-circle-plus"
              size="lg"
              class="content__loop__container__title__icon"
            />
            <font-awesome-icon
              v-show="item.show"
              icon="fa-solid fa-circle-minus"
              size="lg"
              class="content__loop__container__title__icon"
            />
          </div>
          <div v-if="id === 11" class="content__loop__container__response">
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
          <div v-else class="content__loop__container__response">
            <h4 v-show="item.show">{{ item.value }}</h4>
          </div>
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
  position: relative;
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

  .update-anamnese {
    position: absolute;
    top: 10px;
    right: 10px;
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

  .content {
    display: flex;
    flex-direction: column;

    &__loop {
      &--hidden {
        display: none;
      }
      &__container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 16px;
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
          &__icon {
            color: $buttons;
          }
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
