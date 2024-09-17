<template>
  <div class="row">
    <div v-show="users.length" class="card" v-for="user in users" :key="user.login">
        <a :href="user.html_url" target="_blank">
            <img :src="user.avatar_url" style="width: 100px">
        </a>
        <p class="card-text">{{user.login}}</p>
    </div>
    <h1 v-show="isFirst">欢迎使用！</h1>
    <h1 v-show="isLoading">加载中...</h1>
    <h1 v-show="errMsg">{{errMsg}}</h1>
  </div>
</template>

<script>
export default {
    name: 'ContentList',
    data() {
        return {
            isFirst: true,
            isLoading: false,
            errMsg: '',
            users: []
        }
    },
    mounted() {
        this.$bus.$on('getUsers',(users) => {
            console.log('shoudaoshuju',users)
            this.users = users
        })
    }
}
</script>

<style>
    .album {
    min-height: 50rem;
    padding-top: 3rem;
    padding-bottom: 3rem;
    background-color: #f7f7f7;
  }

  .card {
    float:left;
    width: 33.333%;
    padding: .75rem;
    margin-bottom: 2rem;
    border: 1px solid #efefef;
    text-align: center;
  }

  .card > img {
    margin-bottom: .75rem;
    border-radius: 100px;
  }

  .coar-text {
    font-size: 85%;
  }
</style>