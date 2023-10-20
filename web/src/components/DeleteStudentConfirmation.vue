<script setup>
import {
  softDeleteStudent,
  permanentDeleteStudent,
} from "@/services/api/delete";
import { activateStudent } from "@/services/api/put";
import { ref, onMounted } from "vue";

const props = defineProps({
  student: Object,
});

// VARIABLES
const bodyElement = ref(null);
const confirmInput = ref(null);

// Emits
const emit = defineEmits(["closeDelete", "pushHome"]);

// FUNCTIONS
function closeDelete() {
  emit("closeDelete", false);
  bodyElement.value.style.overflow = "auto";
}

async function onSubmit() {
  try {
    if (props.student.typeOfDelete === "soft") {
      await softDeleteStudent(props.student.id);
      location.reload();
    } else if (props.student.typeOfDelete === "permanent") {
      await permanentDeleteStudent(props.student.id);
      sessionStorage.setItem("submitted", true);
      emit("pushHome");
    } else if (props.student.typeOfDelete === "activate") {
      await activateStudent(props.student.id);
      location.reload();
    }
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
          <h1>
            {{
              student?.typeOfDelete === "soft"
                ? "Desativar"
                : student?.typeOfDelete === "permanent"
                ? "Deletar"
                : "Reativar"
            }}
            {{ student?.name }}?
          </h1>
        </div>
        <div class="container__title__buttons">
          <button type="button" @click="closeDelete">
            <font-awesome-icon icon="fa-solid fa-xmark" size="xl" />
          </button>
        </div>
      </div>
      <div class="container__content">
        <p v-if="student?.typeOfDelete === 'soft'">
          O aluno <strong>{{ student?.name }}</strong> será desativado. Nenhum
          dado será perdido!
        </p>
        <p v-if="student?.typeOfDelete === 'permanent'">
          Todos dados de <strong>{{ student?.name }}</strong> serão
          <strong>permanentemente perdidos</strong>. Você tem certeza que deseja
          continuar?
        </p>
        <p v-if="student?.typeOfDelete === 'activate'">
          O aluno <strong>{{ student?.name }}</strong> será reativado. Deseja
          prosseguir?
        </p>
      </div>
      <div
        class="container__input"
        v-if="student?.typeOfDelete === 'permanent'"
      >
        <label for="confirm">Para deletar, insira o nome do aluno:</label>
        <input v-model="confirmInput" type="text" name="confirm" id="confirm" />
      </div>
      <div class="container__submit">
        <button @click="closeDelete" class="container__submit__no">
          Cancelar
        </button>
        <button
          :id="student?.typeOfDelete === 'activate' ? 'activate-btn' : null"
          :class="
            student?.typeOfDelete === 'permanent' &&
            confirmInput !== student.name
              ? 'disabled'
              : null
          "
          :disabled="
            student?.typeOfDelete === 'permanent' &&
            confirmInput !== student.name
          "
          @click="onSubmit"
          class="container__submit__yes"
        >
          {{
            student?.typeOfDelete === "soft"
              ? "Desativar"
              : student?.typeOfDelete === "permanent"
              ? "Deletar"
              : "Reativar"
          }}
        </button>
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

    &__input {
      display: flex;
      flex-direction: column;
      padding: 0 10px 10px 10px;
      label {
        font-size: 14px;
        color: $txt-subtitle;
      }
      input {
        @include createInput();
      }
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

.disabled {
  opacity: 0.3;
  pointer-events: none;
}

#activate-btn {
  background-color: $validation;
}
</style>
