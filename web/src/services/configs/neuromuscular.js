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


export function calcularPontos(student, rm, exerciseConfig) {
  if (student) {
    const forcaRelativa = calcularForcaRelativa(rm, student.peso);
    for (const { sexo, threshold, pontos } of exerciseConfig) {
      if (student.sexo === sexo && forcaRelativa >= threshold) {
        return pontos;
      }
    }
  }
};

// Supino
export const supinoConfig = [
  { sexo: 'Masculino', threshold: 1.5, pontos: 10 },
  { sexo: 'Feminino', threshold: 0.9, pontos: 10 },
  { sexo: 'Masculino', threshold: 1.4, pontos: 9 },
  { sexo: 'Feminino', threshold: 0.85, pontos: 9 },
  { sexo: 'Masculino', threshold: 1.3, pontos: 8 },
  { sexo: 'Feminino', threshold: 0.8, pontos: 8 },
  { sexo: 'Masculino', threshold: 1.2, pontos: 7 },
  { sexo: 'Feminino', threshold: 0.7, pontos: 7 },
  { sexo: 'Masculino', threshold: 1.1, pontos: 6 },
  { sexo: 'Feminino', threshold: 0.65, pontos: 6 },
  { sexo: 'Masculino', threshold: 1, pontos: 5 },
  { sexo: 'Feminino', threshold: 0.6, pontos: 5 },
  { sexo: 'Masculino', threshold: 0.9, pontos: 4 },
  { sexo: 'Feminino', threshold: 0.55, pontos: 4 },
  { sexo: 'Masculino', threshold: 0.8, pontos: 3 },
  { sexo: 'Feminino', threshold: 0.5, pontos: 3 },
  { sexo: 'Masculino', threshold: 0.7, pontos: 2 },
  { sexo: 'Feminino', threshold: 0.45, pontos: 2 },
  { sexo: 'Masculino', threshold: 0.6, pontos: 1 },
  { sexo: 'Feminino', threshold: 0.35, pontos: 1 },
];

// Rosca Direta
export const roscaDiretaConfig = [
  { sexo: 'Masculino', threshold: 0.7, pontos: 10 },
  { sexo: 'Feminino', threshold: 0.5, pontos: 10 },
  { sexo: 'Masculino', threshold: 0.65, pontos: 9 },
  { sexo: 'Feminino', threshold: 0.45, pontos: 9 },
  { sexo: 'Masculino', threshold: 0.6, pontos: 8 },
  { sexo: 'Feminino', threshold: 0.42, pontos: 8 },
  { sexo: 'Masculino', threshold: 0.55, pontos: 7 },
  { sexo: 'Feminino', threshold: 0.38, pontos: 7 },
  { sexo: 'Masculino', threshold: 0.5, pontos: 6 },
  { sexo: 'Feminino', threshold: 0.35, pontos: 6 },
  { sexo: 'Masculino', threshold: 0.45, pontos: 5 },
  { sexo: 'Feminino', threshold: 0.32, pontos: 5 },
  { sexo: 'Masculino', threshold: 0.4, pontos: 4 },
  { sexo: 'Feminino', threshold: 0.28, pontos: 4 },
  { sexo: 'Masculino', threshold: 0.35, pontos: 3 },
  { sexo: 'Feminino', threshold: 0.25, pontos: 3 },
  { sexo: 'Masculino', threshold: 0.3, pontos: 2 },
  { sexo: 'Feminino', threshold: 0.21, pontos: 2 },
  { sexo: 'Masculino', threshold: 0.25, pontos: 1 },
  { sexo: 'Feminino', threshold: 0.18, pontos: 1 },
];

// Puxada Pela Frente
export const puxadaPelaFrenteConfig = [
  { sexo: 'Masculino', threshold: 1.2, pontos: 10 },
  { sexo: 'Feminino', threshold: 0.85, pontos: 10 },
  { sexo: 'Masculino', threshold: 1.15, pontos: 9 },
  { sexo: 'Feminino', threshold: 0.8, pontos: 9 },
  { sexo: 'Masculino', threshold: 1.1, pontos: 8 },
  { sexo: 'Feminino', threshold: 0.75, pontos: 8 },
  { sexo: 'Masculino', threshold: 1.05, pontos: 7 },
  { sexo: 'Feminino', threshold: 0.73, pontos: 7 },
  { sexo: 'Masculino', threshold: 1, pontos: 6 },
  { sexo: 'Feminino', threshold: 0.7, pontos: 6 },
  { sexo: 'Masculino', threshold: 0.95, pontos: 5 },
  { sexo: 'Feminino', threshold: 0.65, pontos: 5 },
  { sexo: 'Masculino', threshold: 0.9, pontos: 4 },
  { sexo: 'Feminino', threshold: 0.63, pontos: 4 },
  { sexo: 'Masculino', threshold: 0.85, pontos: 3 },
  { sexo: 'Feminino', threshold: 0.6, pontos: 3 },
  { sexo: 'Masculino', threshold: 0.8, pontos: 2 },
  { sexo: 'Feminino', threshold: 0.55, pontos: 2 },
  { sexo: 'Masculino', threshold: 0.75, pontos: 1 },
  { sexo: 'Feminino', threshold: 0.5, pontos: 1 },
];

