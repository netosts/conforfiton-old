import { formatAge } from "@/services/formats";

export function fcmax(birth_date, formula) {
  if (!birth_date) return null;
  const age = formatAge(birth_date);
  const formulas = {
    Default: 208 - 0.7 * age,
    Diabetes: 211 - 0.67 * age,
    Hypertension: 164 - 0.7 * age,
  };

  return Math.floor(formulas[formula]);
}

export function calculateL1(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? Math.floor(fcrepouso + 0.6 * fcreserva) : null;
}

export function calculateL2(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? Math.floor(fcrepouso + 0.85 * fcreserva) : null;
}
