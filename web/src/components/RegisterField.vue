<script setup>
import { ref, watch } from 'vue';
import { ErrorMessage, Field } from 'vee-validate';

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
  successMessage: String,
  placeholder: String,
  meta: Object,
  errorMessage: String,
  rules: [String, Object, Array],
  options: Array,
  modelValue: [String, Number],
});

const emit = defineEmits(['update:modelValue']);

const value = ref(props.modelValue);

const updatedValue = ref(false);


watch(value, (newValue, oldValue) => {
  if (props.name === 'telefone' && !newValue.match(/^(?:\+)[0-9]{2}\s?(?:\()[0-9]{2}(?:\))\s?[0-9]{4,5}(?:-)[0-9]{4}$/)) {
    updatedValue.value = true;
    return;
  } else {
    updatedValue.value = false;
  }
  if (props.name === 'telefone' && newValue.replaceAll(/[^0-9]/, '').length === 11) {
    return;
  }
  emitValue(newValue, oldValue);
});

function emitValue(newValue, oldValue) {
  emit('update:modelValue', newValue);
  updatedValue.value = oldValue.length && props.required && !newValue;
}

function verifyNull(evt) {
  if (props.name === 'email' &&
    !evt.target.value.match(/^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/)) {
    updatedValue.value = true;
  }
  if (!value.value && props.required) {
    updatedValue.value = true;
  }
}

// use `toRef` to create reactive references to `name` prop which is passed to `useField`
// this is important because vee-validte needs to know if the field name changes
// https://vee-validate.logaretm.com/v4/guide/composition-api/caveats
// const name = toRef(props, 'name');

// we don't provide any rules here because we are using form-level validation
// https://vee-validate.logaretm.com/v4/guide/validation#form-level-validation
// const {
//   value: inputValue,
//   errorMessage,
//   handleBlur,
//   handleChange,
//   meta,
// } = useField(name, undefined, {
//   initialValue: props.value,
// });
</script>

<template>
  <div class="register-field" :class="{ 'has-error': updatedValue }">
    <div class="label-span">
      <label :for="name">{{ label }} </label>
      <span class="required">{{ required }}</span>
    </div>
    <Field v-if="type === 'select'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event" @blur="verifyNull">
      <option v-for="option, index in options" :key="index" :value="option">{{ option }}</option>
    </Field>
    <Field v-else-if="type === 'textarea'" :name="name" :id="name" :as="type" :rules="rules" :placeholder="placeholder"
      rows="3" @update:model-value="value = $event" @blur="verifyNull">
    </Field>
    <Field v-else :name="name" :id="name" :type="type" :rules="rules" :placeholder="placeholder"
      @update:model-value="value = $event" @blur="verifyNull" />

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
    color: $error-msg !important;
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
    border-color: $error-msg !important;
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
