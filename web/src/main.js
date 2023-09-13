import "./assets/styles/_index.scss";

// Fontawesome Icons
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
/* import specific icons */
import {
  faExpand,
  faMagnifyingGlass,
  faXmark,
  faCheck,
  faLocationDot,
  faPhoneFlip,
  faEnvelope,
  faRotateRight,
  faAnglesLeft,
  faAnglesRight,
  faChevronLeft,
  faUser,
  faHouse,
  faPlus,
  faPrint,
  faFeather,
  faArrowRightToBracket,
} from "@fortawesome/free-solid-svg-icons";
import { faMoon } from "@fortawesome/free-regular-svg-icons";

// Vee validate
import {
  required,
  cpf,
  email,
  minLength,
  maxLength,
  between,
  maxDecimal,
  password,
  asymbol,
  name,
  date,
} from "./services/rules";
import { defineRule } from "vee-validate";

// Vue Application
import { createApp } from "vue";
import { createPinia } from "pinia"; // PINIA APP
import App from "./App.vue";
import router from "./router";

const pinia = createPinia();
const app = createApp(App);

// vee validate rules
defineRule("required", (value) => required(value));
defineRule("cpf", (value) => cpf(value));
defineRule("email", (value) => email(value));
defineRule("minLength", (value, [limit]) => minLength(value, limit));
defineRule("maxLength", (value, [limit]) => maxLength(value, limit));
defineRule("between", (value, [min, max]) => between(value, min, max));
defineRule("maxDecimal", (value, [limit]) => maxDecimal(value, limit));
defineRule("password", (value) => password(value));
defineRule("asymbol", (value) => asymbol(value));
defineRule("name", (value) => name(value));
defineRule("date", (value) => date(value));

library.add(
  faMoon,
  faExpand,
  faMagnifyingGlass,
  faXmark,
  faCheck,
  faLocationDot,
  faPhoneFlip,
  faEnvelope,
  faAnglesLeft,
  faHouse,
  faPlus,
  faPrint,
  faFeather,
  faUser,
  faAnglesRight,
  faChevronLeft,
  faRotateRight,
  faArrowRightToBracket
);

app.use(router);
app.use(pinia);

app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
