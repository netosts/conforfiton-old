import {
  exerciseConfig,
  sitUpConfig,
  pushUpConfig,
  jumpConfig,
  neuromuscularConfig,
} from "./configs";

export function createNeuromuscularForm(
  evaluatedAt,
  neuromuscular_protocol,
  exerciseList,
  total,
  classification
) {
  const form = {
    neuromuscular_protocol,
    total_points: total.value,
    classification,
    created_at: evaluatedAt,
  };
  const properties = ["lifted", "reps", "rm", "points"];

  for (const exercise of exerciseList) {
    for (const item of properties) {
      const propName = exercise.name + "_" + item;
      const propValue = exercise[item];
      form[propName] = propValue;
    }
  }

  return form;
}

export function createNeuromuscularRmlForm(
  evaluatedAt,
  neuromuscular_protocol,
  RMLFPList,
  results
) {
  const form = {
    neuromuscular_protocol,
    created_at: evaluatedAt,
  };

  Object.values(RMLFPList).map((item) => {
    form[item.name] = item.value;
  });

  Object.keys(results).map((key) => {
    form[key] = results[key];
  });

  return form;
}

export function calcular1RMZona(pesoLevantado, reps) {
  const table = {
    1: 100,
    2: 95,
    3: 93,
    4: 90,
    5: 87,
    6: 85,
    7: 83,
    8: 80,
    9: 77,
    10: 75,
    11: 70,
    12: 67,
    15: 65,
  };

  if (pesoLevantado === undefined || reps === undefined) {
    return;
  }

  return Number(((pesoLevantado * 100) / table[reps]).toFixed(1));
}

export function calcularRMEpley(reps, lifted) {
  if (!reps || !lifted) return;
  return (0.0333 * reps * lifted + lifted).toFixed(1);
}

function calcularForcaRelativa(RM, pesoCorporal) {
  if (RM === undefined || pesoCorporal === undefined) {
    return;
  }
  return RM / pesoCorporal;
}

export function calcularPontos(weight, rm, exercise) {
  if (rm) {
    const forcaRelativa = calcularForcaRelativa(rm, weight);

    const findConfig = exerciseConfig.reduce((closestConfig, config) => {
      if (config.exercise === exercise && forcaRelativa >= config.threshold) {
        if (!closestConfig || config.threshold >= closestConfig.threshold) {
          return config;
        }
      }
      return closestConfig;
    }, null);

    return findConfig ? findConfig.points : 0;
  }
}

export function sitUpClass(gender, age, sit_up) {
  const ageRangeStart = age - 5;
  const ageRangeEnd = age + 5;
  const filteredItems = sitUpConfig
    .filter((item) => item.gender === gender)
    .filter((item) => item.age >= ageRangeStart && item.age <= ageRangeEnd);
  const findItem = filteredItems
    .sort((a, b) => b.threshold - a.threshold)
    .find((item) => sit_up >= item.threshold);
  return findItem ? findItem.classification : null;
}

export function pushUpClass(gender, age, push_up) {
  const ageRangeStart = age - 5;
  const ageRangeEnd = age + 5;
  const filteredItems = pushUpConfig
    .filter((item) => item.gender === gender)
    .filter((item) => item.age >= ageRangeStart && item.age <= ageRangeEnd);
  const findItem = filteredItems
    .sort((a, b) => b.threshold - a.threshold)
    .find((item) => push_up >= item.threshold);
  return findItem ? findItem.classification : null;
}

export function jumpClass(gender, age, jump) {
  const ageGroups = [
    { minAge: 11, maxAge: 12 },
    { minAge: 13, maxAge: 14 },
    { minAge: 15, maxAge: Infinity },
  ];
  const matchedAgeGroup = ageGroups.find(
    (group) => age >= group.minAge && age <= group.maxAge
  );
  const filteredItems = jumpConfig
    .filter((item) => item.gender === gender)
    .filter(
      (item) =>
        item.age >= matchedAgeGroup.minAge && item.age <= matchedAgeGroup.maxAge
    );
  const findItem = filteredItems
    .sort((a, b) => b.threshold - a.threshold)
    .find((item) => jump >= item.threshold);
  return findItem ? findItem.classification : null;
}

export function neuromuscularClass(totalPoints) {
  const findItem = neuromuscularConfig
    .sort((a, b) => b.threshold - a.threshold)
    .find((item) => totalPoints.value >= item.threshold);
  return findItem ? findItem.classification : null;
}
