// CPF Validator
export function cpfValidator(value) {
  // Only accept digits [^]=negates
  value = value.replace(/[^\d]/g, '');

  if (value.length > 11) {  // Don't accept over length
    return false;
  }

  var sum = 0;
  var rest;
  var duplicate = 0;

  for (let i = 1; i < value.length; i++) {  // Ex: 111.111.111-11 return false
    if (value[i] == value[i - 1]) {
      duplicate++;
    }
    if (duplicate === 9) {
      return false
    }
  }

  // Start validation
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

// Date of birth validator
export function dateValidator(dateOfBirth) {
  // Check if the date is in correct format
  const regex = /^\d{4}-\d{2}-\d{2}$/;
  if (!regex.test(dateOfBirth)) {
    return false;
  }
  // Check if the date is in the past
  const now = new Date();
  const birthDate = new Date(dateOfBirth);
  if (birthDate > now) {
    return false;
  }

  // The date is valid
  return true;
};