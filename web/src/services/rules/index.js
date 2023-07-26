import { cpfValidator } from '../validators/validators';


export function required(value) {
  if (!value || (typeof value === 'string' && value.trim().length === 0)) {
    return 'Este campo é obrigatório';
  }
  return true;
}


export function cpf(value) {
  value = value.replace(/[^\d]/g, '');

  if (!value.match(/^\d{11}$/)) {
    return 'O CPF precisa ter 11 números.';
  }

  if (!cpfValidator(value)) {
    return 'O CPF não é válido.';
  }
  return true;
}


export function email(value) {
  if (!value || !value.length) {
    return true;
  }

  const emailRegex = /(?:[a-z0-9+!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/i;
  if (!emailRegex.test(value)) {
    return 'O endereço de email não é válido.';
  }

  return true;
}


export function minLength(value, limit) {
  if (!value || !value.length) {
    return true;
  }

  value = value.replace(/[^a-zA-Z0-9]/g, '');

  if (value.length < limit) {
    return `Mínimo de ${limit} caracteres.`;
  }

  return true;
}


export function maxLength(value, limit) {
  if (!value || !value.length) {
    return true;
  }

  value = value.replace(/[^a-zA-Z0-9]/g, '');

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
};


export function maxDecimal(value, limit) {
  if (!value) {
    return true;
  }
  
  const decimalRegex = new RegExp(`^\\d+(\\.\\d{1,${limit}})?$`);

  if (!decimalRegex.test(value)) {
    return `Máximo de ${limit} casas decimais.`
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

  const regex = /^[A-Za-z0-9.,;ãáàâéèêíïóôõöúüç\s'"\(\)]+$/u;
  if (!regex.test(value)) {
    return "Por favor digite apenas letras e números.";
  }

  return true;
}
