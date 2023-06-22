// eslint-disable-next-line no-unused-vars
import React from 'react';
import {Link} from "react-router-dom";

// eslint-disable-next-line react/prop-types
const CategoryItem = ({name, id}) => {
  return (
    <Link to={`/recipes/${id}`}>
      <p className='menuLink'>{name}</p>
    </Link>
  );
};

export default CategoryItem;
