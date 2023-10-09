<script setup>
import {
  countCpfDuplicateEditStudent,
  countEmailDuplicateEditStudent,
  countPhoneDuplicateEditStudent,
} from "@/services/api/get";
import { editStudent } from "@/services/api/put";

import { genderList, shirtList, shortsList } from "@/services/register/lists";
import { translateGenderToPT, translateGenderToEN } from "@/services/helpers";
import { formatCpf, formatTelefone } from "@/services/formats";

import { reactive, onMounted } from "vue";

import { definePage, useRoute, useRouter } from "vue-router/auto";

import { schema } from "@/services/student/edit/schema";
import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";

definePage({
  meta: { requiresAuth: true },
});

const props = defineProps({
  student: Object,
});

const route = useRoute();
const router = useRouter();

const form = reactive({
  name: props.student?.name,
  cpf: formatCpf(props.student?.cpf),
  phone_number: formatTelefone(props.student?.phone_number),
  email: props.student?.email,
  gender: translateGenderToPT(props.student?.gender),
  birth_date: props.student?.birth_date,
  shirt_size: props.student?.shirt_size,
  shorts_size: props.student?.shorts_size,
  height: props.student?.height,
  weight: props.student?.weight,
});

async function onSubmit(_, { setFieldError }) {
  // Transform values
  form.cpf = form.cpf.replace(/\D/g, ""); // only digits
  form.phone_number = form.phone_number.replace(/\D/g, ""); // only digits

  // CPF, Email and Phone DUPLICATE VALIDATION
  const [countedCpf, countedEmail, countedPhone] = await Promise.all([
    countCpfDuplicateEditStudent(form.cpf, route.params.id),
    countEmailDuplicateEditStudent(form.email, route.params.id),
    countPhoneDuplicateEditStudent(form.phone_number, route.params.id),
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
  try {
    const currentDate = new Date();
    const formattedDate = currentDate.toISOString();

    form.gender = translateGenderToEN(form.gender); // from pt to en
    form.created_at = formattedDate;

    await editStudent(route.params.id, form);

    alert(`${form.name} atualizado com sucesso!`);
  } catch (err) {
    console.error(err);
    throw err;
  }
}

onMounted(() => {
  if (!props.student) {
    router.push(`/student/${route.params.id}`);
  }
});
</script>

<template>
  <section>
    <Form @submit="onSubmit" class="form" :validation-schema="schema">
      <div class="form__section">
        <TextField
          v-model="form.name"
          name="name"
          type="text"
          label="Nome completo"
          placeholder="Digite seu nome completo"
        />
        <div class="form__section__1-1sm">
          <TextField
            v-model="form.cpf"
            name="cpf"
            type="text"
            label="CPF"
            placeholder="Digite seu CPF"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.phone_number"
            name="phone_number"
            type="text"
            label="Telefone"
            placeholder="(00)00000-0000"
          />
          <TextField
            v-model="form.email"
            name="email"
            type="text"
            label="Email"
            placeholder="Digite seu Email"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.birth_date"
            type="date"
            name="birth_date"
            label="Data Nascimento"
          />
          <TextField
            v-model="form.gender"
            name="gender"
            type="select"
            label="Sexo Biológico"
            :options="genderList"
          />
        </div>
        <div class="form__section__1-1">
          <TextField
            v-model="form.shirt_size"
            name="shirt_size"
            type="select"
            label="T. Camisa"
            :options="shirtList"
          />
          <TextField
            v-model="form.shorts_size"
            name="shorts_size"
            type="select"
            label="T. Shorts"
            :options="shortsList"
          />
        </div>
        <TextField
          v-model="form.height"
          name="height"
          type="number"
          label="Altura"
          span="(cm)"
          placeholder="Ex: 180"
        />
        <div class="submit">
          <button>Atualizar aluno</button>
        </div>
      </div>
    </Form>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

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

      @include mq(m) {
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

    .submit {
      display: flex;
      justify-content: flex-end;
      button {
        @include submitButtons($buttons, white);
      }
    }
  }
}
</style>
