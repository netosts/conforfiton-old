<script setup>
import { repsList, exerciseList, pontosTotal } from "@/services/configs/lists";
import { Form } from "vee-validate";
import TextField from "../TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

function onSubmit(values) {
  console.log(values);
}
</script>

<template>
  <section>
    <Form @submit="onSubmit">
      <h2 class="avaliar--title">Antropometria</h2>
      <table class="neuro-table">
        <thead>
          <tr>
            <th>Exercício</th>
            <th>Peso L.</th>
            <th>Reps</th>
            <th>1RM</th>
            <th>Pontos</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="exercise in exerciseList" :key="exercise">
            <td>{{ exercise.title }}</td>
            <td>
              <TextField
                v-model="exercise.pesoLevantado"
                :name="`${exercise.name}PesoLevantado`"
                type="number"
              />
            </td>
            <td>
              <TextField
                v-model="exercise.reps"
                :name="`${exercise.name}Reps`"
                type="select"
                :options="repsList"
              />
            </td>
            <td>{{ exercise.rm }}</td>
            <td>{{ exercise.pontos }}</td>
          </tr>
        </tbody>
      </table>

      <div class="neuro-total">
        <h3>Total:</h3>
        <span>{{ pontosTotal }}</span>
      </div>

      <div class="submit--btn">
        <SubmitButton msg="Salvar" />
      </div>
    </Form>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";

section {
  display: flex;
  flex-direction: column;
  gap: 20px;

  form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;

    h2 {
      padding: 10px;
      border-bottom: 1px solid $input-border;
      text-align: center;
      color: $txt-title;
    }

    .neuro-table {
      margin: 0px 10px;
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
      margin: 0 10px 10px 10px;
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

    .submit--btn {
      margin: 10px;
      margin-top: -5px;
    }
  }
}
</style>
