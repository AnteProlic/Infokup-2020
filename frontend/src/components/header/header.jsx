import React from 'react';
import './header.css';
import Title from '../title/title';
import { Link } from 'react-router-dom';

const Header = () => (
  <div>
    <div id='header1'>
      <div id='shade'>
        <div id='button__container'>
          <Link to='/login'>log in</Link>
          <Link to='/'>homepage</Link>
          <Link>>project</Link>
        </div>
        <Title />
      </div>
    </div>
  </div>
);

export default Header;
