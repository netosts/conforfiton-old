import {
  calculateImc,
  imcClass,
  caClass,
  caRisk,
  calculateRcq,
  rcqClass,
  rcaeClass,
  calculateIac,
  iacClass,
  calculatePg,
  weltman,
  jacksonPollock3,
  falkner,
  jacksonPollock7,
  pgClass,
  idoso3Dobras,
  idosoTranWeltman,
} from "./helpers";

import { reactive, computed, ref } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

export const antropometria = reactive({
  abs: undefined,
  waist: undefined,
  hip: undefined,
  thighs: undefined,
  right_biceps: undefined,
  right_forearm: undefined,
  chest: undefined,
  triceps: undefined,
  suprailiac: undefined,
  subscapularis: undefined,
  midaxillary: undefined,
  iliac_circumference: undefined,
  imc_result: computed(() =>
    calculateImc(store.student?.weight, store.student?.height)
  ),
  imc_class: computed(() => imcClass(antropometria.imc)),
  ca_class: computed(() => caClass(antropometria.abs, store.student?.gender)),
  ca_risk: computed(() => caRisk(antropometria.abs, store.student?.gender)),
  rcq_result: computed(() =>
    calculateRcq(antropometria.waist, antropometria.hip)
  ),
  rcq_class: computed(() =>
    rcqClass(
      antropometria.rcq_result,
      store.student?.gender,
      store.student?.age
    )
  ),
  rcae_class: computed(() =>
    rcaeClass(antropometria.abs, store.student?.height)
  ),
  iac_result: computed(() =>
    calculateIac(antropometria.hip, store.student?.height)
  ),
  iac_class: computed(() =>
    iacClass(antropometria.iac_result, store.student?.gender)
  ),
  pg_result: computed(() => {
    if (store.antropometria_protocol === "Default") {
      return calculatePg(
        antropometria.right_biceps,
        antropometria.abs,
        antropometria.right_forearm,
        antropometria.thighs,
        store.student?.gender
      );
    } else if (store.antropometria_protocol === "Weltman") {
      return weltman(
        antropometria.abs,
        store.student?.weight,
        store.student?.height,
        store.student?.gender
      );
    } else if (
      store.antropometria_protocol === "JacksonPollock3Siri" ||
      store.antropometria_protocol === "JacksonPollock3Brozek"
    ) {
      const searchStr = "JacksonPollock3";
      const formula = store.antropometria_protocol.substring(searchStr.length);
      return jacksonPollock3(
        antropometria.chest,
        antropometria.abs,
        antropometria.thighs,
        antropometria.triceps,
        antropometria.suprailiac,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Falkner") {
      return falkner(
        antropometria.triceps,
        antropometria.subscapularis,
        antropometria.suprailiac,
        antropometria.abs
      );
    } else if (
      store.antropometria_protocol === "JacksonPollock7Siri" ||
      store.antropometria_protocol === "JacksonPollock7Brozek"
    ) {
      const searchStr = "JacksonPollock7";
      const formula = store.antropometria_protocol.substring(searchStr.length);
      return jacksonPollock7(
        antropometria.chest,
        antropometria.midaxillary,
        antropometria.triceps,
        antropometria.subscapularis,
        antropometria.abs,
        antropometria.suprailiac,
        antropometria.thighs,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Idoso3Dobras") {
      return idoso3Dobras(
        antropometria.triceps,
        antropometria.subscapularis,
        antropometria.suprailiac
      );
    } else if (store.antropometria_protocol === "IdosoTranWeltman") {
      return idosoTranWeltman(
        antropometria.abs,
        antropometria.hip,
        antropometria.suprailiac,
        store.student?.weight,
        store.student?.height,
        store.student?.age,
        store.student?.gender
      );
    }
  }),
  pg_class: computed(() =>
    pgClass(antropometria.pg_result, store.student?.gender, store.student?.age)
  ),
});

const antropometriaForAppend = [
  {
    value: antropometria.abs,
    name: "abs",
    label: "Abdominal",
    show: ref(true),
  },
  {
    value: antropometria.waist,
    name: "waist",
    label: "Cintura",
    show: ref(true),
  },
  { value: antropometria.hip, name: "hip", label: "Quadril", show: ref(true) },
  {
    value: antropometria.thighs,
    name: "thighs",
    label: "Coxa",
    show: computed(() => {
      if (store.student?.gender === "Female") {
        return ["Default", "JacksonPollock3Siri", "JacksonPollock3Brozek"].some(
          (item) => store.antropometria_protocol?.includes(item)
        );
      } else if (store.student?.gender === "Male") {
        return ["JacksonPollock3Siri", "JacksonPollock3Brozek"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.right_biceps,
    name: "right_biceps",
    label: "Bíceps Direito",
    show: computed(() => {
      if (store.student?.gender === "Male") {
        return ["Default"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.right_forearm,
    name: "right_forearm",
    label: "Antebraço Direito",
    show: computed(() => {
      if (
        store.student?.gender === "Male" ||
        store.student?.gender === "Female"
      ) {
        return ["Default"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.chest,
    name: "chest",
    label: "Peitoral",
    show: computed(() => {
      if (store.student?.gender === "Male") {
        return ["JacksonPollock3Siri", "JacksonPollock3Brozek"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.triceps,
    name: "triceps",
    label: "Tríceps",
    show: computed(() => {
      if (store.student?.gender === "Female") {
        return ["JacksonPollock3Siri", "JacksonPollock3Brozek"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.suprailiac,
    name: "suprailiac",
    label: "Suprailíaca",
    show: computed(() => {
      if (store.student?.gender === "Female") {
        return ["JacksonPollock3Siri", "JacksonPollock3Brozek"].some((item) =>
          store.antropometria_protocol?.includes(item)
        );
      }
    }),
  },
  {
    value: antropometria.subscapularis,
    name: "subscapularis",
    label: "Subescapular",
    show: ref(false),
  },
  {
    value: antropometria.midaxiallry,
    name: "midaxiallry",
    label: "Axilar Média",
    show: ref(true),
  },
  {
    value: antropometria.iliac_circumference,
    name: "iliac_circumference",
    label: "Perímetro ilíaco",
    show: ref(true),
  },
];

export const antropometriaList = computed(() => {
  return antropometriaForAppend.filter((item) => item.show.value);
});

export const protocolsType = {
  default: [
    { value: "Default", name: "Padrão" },
    { value: "Weltman", name: "Weltman" },
    { value: "JacksonPollock3Siri", name: "Jackson e Pollock 3 [Siri]" },
    { value: "JacksonPollock3Brozek", name: "Jackson e Pollock 3 [Brozek]" },
    { value: "Falkner", name: "Falkner" },
    { value: "JacksonPollock7Siri", name: "JacksonPollock 7 [Siri]" },
    { value: "JacksonPollock7Brozek", name: "JacksonPollock 7 [Brozek]" },
  ],
  idoso: [
    { value: "Idoso3Dobras", name: "Idoso [3 Dobras]" },
    { value: "IdosoTranWeltman", name: "Idoso [Tran. & Weltman]" },
  ],
};

export const protocolsList = computed(() => {
  return store.student?.age >= 60 ? protocolsType.idoso : protocolsType.default;
});
