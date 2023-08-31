export function createNeuromuscularForm(exerciseList, total) {
  const currentDate = new Date();
  const formattedDate = currentDate.toISOString();
  const form = {
    total_points: total.value,
    created_at: formattedDate,
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

export function calcular1RM(pesoLevantado, reps) {
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

function calcularForcaRelativa(RM, pesoCorporal) {
  if (RM === undefined || pesoCorporal === undefined) {
    return;
  }
  return RM / pesoCorporal;
}

export function calcularPontos(student, rm, exercise, exerciseConfig) {
  if (student && rm) {
    const forcaRelativa = calcularForcaRelativa(rm, student.weight);

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
