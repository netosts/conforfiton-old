<script setup>
import {
  countCpfDuplicate,
  countEmailDuplicate,
  countPhoneDuplicate,
} from "@/services/api/get";
import { postStudent, uploadPhoto } from "@/services/api/post";
import { genderList, shirtList, shortsList } from "@/services/register/lists";
import { translateGenderToEN } from "@/services/helpers";
import { getSecondUserIdLocal } from "@/services/api/token";

import { definePage, useRouter } from "vue-router/auto";
import { ref } from "vue";

import { schema } from "@/services/register/schemas/student";
import { form } from "@/services/register/forms/student";

import { Form } from "vee-validate";
import TextField from "@/components/TextField.vue";
import SubmitButton from "@/components/SubmitButton.vue";

definePage({
  meta: { requiresAuth: true },
});

const router = useRouter();
const photoTooltip = ref(false);
const fileInput = ref(null);
const photoSrc = ref(null);
const pictureFormData = new FormData();

async function fileChange(event) {
  fileInput.value = event.target.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(fileInput.value);
  reader.onload = (e) => {
    photoSrc.value = e.target.result;
  };
  pictureFormData.append("file", fileInput.value, fileInput.value.name);
}

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

    const uploadedPhoto = await uploadPhoto(pictureFormData);
    form.address_picture = uploadedPhoto;

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
    <Form
      @submit="onSubmit"
      :validation-schema="schema"
      v-slot="{ meta }"
      class="form"
    >
      <section class="form__section">
        <div class="form__section__title">
          <RouterLink to="/" class="back">
            <font-awesome-icon icon="fa-solid fa-angles-left" size="xl" />
          </RouterLink>
          <h1>Cadastrar Aluno sem Anamnese</h1>
        </div>
        <div class="form__section__photo">
          <div class="form__section__photo__input">
            <div class="form__section__photo__input__image">
              <img
                @click="fileInput.click()"
                @mouseover="photoTooltip = true"
                @mouseleave="photoTooltip = false"
                :src="photoSrc ? photoSrc : '/img/default-profile-picture.jpg'"
              />
              <input
                type="file"
                accept="image/*"
                ref="fileInput"
                class="hidden"
                @change="fileChange"
              />
              <Transition name="fade">
                <div
                  class="form__section__photo__input__image--tooltip"
                  v-show="photoTooltip"
                >
                  <span>Selecionar Imagem</span>
                </div>
              </Transition>
            </div>
            <span class="form__section__photo__input--text">Foto do Aluno</span>
          </div>
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

        .back {
          position: absolute;
          top: 20px;
          left: 10px;
          @include tool();
          color: $buttons;
        }

        h1 {
          padding: 0 30px;
          margin-bottom: 10px;
          color: $buttons;
        }
      }

      &__photo {
        &__input {
          position: relative;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 10px;
          &__image {
            position: relative;
            img {
              border: 8px solid $profile-pic;
              border-radius: 50%;
              width: 90px;
              height: 90px;
              cursor: pointer;
            }
            &--tooltip {
              position: absolute;
              z-index: 2;
              top: 28px;
              right: -150px;
              height: 30px;
              border-radius: $border-radius;
              background-color: rgb(80, 80, 80);
              span {
                position: relative;
                z-index: 2;
                padding: 10px;
                font-size: 12px;
                color: rgb(240, 240, 240);
              }
              &::before {
                content: "";
                position: absolute;
                z-index: 1;
                top: 5px;
                left: -2px;
                width: 20px;
                height: 20px;
                background-color: rgb(80, 80, 80);
                transform: rotate(45deg);
              }
            }
          }
          &--text {
            font-size: 14px;
            font-weight: 500;
            color: $txt-title;
          }
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.hidden {
  visibility: hidden;
  position: absolute;
}
</style>
