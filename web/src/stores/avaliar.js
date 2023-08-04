import { defineStore } from 'pinia';
import { ref } from 'vue';


export const useAvaliarStore = defineStore('avaliar', () => {
  const types = ref(undefined);

  return { types }
});