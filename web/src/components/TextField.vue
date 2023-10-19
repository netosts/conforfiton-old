<script setup>
import { ref, watch, toRef } from "vue";
import { ErrorMessage, Field, useField } from "vee-validate";
import { maskCpf, maskTelefone } from "../services/validators/masks";

const props = defineProps({
  type: {
    type: String,
    default: "text",
  },
  name: {
    type: String,
    required: true,
  },
  label: String,
  required: String,
  span: String,
  placeholder: String,
  meta: Object,
  options: Array,
  checked: String,
  radios: Array,
  rows: {
    type: String,
    default: "3",
  },
  tabindex: String,
  modelValue: [String, Number, Boolean, Object],
  rules: [String, Object],
});

const emit = defineEmits(["update:modelValue"]);
const value = ref(props.modelValue);

watch(value, (newValue) => {
  emit("update:modelValue", newValue);

  if (props.name === "cpf") {
    handleChange(maskCpf(newValue));
  } else if (props.name === "phone_number") {
    handleChange(maskTelefone(newValue));
  } else {
    handleChange(newValue);
  }
});

const name = toRef(props, "name");

const { errorMessage, handleChange, meta } = useField(name);
</script>

<template>
  <div
    class="register-field"
    :class="{
      'has-error': !!errorMessage && meta.touched,
      success: !errorMessage && meta.touched && value,
    }"
  >
    <div class="label-span">
      <label :for="name">{{ label }} </label>
      <span class="required" v-show="!!required">{{ required }}</span>
      <span class="span" v-show="!!span">{{ span }}</span>
    </div>

    <div v-if="type === 'select'" class="select-field">
      <Field
        :name="name"
        :value="value"
        @update:model-value="value = $event"
        :tabindex="tabindex"
        v-slot="{ field }"
      >
        <select v-bind="field" :id="name">
          <option
            v-for="(option, index) in options"
            :key="index"
            :value="option"
          >
            {{ option }}
          </option>
        </select>
      </Field>
    </div>

    <Field
      v-else-if="type === 'textarea'"
      :value="value"
      @update:model-value="value = $event"
      :name="name"
      :tabindex="tabindex"
      :rules="rules"
      v-slot="{ field }"
    >
      <textarea
        v-bind="field"
        :id="name"
        :placeholder="placeholder"
        :rows="rows"
      ></textarea>
    </Field>

    <div
      v-else-if="type === 'radio'"
      v-for="radio in radios"
      :key="radio"
      class="radio-container"
    >
      <Field
        :name="name"
        :type="type"
        :id="name + radio.label"
        :rules="rules"
        :value="radio.value"
        @update:model-value="value = $event"
      />
      <label :for="name + radio.label">{{ radio.label }}</label>
    </div>

    <Field
      v-else
      :value="value"
      @update:model-value="value = $event"
      :name="name"
      :tabindex="tabindex"
      :rules="rules"
      v-slot="{ field }"
    >
      <input
        v-bind="field"
        :type="type"
        :id="name"
        :placeholder="placeholder"
      />
    </Field>

    <ErrorMessage :name="name" as="p" class="error-msg" v-show="meta.touched" />
  </div>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";
@import "../assets/styles/mixins";

input,
select,
textarea {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

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

  .select-field {
    position: relative;
    @include inputContainers();

    select {
      background-color: white;
    }

    &::after {
      content: "\0025BC";
      font: normal normal normal 12px/1 FontAwesome;
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      color: $txt-title;
      pointer-events: none;
    }
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
  font-size: 0.75rem;
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
