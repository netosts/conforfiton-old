// function to format the cpf number
export function formatCpf(cpf) {

  // extract the different parts of the cpf number
  const firstPart = cpf.slice(0, 3);
  const secondPart = cpf.slice(3, 6);
  const thirdPart = cpf.slice(6, 9);
  const lastPart = cpf.slice(9, 11);

  // create the formatted cpf number string
  const formattedCpfNumber = `${firstPart}.${secondPart}.${thirdPart}-${lastPart}`;

  return formattedCpfNumber;
};

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

// transform dtNascimento YYYY-MM-DD into person's age
export function formatAge(value) {
  const birthdate = value;
  const today = new Date();

  // extract the birthdate parts
  const birthdateParts = birthdate.split('-');
  const birthYear = parseInt(birthdateParts[0]);
  const birthMonth = parseInt(birthdateParts[1]);
  const birthDay = parseInt(birthdateParts[2]);

  // calculate the person's age
  let age = today.getFullYear() - birthYear;

  // check if the current month and day are before the birth month and day
  if (
    today.getMonth() < birthMonth - 1 ||
    (today.getMonth() === birthMonth - 1 && today.getDate() < birthDay)
  ) {
    age--;
  }

  return age;
};

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