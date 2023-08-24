// const imcClass = [
//   {classification: 'Magreza 3º', threshold: 0,},
//   {classification: 'Magreza 2º', threshold: 16,},
//   {classification: 'Magreza 1º', threshold: 17,},
//   {classification: 'Eutrofia', threshold: 18.5,},
//   {classification: 'Pré-obesidade', threshold: 25,},
//   {classification: 'Obesidade 1º', threshold: 30,},
//   {classification: 'Obesidade 2º', threshold: 35,},
//   {classification: 'Obesidade 3º', threshold: 40,}
// ]

// export function imc(peso, altura) {
//   // peso / altura²
//   // EX: 90KG / 1.80 x 1.80 = 27,27 KG/M²
//   const imc = peso / (altura**2)

//   const findImc = imcClass.reduce((closest, config) => {
//     if (imc >= config.threshold) {
//       if (!closest || config.threshold >= closest.threshold) {
//         return config;
//       }
//     }
//     return closest
//   }, null)

//   return findImc.classification
// }

// const caClass = [
//   { sexo: 'Masculino', threshold: 0 },
//   { sexo: 'Masculino', threshold: 94 },
//   { sexo: 'Masculino', threshold: 102 },
//   { sexo: 'Feminino', threshold: 0 },
//   { sexo: 'Feminino', threshold: 80 },
//   { sexo: 'Feminino', threshold: 88 },
// ]

// export function ca(value, sexo) {
//   const findCa = caClass.reduce((closest, config) => {
//     if (value >= config.threshold && sexo === config.sexo) {
//       if (!closest || config.threshold >= closest.threshold) {
//         return config;
//       }
//     }
//     return closest
//   }, null)

//   return findCa
// }

const rcqClass = [
  {sexo: 'Masculino', idade: 20, threshold: 0, classification: 'baixo'},
  {sexo: 'Masculino', idade: 20, threshold: 0.83 },
  {sexo: 'Masculino', idade: 20, threshold: 0.89 },
  {sexo: 'Masculino', idade: 20, threshold: 0.94 },
  {sexo: 'Masculino', idade: 30, threshold: 0, classification: 'baixo'},
  {sexo: 'Masculino', idade: 30, threshold: 0.84 },
  {sexo: 'Masculino', idade: 30, threshold: 0.92 },
  {sexo: 'Masculino', idade: 30, threshold: 0.96 },
  {sexo: 'Masculino', idade: 40, threshold: 0, classification: 'baixo'},
  {sexo: 'Masculino', idade: 40, threshold: 0.88 },
  {sexo: 'Masculino', idade: 40, threshold: 0.96 },
  {sexo: 'Masculino', idade: 40, threshold: 1 },
  {sexo: 'Masculino', idade: 50, threshold: 0, classification: 'baixo'},
  {sexo: 'Masculino', idade: 50, threshold: 0.9 },
  {sexo: 'Masculino', idade: 50, threshold: 0.97 },
  {sexo: 'Masculino', idade: 50, threshold: 1.02 },
  {sexo: 'Masculino', idade: 60, threshold: 0, classification: 'baixo'},
  {sexo: 'Masculino', idade: 60, threshold: 0.91 },
  {sexo: 'Masculino', idade: 60, threshold: 0.99 },
  {sexo: 'Masculino', idade: 60, threshold: 1.03 },
  {sexo: 'Feminino', idade: 20, threshold: 0, classification: 'baixo'},
  {sexo: 'Feminino', idade: 20, threshold: 0.71 },
  {sexo: 'Feminino', idade: 20, threshold: 0.78 },
  {sexo: 'Feminino', idade: 20, threshold: 0.82 },
  {sexo: 'Feminino', idade: 30, threshold: 0, classification: 'baixo'},
  {sexo: 'Feminino', idade: 30, threshold: 0.72 },
  {sexo: 'Feminino', idade: 30, threshold: 0.79 },
  {sexo: 'Feminino', idade: 30, threshold: 0.84 },
  {sexo: 'Feminino', idade: 40, threshold: 0, classification: 'baixo'},
  {sexo: 'Feminino', idade: 40, threshold: 0.73 },
  {sexo: 'Feminino', idade: 40, threshold: 0.8 },
  {sexo: 'Feminino', idade: 40, threshold: 0.87 },
  {sexo: 'Feminino', idade: 50, threshold: 0, classification: 'baixo'},
  {sexo: 'Feminino', idade: 50, threshold: 0.74 },
  {sexo: 'Feminino', idade: 50, threshold: 0.82 },
  {sexo: 'Feminino', idade: 50, threshold: 0.88 },
  {sexo: 'Feminino', idade: 60, threshold: 0, classification: 'baixo'},
  {sexo: 'Feminino', idade: 60, threshold: 0.76 },
  {sexo: 'Feminino', idade: 60, threshold: 0.84 },
  {sexo: 'Feminino', idade: 60, threshold: 0.9 },
]

export function rcq(cintura, quadril) {
  const rcq = cintura / quadril
}