<template>
    <div>
        <h1>Ninja's Reading Lists</h1>
        <BookList/>
    </div>
</template>

<script>
    import BookList from './BookList';

    export default {
        name: 'Home',

        components: {BookList}
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
