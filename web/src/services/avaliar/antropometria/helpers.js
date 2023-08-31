const imcConfig = [
  {classification: 'Magreza 3º', threshold: 0,},
  {classification: 'Magreza 2º', threshold: 16,},
  {classification: 'Magreza 1º', threshold: 17,},
  {classification: 'Eutrofia', threshold: 18.5,},
  {classification: 'Pré-obesidade', threshold: 25,},
  {classification: 'Obesidade 1º', threshold: 30,},
  {classification: 'Obesidade 2º', threshold: 35,},
  {classification: 'Obesidade 3º', threshold: 40,}
]

export function calculateImc(weight, height) {
  const meters = height / 100
  const imc = weight / (meters**2)

  return imc.toFixed(1)
}

export function imcClass(imc) {
  if (!imc) return null
  const findClass = imcConfig.reduce((closest, config) => {
    if (imc >= config.threshold) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest
  }, null)

  return findClass ? findClass.classification : null;
}

const caConfig = [
  { gender: 'Male', threshold: 0 },
  { gender: 'Male', threshold: 94 },
  { gender: 'Male', threshold: 102 },
  { gender: 'Female', threshold: 0 },
  { gender: 'Female', threshold: 80 },
  { gender: 'Female', threshold: 88 },
]

export function ca(value, gender) {
  const findCa = caConfig.reduce((closest, config) => {
    if (value >= config.threshold && gender === config.gender) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest
  }, null)

  return findCa
}

const rcqConfig = [
  {gender: 'Male', age: 20, threshold: 0, classification: 'Baixo'},
  {gender: 'Male', age: 20, threshold: 0.83, classification: 'Moderado' },
  {gender: 'Male', age: 20, threshold: 0.89, classification: 'Alto' },
  {gender: 'Male', age: 20, threshold: 0.94, classification: 'Muito Alto' },
  {gender: 'Male', age: 30, threshold: 0, classification: 'Baixo'},
  {gender: 'Male', age: 30, threshold: 0.84, classification: 'Moderado' },
  {gender: 'Male', age: 30, threshold: 0.92, classification: 'Alto' },
  {gender: 'Male', age: 30, threshold: 0.96, classification: 'Muito Alto' },
  {gender: 'Male', age: 40, threshold: 0, classification: 'Baixo'},
  {gender: 'Male', age: 40, threshold: 0.88, classification: 'Moderado' },
  {gender: 'Male', age: 40, threshold: 0.96, classification: 'Alto' },
  {gender: 'Male', age: 40, threshold: 1, classification: 'Muito Alto' },
  {gender: 'Male', age: 50, threshold: 0, classification: 'Baixo'},
  {gender: 'Male', age: 50, threshold: 0.9, classification: 'Moderado' },
  {gender: 'Male', age: 50, threshold: 0.97, classification: 'Alto' },
  {gender: 'Male', age: 50, threshold: 1.02, classification: 'Muito Alto' },
  {gender: 'Male', age: 60, threshold: 0, classification: 'Baixo'},
  {gender: 'Male', age: 60, threshold: 0.91, classification: 'Moderado' },
  {gender: 'Male', age: 60, threshold: 0.99, classification: 'Alto' },
  {gender: 'Male', age: 60, threshold: 1.03, classification: 'Muito Alto' },
  {gender: 'Female', age: 20, threshold: 0, classification: 'Baixo'},
  {gender: 'Female', age: 20, threshold: 0.71, classification: 'Moderado' },
  {gender: 'Female', age: 20, threshold: 0.78, classification: 'Alto' },
  {gender: 'Female', age: 20, threshold: 0.82, classification: 'Muito Alto' },
  {gender: 'Female', age: 30, threshold: 0, classification: 'Baixo'},
  {gender: 'Female', age: 30, threshold: 0.72, classification: 'Moderado' },
  {gender: 'Female', age: 30, threshold: 0.79, classification: 'Alto' },
  {gender: 'Female', age: 30, threshold: 0.84, classification: 'Muito Alto' },
  {gender: 'Female', age: 40, threshold: 0, classification: 'Baixo'},
  {gender: 'Female', age: 40, threshold: 0.73, classification: 'Moderado' },
  {gender: 'Female', age: 40, threshold: 0.8, classification: 'Alto' },
  {gender: 'Female', age: 40, threshold: 0.87, classification: 'Muito Alto' },
  {gender: 'Female', age: 50, threshold: 0, classification: 'Baixo'},
  {gender: 'Female', age: 50, threshold: 0.74, classification: 'Moderado' },
  {gender: 'Female', age: 50, threshold: 0.82, classification: 'Alto' },
  {gender: 'Female', age: 50, threshold: 0.88, classification: 'Muito Alto' },
  {gender: 'Female', age: 60, threshold: 0, classification: 'Baixo'},
  {gender: 'Female', age: 60, threshold: 0.76, classification: 'Moderado' },
  {gender: 'Female', age: 60, threshold: 0.84, classification: 'Alto' },
  {gender: 'Female', age: 60, threshold: 0.9, classification: 'Muito Alto' },
]

export function calculateRcq(waist, hip) {
  if (waist === undefined || hip === undefined) {
    return ;
  }
  return (waist / hip).toFixed(2);
}

export function rcqClass(rcq, gender, age) {
  if (!rcq) return null;
  const findClass = rcqConfig.reduce((closest, config) => {
    if ((gender === config.gender && age >= config.age) && rcq >= config.threshold) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null)

  return findClass ? findClass.classification : null;
}