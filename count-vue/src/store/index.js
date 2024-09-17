import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const actions = {
    jiaIn(content,value) {
        if(content.state.sum % 2 != 0) {
            content.commit('JIA',value)
        }
    },
    jiaWait(content,value) {
        setTimeout(() => {
            content.commit('JIA',value)
        },1000)
    }
}
const mutations = {
    JIA(state,value) {
        state.sum += value
    },
    JIAN(state,value) {
        state.sum -= value
    }
}
const state = {
    sum: 0,
    school: '山东女子学院',
    subject: '女红',
    personList: [
        {id: '001',name: '张三'}
    ]
}

const getters = {
    bigSum(state) {
        return state.sum * 10
    }
}

export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})