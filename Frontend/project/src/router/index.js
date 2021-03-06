import Vue from 'vue'
import VueRouter from 'vue-router'
import UserView from '../views/UserView'
import –°ashierView from '../views/–°ashierView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: UserView,
  },
  {
    path: '/cashier',
    name: 'cashier',
    component: –°ashierView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
