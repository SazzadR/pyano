import React, {Component} from 'react';
import {Query} from 'react-apollo';

import {GET_ALL_AUTHORS} from '../queries/queries';

class BookList extends Component {
    render() {
        return (
            <Query query={GET_ALL_AUTHORS}>
                {({loading, error, data}) => {
                    if (loading) {
                        return (<div>Loading authors...</div>);
                    }
                    if (error) {
                        return (`Error! ${error.message}`);
                    }

                    return (
                        <div>
                            <ul id="book-list">
                                {data.allAuthors.map(author => (
                                    <li key={author.id}>{author.authorName}</li>
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
