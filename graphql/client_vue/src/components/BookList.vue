<template>
    <div>
        <ul id="book-list">
            <li v-for="book in allBooks" v-bind:key="book.id">
                <router-link :to="`/book/${book.id}`">{{ book.title }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
    import {GET_ALL_BOOKS} from '../graphql/queries';

    export default {
        name: 'BookList',

        apollo: {
            allBooks: GET_ALL_BOOKS
        }
    }
</script>

<style scoped></style>
