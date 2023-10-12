import {
  updateTranslateMenstruation,
  translateFcMaxFormula,
} from "@/services/helpers";

const periodMapping = {
  MORNING: 1,
  AFTERNOON: 2,
  NIGHT: 3,
};

export function transformQ13(value) {
  const transformedData = value?.map((item) => {
    const periods = item.periods.map((period) => {
      if (typeof period === "string" && periodMapping[period]) {
        return periodMapping[period];
      } else if (typeof period === "number") {
        return period;
      }
      return null; // Handle invalid values
    });

    return {
      day: item.day,
      periods: periods,
    };
  });

  return transformedData ? transformedData : null;
}

export function createAnamneseForm(form) {
  const extractedValues = {
    q4: {
      training: undefined,
      time: undefined,
    },
  };
  for (const key in form) {
    if (form.hasOwnProperty(key)) {
      // Check if the property name starts with 'q4a' or 'q4b' to make a single q4 key
      if (key.startsWith("q4a") && form[key].hasOwnProperty("value")) {
        extractedValues.q4.training = form[key].value;
      } else if (key.startsWith("q4b") && form[key].hasOwnProperty("value")) {
        extractedValues.q4.time = form[key].value;
      } else if (
        key.startsWith("menstruation") &&
        form[key].hasOwnProperty("value")
      ) {
        extractedValues[key] = updateTranslateMenstruation(form[key].value);
      } else if (
        key.startsWith("fc_max_formula") &&
        form[key].hasOwnProperty("value")
      ) {
        extractedValues[key] = translateFcMaxFormula(form[key].value);
      } else if (form[key].hasOwnProperty("value")) {
        extractedValues[key] = form[key].value;
      }
    }
  }

  return extractedValues;
}
