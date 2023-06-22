// eslint-disable-next-line no-unused-vars
import React from 'react';
import {Link} from "react-router-dom";

// eslint-disable-next-line react/prop-types
const RecipeItem = ({catId, recipe}) => {
  return (
      // eslint-disable-next-line react/prop-types
    <Link to={`/recipes/${catId}/${recipe.slug}`}>
        {/* eslint-disable-next-line react/prop-types */}
      <p className='menuLink'>{recipe.title}</p>
    </Link>
  );
};

export default RecipeItem;
