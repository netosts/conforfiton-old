<script setup>
import {
  countCpfDuplicate,
  countEmailDuplicate,
  countPhoneDuplicate,
} from "@/services/api/get";
import { genderList, shirtList, shortsList } from "@/services/register/lists";

import { definePage, useRouter } from "vue-router/auto";

import { schema } from "@/services/register/schemas/student";
import { form } from "@/services/register/forms/student";

import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES
const router = useRouter();

// FUNCTIONS
async function onSubmit(_, { setFieldError }) {
  // Transform values
  const digitsCpf = form.cpf.replace(/\D/g, ""); // only digits
  const digitsPhone = form.phone_number.replace(/\D/g, ""); // only digits

  // CPF, Email and Phone DUPLICATE VALIDATION
  const [countedCpf, countedEmail, countedPhone] = await Promise.all([
    countCpfDuplicate(digitsCpf),
    countEmailDuplicate(form.email),
    countPhoneDuplicate(digitsPhone),
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
  // Save informations in session storage
  try {
    sessionStorage.setItem("registerStudent", JSON.stringify(form));
    router.push("/register/anamnese");
  } catch (err) {
    console.error(err);
    throw err;
  }
}

function onReset() {
  try {
    sessionStorage.removeItem("registerStudent");
    location.reload();
  } catch (e) {
    console.error(e);
    throw e;
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
          <h2>Preencha as Informações de Cadastro</h2>
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
        <div class="submitbox">
          <button type="button" class="reset" @click="onReset">
            <font-awesome-icon icon="fa-solid fa-rotate-right" size="xl" />
            Reiniciar
          </button>
          <div
            class="submitbox__submit"
            :class="{
              'submitbox__submit--disabled': meta ? !meta.valid : null,
            }"
          >
            <button type="submit" class="submitbox__submit__btn">
              Continuar
              <font-awesome-icon icon="fa-solid fa-angles-right" size="xl" />
            </button>
          </div>
        </div>
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
    }

    h1 {
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

      .submitbox {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 20px;

        &__submit {
          display: flex;

          @include mq(xs) {
            flex: 1;
          }

          &__btn {
            @include submitButtons($buttons, white);
            @include mq(xs) {
              flex: 1;
            }
          }

          &--disabled {
            opacity: 0.5;
            cursor: not-allowed;

            .submitbox__submit__btn {
              pointer-events: none;
            }
          }
        }

        .reset {
          @include submitButtons($profile-pic, $txt-title);
          @include mq(xs) {
            flex: 1;
          }
        }
      }
    }
  }
}
</style>
