import {
  fcmax,
  l1reserva,
  l2reserva,
  l1EllestadConconi,
  l2EllestadConconi,
  vo2maxCooper,
  vvo2maxCooper,
  vo2maxWeltman,
  vl1Weltman,
  vl2Weltman,
  vvo2maxWeltman,
  vo2maxActive,
  vo2maxInactive,
  vo2maxBicycle,
  formatPace,
  elderAerobicPower,
  vo2maxAbsolute,
  vo2maxMets,
  weeklyCaloricExpenditure,
  dailyCaloricExpenditure,
} from "./helpers";

import { reactive, computed } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

const form = reactive({
  fc_repouso: {
    value: undefined,
    name: "fc_repouso",
    label: "FC Repouso",
    show: computed(() => store.cardio_protocol?.includes("L1L2Zona")),
  },
  l1: {
    value: undefined,
    name: "l1",
    label: "L1",
    span: "(bpm)",
    show: computed(() => store.cardio_protocol?.includes("EllestadConconi")),
  },
  l2: {
    value: undefined,
    name: "l2",
    label: "L2",
    span: "(bpm)",
    show: computed(() => store.cardio_protocol?.includes("EllestadConconi")),
  },
  distance: {
    value: store.cardio_protocol?.includes("Weltman") ? 3200 : undefined,
    name: "distance",
    label: "Distância",
    span: "(metros)",
    show: computed(
      () =>
        store.cardio_protocol?.includes("Cooper") ||
        store.cardio_protocol === "Elder"
    ),
  },
  time: {
    value: undefined,
    name: "time",
    label: "Tempo percorrido",
    span: "(minutos)",
    show: computed(
      () =>
        store.cardio_protocol?.includes("Weltman") ||
        store.cardio_protocol?.includes("Active") ||
        store.cardio_protocol?.includes("Inactive")
    ),
  },
  fc_5min: {
    value: undefined,
    name: "fc_5min",
    label: "FC do 5º Minuto",
    span: "(bpm)",
    show: computed(() => store.cardio_protocol?.includes("Bicycle")),
  },
});

export const cardioList = computed(() => {
  return Object.values(form).filter((item) => item.show);
});

export const results = reactive({
  fc_max: computed(() => fcmax(store.student?.age, store.cardio_protocol)),
  l1: computed(() => {
    if (store.cardio_protocol?.includes("L1L2Zona")) {
      return l1reserva(results.fc_max, form.fc_repouso.value);
    } else if (store.cardio_protocol?.includes("EllestadConconi")) {
      return form.l1.value;
    }
  }),
  l2: computed(() => {
    if (store.cardio_protocol?.includes("L1L2Zona")) {
      return l2reserva(results.fc_max, form.fc_repouso.value);
    } else if (store.cardio_protocol?.includes("EllestadConconi")) {
      return form.l2.value;
    }
  }),
  l1_fc_max_percentage: computed(() =>
    store.cardio_protocol?.includes("EllestadConconi")
      ? l1EllestadConconi(results.fc_max, form.l1.value)
      : null
  ),
  l2_fc_max_percentage: computed(() =>
    store.cardio_protocol?.includes("EllestadConconi")
      ? l2EllestadConconi(results.fc_max, form.l2.value)
      : null
  ),
  vo2max: computed(() => {
    if (store.cardio_protocol?.includes("Cooper")) {
      return vo2maxCooper(form.distance.value);
    } else if (store.cardio_protocol?.includes("Weltman")) {
      return vo2maxWeltman(form.time.value);
    } else if (store.cardio_protocol?.includes("Active")) {
      return vo2maxActive(form.time.value, store.student?.gender);
    } else if (store.cardio_protocol?.includes("Inactive")) {
      return vo2maxInactive(form.time.value);
    } else if (store.cardio_protocol?.includes("Bicycle")) {
      return vo2maxBicycle(form.fc_5min.value);
    }
  }),
  vo2max_absolute: computed(() =>
    vo2maxAbsolute(results.vo2max, store.student?.weight)
  ),
  vo2max_mets: computed(() => vo2maxMets(results.vo2max)),
  vvo2max: computed(() => {
    if (store.cardio_protocol?.includes("Cooper")) {
      return vvo2maxCooper(form.distance.value);
    } else if (store.cardio_protocol?.includes("Weltman")) {
      return vvo2maxWeltman(form.time.value);
    }
  }),
  vvo2max_pace: computed(() => formatPace(results.vvo2max)),
  vl1: computed(() =>
    store.cardio_protocol?.includes("Weltman")
      ? vl1Weltman(form.time.value)
      : null
  ),
  vl1_pace: computed(() =>
    store.cardio_protocol?.includes("Weltman") ? formatPace(results.vl1) : null
  ),
  vl2: computed(() =>
    store.cardio_protocol?.includes("Weltman")
      ? vl2Weltman(form.time.value)
      : null
  ),
  vl2_pace: computed(() =>
    store.cardio_protocol?.includes("Weltman") ? formatPace(results.vl2) : null
  ),
  elder_aerobic_power: computed(() =>
    store.cardio_protocol === "Elder"
      ? elderAerobicPower(
          store.student?.gender,
          store.student?.age,
          form.distance.value
        )
      : null
  ),
  weekly_caloric_expenditure: computed(() =>
    weeklyCaloricExpenditure(store.student?.weight)
  ),
  daily_caloric_expenditure: computed(() =>
    dailyCaloricExpenditure(store.student?.weight)
  ),
});

export const fcmaxList = [
  { id: "default", value: "Default", label: "Padrão" },
  { id: "diabetes", value: "Diabetes", label: "Diabetes" },
  { id: "hypertension", value: "Hypertension", label: "Hipertensão" },
];

export const l1l2List = [
  { id: "zona", value: "L1L2Zona", label: "Zona por FC Reserva" },
  {
    id: "EllestadConconi",
    value: "EllestadConconi",
    label: "Percentual FC Max [Ellestad & Conconi]",
  },
];

export const vo2maxList = [
  { id: "cooper", value: "Cooper", label: "Teste de Cooper" },
  { id: "weltman", value: "Weltman", label: "Teste de Weltman" },
  { id: "active", value: "Active", label: "Ellestad Adultos Ativos" },
  {
    id: "inactive",
    value: "Inactive",
    label: "Ellestad Adultos Iniciantes/Inativos",
  },
  { id: "bicycle", value: "Bicycle", label: "Bicicleta FOX 5min" },
];

export const renameProtocol = computed(() => {
  if (store.cardio_protocol === "Elder") {
    return "Potência Aeróbica em Idosos";
  }

  let fcmaxLabel,
    l1l2Label,
    vo2maxLabel = null;
  for (const item of fcmaxList) {
    if (store.cardio_protocol?.includes(item.value)) {
      fcmaxLabel = item.label;
    }
  }
  for (const item of l1l2List) {
    if (store.cardio_protocol?.includes(item.value)) {
      l1l2Label = item.label;
    }
  }
  for (const item of vo2maxList) {
    if (store.cardio_protocol?.includes(item.value)) {
      vo2maxLabel = item.label;
    }
  }
  return fcmaxLabel && l1l2Label
    ? `${fcmaxLabel} + ${l1l2Label} + ${vo2maxLabel}`
    : "Sem Protocolo";
});
