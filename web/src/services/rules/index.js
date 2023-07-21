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
