<template>
    <div>
        <ul id="author-list">
            <li v-for="author in allAuthors" v-bind:key="author.id">{{ author.authorName }}</li>
        </ul>
    </div>
</template>

<script>
    import {GET_ALL_AUTHORS} from '../graphql/queries';

    export default {
        name: 'AuthorList',

        apollo: {
            allAuthors: GET_ALL_AUTHORS
        }
    }
</script>

<style scoped></style>
