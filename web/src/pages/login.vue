<script setup>
import http from '../services/api/http';
import { getToken } from '../services/api/post';

import { useAuthStore } from '../stores/auth';

import { definePage } from 'vue-router/auto';
import { reactive } from 'vue';

import TextField from '../components/TextField.vue';
import { Form } from 'vee-validate';


definePage({
  beforeEnter: () => {
    const logged = localStorage.getItem('user')
    if (logged) return { path: '/' };
  }
});

const auth = useAuthStore();

const login = reactive({
  username: undefined,
  password: undefined,
});

const schema = {
  username: 'required|maxLength:30',
  password: 'required|password|maxLength:30'
};

async function onSubmit(values, { setErrors }) {
  try {
    // Using OAuth2PasswordRequestForm
    // data need to be in form_data format
    const payload = new FormData()
    payload.append('username', login.username);
    payload.append('password', login.password);
    const data = await getToken(http, payload);
    auth.setExpToken(data.access_token, 60 * 1000);
    auth.setUser(data.user_id);
    location.reload();
  } catch {
    setErrors({
      'username': ' ',
      'password': 'Usuário ou senha inválido.'
    });
  };
};

function bt() {
  console.log(auth.user);
}
</script>

<template>
  <aside>
    <pre><button @click="bt"> BT</button></pre>
    <Form @submit="onSubmit" :validation-schema="schema" class="login">
      <div class="login__title">
        <h1>LOGIN</h1>
      </div>
      <div class="login__credentials">
        <div class="login__credentials__username">
          <TextField v-model="login.username" name="username" type="text" label="Usuário"
            placeholder="Digite o usuário" />
        </div>
        <div class="login__credentials__password">
          <TextField v-model="login.password" name="password" type="password" label="Senha"
            placeholder="Digite a senha" />
        </div>
      </div>
      <div class="login__buttons">
        <button type="submit" class="submit">LOGIN</button>
      </div>
    </Form>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';


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