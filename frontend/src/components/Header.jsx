// eslint-disable-next-line no-unused-vars
import React from 'react';
import {Link} from "react-router-dom";
import {useGetCategoriesQuery} from "../redux/recipes.api";

const Header = () => {
  const { data: error, isLoading } = useGetCategoriesQuery();
  if (isLoading) return <h1>Загрузка...</h1>
  return (
    <header>
      <Link to="/"><h3 className='logo_text'>Главная</h3></Link>
    </header>
  );
};

export default Header;
