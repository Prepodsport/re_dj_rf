// eslint-disable-next-line no-unused-vars
import React from 'react';
import {useParams} from "react-router-dom";
import {useGetRecipeQuery} from "../redux/recipes.api";
import ButtonGoBack from "../components/ButtonGoBack";

const RecipePage = () => {
  const {slug} = useParams();
  const {data: recipe, error, isLoading} = useGetRecipeQuery(slug);
  const ingredients = recipe?.ingredients.split('-');
  const instructions = recipe?.instructions.split('-');
  const preview = recipe?.preview;

  if (isLoading) return (
    <div className="container">
      <h1 className="mainTitle">Загрузка...</h1>
    </div>
  )
  return (
    <>
      <ButtonGoBack />
      {error ? (
          <>На этой странице ошибка. Сервер не запущен.</>
        ) :
        (
          <div className="recipeCard">
            <h1>{recipe?.title}</h1>
            <div>
              <div className='title_descript'>Ингредиенты:</div>
              <ol>
                {
                  ingredients?.map((ingredient, index) => <li key={index + 1}
                                                              className='cardTextIngredients'>{ingredient}</li>)
                }
              </ol>
              <div className='title_descript'>Шаги приготовления:</div>
              <ol>
                {
                  instructions?.map((instruction, index) => <li key={index + 1}
                                                                className='cardTextInstructions'>{instruction}</li>)
                }
              </ol>
            </div>
          </div>
        )
      }
      <div className="recipeCard">
          <h1>Готовое блюдо</h1>
          <div>
              <div className="preview" style={{background: `url(${recipe.preview})`}}></div>
          </div>
      </div>
    </>
  );
};

export default RecipePage;
