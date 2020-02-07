import React from 'react';
import './logInInput.css';
import { Link } from 'react-router-dom';

const logInInput = () => (
  <div id='container__logInInput'>
    <div id='logInInput__image' />
    <div id='logInInput__container'>
      <p id='logInInput__title'>Log In</p>
      <p>Email:</p>
      <input type='text' name='email' />
      <p>Password:</p>
      <input type='password' name='password' />
      <div id='logInInput__button'>Log In</div>
      <Link to='/register'>Register</Link>
    </div>
  </div>

);

export default logInInput;
