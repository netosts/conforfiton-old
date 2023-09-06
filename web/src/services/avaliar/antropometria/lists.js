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
  filterShow,
} from "./helpers";

import { reactive, computed } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

const form = reactive({
  abdominal_circumference: {
    value: undefined,
    name: "abdominal_circumference",
    label: "Abdômen",
    span: "(perímetro)",
    show: true,
  },
  waist_circumference: {
    value: undefined,
    name: "waist_circumference",
    label: "Cintura",
    span: "(perímetro)",
    show: true,
  },
  hip_circumference: {
    value: undefined,
    name: "hip_circumference",
    label: "Quadril",
    span: "(perímetro)",
    show: true,
  },
  thighs_circumference: {
    value: undefined,
    name: "thighs_circumference",
    label: "Coxa",
    span: "(perímetro)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.thighs_circumference.name,
        store.antropometria_protocol
      )
    ),
  },
  right_biceps_circumference: {
    value: undefined,
    name: "right_biceps_circumference",
    label: "Bíceps Direito",
    span: "(perímetro)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.right_biceps_circumference.name,
        store.antropometria_protocol
      )
    ),
  },
  right_forearm_circumference: {
    value: undefined,
    name: "right_forearm_circumference",
    label: "Antebraço Direito",
    span: "(perímetro)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.right_forearm_circumference.name,
        store.antropometria_protocol
      )
    ),
  },
  chest_skinfold: {
    value: undefined,
    name: "chest_skinfold",
    label: "Peitoral",
    span: "(dobra cutânea)",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.chest_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  triceps_skinfold: {
    value: undefined,
    name: "triceps_skinfold",
    label: "Tríceps",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.triceps_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  suprailiac_skinfold: {
    value: undefined,
    name: "suprailiac_skinfold",
    label: "Suprailíaca",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.suprailiac_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  subscapularis_skinfold: {
    value: undefined,
    name: "subscapularis_skinfold",
    label: "Subescapular",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.subscapularis_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  midaxillary_skinfold: {
    value: undefined,
    name: "midaxiallry",
    label: "Axilar Média",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.midaxillary_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  abdominal_skinfold: {
    value: undefined,
    name: "abdominal_skinfold",
    label: "Abdominal",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.abdominal_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  thighs_skinfold: {
    value: undefined,
    name: "thighs_skinfold",
    label: "Coxa",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.thighs_skinfold.name,
        store.antropometria_protocol
      )
    ),
  },
  iliac_circumference: {
    value: undefined,
    name: "iliac_circumference",
    label: "Perímetro ilíaco",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.iliac_circumference.name,
        store.antropometria_protocol
      )
    ),
  },
});

export const antropometriaList = computed(() => {
  return Object.values(form).filter((item) => item.show);
});

export const results = reactive({
  imc_result: computed(() =>
    calculateImc(store.student?.weight, store.student?.height)
  ),
  imc_class: computed(() => imcClass(results.imc_result)),
  ca_class: computed(() =>
    caClass(form.abdominal_circumference.value, store.student?.gender)
  ),
  ca_risk: computed(() =>
    caRisk(form.abdominal_circumference.value, store.student?.gender)
  ),
  rcq_result: computed(() =>
    calculateRcq(form.waist_circumference.value, form.hip_circumference.value)
  ),
  rcq_class: computed(() =>
    rcqClass(results.rcq_result, store.student?.gender, store.student?.age)
  ),
  rcae_class: computed(() =>
    rcaeClass(form.abdominal_circumference.value, store.student?.height)
  ),
  iac_result: computed(() =>
    calculateIac(form.hip_circumference.value, store.student?.height)
  ),
  iac_class: computed(() =>
    iacClass(results.iac_result, store.student?.gender)
  ),
  pg_result: computed(() => {
    if (store.antropometria_protocol === "Default") {
      return calculatePg(
        form.right_biceps_circumference.value,
        form.abdominal_circumference.value,
        form.right_forearm_circumference.value,
        form.thighs_circumference.value,
        store.student?.gender
      );
    } else if (store.antropometria_protocol === "Weltman") {
      return weltman(
        form.abdominal_circumference.value,
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
        form.chest_skinfold.value,
        form.abdominal_skinfold.value,
        form.thighs_skinfold.value,
        form.triceps_skinfold.value,
        form.suprailiac_skinfold.value,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Falkner") {
      return falkner(
        form.triceps_skinfold.value,
        form.subscapularis_skinfold.value,
        form.suprailiac_skinfold.value,
        form.abdominal_skinfold.value
      );
    } else if (
      store.antropometria_protocol === "JacksonPollock7Siri" ||
      store.antropometria_protocol === "JacksonPollock7Brozek"
    ) {
      const searchStr = "JacksonPollock7";
      const formula = store.antropometria_protocol.substring(searchStr.length);
      return jacksonPollock7(
        form.chest_skinfold.value,
        form.midaxillary_skinfold.value,
        form.triceps_skinfold.value,
        form.subscapularis_skinfold.value,
        form.abdominal_skinfold.value,
        form.suprailiac_skinfold.value,
        form.thighs_skinfold.value,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Idoso3Dobras") {
      return idoso3Dobras(
        form.triceps_skinfold.value,
        form.subscapularis_skinfold.value,
        form.suprailiac_skinfold.value
      );
    } else if (store.antropometria_protocol === "IdosoTranWeltman") {
      return idosoTranWeltman(
        form.abdominal_circumference.value,
        form.hip_circumference.value,
        form.iliac_circumference.value,
        store.student?.weight,
        store.student?.height,
        store.student?.age,
        store.student?.gender
      );
    }
  }),
  pg_class: computed(() =>
    pgClass(results.pg_result, store.student?.gender, store.student?.age)
  ),
});

const protocolsType = {
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
