import React, {Component} from 'react';
import {Query} from 'react-apollo';
import {Link} from 'react-router-dom';

import {GET_ALL_BOOKS} from '../queries/queries';

class BookList extends Component {
    render() {
        return (
            <Query query={GET_ALL_BOOKS}>
                {({loading, error, data}) => {
                    if (loading) {
                        return (<div>Loading books...</div>);
                    }
                    if (error) {
                        return (`Error! ${error.message}`);
                    }

                    return (
                        <div>
                            <h1>Ninja's Reading List</h1>
                            <ul id="book-list">
                                {data.allBooks.map(book => (
                                    <li key={book.id}>
                                        <Link to={'/book/' + book.id}>
                                            {book.title}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    );
                }}
            </Query>
        );
    }
}

export default BookList;
