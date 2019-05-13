import React, {Component} from 'react';
import {Query, Mutation} from 'react-apollo';

import {GET_ALL_AUTHORS, GET_ALL_BOOKS, CREATE_BOOK} from '../queries/queries';

class CreateBook extends Component {
    state = {
        title: '',
        genre: '',
        authorId: ''
    };

    render() {
        return (
            <Mutation mutation={CREATE_BOOK} refetchQueries={() => {
                return [{
                    query: GET_ALL_BOOKS
                }]
            }}>
                {(createBook, {data}) => (
                    <form id="create-book" onSubmit={event => {
                        event.preventDefault();
                        createBook({
                            variables: {
                                title: this.state.title,
                                genre: this.state.genre,
                                authorId: parseInt(this.state.authorId)
                            }
                        });
                        this.state.title = '';
                        this.state.genre = '';
                        this.state.authorId = '';
                    }}>
                        <div className="field">
                            <label htmlFor="title">Title: </label>
                            <input type="text" id="title"
                                   value={this.state.title}
                                   onChange={event => this.setState({title: event.target.value})}/>
                        </div>
                        <div className="field">
                            <label htmlFor="genre">Genre: </label>
                            <input type="text" id="genre"
                                   value={this.state.genre}
                                   onChange={event => this.setState({genre: event.target.value})}/>
                        </div>
                        <div className="field">
                            <label htmlFor="author">Author: </label>
                            <select name="author_id" id="author"
                                    value={this.state.authorId}
                                    onChange={event => this.setState({authorId: event.target.value})}>
                                <option>Select Author</option>
                                <Query query={GET_ALL_AUTHORS}>
                                    {({loading, error, data}) => {
                                        if (loading) {
                                            return (<optgroup>
                                                <option>Loading Authors...</option>
                                            </optgroup>);
                                        }

                                        return (
                                            <optgroup>
                                                {data.allAuthors.map(author => (
                                                    <option key={author.id}
                                                            value={author.id}>{author.authorName}</option>
                                                ))}
                                            </optgroup>
                                        );
                                    }}
                                </Query>
                            </select>
                        </div>
                        <button type="submit">Create</button>
                    </form>
                )}
            </Mutation>
        );
    }
}

export default CreateBook;
