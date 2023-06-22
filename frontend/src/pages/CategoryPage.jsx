// eslint-disable-next-line no-unused-vars
import React from 'react';
import {useGetCategoriesQuery, useGetRecipesByCatQuery} from "../redux/recipes.api";
import {useParams} from "react-router-dom";
import RecipeItem from "../components/RecipeItem";
import ButtonGoBack from "../components/ButtonGoBack";

const CategoryPage = () => {
  const {categoryId} = useParams();
  const {data: recipesByCat, error, isLoading} = useGetRecipesByCatQuery(categoryId);
  const {data: categories} = useGetCategoriesQuery();
  const currentCategory = categories?.find(({id}) => id.toString() === categoryId.toString());

  if (isLoading) return (
    <div className="container">
      <h1 className="mainTitle">Загрузка...</h1>
    </div>
  )
  return (
    <>
      <ButtonGoBack />
      <div className="container">
        <h1 className="mainTitle">{currentCategory?.name}</h1>
        <div className="mainPageLinks">
          {error ? (
              <>На этой странице ошибка. Сервер не загружен</>
            ) :
            recipesByCat?.map((recipe) => <RecipeItem key={recipe.id} recipe={recipe} catId={categoryId}/>)
          }
        </div>
      </div>
    </>
  );
};

export default CategoryPage;
