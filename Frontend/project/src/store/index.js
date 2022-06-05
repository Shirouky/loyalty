import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';

Vue.use(Vuex);
Axios.defaults.baseURL = 'http://127.0.0.1:8000'

export const store = new Vuex.Store({
    state: {
        user: {
        },
        products: []
    },
    getters: {
    },
    mutations: {
        SET_POINTS: (state, payload) => {
            state.user.points = payload;
        },
        SET_USER: (state, payload) => {
            state.user = payload;
        },
        SET_PRODUCTS: (state, payload) => {
            state.products = payload;
        },

    },
    actions: {

        async SAVE_POINTS({ commit }) {
            const user_id = 1
            await Axios
                .post(`/save/points/${user_id}`)
                .then(function (response) {
                    commit('SET_POINTS', response.data);
                })
        },

        async SPEND_POINTS({ commit }, data) {
            await Axios
                .post(`/spend/points`, data)
                .then(function (response) {
                    commit('SET_POINTS', response.data);
                })
        },

        async SET_USER({ commit }, user_id) {
            await Axios
                .get(`/user/${user_id}`)
                .then(function (response) {
                    commit('SET_USER', response.data);
                })
        },

        async SET_PRODUCTS({ commit }) {
            await Axios
                .get(`/products`)
                .then(function (response) {
                    commit('SET_PRODUCTS', response.data);
                })
        },
    }
});