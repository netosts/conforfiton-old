const genderTranslationsToPT = {
  Male: "Masculino",
  Female: "Feminino",
};

const genderTranslationsToEN = {
  Masculino: "Male",
  Feminino: "Female",
};

export function translateGenderToPT(value) {
  return genderTranslationsToPT[value] || value;
}

export function translateGenderToEN(value) {
  return genderTranslationsToEN[value] || value;
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
  "Prefiro não responder": undefined,
};

export function translateMenstruation(value) {
  return menstruationTranslations[value];
}

const fcMaxFormulaTranslations = {
  Padrão: "Default",
  Diabéticos: "Diabetes",
  Hipertensos: "Hypertension",
};

export function translateFcMaxFormula(value) {
  return fcMaxFormulaTranslations[value] || value;
}

const fcMaxFormulaUntranslations = {
  Default: "Padrão",
  Diabetes: "Diabéticos",
  Hypertension: "Hipertensos",
};

export function untranslateFcMaxFormula(value) {
  return fcMaxFormulaUntranslations[value] || value;
}

export function untranslateMenstruation(value) {
  if (value === true) {
    return "Sim, menstrua regularmente";
  } else if (value === false) {
    return "Não, não menstrua";
  } else if (value === null) {
    return "Prefere não responder";
  } else {
    return value;
  }
}

const updateMenstruationTranslations = {
  "Sim, menstrua regularmente": true,
  "Não, não menstrua": false,
  "Prefere não responder": undefined,
};

export function updateTranslateMenstruation(value) {
  return updateMenstruationTranslations[value];
}
