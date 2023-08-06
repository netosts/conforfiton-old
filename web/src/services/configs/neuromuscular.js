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
  }

  if (pesoLevantado === undefined || reps === undefined) {
    return ;
  }

  return Number((pesoLevantado * 100 / table[reps]).toFixed(1));
};


function calcularForcaRelativa(RM, pesoCorporal) {
  if (RM === undefined || pesoCorporal === undefined) {
    return ;
  }
  return RM / pesoCorporal;
};


export function calcularPontos(student, rm, exercise, exerciseConfig) {
  if (student && rm) {
    const forcaRelativa = calcularForcaRelativa(rm, student.peso);

    const sortedConfig = exerciseConfig.sort((a, b) => a.threshold - b.threshold);

    const findConfig = sortedConfig.reduce((closestConfig, config) => {
      if (config.exercicio === exercise && forcaRelativa >= config.threshold) {
        if (!closestConfig || config.threshold > closestConfig.threshold) {
          return config;
        }
      }
      return closestConfig;
    }, null);

    return findConfig ? findConfig.pontos : null;
  }
};
