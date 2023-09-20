import Neuromuscular from "@/components/avaliar/Neuromuscular.vue";
import Antropometria from "@/components/avaliar/Antropometria.vue";
import Cardio from "@/components/avaliar/Cardio.vue";

export const evaluationComponents = [
  { component: Neuromuscular, includes: "neuromuscular" },
  { component: Antropometria, includes: "antropometria" },
  { component: Cardio, includes: "cardio" },
];
