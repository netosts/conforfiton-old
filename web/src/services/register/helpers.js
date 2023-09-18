import { formatAge } from "@/services/formats";

export function fcmax(birth_date, diabetes, hypertension) {
  if (!birth_date) return null;
  const age = formatAge(birth_date);
  const formulas = {
    default: 208 - 0.7 * age,
    diabetes: 211 - 0.67 * age,
    hypertension: 164 - 0.7 * age,
  };

  if (diabetes) {
    return Math.floor(formulas.diabetes);
  } else if (hypertension) {
    return Math.floor(formulas.hypertension);
  } else {
    return Math.floor(formulas.default);
  }
}

export function calculateL1(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? Math.floor(fcrepouso + 0.6 * fcreserva) : null;
}

export function calculateL2(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? Math.floor(fcrepouso + 0.85 * fcreserva) : null;
}
