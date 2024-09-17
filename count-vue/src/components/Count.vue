<template>
  <div>
    <h1>当前求和为：{{$store.state.sum}}</h1>
    <h3>当前求和放大十倍为：{{$store.getters.bigSum}}</h3>
    <h3>我在{{$store.state.school}}，学习{{$store.state.subject}}</h3>
    <select v-model.number="n">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
    </select>
    <button @click="add">+</button>
    <button @click="decrement">-</button>
    <button @click="addOdd">当前奇数加</button>
    <button @click="addWait">等会再加</button>
  </div>
</template>

<script>
export default {
    name: 'ContentList',
    data() {
      return {
        n: 1
      }
    },
    methods: {
      add() {
        this.$store.commit('JIA',this.n)
      },
      decrement() {
        this.$store.commit('JIAN',this.n)
      },
      addOdd() {
        this.$store.dispatch('jiaIn',this.n)
      },
      addWait() {
        this.$store.dispatch('jiaWait',this.n)
      }
    }
}
</script>

<style>
    button {
      margin-left: 5px;
    }
</style>