const genderTranslations = {
  Masculino: "Male",
  Feminino: "Female",
  Male: "Masculino",
  Female: "Feminino",
};

export function translateGender(value) {
  return genderTranslations[value] || value;
}

const roleTranslations = {
  Aluno: "Student",
  Student: "Aluno",
  Guest: "Hóspede",
  Hóspede: "Guest",
};

export function translateRole(value) {
  return roleTranslations[value] || value;
}

const daysTranslations = {
  Domingo: "Sunday",
  Segunda: "Monday",
  Terça: "Tuesday",
  Quarta: "Wednesday",
  Quinta: "Thursday",
  Sexta: "Friday",
  Sábado: "Saturday",
  Sunday: "Domingo",
  Monday: "Segunda",
  Tuesday: "Terça",
  Wednesday: "Quarta",
  Thursday: "Quinta",
  Friday: "Sexta",
  Saturday: "Sábado",
};

export function translateDays(value) {
  return daysTranslations[value] || value;
}

export function formatDate(inputDate) {
  const date = new Date(inputDate);
  const options = { day: "numeric", month: "long", year: "numeric" };
  const formattedDate = date.toLocaleDateString("pt-BR", options);

  return formattedDate;
}