// Leg Press
export const legPressConfig = [
  { sexo: 'Masculino', threshold: 3, pontos: 10 },
  { sexo: 'Feminino', threshold: 2.7, pontos: 10 },
  { sexo: 'Masculino', threshold: 2.8, pontos: 9 },
  { sexo: 'Feminino', threshold: 2.5, pontos: 9 },
  { sexo: 'Masculino', threshold: 2.6, pontos: 8 },
  { sexo: 'Feminino', threshold: 2.3, pontos: 8 },
  { sexo: 'Masculino', threshold: 2.4, pontos: 7 },
  { sexo: 'Feminino', threshold: 2.1, pontos: 7 },
  { sexo: 'Masculino', threshold: 2.2, pontos: 6 },
  { sexo: 'Feminino', threshold: 2, pontos: 6 },
  { sexo: 'Masculino', threshold: 2, pontos: 5 },
  { sexo: 'Feminino', threshold: 1.8, pontos: 5 },
  { sexo: 'Masculino', threshold: 1.8, pontos: 4 },
  { sexo: 'Feminino', threshold: 1.6, pontos: 4 },
  { sexo: 'Masculino', threshold: 1.6, pontos: 3 },
  { sexo: 'Feminino', threshold: 1.4, pontos: 3 },
  { sexo: 'Masculino', threshold: 1.4, pontos: 2 },
  { sexo: 'Feminino', threshold: 1.2, pontos: 2 },
  { sexo: 'Masculino', threshold: 1.2, pontos: 1 },
  { sexo: 'Feminino', threshold: 1, pontos: 1 },
];

// Extensão de Joelhos
export const extensaoDeJoelhosConfig = [
  { sexo: 'Masculino', threshold: 0.8, pontos: 10 },
  { sexo: 'Feminino', threshold: 0.7, pontos: 10 },
  { sexo: 'Masculino', threshold: 0.75, pontos: 9 },
  { sexo: 'Feminino', threshold: 0.65, pontos: 9 },
  { sexo: 'Masculino', threshold: 0.7, pontos: 8 },
  { sexo: 'Feminino', threshold: 0.6, pontos: 8 },
  { sexo: 'Masculino', threshold: 0.65, pontos: 7 },
  { sexo: 'Feminino', threshold: 0.55, pontos: 7 },
  { sexo: 'Masculino', threshold: 0.6, pontos: 6 },
  { sexo: 'Feminino', threshold: 0.52, pontos: 6 },
  { sexo: 'Masculino', threshold: 0.55, pontos: 5 },
  { sexo: 'Feminino', threshold: 0.5, pontos: 5 },
  { sexo: 'Masculino', threshold: 0.5, pontos: 4 },
  { sexo: 'Feminino', threshold: 0.45, pontos: 4 },
  { sexo: 'Masculino', threshold: 0.45, pontos: 3 },
  { sexo: 'Feminino', threshold: 0.4, pontos: 3 },
  { sexo: 'Masculino', threshold: 0.4, pontos: 2 },
  { sexo: 'Feminino', threshold: 0.35, pontos: 2 },
  { sexo: 'Masculino', threshold: 0.35, pontos: 1 },
  { sexo: 'Feminino', threshold: 0.3, pontos: 1 },
];

// Flexão de Joelhos
export const flexaoDeJoelhosConfig = [
  { sexo: 'Masculino', threshold: 0.7, pontos: 10 },
  { sexo: 'Feminino', threshold: 0.6, pontos: 10 },
  { sexo: 'Masculino', threshold: 0.65, pontos: 9 },
  { sexo: 'Feminino', threshold: 0.55, pontos: 9 },
  { sexo: 'Masculino', threshold: 0.6, pontos: 8 },
  { sexo: 'Feminino', threshold: 0.52, pontos: 8 },
  { sexo: 'Masculino', threshold: 0.55, pontos: 7 },
  { sexo: 'Feminino', threshold: 0.5, pontos: 7 },
  { sexo: 'Masculino', threshold: 0.5, pontos: 6 },
  { sexo: 'Feminino', threshold: 0.45, pontos: 6 },
  { sexo: 'Masculino', threshold: 0.45, pontos: 5 },
  { sexo: 'Feminino', threshold: 0.4, pontos: 5 },
  { sexo: 'Masculino', threshold: 0.4, pontos: 4 },
  { sexo: 'Feminino', threshold: 0.35, pontos: 4 },
  { sexo: 'Masculino', threshold: 0.35, pontos: 3 },
  { sexo: 'Feminino', threshold: 0.3, pontos: 3 },
  { sexo: 'Masculino', threshold: 0.3, pontos: 2 },
  { sexo: 'Feminino', threshold: 0.25, pontos: 2 },
  { sexo: 'Masculino', threshold: 0.25, pontos: 1 },
  { sexo: 'Feminino', threshold: 0.2, pontos: 1 },
];
