<template>
    <div>
        <BookList/>
        <CreateBook/>
    </div>
</template>

<script>
    import BookList from './BookList';
    import CreateBook from './CreateBook';

    export default {
        name: 'Books',

        components: {
            BookList,
            CreateBook
        }
    }
</script>

<style scoped>

</style>
