import {
  calcular1RMZona,
  calcularRMEpley,
  calcularPontos,
  sitUpClass,
  pushUpClass,
  jumpClass,
} from "./helpers";
import { computed, reactive } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

import RMZona from "@/components/avaliar/neuromuscular/RMZona.vue";
import RMLFP from "@/components/avaliar/neuromuscular/RMLFP.vue";

const store = useAvaliarStore();

export const repsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15];

export const exerciseList = reactive([
  {
    title: "Supino",
    name: "bench_press",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[0].lifted, exerciseList[0].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[0].reps, exerciseList[0].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[0].rm,
        exerciseList[0].name,
        store.rmConfig
      )
    ),
  },
  {
    title: "Rosca Direta",
    name: "barbell_curl",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[1].lifted, exerciseList[1].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[1].reps, exerciseList[1].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[1].rm,
        exerciseList[1].name,
        store.rmConfig
      )
    ),
  },
  {
    title: "Puxada Pela Frente",
    name: "pull_down",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[2].lifted, exerciseList[2].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[2].reps, exerciseList[2].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[2].rm,
        exerciseList[2].name,
        store.rmConfig
      )
    ),
  },
  {
    title: "Leg Press",
    name: "leg_press",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[3].lifted, exerciseList[3].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[3].reps, exerciseList[3].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[3].rm,
        exerciseList[3].name,
        store.rmConfig
      )
    ),
  },
  {
    title: "Extensão de Joelhos",
    name: "leg_extension",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[4].lifted, exerciseList[4].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[4].reps, exerciseList[4].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[4].rm,
        exerciseList[4].name,
        store.rmConfig
      )
    ),
  },
  {
    title: "Flexão de Joelhos",
    name: "leg_curl",
    lifted: undefined,
    reps: undefined,
    rm: computed(() => {
      if (store.neuromuscular_protocol === "1RMZona") {
        return calcular1RMZona(exerciseList[5].lifted, exerciseList[5].reps);
      } else if (store.neuromuscular_protocol === "RMEpley") {
        return calcularRMEpley(exerciseList[5].reps, exerciseList[5].lifted);
      }
    }),
    points: computed(() =>
      calcularPontos(
        store.student,
        exerciseList[5].rm,
        exerciseList[5].name,
        store.rmConfig
      )
    ),
  },
]);

export const total = computed(() => {
  const points = exerciseList.map((exercise) => exercise.points);
  const total = points.reduce((total, points) => total + points, 0);
  return total ? total : 0;
});

const protocolsType = {
  default: [
    { value: "1RMZona", name: "Teste de 1RM [Zona]" },
    { value: "RMEpley", name: "RM de Epley (1995)" },
    { value: "RMLFP", name: "Testes de força e resistência" },
  ],
};

export const protocolsList = computed(() => {
  return protocolsType.default;
});

export const neuroComponents = [
  { protocol: "1RMZona", component: RMZona },
  { protocol: "RMEpley", component: RMZona },
  { protocol: "RMLFP", component: RMLFP },
];

export const RMLFPList = reactive({
  sit_up: {
    value: undefined,
    name: "sit_up",
    label: "Abdominal",
    span: "(reps)",
  },
  push_up: {
    value: undefined,
    name: "push_up",
    label: "Flexão de braço",
    span: "(reps)",
  },
  jump: {
    value: undefined,
    name: "jump",
    label: "Salto",
    span: "(horizontal ou vertical)",
  },
});

export const results = reactive({
  sit_up_result: computed(() =>
    sitUpClass(
      store.student?.gender,
      store.student?.age,
      RMLFPList.sit_up.value
    )
  ),
  push_up_result: computed(() =>
    pushUpClass(
      store.student?.gender,
      store.student?.age,
      RMLFPList.push_up.value
    )
  ),
  jump_result: computed(() =>
    jumpClass(store.student?.gender, store.student?.age, RMLFPList.jump.value)
  ),
});
