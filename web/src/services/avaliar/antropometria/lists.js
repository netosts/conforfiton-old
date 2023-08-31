import { calculateImc, imcClass, calculateRcq, rcqClass } from './helpers'

import { reactive, computed } from 'vue'
import { useAvaliarStore } from '@/stores/avaliar'

const store = useAvaliarStore()

export const antropometria = reactive({
  imc: computed(() => calculateImc(store.student?.weight, store.student?.height)),
  imcClass: computed(() => imcClass(antropometria.imc)),
  waist: undefined,
  hip: undefined,
  rcq: computed(() => calculateRcq(antropometria.waist, antropometria.hip)),
  rcqClass: computed(() => rcqClass(antropometria.rcq, store.student?.gender, store.student?.age))
})
