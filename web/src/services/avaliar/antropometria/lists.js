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
} from "./helpers";

import { reactive, computed } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

export const antropometria = reactive({
  imc: computed(() =>
    calculateImc(store.student?.weight, store.student?.height)
  ),
  imcClass: computed(() => imcClass(antropometria.imc)),
  ca: undefined,
  caClass: computed(() => caClass(antropometria.ca, store.student?.gender)),
  caRisk: computed(() => caRisk(antropometria.ca, store.student?.gender)),
  waist: undefined,
  hip: undefined,
  rcq: computed(() => calculateRcq(antropometria.waist, antropometria.hip)),
  rcqClass: computed(() =>
    rcqClass(antropometria.rcq, store.student?.gender, store.student?.age)
  ),
  rcaeClass: computed(() => rcaeClass(antropometria.ca, store.student?.height)),
  iac: computed(() => calculateIac(antropometria.hip, store.student?.height)),
  iacClass: computed(() => iacClass(antropometria.iac, store.student?.gender)),
  pgA: undefined,
  pgB: undefined,
  pgC: undefined,
  pg: computed(() =>
    calculatePg(
      antropometria.pgA,
      antropometria.pgB,
      antropometria.pgC,
      store.student?.gender
    )
  ),
});
