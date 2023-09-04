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
} from "./helpers";

import { reactive, computed } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

export const antropometria = reactive({
  abs: undefined,
  waist: undefined,
  hip: undefined,
  thighs: undefined,
  rightForearm: undefined,
  chest: undefined,
  triceps: undefined,
  suprailiac: undefined,
  subscapularis: undefined,
  midaxillary: undefined,
  imc: computed(() =>
    calculateImc(store.student?.weight, store.student?.height)
  ),
  imcClass: computed(() => imcClass(antropometria.imc)),
  caClass: computed(() => caClass(antropometria.abs, store.student?.gender)),
  caRisk: computed(() => caRisk(antropometria.abs, store.student?.gender)),
  rcq: computed(() => calculateRcq(antropometria.waist, antropometria.hip)),
  rcqClass: computed(() =>
    rcqClass(antropometria.rcq, store.student?.gender, store.student?.age)
  ),
  rcaeClass: computed(() =>
    rcaeClass(antropometria.abs, store.student?.height)
  ),
  iac: computed(() => calculateIac(antropometria.hip, store.student?.height)),
  iacClass: computed(() => iacClass(antropometria.iac, store.student?.gender)),
  pg: computed(() => {
    if (store.antropometria_protocol === "Default") {
      return calculatePg(
        antropometria.abs,
        antropometria.thighs,
        antropometria.rightForearm,
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
        antropometria.subscapularis,
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
    }
  }),
  pgClass: computed(() =>
    pgClass(antropometria.pg, store.student?.gender, store.student?.age)
  ),
});
