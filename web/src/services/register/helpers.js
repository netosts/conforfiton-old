const genderTranslations = {
  'Masculino': 'Male',
  'Feminino': 'Female',
};

export function translateGender(value) {
  return genderTranslations[value] || value;
}