import React from 'react';
import './registerInput.css';

const RegisterInput = () => (
  <div id='container__logInInput'>
    <div id='logInInput__image' />
    <div id='logInInput__container'>
      <p id='logInInput__title'>Register</p>
      <p>Email:</p>
      <input type='text' name='email' />
      <p>Password:</p>
      <input type='password' name='password' />
      <div id='logInInput__button'>Welcome</div>
    </div>
  </div>

);

export default RegisterInput;