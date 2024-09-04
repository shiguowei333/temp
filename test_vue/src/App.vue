<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <School></School>
    <Student></Student>
  </div>
</template>

<script>
import School from './components/School.vue'
import Student from './components/Student.vue'

export default {
  name: 'App',
  components: {
    School,
    Student
  }
}
</script>

