// eslint-disable-next-line no-unused-vars
import React from 'react';
import {useGetCategoriesQuery} from "../redux/recipes.api";
import CategoryItem from "../components/CategoryItem";

const HomePage = () => {
  const { data: categories, error, isLoading } = useGetCategoriesQuery()

  if (isLoading) return (
    <div className="container">
      <h1 className="mainTitle">Загрузка...</h1>
    </div>
  )
  return (
    <div className="container">
      <h1 className="title">Рецепты</h1>
      <div className="mainPageLinks">
        {error ? (
            <>На этой странице ошибка. Сервер не запущен.</>
          ) :
          categories?.map(({id, name}) => <CategoryItem key={id} name={name} id={id}/>)
        }
      </div>

    </div>
  );
};

export default HomePage;
