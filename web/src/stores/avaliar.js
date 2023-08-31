import { defineStore } from "pinia";
import { ref } from "vue";

export const useAvaliarStore = defineStore("avaliar", () => {
  const types = ref([]);

  const student = ref(null);

  const rmConfig = ref(null);

  const rcqCintura = ref(null);
  const rcqQuadril = ref(null);

  return { types, student, rmConfig, rcqCintura, rcqQuadril };
});
