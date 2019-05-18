<template>
    <div>
        <h1>Ninja's Reading Lists</h1>
        <ul id="book-list">
            <li v-for="book in allBooks" v-bind:key="book.id">{{ book.title }}</li>
        </ul>
    </div>
</template>

<script>
    import gql from 'graphql-tag';

    export default {
        name: 'BookList',
        apollo: {
            allBooks: gql`query {
                allBooks {
                    id
                    title
                }
            }`
        }
    }
</script>

<style scoped>

</style>
