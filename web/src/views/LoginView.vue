<script setup>
import RegisterField from '../components/RegisterField.vue';
import { Form } from 'vee-validate';
import { reactive } from 'vue';


const login = reactive({
  username: '',
  password: '',
});

const schema = {
  username: 'required|maxLength:30',
  password: 'required|password|maxLength:30'
};

function onSubmit() {
  console.log(login);
};
</script>

<template>
  <aside>
    <Form @submit="onSubmit" :validation-schema="schema" class="login">
      <div class="login__title">
        <h1>LOGIN</h1>
      </div>
      <div class="login__credentials">
        <div class="login__credentials__username">
          <RegisterField v-model="login.username" name="username" type="text" label="Usuário"
            placeholder="Digite o usuário" />
        </div>
        <div class="login__credentials__password">
          <RegisterField v-model="login.password" name="password" type="password" label="Senha"
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
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;

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