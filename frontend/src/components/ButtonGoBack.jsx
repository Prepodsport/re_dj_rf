// eslint-disable-next-line no-unused-vars
import React from 'react';
import {useNavigate} from "react-router-dom";
const ButtonGoBack = () => {
  const navigate = useNavigate();
  const goBack = () => navigate(-1);
  return (
    <button className='btnGoBack' onClick={goBack}>Назад</button>
  );
};

export default ButtonGoBack;
