<script setup>
import { getToken } from "../services/api/post";
import { setExpToken } from "../services/api/token";

import { definePage } from "vue-router/auto";
import { reactive } from "vue";

import TextField from "../components/TextField.vue";
import { Form } from "vee-validate";

definePage({
  beforeEnter: () => {
    const logged = localStorage.getItem("user");
    if (logged) return { path: "/" };
  },
});

const login = reactive({
  email: undefined,
  password: undefined,
});

const schema = {
  email: "required|maxLength:30",
  password: "required|password|maxLength:30",
};

async function onSubmit(_, { setErrors }) {
  try {
    // Using OAuth2PasswordRequestForm
    // data need to be in form_data format
    const payload = new FormData();
    payload.append("username", login.email);
    payload.append("password", login.password);

    const data = await getToken(payload);

    setExpToken(data.access_token, 3 * 60 * 60 * 1000); // Set expiry by milliseconds
    localStorage.setItem("user", data.user_id);

    location.reload();
  } catch (e) {
    console.error(e);
    setErrors({
      email: " ",
      password: "Usuário ou senha inválido.",
    });
  }
}
</script>

<template>
  <aside>
    <Form @submit="onSubmit" :validation-schema="schema" class="login">
      <div class="login__title">
        <h1>LOGIN</h1>
      </div>
      <div class="login__credentials">
        <div class="login__credentials__email">
          <TextField
            v-model="login.email"
            name="email"
            type="text"
            label="Email"
            placeholder="Digite o email"
          />
        </div>
        <div class="login__credentials__password">
          <TextField
            v-model="login.password"
            name="password"
            type="password"
            label="Senha"
            placeholder="Digite a senha"
          />
        </div>
      </div>
      <div class="login__buttons">
        <button type="submit" class="submit">LOGIN</button>
      </div>
    </Form>
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
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;

  @include mq(s) {
    padding: 10px;
  }

  .login {
    position: relative;
    z-index: 999;
    margin: auto;
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: 350px;

    &__title {
      text-align: center;
    }

    &__credentials {
      display: flex;
      flex-direction: column;
      gap: 10px;
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
