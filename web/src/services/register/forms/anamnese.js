import { reactive } from "vue";

const form = reactive({
  diabetes: undefined,
  hypertension: undefined,
  fc_max: undefined,
  fc_repouso: undefined,
  l1: undefined,
  l2: undefined,
  ...Object.fromEntries(
    Array.from({ length: 27 }, (_, i) => [
      `q${i + 1}`,
      i + 1 === 13 ? [] : undefined,
    ])
  ),
  q4: { training: undefined, time: undefined },
});

export { form };
