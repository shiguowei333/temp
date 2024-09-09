<template>
    <div class="todo-footer" v-show='total'>
      <label>
        <input type="checkbox" v-model='isAll'/>
      </label>
      <span>
        <span>已完成：{{completedNum}}</span> / 全部{{total}}
      </span>
      <button class="btn btn-danger" @click='clear()'>清除已完成任务</button>
    </div>
</template>

<script>
    export default {
        name: 'MyFooter',
        props: ['events'],
        methods: {
            clear() {
                this.$emit('clearAll')
            }
        },
        computed: {
            total() {
                return this.events.length
            },
            completedNum() {
                return this.events.reduce((pre, e) => pre + (e.completed ? 1 : 0),0)
            },
            isAll: {
                get() {
                    return this.total > 0 && this.total === this.completedNum
                },
                set(status) {
                    this.$emit('makeAppAll', status)
                }
            }
        }
    }
</script>

<style scoped>
    .todo-footer {
        height: 40px;
        line-height: 40px;
        padding-left: 6px;
        margin-top: 5px;
    }

    .todo-footer label {
        display: inline-block;
        margin-right: 20px;
        cursor:pointer
    }

    .todo-footer label input {
        position: relative;
        top: -1px;
        vertical-align: middle;
        margin-right: 5px;
    }

    .todo-footer button {
        float: right;
        margin-top: 5px;
    }
</style>