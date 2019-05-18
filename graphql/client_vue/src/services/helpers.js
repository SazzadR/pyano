const reset_object_to_empty = (obj) => {
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            obj[key] = '';
        }
    }
};

export {reset_object_to_empty};
