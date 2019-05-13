import React, {Component} from 'react';
import {Query} from 'react-apollo';

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
                            <ul id="book-list">
                                {data.allBooks.map(book => (
                                    <li key={book.id}>{book.title}</li>
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
