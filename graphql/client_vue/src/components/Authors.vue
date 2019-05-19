<template>
    <div>
        <AuthorList/>
        <CreateAuthor/>
    </div>
</template>


<script>
    import AuthorList from './AuthorList';
    import CreateAuthor from './CreateAuthor';

    export default {
        name: 'Authors',

        components: {
            AuthorList,
            CreateAuthor
        }
    }
</script>

<style scoped></style>
