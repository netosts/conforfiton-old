import { calcular1RM, calcularPontos } from '../../services/configs/neuromuscular';
import { computed, reactive } from 'vue';
import { useAvaliarStore } from '../../stores/avaliar';


const store = useAvaliarStore();

// Register-Anamnese.vue
export const ufList = [
  '', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
  'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
];

export const sexoList = [
  'Masculino', 'Feminino'
];

export const camisaList = [
  'PP', 'P', 'M', 'G', 'GG', 'XG', 'XXG'
];

export const shortsList = [
  'PP-36/38', 'P-38/40', 'M-40/42', 'G-42/44', 'GG-44/46',
  'G1-48', 'G2-50', 'G3-52', 'G4-54', 'G5-56'
];

export const q4Radio = [
  { label: 'Parado', value: false },
  { label: 'Treinando', value: true }
];

export const YesOrNoRadio = [
  { label: 'Sim', value: true },
  { label: 'Não', value: false }
];

export const days = [
  'Domingo',
  'Segunda',
  'Terça',
  'Quarta',
  'Quinta',
  'Sexta',
  'Sábado'
];

// Avaliar.vue
export const repsList = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15
];

export const exerciseList = reactive([
  {
    title: 'Supino',
    name: 'supino',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[0].pesoLevantado, exerciseList[0].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[0].rm, exerciseList[0].name, store.rmConfig))
  },
  {
    title: 'Rosca Direta',
    name: 'roscaDireta',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[1].pesoLevantado, exerciseList[1].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[1].rm, exerciseList[1].name, store.rmConfig))
  },
  {
    title: 'Puxada Pela Frente',
    name: 'puxadaPelaFrente',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[2].pesoLevantado, exerciseList[2].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[2].rm, exerciseList[2].name, store.rmConfig))
  },
  {
    title: 'Leg Press',
    name: 'legPress',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[3].pesoLevantado, exerciseList[3].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[3].rm, exerciseList[3].name, store.rmConfig))
  },
  {
    title: 'Extensão de Joelhos',
    name: 'extensaoDeJoelhos',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[4].pesoLevantado, exerciseList[4].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[4].rm, exerciseList[4].name, store.rmConfig))
  },
  {
    title: 'Flexão de Joelhos',
    name: 'flexaoDeJoelhos',
    pesoLevantado: undefined,
    reps: undefined,
    rm: computed(() => calcular1RM(exerciseList[5].pesoLevantado, exerciseList[5].reps)),
    pontos: computed(() => calcularPontos(store.student, exerciseList[5].rm, exerciseList[5].name, store.rmConfig))
  }
]);

export const pontosTotal = computed(() => {
  const pontos = exerciseList.map(exercise => exercise.pontos)
  const total = pontos.reduce((total, pontos) => total + pontos, 0)
  return total ? total : null
});
