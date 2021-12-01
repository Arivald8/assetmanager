import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Signin from './components/Signin';

import { 
  BrowserRouter,
  Routes,
  Route 
} from "react-router-dom";

import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>
          <Route path="/signin" element={<Signin />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

