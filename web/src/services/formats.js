export function formatCpf(cpf) {
  if (!cpf) return null;
  // Extract the different parts of the cpf number
  const firstPart = cpf.slice(0, 3);
  const secondPart = cpf.slice(3, 6);
  const thirdPart = cpf.slice(6, 9);
  const lastPart = cpf.slice(9, 11);

  // Create the formatted cpf number string
  const formattedCpfNumber = `${firstPart}.${secondPart}.${thirdPart}-${lastPart}`;

  return formattedCpfNumber;
}

export function formatTelefone(value) {
  if (!value) return null;
  const match = value.match(/^(\d{2})(\d{5})(\d{4})$/);
  if (match) {
    return `(${match[1]})${match[2]}-${match[3]}`;
  }
  return value;
}

export function formatAltura(value) {
  if (!value) return null;
  const match = value.match(/^(\d{3})$/);
  if (match) {
    return `${match[0]}cm`;
  }
  return value;
}

export function cmToMeters(value) {
  if (!value) return null;
  value = value.toString();
  const firstPart = value.slice(0, 1);
  const secondPart = value.slice(1);
  return `${firstPart}.${secondPart}`;
}

// transform date YYYY-MM-DD into person's age
export function formatAge(value) {
  if (!value) return null;
  const birthdate = value;
  const today = new Date();

  // Extract the birthdate parts
  const birthdateParts = birthdate.split("-");
  const birthYear = parseInt(birthdateParts[0]);
  const birthMonth = parseInt(birthdateParts[1]);
  const birthDay = parseInt(birthdateParts[2]);

  // Calculate the person's age
  let age = today.getFullYear() - birthYear;

  // Check if the current month and day are before the birth month and day
  if (
    today.getMonth() < birthMonth - 1 ||
    (today.getMonth() === birthMonth - 1 && today.getDate() < birthDay)
  ) {
    age--;
  }

  return age;
}

export function formatDate(inputDate) {
  const date = new Date(inputDate);
  const options = { day: "numeric", month: "long", year: "numeric" };
  const formattedDate = date.toLocaleDateString("pt-BR", options);

  return formattedDate;
}
