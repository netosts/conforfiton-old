<script setup>
import { deleteEvaluation } from "@/services/api/delete";
import { ref, onMounted } from "vue";

import { useStudentStore } from "@/stores/student";

const props = defineProps({
  evaluation: Object,
});

// VARIABLES
const store = useStudentStore();
const bodyElement = ref(null);

// Emits
const emit = defineEmits(["deactivateDelete", "closeDeleteButton"]);

// FUNCTIONS
function closeDelete() {
  emit("deactivateDelete", props.evaluation.id);
  bodyElement.value.style.overflow = "auto";
}

function closeDeleteButton() {
  emit("closeDeleteButton");
  bodyElement.value.style.overflow = "auto";
}

async function updateStorage() {
  if (
    props.evaluation.type === "neuromuscular" ||
    props.evaluation.type === "neuromuscular/rml"
  ) {
    store.neuromuscular.value = store.neuromuscular.value.filter(
      (item) => item.id !== props.evaluation.id
    );
  } else if (props.evaluation.type === "antropometria") {
    store.antropometria.value = store.antropometria.value.filter(
      (item) => item.id !== props.evaluation.id
    );
  } else if (props.evaluation.type === "cardio") {
    store.cardio.value = store.cardio.value.filter(
      (item) => item.id !== props.evaluation.id
    );
  }
}

async function onSubmit() {
  try {
    await deleteEvaluation(props.evaluation.type, props.evaluation.id);
    await updateStorage();
    closeDelete();
  } catch (err) {
    console.error(err);
  }
}

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside @click.self="closeDelete">
    <div class="container">
      <div class="container__title">
        <div class="container__title__text">
          <h1>Deletar avaliação?</h1>
        </div>
        <div class="container__title__buttons">
          <button type="button" @click="closeDelete">
            <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
          </button>
        </div>
      </div>
      <div class="container__content">
        <p>
          A avaliação <strong>{{ evaluation.name }}</strong> será deletada.
        </p>
      </div>
      <div class="container__submit">
        <button @click="closeDeleteButton" class="container__submit__no">
          Cancelar
        </button>
        <button @click="onSubmit" class="container__submit__yes">Delete</button>
      </div>
    </div>
  </aside>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

aside {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;
  background-color: rgba(79, 79, 79, 0.442);

  @include mq(s) {
    padding: 10px;
  }

  .container {
    width: 375px;
    border-radius: $border-radius;
    background-color: rgb(245, 245, 245);

    @include mq(xs) {
      width: 300px;
    }

    &__title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid $input-border;

      &__text {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 20px;

        h1 {
          font-size: 1.2rem;
          font-weight: 800;
          color: $txt-title;
        }
      }

      &__buttons {
        button {
          margin-right: 10px;
          width: 40px;
          height: 40px;
          border: none;
          border-radius: 50%;
          background-color: transparent;
          color: rgba(85, 85, 85, 0.588);
          cursor: pointer;
          transition: 0.2s;

          &:hover {
            color: $txt-aside;
            background-color: rgba(186, 186, 186, 0.267);
          }
        }
      }
    }

    &__content {
      display: flex;
      flex-direction: column;
      gap: 5px;
      padding: 20px 10px 10px 10px;
      color: $txt-aside;
    }

    &__submit {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      padding: 10px;

      &__yes {
        background-color: red;
        color: white;
      }

      &__no {
        background-color: rgb(223, 223, 223);
      }

      button {
        padding: 10px 20px;
        border: none;
        border-radius: $border-radius;
        cursor: pointer;
        transition: 0.2s;

        &:hover {
          filter: brightness(0.9);
        }

        &:active {
          filter: brightness(0.7);
        }
      }
    }
  }
}
</style>
