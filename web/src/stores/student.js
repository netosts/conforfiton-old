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
  const neuromuscular = ref({
    id: undefined,
    value: undefined,
  });
  const antropometria = ref({
    id: undefined,
    value: undefined,
  });
  const cardio = ref({
    id: undefined,
    value: undefined,
  });

  return { student, anamnese, neuromuscular, antropometria, cardio };
});
