// function to format the telefone number
export function formatTelefone(value) {
  const match = value.match(/^(\d{2})(\d{5})(\d{4})$/);
  if (match) {
    return `(${match[1]})${match[2]}-${match[3]}`;
  }
  return value;
};

// function to format the altura value
export function formatAltura(value) {
  const match = value.match(/^(\d{3})$/)
  if (match) {
    return `${match[0]}cm`;
  }
  return value;
}

// cpf validator
export function cpfValidator(value) {
  var sum = 0;
  var rest;
  var duplicate = 0;

  for (let i = 1; i < value.length; i++) {
    if (value[i] == value[i - 1]) {
      duplicate++;
    }
    if (duplicate === 9) {
      return false
    }
  }

  for (let i = 1; i <= 9; i++) {
    sum += parseInt(value.substring(i - 1, i)) * (11 - i);
  }

  rest = (sum * 10) % 11;
  if ((rest == 10) || (rest == 11)) {
    rest = 0;
  }
  if (rest != parseInt(value.substring(9, 10))) {
    return false;
  }

  sum = 0;

  for (let i = 1; i <= 10; i++) {
    sum += parseInt(value.substring(i - 1, i)) * (12 - i);
  }

  rest = (sum * 10) % 11;
  if ((rest == 10) || (rest == 11)) {
    rest = 0;
  }
  if (rest != parseInt(value.substring(10, 11))) {
    return false;
  }

  return true;
};