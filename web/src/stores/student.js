import { defineStore } from "pinia";
import { ref } from "vue";

export const useStudentStore = defineStore("student", () => {
  const student = ref({
    id: undefined,
    value: undefined,
  });
  const anamnese = ref({
    id: undefined,
    value: undefined,
  });
  const evaluations = ref({
    id: undefined,
    neuromuscular: undefined,
    antropometria: undefined,
    cardio: undefined,
  });

  return { student, anamnese, evaluations };
});
