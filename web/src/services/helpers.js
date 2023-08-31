const genderTranslations = {
  'Masculino': 'Male',
  'Feminino': 'Female',
  'Male': 'Masculino',
  'Female': 'Feminino'
};

export function translateGender(value) {
  return genderTranslations[value] || value;
}

const daysTranslations = {
  'Domingo': 'Sunday',
  'Segunda': 'Monday',
  'Terça': 'Tuesday',
  'Quarta': 'Wednesday',
  'Quinta': 'Thursday',
  'Sexta': 'Friday',
  'Sábado': 'Saturday',
  'Sunday': 'Domingo',
  'Monday': 'Segunda',
  'Tuesday': 'Terça',
  'Wednesday': 'Quarta',
  'Thursday': 'Quinta',
  'Friday': 'Sexta',
  'Saturday': 'Sábado',
}

export function translateDays(value) {
  return daysTranslations[value] || value;
}