<template>
    <div>
        <form action="javascript:void(0)" id="create-book">
            <div class="field">
                <label for="title">Title: </label>
                <input type="text" id="title" v-model="book.title">
            </div>
            <div class="field">
                <label for="genre">Genre: </label>
                <input type="text" id="genre" v-model="book.genre">
            </div>
            <div class="field">
                <label for="author_id">Author: </label>
                <select name="author_id" id="author_id" v-model="book.author_id">
                    <option value="">Select Author</option>
                    <option v-for="author in allAuthors" v-bind:value="author.id" v-bind:key="author.id">
                        {{ author.authorName }}
                    </option>
                </select>
            </div>
            <button type="submit" @click="create_book()">Create</button>
        </form>
    </div>
</template>

<script>
    import {GET_ALL_AUTHORS, GET_ALL_BOOKS, CREATE_BOOK} from '../graphql/queries';

    export default {
        name: 'CreateBook',

        data() {
            return {
                book: {
                    title: '',
                    genre: '',
                    author_id: ''
                }
            }
        },

        apollo: {
            allAuthors: GET_ALL_AUTHORS
        },

        methods: {
            create_book() {
                const {title, genre, author_id} = this.book;
                this.book.title = '';
                this.book.genre = '';
                this.book.author_id = '';
                this.$apollo.mutate({
                    mutation: CREATE_BOOK,
                    variables: {
                        title: title,
                        genre: genre,
                        authorId: parseInt(author_id)
                    },
                    update: (store, {data: {createBook}}) => {
                        const data = store.readQuery({query: GET_ALL_BOOKS});
                        data.allBooks.push(createBook.book);
                        store.writeQuery({query: GET_ALL_BOOKS, data});
                    }
                }).then((data) => {
                    console.log(data);
                }).catch((error) => {
                    console.log(error);
                    this.book.title = title;
                    this.book.genre = genre;
                    this.book.author_id = author_id;
                });
            }
        }
    }
</script>

<style scoped></style>
