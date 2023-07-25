import './assets/styles/_index.scss'

// Fontawesome Icons
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX } from '@fortawesome/free-solid-svg-icons'
import { faMoon } from '@fortawesome/free-regular-svg-icons'

// Vue Motion plugin
import { MotionPlugin } from '@vueuse/motion'

// Vee validate
import { required, cpf, email, minLength, maxLength, between, maxDecimal, password } from './services/rules'
import { defineRule } from 'vee-validate'

// Vue Application
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'

const app = createApp(App)

// vee validate rules
defineRule('required', value => required(value))
defineRule('cpf', value => cpf(value))
defineRule('email', value => email(value))
defineRule('minLength', (value, [limit]) => minLength(value, limit))
defineRule('maxLength', (value, [limit]) => maxLength(value, limit))
defineRule('between', (value, [min, max]) => between(value, min, max))
defineRule('maxDecimal', (value, [limit]) => maxDecimal(value, limit))
defineRule('password', value => password(value))

library.add(faMoon, faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000'

// Use Vue Router and Vue Motion plugins
app.use(MotionPlugin)
app.use(router)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
