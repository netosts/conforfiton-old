import {
  imcConfig,
  caConfig,
  rcqConfig,
  iacConfig,
  pgMaleConfig,
  pgFemaleConfig,
  pgConfigElder,
  pgConfig,
  filterConfig,
} from "./configs";

export function createAntropometriaForm(
  weight,
  evaluatedAt,
  antropometria_protocol,
  antropometriaList,
  results
) {
  const form = {
    weight,
    antropometria_protocol,
    created_at: evaluatedAt,
  };

  const extractedValues = antropometriaList.map((proxy) => proxy.value);
  const extractedNames = antropometriaList.map((proxy) => proxy.name);

  for (const [index, value] of extractedNames.entries()) {
    form[value] = extractedValues[index];
  }

  Object.keys(results).map((key) => {
    form[key] = results[key];
  });

  return form;
}

export function calculateImc(weight, height) {
  const meters = height / 100;
  const imc = weight / meters ** 2;

  return imc.toFixed(2);
}

export function imcClass(imc) {
  if (!imc) return null;
  const findClass = imcConfig.reduce((closest, config) => {
    if (imc >= config.threshold) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

export function caClass(abs, gender) {
  const findClass = caConfig.reduce((closest, config) => {
    if (abs >= config.threshold && gender === config.gender) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

export function caRisk(abs, gender) {
  const risk =
    gender === "Male" ? abs - 102 : gender === "Female" ? abs - 88 : null;

  if (!risk || risk < 1) {
    return null;
  }

  const riskTable = {
    dc: (risk * 3).toFixed(1),
    diabetes_ii: (risk * 2.7).toFixed(1),
    hypertension: (risk * 1.8).toFixed(1),
    cancer: (risk * 4.0).toFixed(1),
    depression: (risk * 1.4).toFixed(1),
    metabolic_syndrome: (risk * 2.5).toFixed(1),
  };

  return riskTable;
}

export function calculateRcq(waist, hip) {
  if (waist === undefined || hip === undefined) {
    return;
  }
  return (waist / hip).toFixed(2);
}

export function rcqClass(rcq, gender, age) {
  if (!rcq) return null;
  const findClass = rcqConfig.reduce((closest, config) => {
    if (
      gender === config.gender &&
      age >= config.age &&
      rcq >= config.threshold
    ) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

export function calculateRcae(abs, height) {
  if (!abs) return null;
  return (abs / height).toFixed(2);
}

export function rcaeClass(rcae) {
  if (!rcae) return null;
  return rcae > 0.5 ? "Risco elevado" : "Risco baixo";
}

export function calculateIac(hip, height) {
  const meters = height / 100;

  const iac = hip / meters ** 2 - 18;

  return iac > 0 ? iac.toFixed(2) : null;
}

export function iacClass(iac, gender) {
  const findClass = iacConfig.reduce((closest, config) => {
    if (iac >= config.threshold && gender === config.gender) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

function pgConstantMale(cm, type) {
  const items = pgMaleConfig
    .filter((item) => item.type === type)
    .sort((a, b) => b.threshold - a.threshold);
  const findItem = items.find((item) => cm >= item.threshold);
  return findItem ? findItem.constant : null;
}

function pgConstantFemale(cm, type) {
  const items = pgFemaleConfig
    .filter((item) => item.type === type)
    .sort((a, b) => b.threshold - a.threshold);
  const findItem = items.find((item) => cm >= item.threshold);
  return findItem ? findItem.constant : null;
}

export function calculatePg(rightBiceps, abs, rightForearm, thighs, gender) {
  let a,
    b,
    c = null;
  if (gender === "Male") {
    a = pgConstantMale(rightBiceps, "A");
    b = pgConstantMale(abs, "B");
    c = pgConstantMale(rightForearm, "C");
  } else if (gender === "Female") {
    a = pgConstantFemale(abs, "A");
    b = pgConstantFemale(thighs, "B");
    c = pgConstantFemale(rightForearm, "C");
  }

  if (a && b && c) {
    const result =
      gender === "Male"
        ? a + b - c - 10.2
        : gender === "Female"
        ? a + b - c - 19.6
        : 0;

    return result > 0 ? result.toFixed(1) : "Abaixo de 0";
  }
}

export function weltman(abs, weight, height, gender) {
  const male = 0.31457 * abs - 0.10969 * weight + 10.8336;
  const female = 0.11077 * abs - 0.17666 * height + 0.187 * weight + 51.03301;

  return gender === "Male"
    ? male.toFixed(1)
    : gender === "Female"
    ? female.toFixed(1)
    : null;
}

export function jacksonPollock3(
  chest,
  abs,
  thighs,
  triceps,
  suprailiac,
  age,
  gender,
  formula
) {
  let density;
  if (gender === "Male") {
    density =
      1.10938 -
      0.0008267 * (chest + abs + thighs) +
      0.0000016 * (chest + abs + thighs) ** 2 -
      0.0002574 * age;
  } else if (gender === "Female") {
    density =
      1.0994992 -
      0.0009929 * (triceps + suprailiac + thighs) +
      0.0000023 * (triceps + suprailiac + thighs) ** 2 -
      0.0001392 * age;
  } else {
    return null;
  }

  const siri = (4.95 / density - 4.5) * 100;
  const brozek = (5.47 / density - 4.142) * 100;

  return formula === "Siri"
    ? siri.toFixed(1)
    : formula === "Brozek"
    ? brozek.toFixed(1)
    : null;
}

export function falkner(triceps, subscapularis, suprailiac, abs) {
  const calculus = (triceps + subscapularis + suprailiac + abs) * 0.153 + 5.783;
  return calculus > 0 ? calculus.toFixed(1) : null;
}

export function jacksonPollock7(
  chest,
  midaxillary,
  triceps,
  subscapularis,
  abs,
  suprailiac,
  thighs,
  age,
  gender,
  formula
) {
  let density;
  if (gender === "Male") {
    density =
      1.112 -
      0.00043499 *
        (chest +
          midaxillary +
          triceps +
          subscapularis +
          abs +
          suprailiac +
          thighs) +
      0.00000055 *
        (chest +
          midaxillary +
          triceps +
          subscapularis +
          abs +
          suprailiac +
          thighs) **
          2 -
      0.00028826 * age;
  } else if (gender === "Female") {
    density =
      1.097 -
      0.00046971 *
        (chest +
          midaxillary +
          triceps +
          subscapularis +
          abs +
          suprailiac +
          thighs) +
      0.00000056 *
        (chest +
          midaxillary +
          triceps +
          subscapularis +
          abs +
          suprailiac +
          thighs) **
          2 -
      0.00012828 * age;
  }

  const siri = (4.95 / density - 4.5) * 100;
  const brozek = (5.47 / density - 4.142) * 100;

  return formula === "Siri"
    ? siri.toFixed(1)
    : formula === "Brozek"
    ? brozek.toFixed(1)
    : null;
}

export function pgClass(pg, gender, age) {
  const config = age >= 60 ? pgConfigElder : pgConfig;
  const items = config
    .filter((item) => item.gender === gender)
    .sort((a, b) => b.threshold - a.threshold);
  const findItem = items.find((item) => pg >= item.threshold);
  return findItem ? findItem.classification : null;
}

export function idoso3Dobras(triceps, subscapularis, suprailiac) {
  return triceps && subscapularis && suprailiac
    ? (triceps + subscapularis + suprailiac).toFixed(1)
    : null;
}

export function idosoTranWeltman(
  abs,
  hip,
  iliac_circumference,
  weight,
  height,
  age,
  gender
) {
  const male =
    -47.371817 +
    0.57914807 * abs +
    0.25189114 * hip +
    0.21366088 * iliac_circumference -
    0.35595404 * weight;
  const female =
    1.168297 -
    0.002824 * abs +
    0.0000122098 * abs ** 2 -
    0.000733128 * hip +
    0.000510477 * height -
    0.000216161 * age;

  return gender === "Male"
    ? male.toFixed(1)
    : gender === "Female"
    ? female.toFixed(1)
    : null;
}

export function filterShow(gender, area, storeProtocol) {
  if (!storeProtocol) return null;
  const filteredConfig = filterConfig.filter(
    (item) => item.gender === gender && item.area === area
  )[0];

  if (filteredConfig) {
    return filteredConfig.protocols.some((item) =>
      storeProtocol.includes(item)
    );
  }
  return false;
}

export function calculateMig(pg) {
  return pg ? (100 - pg).toFixed(1) : null;
}

export function calculateFatWeight(weight, pg) {
  return pg ? ((pg / 100) * weight).toFixed(2) : null;
}

export function calculateMigWeight(weight, mig) {
  return mig ? ((mig / 100) * weight).toFixed(2) : null;
}

export function calculateWeightGoal(fatWeight, fatWeightGoal, weight) {
  const exceededFatWeight = fatWeight - fatWeightGoal;
  return exceededFatWeight ? (weight - exceededFatWeight).toFixed(2) : null;
}

export function calculateMigGoal(pgGoal) {
  return pgGoal ? 100 - pgGoal : null;
}

export function calculateFatWeightGoal(pgGoal, weight) {
  return pgGoal ? ((pgGoal / 100) * weight).toFixed(2) : null;
}

export function calculateMigWeightGoal(fatWeightGoal, weight) {
  return fatWeightGoal ? weight - fatWeightGoal : null;
}

// export function sumSkinFolds(
//   chest,
//   abdominal,
//   thighs,
//   triceps,
//   suprailiac,
//   subscapularis,
//   midaxillary
// ) {
//   const sum =
//     chest +
//     abdominal +
//     thighs +
//     triceps +
//     suprailiac +
//     subscapularis +
//     midaxillary;
//   return sum ? sum : null;
// }

// export function calculatePeripheralAdiposity(biceps, triceps) {

// }
// export function calculateCentralAdiposity() {

// }
