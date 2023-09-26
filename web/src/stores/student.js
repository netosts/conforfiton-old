import { defineStore } from "pinia";
import { ref } from "vue";

export const useStudentStore = defineStore("student", () => {
  const student = ref({
    id: undefined,
    value: undefined,
  });
  const overview = ref({
    id: undefined,
    value: undefined,
    initiated: false,
  });
  const anamnese = ref({
    id: undefined,
    value: undefined,
    initiated: false,
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

  return { student, overview, anamnese, neuromuscular, antropometria, cardio };
});
