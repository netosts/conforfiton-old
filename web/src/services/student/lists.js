import Overview from "@/components/student/Overview.vue";
import Evaluations from "@/components/student/Evaluations.vue";
import Anamnese from "@/components/student/Anamnese.vue";

export const studentButtons = ["Geral", "Anamnese", "Avaliações"];

export const studentComponents = [
  { component: Overview, get: "student" },
  { component: Anamnese, get: "anamnese" },
  { component: Evaluations, get: "evaluations" },
];
