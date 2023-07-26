<script setup>
import { ref, watch, toRef } from 'vue';
import { ErrorMessage, Field, useField } from 'vee-validate';
import { maskName, maskCpf, maskRg, maskTelefone } from '../services/validators/masks';


const props = defineProps({
  type: {
    type: String,
    default: 'text',
  },
  name: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    required: false,
  },
  required: String,
  span: String,
  placeholder: String,
  meta: Object,
  rules: [String, Object, Array],
  options: Array,
  radios: Array,
  rows: {
    type: String,
    default: '3',
  },
  tabindex: String,
  modelValue: [String, Number],
});

const emit = defineEmits(['update:modelValue']);
const value = ref(props.modelValue);

watch(value, (newValue) => {
  emit('update:modelValue', newValue);

  if (props.name === 'name') {
    handleChange(maskName(newValue));
  } else if (props.name === 'cpf') {
    handleChange(maskCpf(newValue));
  } else if (props.name === 'rg') {
    handleChange(maskRg(newValue));
  } else if (props.name === 'telefone') {
    handleChange(maskTelefone(newValue));
  } else {
    handleChange(newValue);
  }
});

const name = toRef(props, 'name');

const {
  errorMessage,
  handleChange,
  meta,
} = useField(name);
</script>

<template>
  <div class="register-field"
    :class="{ 'has-error': !!errorMessage && meta.touched, success: !errorMessage && meta.touched && value !== '' }">
    <div class="label-span">
      <label :for="name">{{ label }} </label>
      <span class="required" v-show="!!required">{{ required }}</span>
      <span class="span" v-show="!!span">{{ span }}</span>
    </div>

    <Field v-if="type === 'select'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event" :tabindex="tabindex">
      <option v-for="option, index in options" :key="index" :value="option">{{ option }}</option>
    </Field>

    <Field v-else-if="type === 'textarea'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      :rows="rows" @update:model-value="value = $event" :tabindex="tabindex" />

    <div v-else-if="type === 'radio'" v-for="radio in radios" :key="radio" class="radio-container">
      <Field :name="name" :type="type" :id="radio.label" :rules="rules" :value="radio.value"
        @update:model-value="value = $event" />
      <label :for="radio.label">{{ radio.label }}</label>
    </div>

    <Field v-else :name="name" :id="name" :type="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event" :tabindex="tabindex" />

    <ErrorMessage :name="name" as="p" class="error-msg" v-show="meta.touched" />
  </div>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

.label-span {
  display: flex;
  align-items: center;
  flex-wrap: wrap;

  .required {
    height: 1em;
    font-size: 1.2rem;
    color: red;
    margin-left: 5px;
  }

  .span {

    font-size: 0.78rem;
    font-weight: 500;
    color: $txt-subtitle;
    margin-left: 5px;
  }
}

.register-field {
  @include inputContainers();

  p {
    color: $error-msg;
  }

  .radio-container {
    display: flex;
    gap: 5px;
    padding: 0 10px;

    label {
      font-size: 0.95rem;
      font-weight: 600;
      color: $txt-aside;
    }
  }
}

textarea {
  @include createInput();
  resize: none;
}

.error-msg {
  margin-left: 0px;
  font-size: .75rem;
}

.register-field.has-error {

  input,
  select,
  textarea {
    border-color: $error-msg;
  }
}

.register-field.success {

  input,
  select,
  textarea {
    border-color: $validation;
  }

  .error-msg {
    color: $validation;
  }
}
</style>
