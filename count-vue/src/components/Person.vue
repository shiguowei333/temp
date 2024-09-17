<template>
  <div>
    <h1>人员列表</h1>
    <input type="text" placeholder="请输入名字" v-model="name"/>
    <button @click="add">添加</button>
    <ul>
      <li v-for="p in personList" :key='p.id'>{{p.name}}</li>
    </ul>
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
    name: 'PersonList',
    data() {
      return {
        name: ''
      }
    },
    computed: {
      ...mapState(['personList'])
    },
    methods: {
      add() {
        
      }
    }
}
</script>

<style>
    button {
      margin-left: 5px;
    }
</style>