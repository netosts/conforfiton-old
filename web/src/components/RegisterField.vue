<script setup>
import { ref, watch, toRef } from 'vue';
import { ErrorMessage, Field, useField } from 'vee-validate';
import { maskCpf, maskRg } from '../services/validators/masks';


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
    required: true,
  },
  required: String,
  placeholder: String,
  meta: Object,
  rules: [String, Object, Array],
  options: Array,
  modelValue: [String, Number],
});

const emit = defineEmits(['update:modelValue']);
const value = ref(props.modelValue);

watch(value, (newValue) => {
  emit('update:modelValue', newValue);

  if (props.name === 'cpf') {
    handleChange(maskCpf(newValue));
  } else if (props.name === 'rg') {
    handleChange(maskRg(newValue));
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
    :class="{ 'has-error': !!errorMessage, success: !errorMessage && meta.touched && value !== '' }">
    <div class="label-span">
      <label :for="name">{{ label }} </label>
      <span class="required">{{ required }}</span>
    </div>

    <Field v-if="type === 'select'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event">
      <option v-for="option, index in options" :key="index" :value="option">{{ option }}</option>
    </Field>

    <Field v-else-if="type === 'textarea'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      rows="3" @update:model-value="value = $event" />

    <Field v-else :name="name" :id="name" :type="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event" />

    <ErrorMessage :name="name" as="p" class="error-msg" />
  </div>
</template>

<style lang="scss" scoped>
@import '../assets/styles/variables';
@import '../assets/styles/mixins';

.label-span {
  display: flex;
  align-items: center;
}

.register-field {
  @include inputContainers();

  p {
    color: $error-msg;
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
  select {
    border-color: $error-msg;
  }
}

.register-field.success {
  input {
    border-color: $validation;
  }

  .error-msg {
    color: $validation;
  }
}

.required {
  height: 1em;
  color: red;
  font-size: 1.2rem;
  margin-left: 5px;
}
</style>
