import {
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
  l1_ellestad_conconi: {
    value: undefined,
    name: "l1_ellestad_conconi",
    label: "L1",
    span: "(bpm)",
    show: computed(
      () =>
        store.cardio_protocol === "EllestadActive" ||
        store.cardio_protocol === "EllestadInactive"
    ),
  },
  l2_ellestad_conconi: {
    value: undefined,
    name: "l2_ellestad_conconi",
    label: "L2",
    span: "(bpm)",
    show: computed(
      () =>
        store.cardio_protocol === "EllestadActive" ||
        store.cardio_protocol === "EllestadInactive"
    ),
  },
  distance: {
    value: store.cardio_protocol === "Weltman" ? 3200 : undefined,
    name: "distance",
    label: "Distância",
    span: "(metros)",
    show: computed(
      () =>
        store.cardio_protocol === "Cooper" || store.cardio_protocol === "Elder"
    ),
  },
  time: {
    value: undefined,
    name: "time",
    label: "Tempo percorrido",
    span: "(minutos)",
    show: computed(
      () =>
        store.cardio_protocol === "Weltman" ||
        store.cardio_protocol === "EllestadActive" ||
        store.cardio_protocol === "EllestadInactive"
    ),
  },
  fc_5min: {
    value: undefined,
    name: "fc_5min",
    label: "FC do 5º Minuto",
    span: "(bpm)",
    show: computed(() => store.cardio_protocol === "Bicycle"),
  },
});

export const cardioList = computed(() => {
  return Object.values(form).filter((item) => item.show);
});

export const results = reactive({
  l1_fc_max_percentage: computed(() => {
    if (
      store.cardio_protocol === "EllestadActive" ||
      store.cardio_protocol === "EllestadInactive"
    ) {
      return l1EllestadConconi(
        store.student?.fc_max,
        form.l1_ellestad_conconi.value
      );
    }
  }),
  l2_fc_max_percentage: computed(() => {
    if (
      store.cardio_protocol === "EllestadActive" ||
      store.cardio_protocol === "EllestadInactive"
    ) {
      return l2EllestadConconi(
        store.student?.fc_max,
        form.l2_ellestad_conconi.value
      );
    }
  }),
  vo2max: computed(() => {
    if (store.cardio_protocol === "Cooper") {
      return vo2maxCooper(form.distance.value);
    } else if (store.cardio_protocol === "Weltman") {
      return vo2maxWeltman(form.time.value);
    } else if (store.cardio_protocol === "EllestadActive") {
      return vo2maxActive(form.time.value, store.student?.gender);
    } else if (store.cardio_protocol === "EllestadInactive") {
      return vo2maxInactive(form.time.value);
    } else if (store.cardio_protocol === "Bicycle") {
      return vo2maxBicycle(form.fc_5min.value);
    }
  }),
  vo2max_absolute: computed(() =>
    vo2maxAbsolute(results.vo2max, store.student?.weight)
  ),
  vo2max_mets: computed(() => vo2maxMets(results.vo2max)),
  vvo2max: computed(() => {
    if (store.cardio_protocol === "Cooper") {
      return vvo2maxCooper(form.distance.value);
    } else if (store.cardio_protocol === "Weltman") {
      return vvo2maxWeltman(form.time.value);
    }
  }),
  vvo2max_pace: computed(() => formatPace(results.vvo2max)),
  vl1: computed(() =>
    store.cardio_protocol === "Weltman" ? vl1Weltman(form.time.value) : null
  ),
  vl1_pace: computed(() =>
    store.cardio_protocol === "Weltman" ? formatPace(results.vl1) : null
  ),
  vl2: computed(() =>
    store.cardio_protocol === "Weltman" ? vl2Weltman(form.time.value) : null
  ),
  vl2_pace: computed(() =>
    store.cardio_protocol === "Weltman" ? formatPace(results.vl2) : null
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

export const protocolsType = {
  default: [
    { id: "cooper", value: "Cooper", name: "Teste de Cooper" },
    { id: "weltman", value: "Weltman", name: "Teste de Weltman" },
    { id: "active", value: "EllestadActive", name: "Ellestad Adultos Ativos" },
    {
      id: "inactive",
      value: "EllestadInactive",
      name: "Ellestad Adultos Iniciantes/Inativos",
    },
    { id: "bicycle", value: "Bicycle", name: "Bicicleta FOX 5min" },
  ],
  idoso: [{ value: "Elder", name: "Potência Aeróbica em Idosos" }],
};

export const protocolsList = computed(() => {
  return store.student?.age >= 60 ? protocolsType.idoso : protocolsType.default;
});
