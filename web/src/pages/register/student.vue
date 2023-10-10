<script setup>
import {
  countCpfDuplicate,
  countEmailDuplicate,
  countPhoneDuplicate,
} from "@/services/api/get";
import { postStudent } from "@/services/api/post";
import { genderList, shirtList, shortsList } from "@/services/register/lists";
import { translateGenderToEN } from "@/services/helpers";
import { getSecondUserIdLocal } from "@/services/api/token";

import { definePage } from "vue-router/auto";

import { schema } from "@/services/register/schemas/student";
import { form } from "@/services/register/forms/student";

import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

definePage({
  meta: { requiresAuth: true },
});

// FUNCTIONS
async function onSubmit(_, { setFieldError }) {
  // Transform values
  form.cpf = form.cpf.replace(/\D/g, ""); // only digits
  form.phone_number = form.phone_number.replace(/\D/g, ""); // only digits

  // CPF, Email and Phone DUPLICATE VALIDATION
  const [countedCpf, countedEmail, countedPhone] = await Promise.all([
    countCpfDuplicate(form.cpf),
    countEmailDuplicate(form.email),
    countPhoneDuplicate(form.phone_number),
  ]);

  let errors = 0;

  if (countedCpf > 0) {
    setFieldError("cpf", "O CPF já foi cadastrado.");
    errors++;
  }

  if (countedEmail > 0) {
    setFieldError("email", "O Email já foi cadastrado.");
    errors++;
  }

  if (countedPhone > 0) {
    setFieldError("phone_number", "O Telefone já foi cadastrado.");
    errors++;
  }

  if (errors > 0) {
    return;
  }

  // SUBMIT
  try {
    const currentDate = new Date();
    const formattedDate = currentDate.toISOString();

    const userId = getSecondUserIdLocal();

    form.gender = translateGenderToEN(form.gender); // from pt to en
    form.created_at = formattedDate;
    form.personal_id = userId;

    await postStudent(form);

    alert(`${form.name} cadastrado com sucesso!`);

    sessionStorage.removeItem("registerStudent");
    sessionStorage.setItem("submitted", true);
    router.push("/");
  } catch (err) {
    console.error(err);
    throw err;
  }
}
</script>

<template>
  <main>
    <div class="top">
      <RouterLink to="/" class="back">
        <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
      </RouterLink>
      <h1>Bem-Vindo</h1>
    </div>

    <Form
      @submit="onSubmit"
      :validation-schema="schema"
      v-slot="{ meta }"
      class="form"
    >
      <section class="form__section">
        <div class="form__section__title">
          <h2>Cadastrar Aluno sem Anamnese</h2>
        </div>
        <TextField
          v-model="form.name"
          :meta="meta"
          name="name"
          type="text"
          label="Nome completo"
          placeholder="Digite seu nome completo"
        />
        <div class="form__section__1-1sm">
          <TextField
            v-model="form.cpf"
            :meta="meta"
            name="cpf"
            type="text"
            label="CPF"
            placeholder="Digite seu CPF"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.phone_number"
            :meta="meta"
            name="phone_number"
            type="text"
            label="Telefone"
            placeholder="(00)00000-0000"
          />
          <TextField
            v-model="form.email"
            :meta="meta"
            name="email"
            type="text"
            label="Email"
            placeholder="Digite seu Email"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.birth_date"
            :meta="meta"
            type="date"
            name="birth_date"
            label="Data Nascimento"
          />
          <TextField
            v-model="form.gender"
            :meta="meta"
            name="gender"
            type="select"
            label="Sexo Biológico"
            :options="genderList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.shirt_size"
            :meta="meta"
            name="shirt_size"
            type="select"
            label="T. Camisa"
            :options="shirtList"
          />
          <TextField
            v-model="form.shorts_size"
            :meta="meta"
            name="shorts_size"
            type="select"
            label="T. Shorts"
            :options="shortsList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.height"
            :meta="meta"
            name="height"
            type="number"
            label="Altura"
            span="(cm)"
            placeholder="Ex: 180"
          />
          <TextField
            v-model="form.weight"
            :meta="meta"
            name="weight"
            type="number"
            label="Peso"
            span="(kg)"
            placeholder="Ex: 90,30"
          />
        </div>
        <SubmitButton msg="Cadastrar" :meta="meta" />
      </section>
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 30px;
  transition: 0.2s;

  @include mq(xs-s) {
    margin: 10px;
  }

  .top {
    display: flex;
    flex-direction: column;
    padding: 10px;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;
    box-shadow: $box-shadow;

    .back {
      position: absolute;
      top: 40px;
      @include tool();
      color: $buttons;

      @include mq(xs-s) {
        top: 20px;
      }
    }

    h1 {
      padding: 0 40px;
      text-align: center;
      text-transform: uppercase;
    }
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 16px;

    &__section {
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding: 16px;
      background-color: white;
      border-radius: $border-radius;
      box-shadow: $box-shadow;

      &__title {
        padding: 10px;
        margin-bottom: 10px;
        text-align: center;
        border-bottom: 3px dotted $background;

        h2 {
          color: $buttons;
        }
      }

      &__1-1 {
        display: flex;
        gap: 20px;

        @include mq(xs-s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }
      }

      &__1-1sm {
        display: flex;
        gap: 20px;

        @include mq(s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }

        &__1sm {
          flex: 1;
          display: grid;
          gap: 20px;
          grid-template-columns: 1fr 80px;

          @include mq(xs) {
            display: flex;
            flex-direction: column;
          }
        }
      }

      &__1-1-1 {
        display: flex;
        gap: 20px;

        @include mq(s) {
          flex-direction: column;
        }

        div {
          flex: 1;
        }
      }

      .q4time {
        display: flex;
        gap: 20px;

        .register-field {
          flex: 1;
        }

        &__select {
          display: flex;
          flex-direction: column;
          gap: 5px;
          flex: 1;

          select {
            @include createInput();
          }
        }
      }

      table {
        border-collapse: collapse;
        border: 1px solid $input-border;

        th,
        td {
          border: 1px solid $input-border;
          padding: 8px;
          text-align: center;
        }

        th {
          background-color: $buttons;
          color: white;
        }

        td {
          font-weight: 500;
          color: $txt-aside;
        }
      }

      .final {
        margin: 10px;
        font-weight: 500;
        text-align: center;
      }
    }
  }
}
</style>
