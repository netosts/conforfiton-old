import { imcConfig, caConfig, rcqConfig, iacConfig, pgConfig } from "./configs";

export function calculateImc(weight, height) {
  const meters = height / 100;
  const imc = weight / meters ** 2;

  return imc.toFixed(1);
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

export function caClass(ca, gender) {
  const findClass = caConfig.reduce((closest, config) => {
    if (ca >= config.threshold && gender === config.gender) {
      if (!closest || config.threshold >= closest.threshold) {
        return config;
      }
    }
    return closest;
  }, null);

  return findClass ? findClass.classification : null;
}

export function caRisk(ca, gender) {
  const risk =
    gender === "Male" ? ca - 102 : gender === "Female" ? ca - 88 : null;

  if (!risk || risk < 1) {
    return null;
  }

  const riskTable = {
    dc: String(risk * 3) + "%",
    diabetes_ii: String(risk * 2.7) + "%",
    hypertension: String(risk * 1.8) + "%",
    cancer: String(risk * 4) + "%",
    depression: String(risk * 1.4) + "%",
    metabolic_syndrome: String(risk * 2.5) + "%",
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

export function rcaeClass(ca, height) {
  if (!ca) return null;
  const rcae = ca / height;
  return rcae > 0.5 ? "Risco elevado" : "Risco baixo";
}

export function calculateIac(hip, height) {
  const meters = height / 100;

  const iac = hip / (meters * Math.sqrt(meters)) - 18;

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

function pgConstant(cm, type) {
  const items = pgConfig
    .filter((item) => item.type === type)
    .sort((a, b) => b.threshold - a.threshold);
  const findItem = items.find((item) => cm >= item.threshold);
  return findItem ? findItem.constant : null;
}

export function calculatePg(a, b, c, gender) {
  a = pgConstant(a, "A");
  b = pgConstant(b, "B");
  c = pgConstant(c, "C");

  console.log(a, b, c, gender);

  if (a && b && c) {
    return gender === "Male"
      ? a + b - c - 10.2
      : gender === "Female"
      ? a + b - c - 19.6
      : null;
  }
}
