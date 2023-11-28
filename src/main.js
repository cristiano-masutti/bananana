// ./src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

// Add a global component for SharkView
import HomeView from './views/HomeView.vue'
app.component('SharkView', HomeView)

app.mount('#app')
