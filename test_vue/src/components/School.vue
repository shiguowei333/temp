<template>
    <div>
        <h2>{{name}}</h2>
        <h2>{{address}}</h2>
    </div>
</template>

<script>
export default {
    name: 'MySchool',
    data() {
                return {
                    name: '学校名',
                    address: '北京'
                }
            }
}
</script>
