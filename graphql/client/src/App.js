import React from 'react';
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from 'react-apollo';
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';

import Home from './components/Home';
import Books from './components/Books';
import BookDetail from './components/BookDetail';
import Authors from './components/Authors';
import AuthorDetail from './components/AuthorDetail';

const client = new ApolloClient({
    uri: 'http://127.0.0.1:8000/graphql/'
});

function App() {
    return (
        <ApolloProvider client={client}>
            <Router>
                <div id="main">
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/books">Books</Link>
                        </li>
                        <li>
                            <Link to="/authors">Authors</Link>
                        </li>
                    </ul>
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Route exact path="/books" component={Books}/>
                        <Route exact path="/book/:id" component={BookDetail}/>
                        <Route exact path="/authors" component={Authors}/>
                        <Route exact path="/author/:id" component={AuthorDetail}/>
                    </Switch>
                </div>
            </Router>
        </ApolloProvider>
    );
}

export default App;
