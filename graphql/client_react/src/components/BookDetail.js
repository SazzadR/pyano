import React, {Component} from 'react';
import {Query} from 'react-apollo';

import {GET_BOOK} from '../queries/queries';

class BookDetail extends Component {
    render() {
        const book_id = this.props.match.params.id;
        return (
            <Query query={GET_BOOK} variables={{id: book_id}}>
                {({loading, error, data}) => {
                    if (loading) {
                        return (<div>Loading book...</div>);
                    }
                    if (error) {
                        return (`Error! ${error.message}`);
                    }

                    return (
                        <div>
                            <p><strong>Name:</strong> {data.book.title}</p>
                            <p><strong>Genre:</strong> {data.book.genre}</p>
                            <p><strong>Author:</strong> {data.book.author.authorName}</p>
                        </div>
                    );
                }}
            </Query>
        );
    }
}

export default BookDetail;
