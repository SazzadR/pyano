import {gql} from 'apollo-boost';

const GET_ALL_AUTHORS = gql`
    query {
        allAuthors {
            id
            authorName
        }
    }
`;

const CREATE_AUTHOR = gql`
    mutation createAuthor($authorName: String!, $age: Int!) {
        createAuthor(authorName: $authorName, age: $age) {
            author {
                id
                authorName
            }
        }
    }
`;

const GET_ALL_BOOKS = gql`
    query {
        allBooks {
            id
            title
        }
    }
`;

const CREATE_BOOK = gql`
    mutation createBook($title: String!, $genre: String!, $authorId: Int!) {
        createBook(title: $title, genre: $genre, authorId: $authorId) {
            book {
                id
                title
            }
        }
    }
`;

export {GET_ALL_AUTHORS, CREATE_AUTHOR, GET_ALL_BOOKS, CREATE_BOOK};