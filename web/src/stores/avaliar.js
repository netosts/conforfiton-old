import { defineStore } from "pinia";
import { ref } from "vue";

export const useAvaliarStore = defineStore("avaliar", () => {
  const types = ref([]);
  const evaluatedAt = ref(null);

  const student = ref(null);

  const rmConfig = ref(null);

  const antropometria_protocol = ref(null);
  const neuromuscular_protocol = ref(null);
  const cardio_protocol = ref(null);

  return {
    types,
    evaluatedAt,
    student,
    rmConfig,
    antropometria_protocol,
    neuromuscular_protocol,
    cardio_protocol,
  };
});
