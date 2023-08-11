<script setup>
import { ufList, sexoList, camisaList } from "../../services/configs/lists";

import { reactive } from "vue";
import { definePage } from "vue-router/auto";

import { Form } from "vee-validate";
import TextField from "../../components/TextField.vue";
import SubmitButton from "../../components/SubmitButton.vue";

definePage({
  meta: { requiresAuth: true },
});

// VARIABLES

// Form variables
const form = reactive({
  nm_pessoa: "",
  ser: "Aluno",
  tipo_pessoa: "PF",
  cpf_cnpj: "",
  rg: "",
  uf_rg: "",
  emp_personal: false,
  dt_nascimento: "",
  ds_obs: "",
  ds_email: "",
  telefone: "",
  altura: "",
  sexo: "",
  tm_camisa: "",
  foto_aluno: null,
  id_empresa: 1,
  id_personal: 2,
  peso: "",
  dt_data: "",
});

// Validation schema
const schema = {
  name: "required|maxLength:100",
  cpf: "required|cpf|maxLength:11",
  rg: "maxLength:20",
  telefone: "minLength:11|maxLength:11",
  email: "required|email|maxLength:80",
  sexo: "required",
  camisa: "required",
  altura: "required|between:0,250|maxDecimal:1",
  peso: "required|between:0,600|maxDecimal:2",
  ds_obs: "maxLength:300",
};

// FUNCTIONS
async function onSubmit(values, { setFieldError, setErrors }) {
  console.log("CRIANDO ALUNO...");

  let errors = 0;

  // CPF Duplicate validation
  form.cpf_cnpj = form.cpf_cnpj.replace(/\D/g, ""); // only digits
  const countedCpf = await countCpfDuplicate(form.cpf_cnpj);
  if (countedCpf > 0) {
    setFieldError("cpf", "O CPF já foi cadastrado.");
    errors++;
  }

  // RG and UF must be together
  if (
    (form.rg !== "" && form.uf_rg === "") ||
    (form.uf_rg !== "" && form.rg === "")
  ) {
    setErrors({
      rg: "O RG e UF precisam ser cadastrados juntos.",
      uf: " ",
    });
    errors++;
  } else if (form.rg !== "" && form.uf_rg !== "") {
    // RG in UF Duplicate validation
    const countedRgUf = await countRgUfDuplicate(form.rg, form.uf_rg);
    if (countedRgUf > 0) {
      setFieldError("rg", `O RG já foi cadastrado em ${form.uf_rg}.`);
      errors++;
    }
  }

  // Email duplicate validation
  const countedEmail = await countEmailDuplicate(form.ds_email);
  if (countedEmail > 0) {
    setFieldError("email", "Este email já foi cadastrado.");
    errors++;
  }

  if (errors > 0) {
    // only proceed without errors
    return;
  }

  // Get the current date and time and use as dt_data
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  // Format problematic values before posting
  form.dt_data = formattedDate;
  form.rg = form.rg.replace(/\D/g, ""); // only digits
  form.telefone = form.telefone.replace(/\D/g, ""); // only digits

  // Post new student
  postStudent(form);
}
</script>

<template>
  <main>
    <div class="top">
      <RouterLink to="/" class="voltar">
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
          <h2>Informações de Cadastro</h2>
        </div>
        <TextField
          v-model="form.nm_pessoa"
          :meta="meta"
          name="name"
          type="text"
          label="Nome completo"
          required="*"
          placeholder="Digite o nome do aluno"
        />
        <div class="form__section__1-1sm">
          <TextField
            v-model="form.cpf_cnpj"
            :meta="meta"
            name="cpf"
            type="text"
            label="CPF"
            required="*"
            placeholder="Digite o CPF do aluno"
          />
          <div class="form__section__1-1sm__1sm">
            <TextField
              v-model="form.rg"
              :meta="meta"
              name="rg"
              type="text"
              label="RG"
              placeholder="Digite o RG do aluno"
            />
            <TextField
              v-model="form.uf_rg"
              :meta="meta"
              name="uf"
              type="select"
              label="UF"
              :options="ufList"
            />
          </div>
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.telefone"
            :meta="meta"
            name="telefone"
            type="text"
            label="Telefone"
            placeholder="(00)00000-0000"
          />
          <TextField
            v-model="form.ds_email"
            :meta="meta"
            name="email"
            type="text"
            label="E-mail"
            required="*"
            placeholder="Digite o Email do aluno"
          />
        </div>
        <div class="form__section__1-1-1">
          <div class="form__section__1-1-1__date">
            <label for="date">Data Nascimento</label>
            <input v-model="form.dt_nascimento" type="date" id="date" />
          </div>
          <TextField
            v-model="form.sexo"
            :meta="meta"
            name="sexo"
            type="select"
            label="Sexo Biológico"
            required="*"
            :options="sexoList"
          />
          <TextField
            v-model="form.tm_camisa"
            :meta="meta"
            name="camisa"
            type="select"
            label="T. Camisa"
            required="*"
            :options="camisaList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.altura"
            :meta="meta"
            name="altura"
            type="number"
            label="Altura(cm)"
            required="*"
            placeholder="Ex: 180"
          />
          <TextField
            v-model="form.peso"
            :meta="meta"
            name="peso"
            type="number"
            label="Peso(kg)"
            required="*"
            placeholder="Ex: 90,30"
          />
        </div>
        <TextField
          v-model="form.ds_obs"
          :meta="meta"
          name="dsObs"
          type="textarea"
          label="Observação"
          placeholder="Digite aqui se tiver alguma observação"
        />
      </section>

      <div class="form__section">
        <SubmitButton msg="Concluir" :reset="true" :meta="meta" />
      </div>
    </Form>
  </main>
</template>

<style lang="scss" scoped>
@import "../../assets/styles/variables";
@import "../../assets/styles/mixins";

main {
  display: flex;
  flex-direction: column;
  gap: 16px;

  .top {
    display: flex;
    flex-direction: column;
    padding: 10px;
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;
    color: $txt-aside;
    box-shadow: $box-shadow;

    .voltar {
      position: absolute;
      top: 12px;
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

        div {
          flex: 1;
        }
      }

      &__1-1sm {
        display: flex;
        gap: 20px;

        @include mq(m) {
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
        }
      }

      &__1-1-1 {
        display: flex;
        gap: 20px;

        div {
          flex: 1;
        }

        &__date {
          @include inputContainers();
        }
      }
    }
  }
}
</style>
