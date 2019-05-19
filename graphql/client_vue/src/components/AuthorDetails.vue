<template>
    <div>
        <div v-if="$apollo.loading">Loading...</div>
        <div v-else>
            <p><strong>Name:</strong> {{ author.authorName }}</p>
            <p><strong>Age:</strong> {{ author.age }}</p>
            <p><strong>Books:</strong></p>
            <ul>
                <li v-for="book in author.books" v-bind:key="book.id">{{ book.title }}</li>
            </ul>
        </div>
    </div>
</template>

<script>
    import {GET_AUTHOR} from '../graphql/queries';

    export default {
        name: 'AuthorDetails',

        apollo: {
            author: {
                query: GET_AUTHOR,
                variables() {
                    return {
                        id: this.$route.params.id
                    }
                }
            }
        }
    }
</script>

<style scoped></style>
