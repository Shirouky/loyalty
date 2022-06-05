import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { store } from './store'
import VueQrcode from '@chenfengyuan/vue-qrcode';
import { QrcodeStream } from 'vue-qrcode-reader'

// eslint-disable-next-line
Vue.component('qrcode-stream', QrcodeStream)
Vue.component('qrcode-code', VueQrcode);
Vue.use(VueAxios, axios);
Vue.config.productionTip = false


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

