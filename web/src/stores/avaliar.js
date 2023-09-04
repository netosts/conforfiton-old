import { defineStore } from "pinia";
import { ref } from "vue";

export const useAvaliarStore = defineStore("avaliar", () => {
  const types = ref([]);

  const student = ref(null);

  const rmConfig = ref(null);

  const antropometria_protocol = ref("Default");

  return { types, student, rmConfig, antropometria_protocol };
});
