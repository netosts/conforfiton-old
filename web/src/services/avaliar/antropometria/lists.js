import {
  calculateImc,
  imcClass,
  caClass,
  caRisk,
  calculateRcq,
  rcqClass,
  calculateRcae,
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
  calculateMig,
  calculateFatWeight,
  calculateMigWeight,
  calculateWeightGoal,
  calculateMigGoal,
  calculateFatWeightGoal,
  calculateMigWeightGoal,
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
  chest_skin_fold: {
    value: undefined,
    name: "chest_skin_fold",
    label: "Peitoral",
    span: "(dobra cutânea)",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.chest_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  abdominal_skin_fold: {
    value: undefined,
    name: "abdominal_skin_fold",
    label: "Abdominal",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.abdominal_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  thighs_skin_fold: {
    value: undefined,
    name: "thighs_skin_fold",
    label: "Coxa",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.thighs_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  triceps_skin_fold: {
    value: undefined,
    name: "triceps_skin_fold",
    label: "Tríceps",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.triceps_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  suprailiac_skin_fold: {
    value: undefined,
    name: "suprailiac_skin_fold",
    label: "Suprailíaca",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.suprailiac_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  subscapularis_skin_fold: {
    value: undefined,
    name: "subscapularis_skin_fold",
    label: "Subescapular",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.subscapularis_skin_fold.name,
        store.antropometria_protocol
      )
    ),
  },
  midaxillary_skin_fold: {
    value: undefined,
    name: "midaxillary_skin_fold",
    label: "Axilar Média",
    span: "(dobra cutânea)",
    show: computed(() =>
      filterShow(
        store.student?.gender,
        form.midaxillary_skin_fold.name,
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
  pg_goal: {
    value: undefined,
    name: "pg_goal",
    label: "Meta %G",
    show: true,
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
  rcae_result: computed(() =>
    calculateRcae(form.abdominal_circumference.value, store.student?.height)
  ),
  rcae_class: computed(() => rcaeClass(results.rcae_result)),
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
        form.chest_skin_fold.value,
        form.abdominal_skin_fold.value,
        form.thighs_skin_fold.value,
        form.triceps_skin_fold.value,
        form.suprailiac_skin_fold.value,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Falkner") {
      return falkner(
        form.triceps_skin_fold.value,
        form.subscapularis_skin_fold.value,
        form.suprailiac_skin_fold.value,
        form.abdominal_skin_fold.value
      );
    } else if (
      store.antropometria_protocol === "JacksonPollock7Siri" ||
      store.antropometria_protocol === "JacksonPollock7Brozek"
    ) {
      const searchStr = "JacksonPollock7";
      const formula = store.antropometria_protocol.substring(searchStr.length);
      return jacksonPollock7(
        form.chest_skin_fold.value,
        form.midaxillary_skin_fold.value,
        form.triceps_skin_fold.value,
        form.subscapularis_skin_fold.value,
        form.abdominal_skin_fold.value,
        form.suprailiac_skin_fold.value,
        form.thighs_skin_fold.value,
        store.student?.age,
        store.student?.gender,
        formula
      );
    } else if (store.antropometria_protocol === "Idoso3Dobras") {
      return idoso3Dobras(
        form.triceps_skin_fold.value,
        form.subscapularis_skin_fold.value,
        form.suprailiac_skin_fold.value
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
  weight_goal: computed(() =>
    calculateWeightGoal(
      results.fat_weight_result,
      results.fat_weight_goal,
      store.student?.weight
    )
  ),
  mig_result: computed(() => calculateMig(results.pg_result)),
  mig_goal: computed(() => calculateMigGoal(form.pg_goal.value)),
  fat_weight_result: computed(() =>
    calculateFatWeight(store.student?.weight, results.pg_result)
  ),
  fat_weight_goal: computed(() =>
    calculateFatWeightGoal(form.pg_goal.value, store.student?.weight)
  ),
  mig_weight_result: computed(() =>
    calculateMigWeight(store.student?.weight, results.mig_result)
  ),
  mig_weight_goal: computed(() =>
    calculateMigWeightGoal(results.fat_weight_goal, store.student?.weight)
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
