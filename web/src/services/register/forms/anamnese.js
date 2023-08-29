import { reactive } from 'vue';

const form = reactive({
  ...Object.fromEntries(Array.from({ length: 27 }, (_, i) => [`q${i + 1}`, i + 1 === 13 ? [] : undefined])),
  q4: { treinando: undefined, tempo: undefined },
});

export { form };
