import React, {Component} from 'react';
import {Query, Mutation} from 'react-apollo';

import {GET_ALL_AUTHORS, CREATE_AUTHOR} from '../queries/queries';

class CreateAuthor extends Component {
    state = {
        authorName: '',
        age: ''
    };

    render() {
        return (
            <Mutation mutation={CREATE_AUTHOR} refetchQueries={() => {
                return [{
                    query: GET_ALL_AUTHORS
                }]
            }}>
                {(createBook, {data}) => (
                    <form id="create-author" onSubmit={event => {
                        event.preventDefault();
                        createBook({
                            variables: {
                                authorName: this.state.authorName,
                                age: this.state.age
                            }
                        });
                        this.state.authorName = '';
                        this.state.age = '';
                    }}>
                        <div className="field">
                            <label htmlFor="name">Name: </label>
                            <input type="text" id="name"
                                   value={this.state.authorName}
                                   onChange={event => this.setState({authorName: event.target.value})}/>
                        </div>
                        <div className="field">
                            <label htmlFor="age">Age: </label>
                            <input type="number" id="age"
                                   value={this.state.age}
                                   onChange={event => this.setState({age: event.target.value})}/>
                        </div>
                        <button type="submit">Create</button>
                    </form>
                )}
            </Mutation>
        );
    }
}

export default CreateAuthor;
