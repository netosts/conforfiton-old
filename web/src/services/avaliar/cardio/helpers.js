import { elderAerobicPowerConfig } from "./configs";

export function createCardioForm(weight, cardio_protocol, cardioList, results) {
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  const form = {
    weight,
    cardio_protocol,
    created_at: formattedDate,
  };

  const extractedValues = cardioList.map((proxy) => proxy.value);
  const extractedNames = cardioList.map((proxy) => proxy.name);

  for (const [index, value] of extractedNames.entries()) {
    form[value] = extractedValues[index];
  }

  Object.keys(results).map((key) => {
    form[key] = results[key];
  });

  return form;
}

export function fcmax(age, protocol) {
  if (!protocol) return null;
  const formulas = {
    Default: 208 - 0.7 * age,
    Diabetes: 211 - 0.67 * age,
    Hypertension: 164 - 0.7 * age,
  };

  for (const name of Object.keys(formulas)) {
    if (protocol.includes(name)) {
      return Math.floor(formulas[name]);
    }
  }
}

export function l1reserva(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? fcrepouso + 0.6 * fcreserva : null;
}

export function l2reserva(fcmax, fcrepouso) {
  const fcreserva = fcmax - fcrepouso;
  return fcrepouso ? fcrepouso + 0.85 * fcreserva : null;
}

export function l1EllestadConconi(fcmax, l1) {
  return l1 ? ((l1 * 100) / fcmax).toFixed(1) : null;
}

export function l2EllestadConconi(fcmax, l2) {
  return l2 ? ((l2 * 100) / fcmax).toFixed(1) : null;
}

export function vo2maxCooper(distance) {
  return distance ? ((distance - 504.1) / 44.9).toFixed(1) : null;
}
export function vvo2maxCooper(distance) {
  return distance ? ((distance / 12) * 0.06).toFixed(2) : null;
}

export function vo2maxWeltman(time) {
  return time ? (118.4 - 4.774 * time).toFixed(1) : null;
}

export function vvo2maxWeltman(time) {
  return time ? ((498 - 18.84 * time) * 0.06).toFixed(2) : null;
}

export function vl1Weltman(time) {
  return time ? ((497.3 - 21.56 * time) * 0.06).toFixed(2) : null;
}

export function vl2Weltman(time) {
  return time ? ((509.5 - 20.82 * time) * 0.06).toFixed(2) : null;
}

export function vo2maxActive(time, gender) {
  let result = null;
  if (gender === "Male") {
    result = 8.33 + 2.94 * time;
  } else if (gender === "Female") {
    result = 8.05 + 2.74 * time;
  }
  return result ? result.toFixed(1) : null;
}

export function vo2maxInactive(time) {
  return time ? (4.46 + 3.933 * time).toFixed(1) : null;
}

export function vo2maxBicycle(fc5min) {
  return fc5min ? (6300 - 19.26 * fc5min).toFixed(1) : null;
}

export function formatPace(kmh) {
  if (kmh) {
    const pace = 60 / kmh;
    const minutes = Math.floor(pace);
    const seconds = Math.round((pace - minutes) * 60);
    return `${minutes}.${seconds}`;
  }
  return null;
}

export function elderAerobicPower(gender, age, distance) {
  if (!distance) return null;
  const findClass = elderAerobicPowerConfig.reduce((closest, config) => {
    if (
      gender === config.gender &&
      age >= config.age &&
      distance >= config.threshold
    ) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

export function vo2maxAbsolute(vo2max, weight) {
  return vo2max ? ((vo2max * weight) / 1000).toFixed(1) : null;
}

export function vo2maxMets(vo2max) {
  return vo2max ? (vo2max / 3.5).toFixed(1) : null;
}

export function weeklyCaloricExpenditure(weight) {
  return weight ? Math.floor((weight * 2000) / 70) : null;
}

export function dailyCaloricExpenditure(weight) {
  return weight ? Math.floor((weight * 300) / 70) : null;
}
