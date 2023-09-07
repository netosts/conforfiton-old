import { defineStore } from "pinia";
import { ref } from "vue";

export const useStudentStore = defineStore("student", () => {
  const show = ref(
    Array.from({ length: 3 }, (_, i) => (i === 0 ? true : false))
  );

  return { show };
});
