import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import HomePage from './pages/homePage/homePage';
import LogInPage from './pages/logInPage/logInPage';
import MapPage from './pages/mapPage/mapPage';
import RegisterPage from './pages/registerPage/registerPage';
const routes = (
  <BrowserRouter>
    <Switch>
      <Route exact path='/' component={HomePage} />
      <Route path='/login' component={LogInPage} />
      <Route path='/map' component={MapPage} />
      <Route path='/register' component={RegisterPage} />
    </Switch>
  </BrowserRouter>
);

export default routes;

ReactDOM.render(routes, document.getElementById('root'));