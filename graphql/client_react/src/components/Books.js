import React, {Component} from 'react';

import BookList from './BookList';
import CreateBook from './CreateBook';

class Books extends Component {
    render() {
        return (
            <div>
                <BookList/>
                <CreateBook/>
            </div>
        );
    }
}

export default Books;
