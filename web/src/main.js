import './assets/styles/_index.scss'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faExpand } from '@fortawesome/free-solid-svg-icons'
import { faMoon } from '@fortawesome/free-regular-svg-icons'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'

library.add(faMoon, faExpand)

const app = createApp(App)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000'

app.use(router)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
