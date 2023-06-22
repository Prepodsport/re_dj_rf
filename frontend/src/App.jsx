import {Route, Routes} from "react-router-dom";
import Header from "./components/Header";
import HomePage from "./pages/HomePage";
import CategoryPage from "./pages/CategoryPage";
import RecipePage from "./pages/RecipePage";

function App() {
  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path='/' element={<HomePage/>}/>
        <Route path="recipes/:categoryId" element={<CategoryPage/>}/>
        <Route path="recipes/:categoryId/:slug" element={<RecipePage/>}/>
      </Routes>
    </div>
  );
}

export default App;
