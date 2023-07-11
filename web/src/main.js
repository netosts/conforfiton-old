import './assets/styles/_index.scss'

// Fontawesome Icons
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX } from '@fortawesome/free-solid-svg-icons'
import { faMoon } from '@fortawesome/free-regular-svg-icons'

// Vue Motion plugin
import { MotionPlugin } from '@vueuse/motion'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'

library.add(faMoon, faExpand, faMagnifyingGlass, faXmark, faCheck, faLocationDot, faPhoneFlip, faEnvelope, faX)

const app = createApp(App)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000'

// Use Vue Router and Vue Motion plugins
app.use(MotionPlugin)
app.use(router)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
