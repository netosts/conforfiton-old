import { cpfValidator } from "../validators/validators";

export function required(value) {
  if (
    value === undefined ||
    (typeof value === "string" && value.trim().length === 0)
  ) {
    return "Este campo é obrigatório.";
  }
  return true;
}

export function cpf(value) {
  value = value.replace(/[^\d]/g, "");

  if (!value.match(/^\d{11}$/)) {
    return "O CPF precisa ter 11 números.";
  }

  if (!cpfValidator(value)) {
    return "O CPF não é válido.";
  }
  return true;
}

export function email(value) {
  if (!value || !value.length) {
    return true;
  }

  const emailRegex =
    /(?:[a-z0-9+!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/i;
  if (!emailRegex.test(value)) {
    return "O endereço de email não é válido.";
  }

  return true;
}

export function minLength(value, limit) {
  if (!value || !value.length) {
    return true;
  }

  value = value.replace(/[^a-zA-Z0-9]/g, "");

  if (value.length < limit) {
    return `Mínimo de ${limit} caracteres.`;
  }

  return true;
}

export function maxLength(value, limit) {
  if (!value || !value.length) {
    return true;
  }

  value = value.replace(/[^a-zA-Z0-9]/g, "");

  if (value.length > limit) {
    return `Máximo de ${limit} caracteres.`;
  }

  return true;
}

export function between(value, min, max) {
  const numericValue = Number(value);
  if (numericValue < min) {
    return `O valor precisa ser maior que ${min}.`;
  }
  if (numericValue > max) {
    return `O valor precisa ser menor que ${max}.`;
  }
  return true;
}

export function password(value) {
  // Check individual requirements and return corresponding error messages
  if (value.length < 8) {
    return "A senha deve ter pelo menos 8 caracteres.";
  }

  if (!/\d/.test(value)) {
    return "A senha deve ter pelo menos 1 número.";
  }

  if (!/[a-z]/.test(value)) {
    return "A senha deve ter pelo menos 1 letra minúscula.";
  }

  if (!/[A-Z]/.test(value)) {
    return "A senha deve ter pelo menos 1 letra maiúscula.";
  }

  if (!/[!@#$%^&*]/.test(value)) {
    return "A senha deve ter pelo menos 1 símbolo especial (!@#$%^&*).";
  }

  // If all requirements are met, return a success message
  return true;
}

export function asymbol(value) {
  if (!value) {
    return true;
  }

  const regex = /^[A-Za-z0-9.,;ãáàâéèêíïóôõöúüç\s'"()\-\[\]]+$/u;
  if (!regex.test(value)) {
    return "Por favor digite apenas letras e números.";
  }

  return true;
}

export function name(value) {
  if (!value) {
    return true;
  }

  const regex = /^[A-Za-záàâãéèêíïóôõöúçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ\s~]+$/;
  if (!regex.test(value)) {
    return "Por favor digite apenas letras.";
  }

  return true;
}

// 0054-08-19
export function date(value) {
  if (!value) {
    return true;
  }

  const datePattern = /^\d{4}-\d{2}-\d{2}$/;
  if (!datePattern.test(value)) {
    return "Formato de data inválida.";
  }

  const parts = value.split("-");
  const year = parseInt(parts[0]);
  const month = parseInt(parts[1]);
  const day = parseInt(parts[2]);

  const currentDate = new Date();
  const inputDate = new Date(year, month - 1, day);

  const maxAgeDate = new Date();
  maxAgeDate.setFullYear(maxAgeDate.getFullYear() - 120); // Subtract 120 years

  if (inputDate > currentDate) {
    return "A data de nascimento não pode ser no futuro.";
  }

  if (inputDate < maxAgeDate) {
    return "A idade máxima é de 120 anos.";
  }

  return true;
}

export function distance(value) {
  if (!value) {
    return true;
  }
  const numericValue = Number(value);
  if (numericValue < 0 || numericValue > 10000) {
    return "Distância até 10.000 metros.";
  }
  return true;
}

export function bpm(value) {
  if (!value) {
    return true;
  }
  const numericValue = Number(value);
  if (numericValue < 0 || numericValue > 220) {
    return "Máximo 220 batimentos por minuto.";
  }
  return true;
}

export function time(value) {
  if (!value) {
    return true;
  }
  const numericValue = Number(value);
  if (numericValue < 0 || numericValue > 60) {
    return "Máximo 60 minutos percorridos.";
  }
  return true;
}
