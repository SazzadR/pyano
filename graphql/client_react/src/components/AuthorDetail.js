import React, {Component} from 'react';
import {Query} from 'react-apollo';

import {GET_AUTHOR} from '../queries/queries';

class AuthorDetail extends Component {
    render() {
        const author_id = this.props.match.params.id;
        return (
            <Query query={GET_AUTHOR} variables={{id: author_id}}>
                {({loading, error, data}) => {
                    if (loading) {
                        return (<div>Loading author...</div>);
                    }
                    if (error) {
                        return (`Error! ${error.message}`);
                    }

                    return (
                        <div>
                            <p><strong>Name:</strong> {data.author.authorName}</p>
                            <p><strong>Age:</strong> {data.author.age}</p>
                            <p><strong>Books:</strong></p>
                            <ul>
                                {data.author.books.map(book => (
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

export default AuthorDetail;
