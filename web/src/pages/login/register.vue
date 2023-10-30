<script setup>
import { definePage } from "vue-router/auto";
import { reactive } from "vue";

import TextField from "@/components/TextField.vue";
import { Form } from "vee-validate";

definePage({
  beforeEnter: () => {
    const logged = localStorage.getItem("user");
    if (logged) return { path: "/" };
  },
});

const form = reactive({
  name: undefined,
  cpf: undefined,
  gender: undefined,
  role: undefined,
  email: undefined,
  phone_number: undefined,
  birth_date: undefined,
  shirt_size: undefined,
  shorts_size: undefined,
  address_picture: undefined,
  company_id: undefined,
  cref: undefined,
  status: undefined,
});

const schema = {
  name: "required|maxLength:100|name",
  cpf: "required|cpf|maxLength:11",
  phone_number: "required|minLength:11|maxLength:11",
  email: "required|email|maxLength:255",
  birth_date: "required|date",
  gender: "required",
  shirt_size: "required",
  shorts_size: "required",
};

async function onSubmit(_, { setErrors }) {
  try {
    console.log(form);
  } catch (e) {
    console.error(e);
  }
}
</script>

<template>
  <aside>
    <Form @submit="onSubmit" :validation-schema="schema" class="register">
      <div class="register__title">
        <RouterLink to="/login" class="back">
          <font-awesome-icon icon="fa-solid fa-chevron-left" size="xl" />
        </RouterLink>
        <h1>CADASTRO</h1>
      </div>
      <div class="register__credentials">
        <TextField
          v-model="form.name"
          :meta="meta"
          name="name"
          type="text"
          label="Nome completo"
          placeholder="Digite seu nome completo"
        />
        <div class="register__credentials__1-1sm">
          <TextField
            v-model="form.cpf"
            :meta="meta"
            name="cpf"
            type="text"
            label="CPF"
            placeholder="Digite seu CPF"
          />
        </div>
        <div class="register__credentials__1-1">
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
        <div class="register__credentials__1-1">
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
        <div class="register__credentials__1-1">
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
      </div>
      <div class="register__buttons">
        <button type="submit" class="submit">Cadastrar</button>
      </div>
    </Form>
  </aside>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

aside {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;

  @include mq(s) {
    padding: 10px;
  }

  .register {
    position: relative;
    z-index: 999;
    margin: auto;
    display: flex;
    flex-direction: column;
    gap: 30px;
    padding: 16px;
    background-color: white;
    border-radius: $border-radius;
    box-shadow: $box-shadow;

    &__title {
      padding: 0 40px;
      text-align: center;

      .back {
        position: absolute;
        top: 11px;
        left: 6px;
        @include tool();
        color: $buttons;
      }
    }

    &__credentials {
      display: flex;
      flex-direction: column;
      gap: 10px;

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
    }

    &__buttons {
      display: flex;

      .submit {
        flex: 1;
        @include submitButtons($sidebar, white);
      }
    }
  }
}
</style>
