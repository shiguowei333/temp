<template>
  <div id="app">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader @addEvent='addEvent'></MyHeader>
        <MyList :events='events'></MyList>
        <MyFooter :events='events' @makeAppAll='makeAppAll' @clearAll='clearAll'></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
    import pubsub from 'pubsub-js'
    import MyHeader from './components/MyHeader'
    import MyList from './components/MyList'
    import MyFooter from './components/MyFooter'

    export default {
      name: 'App',
      components: {
        MyHeader,
        MyList,
        MyFooter
      },
      methods: {
        addEvent(e) {
          this.events.unshift(e)
        },
        changeStatus(id) {
          this.events.forEach(e => {
            if(e.id === id) e.completed = !e.completed
          })
        },
        deleteEvent(_,msg) {
          if(confirm(`确定删除${msg[1]}吗`)) {
            this.events = this.events.filter(e => e.id !== msg[0])
          }
        },
        makeAppAll(status) {
          this.events.forEach(e => {
            e.completed = status
          })
        },
        clearAll() {
          if(confirm(`确定删除勾选的数据吗`)) {
            this.events = this.events.filter(e => {
              return e.completed === false
            })
          }
        }
      },
      data() {
        return {
          events: JSON.parse(localStorage.getItem('events')) || []
        }
      },
      watch: {
        events: {
          deep: true,
          handler(value) {
            localStorage.setItem('events',JSON.stringify(value))
          }
        }
      },
      mounted() {
        this.$bus.$on('changeStatus',this.changeStatus),
        this.pubId = pubsub.subscribe('deleteEv',this.deleteEvent)
      },
      beforDestroy() {
        this.$bus.$off('changeStatus'),
        pubsub.unsubscribe(this.pubId)
      }
    }
</script>

<style>
  body {
    background: #fff;
  }

  .btn {
    display: inline-block;
    padding: 4px 12px;
    margin-bottom: 0;
    font-size: 14px;
    line-height: 20px;
    text-align: center;
    vertical-align: middle;
    cursor: pointer;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  }

  .btn-danger {
    color: #fff;
    background-color: #da4f49;
    border: 1px solid #bd362f;
  }

  .btn-danger:hover {
    color: #fff;
    background-color: #bd362f;
  }

  .btn:focus {
    outline: none
  }

  .todo-container {
    width: 600px;
    margin:0 auto
  }

  .todo-container .todo-wrap {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px
  }

  input[type="checkbox"] {
    cursor: pointer;
  }
</style>
