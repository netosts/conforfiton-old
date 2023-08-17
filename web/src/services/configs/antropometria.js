const imcClass = [
  {classification: 'Magreza 3º', threshold: 0,},
  {classification: 'Magreza 2º', threshold: 16,},
  {classification: 'Magreza 1º', threshold: 17,},
  {classification: 'Eutrofia', threshold: 18.5,},
  {classification: 'Pré-obesidade', threshold: 25,},
  {classification: 'Obesidade 1º', threshold: 30,},
  {classification: 'Obesidade 2º', threshold: 35,},
  {classification: 'Obesidade 3º', threshold: 40,}
]

export function imc(peso, altura) {
  // peso / altura²
  // EX: 90KG / 1.80 x 1.80 = 27,27 KG/M²
  const imc = peso / (altura**2)

  const findImc = imcClass.reduce((closest, config) => {
    if (imc >= config.threshold) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest
  }, null)

  return findImc.classification
}
