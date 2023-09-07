<script setup>
import {
  getStudentAvaliar,
  getRmConfig,
  getAntropometriaProtocol,
  getNeuromuscularProtocol,
} from "@/services/api/get";
import { translateGender } from "@/services/helpers";
import { formatAge } from "@/services/validators/formats";

import { useAvaliarStore } from "@/stores/avaliar";

import { onMounted } from "vue";
import { useRoute, useRouter, definePage } from "vue-router/auto";

import Neuromuscular from "@/components/avaliar/Neuromuscular.vue";
import Antropometria from "@/components/avaliar/Antropometria.vue";

definePage({
  meta: { isStudent: true, requiresAuth: true },
});

// VARIABLES
const router = useRouter();
const route = useRoute();
const store = useAvaliarStore();

async function initRequests() {
  try {
    store.student = await getStudentAvaliar(route.params.id);
    store.student["age"] = formatAge(store.student.birth_date);
    if (store.types.includes("Neuromuscular")) {
      store.neuromuscular_protocol = await getNeuromuscularProtocol(
        store.student?.id
      );
      store.rmConfig = await getRmConfig(store.student.gender);
    }
    if (store.types.includes("Antropometria")) {
      store.antropometria_protocol = await getAntropometriaProtocol(
        store.student?.id
      );
    }
  } catch {
    alert("Houve um erro e o aluno não pôde ser encontrado.");
    router.push("/");
  }
}

// DOM Mount
onMounted(() => {
  initRequests();
});
</script>

<template>
  <main>
    <section class="student">
      <div class="top">
        <RouterLink to="/" class="voltar">
          <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
        </RouterLink>
        <h1>{{ store.student?.name }}</h1>
      </div>

      <div class="student__details">
        <p>Peso: {{ store.student?.weight }}kg</p>
        <p>Sexo: {{ translateGender(store.student?.gender) }}</p>
        <p>Altura: {{ store.student?.height }}cm</p>
        <p>Idade: {{ store.student?.age }}</p>
      </div>
    </section>

    <Neuromuscular v-if="store.types?.includes('Neuromuscular')" />

    <Antropometria v-if="store.types?.includes('Antropometria')" />

    <section v-if="store.types?.includes('Cardio')">
      <h2>Cardio</h2>
    </section>
  </main>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 20px;

  .student {
    display: flex;
    flex-direction: column;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;

    .top {
      padding: 10px;
      box-shadow: $box-shadow;

      .voltar {
        position: absolute;
        top: 5px;
        @include tool();
        color: $buttons;
      }

      h1 {
        text-align: center;
        padding: 0 40px;
      }
    }

    &__details {
      display: flex;
      justify-content: space-evenly;
      gap: 5px;
      background-color: $readonly;
      font-weight: 600;
      pointer-events: none;

      p {
        flex: 1;
        padding: 20px;
        text-align: center;
      }

      p:nth-child(1) {
        border-right: 2px solid $background;
      }
      p:nth-child(2) {
        border-right: 2px solid $background;
      }
    }
  }
}
</style>
