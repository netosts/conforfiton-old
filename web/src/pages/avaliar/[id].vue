<script setup>
import {
  getStudentAvaliar,
  getAntropometriaProtocol,
  getNeuromuscularProtocol,
  getCardioProtocol,
} from "@/services/api/get";

import { postWeight } from "@/services/api/post";

import { evaluationComponents } from "@/services/avaliar/lists";
import { translateGenderToPT } from "@/services/helpers";
import { formatAge } from "@/services/formats";

import { useAvaliarStore } from "@/stores/avaliar";

import { onMounted, ref } from "vue";
import { useRoute, useRouter, definePage } from "vue-router/auto";
import TextField from "../../components/TextField.vue";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const router = useRouter();
const route = useRoute();
const store = useAvaliarStore();

const weight = ref(undefined);
const weightInputActive = ref(false);

async function initRequests() {
  try {
    store.student = await getStudentAvaliar(route.params.id);
    store.student["age"] = formatAge(store.student.birth_date);
    if (store.types.includes("neuromuscular")) {
      store.neuromuscular_protocol = await getNeuromuscularProtocol(
        store.student?.id
      );
    }
    if (store.types.includes("antropometria")) {
      store.antropometria_protocol = await getAntropometriaProtocol(
        store.student?.id
      );
    }
    if (store.types.includes("cardio")) {
      store.cardio_protocol = await getCardioProtocol(store.student?.id);
    }
  } catch {
    alert("Houve um erro e o aluno não pôde ser encontrado.");
    router.push("/");
  }
}

async function submitWeight() {
  try {
    if (!weight.value) {
      weightInputActive.value = false;
      return;
    }

    if (weight.value < 0) {
      alert(`O valor precisa ser maior que 0.`);
      return;
    }
    if (weight.value > 600) {
      alert(`O valor precisa ser menor que 600.`);
      return;
    }

    const currentDate = new Date();
    const formattedDate = currentDate.toISOString();

    const weightForm = {
      weight: weight.value,
      created_at: formattedDate,
    };

    await postWeight(store.student?.id, weightForm);
    store.student.weight = weight.value.toFixed(2);

    weightInputActive.value = false;
  } catch (err) {
    console.log(err);
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
        <RouterLink to="/" class="back">
          <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
        </RouterLink>
        <h1>{{ store.student?.name }}</h1>
        <RouterLink
          :to="`/student/${store.student?.id}/evaluations`"
          class="evaluation"
        >
          <font-awesome-icon icon="fa-solid fa-dna" size="xl" />
        </RouterLink>
      </div>

      <div class="student__details">
        <p v-if="!weightInputActive">Peso: {{ store.student?.weight }}kg</p>
        <TextField
          v-if="weightInputActive"
          v-model="weight"
          type="number"
          name="weight"
        />
        <p>Sexo: {{ translateGenderToPT(store.student?.gender) }}</p>
        <p>Altura: {{ store.student?.height }}cm</p>
        <p>Idade: {{ store.student?.age }}</p>
      </div>
    </section>

    <button
      v-if="!weightInputActive"
      class="update-weight"
      @click="weightInputActive = true"
    >
      Atualizar peso
    </button>
    <button
      v-if="weightInputActive"
      class="update-weight"
      @click="submitWeight"
    >
      Confirmar
    </button>

    <div class="evaluation">
      <div v-for="(item, id) in evaluationComponents" :key="id">
        <component
          :is="item.component"
          v-if="store.types?.includes(item.includes)"
          class="evaluation__component"
        />
      </div>
    </div>
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

      .back {
        position: absolute;
        top: 5px;
        @include tool();
        color: $buttons;
      }

      .evaluation {
        position: absolute;
        top: 5px;
        right: 10px;
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

      @include mq(m) {
        display: grid;
        grid-template-columns: 1fr 1fr;
      }

      .register-field {
        max-width: 80px;
        margin: 0 50px;
        justify-content: center;
      }

      p {
        flex: 1;
        padding: 20px;
        text-align: center;
        pointer-events: none;
      }

      p:nth-child(1) {
        border-right: 2px solid $background;
        @include mq(m) {
          border-bottom: 2px solid $background;
        }
      }

      p:nth-child(2) {
        border-right: 2px solid $background;
        @include mq(m) {
          border-right: none;
          border-bottom: 2px solid $background;
        }
      }
      p:nth-child(3) {
        border-right: 2px solid $background;
      }
    }
  }

  .update-weight {
    width: 150px;
    padding: 5px 20px;
    margin-top: -19px;
    margin-left: 16px;
    border: none;
    border-radius: 0 0 5px 5px;
    background-color: $readonly;
    box-shadow: $box-shadow;
    text-transform: lowercase;
    font-weight: 700;
    cursor: pointer;
    transition: 0.2s;

    &:hover {
      filter: brightness(0.9);
    }

    &:active {
      filter: brightness(0.7);
    }
  }

  .evaluation__component {
    margin-bottom: 20px;
  }
}
</style>
