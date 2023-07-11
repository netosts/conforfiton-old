<script setup>
import { ref, onMounted } from 'vue';


// Variables
const bodyElement = ref(null);

// Emits
const emit = defineEmits(['isStudentDetailsActive']);

// Props
const props = defineProps({
  studentDetails: Object
});

// Functions
function closeDetails() {
  emit('isStudentDetailsActive', false);
  bodyElement.value.style.overflow = 'auto';
}

// format functions
function formatTelefone(phoneNumber) {
  const tel = phoneNumber;

  // extract the different parts of the phone number
  const ddd = tel.slice(0, 2);
  const firstPart = tel.slice(2, 7);
  const secondPart = tel.slice(7, 11);

  // create the formatted phone number string
  const formattedPhoneNumber = `(${ddd})${firstPart}-${secondPart}`;

  return formattedPhoneNumber;
};

// DOM Mount
onMounted(() => {
  bodyElement.value = document.body;
});
</script>

<template>
  <aside class="details">
    <div class="details__container" v-if="studentDetails" v-motion-slide-visible-right>
      <div class="details__container__button">
        <button @click="closeDetails">
          <font-awesome-icon icon="fa-solid fa-xmark" size="2xl" />
        </button>
      </div>
      <p>Nome do aluno: {{ studentDetails.nmPessoa }}</p>
      <p>Telefone: {{ studentDetails.telefone ? formatTelefone(studentDetails.telefone) : '' }}</p>
    </div>
  </aside>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';


.details {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;
  background-color: rgba(128, 128, 128, 0.204);

  &__container {
    position: relative;
    z-index: 999;
    margin-top: auto;
    margin-left: auto;
    border-radius: $border-radius;
    background-color: white;
    transition: .2s ease-out;
    width: 400px;
    height: 1000px;
  }
}
</style>