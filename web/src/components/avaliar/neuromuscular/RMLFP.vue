<script setup>
import { RMLFPList, results } from "@/services/avaliar/neuromuscular/lists";

import { createNeuromuscularRmlForm } from "@/services/avaliar/neuromuscular/helpers";
import { postNeuromuscularRml } from "@/services/api/post";

import { useRoute } from "vue-router/auto";
import { useAvaliarStore } from "@/stores/avaliar";

import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

const route = useRoute();
const store = useAvaliarStore();

async function onSubmit() {
  try {
    const form = await createNeuromuscularRmlForm(
      store.neuromuscular_protocol,
      RMLFPList,
      results
    );

    await postNeuromuscularRml(form, route.params.id);

    sessionStorage.setItem("submitted", true);

    alert("Neuromuscular salvo com sucesso");

    // Remove Neuromuscular from the screen
    const indexToRemove = store.types.indexOf("Neuromuscular");
    store.types.splice(indexToRemove, 1);
  } catch (err) {
    console.error(err);
    throw err;
  }
}
</script>

<template>
  <Form @submit="onSubmit">
    <div class="input--grid">
      <div v-for="(item, id) in RMLFPList" :key="id">
        <TextField
          v-model="item.value"
          type="number"
          :name="item.name"
          :label="item.label"
          :span="item.span"
          rules="between:0,999"
        />
      </div>
    </div>

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
  margin: 0 20px 20px 20px;
  .input--grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;

    @include mq(l-xl) {
      grid-template-columns: 1fr 1fr;
    }

    @include mq(m) {
      grid-template-columns: 1fr;
    }

    .register-field {
      flex: 1;
    }
  }
}
</style>
