<template>
    <div id="app">
        <nav>
            <router-link to="/"><a href="javascript:void(0)">Home</a></router-link> |
            <router-link to="/books/"><a href="javascript:void(0)">Books</a></router-link>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: 'app'
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }
</style>
