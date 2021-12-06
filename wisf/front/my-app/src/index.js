import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Signin from './components/Signin';

import store from './app/store'
import { Provider } from 'react-redux';

import { 
  BrowserRouter,
  Routes,
  Route 
} from "react-router-dom";

import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />}>
            <Route path="/signin" element={<Signin />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

