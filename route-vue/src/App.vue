<template>
  <div>
    <div class="row">
      <banner></banner>
    </div>
    <div class="row">
      <div class="col-xs-2 col-xs-offset-2">
        <div class="list-froup">
          <router-link to="/about" class="list-group-item" active-class="active">About</router-link>
          <router-link to="/home" class="list-group-item" active-class="active">Home</router-link>
        </div>
      </div>
      <div class="col-xs-6">
        <div class="panel">
          <div class="panel-body">
            <router-view></router-view>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import Banner from './components/Banner'
    export default {
      name: 'App',
      components: {Banner}
    }
</script>

