const supinoConfig = [
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

const supinoConfig2 = supinoConfig.sort((a, b) => a.threshold - b.threshold)

console.log(supinoConfig2.find(config => {
  return config.sexo === 'Masculino' && config.threshold >= 0.71
}));