export function fcmax(age, protocol) {
  const formulas = {
    Default: 208 - 0.7 * age,
    Diabetes: 211 - 0.67 * age,
    Hypertension: 164 - 0.7 * age,
  };

  for (const name of Object.keys(formulas)) {
    if (protocol.includes(name)) {
      return formulas[name];
    }
  }

  return null;
}
