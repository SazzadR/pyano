import React from 'react';
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from 'react-apollo';

import BookList from './components/BookList';
import CreateBook from './components/CreateBook';

const client = new ApolloClient({
    uri: 'http://127.0.0.1:8000/graphql/'
});

function App() {
    return (
        <ApolloProvider client={client}>
            <div id="main">
                <h1>Ninja's Reading List</h1>
                <BookList/>
                <CreateBook/>
            </div>
        </ApolloProvider>
    );
}

export default App;
