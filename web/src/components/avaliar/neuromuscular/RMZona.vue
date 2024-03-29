<script setup>
import {
  repsList,
  total,
  classification,
  exerciseList,
} from "@/services/avaliar/neuromuscular/lists";

import { createNeuromuscularForm } from "@/services/avaliar/neuromuscular/helpers";
import { postNeuromuscular } from "@/services/api/post";

import { useRoute } from "vue-router/auto";
import { useAvaliarStore } from "@/stores/avaliar";

import { schema } from "@/services/avaliar/neuromuscular/schema";
import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const route = useRoute();
const store = useAvaliarStore();

async function onSubmit() {
  try {
    const form = await createNeuromuscularForm(
      store.evaluatedAt,
      store.neuromuscular_protocol,
      exerciseList,
      total,
      classification.value
    );

    await postNeuromuscular(form, route.params.id);

    sessionStorage.setItem("submitted", true);

    alert("Neuromuscular salvo com sucesso");

    // Remove Neuromuscular from the screen
    const indexToRemove = store.types.indexOf("neuromuscular");
    store.types.splice(indexToRemove, 1);
  } catch (err) {
    console.error(err);
    throw err;
  }
}
</script>

<template>
  <Form @submit="onSubmit" :validation-schema="schema">
    <table class="neuro-table">
      <thead>
        <tr>
          <th>Exercício</th>
          <th>Peso L.</th>
          <th>Reps</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(exercise, id) in exerciseList" :key="id">
          <td>{{ exercise.title }}</td>
          <td>
            <TextField
              v-model="exercise.lifted"
              :name="`${exercise.name}_lifted`"
              type="number"
              rules="required"
            />
          </td>
          <td>
            <TextField
              v-model="exercise.reps"
              :name="`${exercise.name}_reps`"
              type="select"
              :options="repsList"
              rules="required"
            />
          </td>
        </tr>
      </tbody>
    </table>

    <SubmitButton msg="Salvar" />
  </Form>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 0 20px 10px 20px;
  .neuro-table {
    border-collapse: collapse;
    border: 1px solid $input-border;

    th,
    td {
      border: 1px solid $input-border;
      padding: 8px;
      text-align: center;
    }

    th {
      color: $txt-aside;
    }

    td {
      font-weight: 500;
      color: $txt-aside;

      &:not(:nth-child(1)) {
        min-width: 50px;
        max-width: 100px;

        .register-field {
          min-width: 50px;
        }
      }
    }
  }

  .neuro-total {
    display: flex;
    margin-bottom: 10px;
    border: 1px solid $input-border;

    h3 {
      padding: 0 10px;
      font-size: 1.2rem;
    }

    span {
      flex: 1;
      font-size: 1.2rem;
      font-weight: 800;
      color: $logo-color;
    }
  }
}
</style>
