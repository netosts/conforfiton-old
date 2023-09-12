import {} from "./helpers";

import { reactive, computed } from "vue";
import { useAvaliarStore } from "@/stores/avaliar";

const store = useAvaliarStore();

const form = reactive({});

export const formulaList = [
  { id: "default", value: "Default", label: "Padrão" },
  { id: "diabetes", value: "Diabetes", label: "Diabetes" },
  { id: "hypertension", value: "Hypertension", label: "Hipertensão" },
];

export const protocolsList = [
  { id: "zona", value: "L1L2Zona", label: "Zona por FC Reserva" },
];
