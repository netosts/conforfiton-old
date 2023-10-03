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

const periodsTranslations = {
  MORNING: "Manhã",
  AFTERNOON: "Tarde",
  NIGHT: "Noite",
};

export function translatePeriods(value) {
  return periodsTranslations[value] || value;
}

const menstruationTranslations = {
  "Sim, menstruo regularmente": true,
  "Não, não menstruo": false,
  "Prefiro não responder": null,
};

export function translateMenstruation(value) {
  return menstruationTranslations[value] || value;
}
