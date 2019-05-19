<template>
    <div>
        <div v-if="$apollo.loading">Loading...</div>
        <div v-else>
            <p><strong>Name:</strong> {{ book.title }}</p>
            <p><strong>Genre:</strong> {{ book.genre }}</p>
            <p><strong>Author:</strong> {{ book.author.authorName }}</p>
        </div>
    </div>
</template>

<script>
    import {GET_BOOK} from '../graphql/queries';

    export default {
        name: 'BookDetails',

        apollo: {
            book: {
                query: GET_BOOK,
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
