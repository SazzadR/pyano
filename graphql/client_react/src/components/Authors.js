import React, {Component} from 'react';

import AuthorList from './AuthorList';
import CreateAuthor from './CreateAuthor';

class Authors extends Component {
    render() {
        return (
            <div>
                <AuthorList/>
                <CreateAuthor/>
            </div>
        );
    }
}

export default Authors;
