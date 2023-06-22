import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";

export const recipesApi = createApi({
  reducerPath: 'recipesApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/' }),
  tagTypes: ['Categories'],
  endpoints: (builder) => ({
    getCategories: builder.query({
      query: () => `categories/`,
      providesTags: ['Categories'],
    }),
    getRecipesByCat: builder.query({
      query: (id) => `categories/${id}/`,
    }),
    getRecipe: builder.query({
      query: (slug) => `recipes/${slug}/`,
    }),
  }),
});

export const {useGetCategoriesQuery, useGetRecipesByCatQuery, useGetRecipeQuery} = recipesApi;
