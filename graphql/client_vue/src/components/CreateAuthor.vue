<template>
    <div>
        <form action="javascript:void(0)" id="create-author">
            <div class="field">
                <label for="name">Name: </label>
                <input type="text" id="name" v-model="author.name">
            </div>
            <div class="field">
                <label for="age">Age: </label>
                <input type="number" id="age" v-model="author.age">
            </div>
            <button type="submit" @click="create_author()">Create</button>
        </form>
    </div>
</template>

<script>
    import {reset_object_to_empty} from '../services/helpers';
    import {GET_ALL_AUTHORS, CREATE_AUTHOR} from '../graphql/queries';

    export default {
        name: 'CreateAuthor',

        data() {
            return {
                author: {
                    name: '',
                    age: '',
                    author_id: ''
                }
            }
        },

        methods: {
            create_author() {
                const {name, age} = this.author;
                reset_object_to_empty(this.author);

                this.$apollo.mutate({
                    mutation: CREATE_AUTHOR,
                    variables: {
                        authorName: name,
                        age: parseInt(age)
                    },
                    update: (store, {data: {createAuthor}}) => {
                        const data = store.readQuery({query: GET_ALL_AUTHORS});
                        data.allAuthors.push(createAuthor.author);
                        store.writeQuery({query: GET_ALL_AUTHORS, data});
                    }
                }).then((data) => {
                    console.log(data);
                }).catch((error) => {
                    console.log(error);
                    this.author.name = name;
                    this.author.age = age;
                });
            }
        }
    }
</script>

<style scoped></style>
