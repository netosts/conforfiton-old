import './assets/styles/_index.scss'

// Fontawesome Icons
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX } from '@fortawesome/free-solid-svg-icons'
import { faMoon } from '@fortawesome/free-regular-svg-icons'

// Vue Motion plugin
import { MotionPlugin } from '@vueuse/motion'

import { localize } from "@vee-validate/i18n"
import pt_BR from "@vee-validate/i18n/dist/locale/pt_BR.json"
import AllRules from "@vee-validate/rules"
import { defineRule, configure } from "vee-validate"
import { createI18n } from "vue-i18n"

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'

const app = createApp(App)

library.add(faMoon, faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX)

Object.keys(AllRules).forEach((rule) => {
  defineRule(rule, AllRules[rule])
})

const i18n = createI18n({
  locale: 'pt-BR',
  messages: {
    'pt-BR': {
      '$date': {
        locale: 'pt-br'
      }
    },
    'en-US': {
      '$date': {
        locale: 'en'
      }
    }
  }
})

configure({
  generateMessage: localize({
    'pt-BR': pt_BR,
  }),
})

localize('pt-BR')

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000'

// Use Vue Router and Vue Motion plugins
app.use(MotionPlugin)
app.use(router)
app.use(i18n)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
