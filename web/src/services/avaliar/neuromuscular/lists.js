import { calcular1RM, calcularPontos } from './helpers';
import { computed, reactive } from 'vue';
import { useAvaliarStore } from '@/stores/avaliar';


const store = useAvaliarStore();

export const repsList = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15
];

export const exerciseList = reactive([
  {
    title: 'Supino',
    name: 'bench_press',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[0].lifted, exerciseList[0].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[0].rm, exerciseList[0].name, store.rmConfig))
  },
  {
    title: 'Rosca Direta',
    name: 'barbell_curl',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[1].lifted, exerciseList[1].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[1].rm, exerciseList[1].name, store.rmConfig))
  },
  {
    title: 'Puxada Pela Frente',
    name: 'pull_down',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[2].lifted, exerciseList[2].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[2].rm, exerciseList[2].name, store.rmConfig))
  },
  {
    title: 'Leg Press',
    name: 'leg_press',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[3].lifted, exerciseList[3].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[3].rm, exerciseList[3].name, store.rmConfig))
  },
  {
    title: 'Extensão de Joelhos',
    name: 'leg_extension',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[4].lifted, exerciseList[4].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[4].rm, exerciseList[4].name, store.rmConfig))
  },
  {
    title: 'Flexão de Joelhos',
    name: 'leg_curl',
    lifted: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[5].lifted, exerciseList[5].reps)),
    points: computed(() => calcularPontos(store.student, exerciseList[5].rm, exerciseList[5].name, store.rmConfig))
  }
]);

export const total = computed(() => {
  const points = exerciseList.map(exercise => exercise.points)
  const total = points.reduce((total, points) => total + points, 0)
  return total ? total : 0
});
