/* eslint-disable react/prop-types */
/* eslint-disable react/destructuring-assignment */
/* eslint-disable react/jsx-one-expression-per-line */
import React from 'react';
import './profileCard.css';

function ProfileCard(props) {
  return (
    <div id='card'>
      <img src={props.image} alt={props.name} />
      <div>
        <p id='name'>{props.name}</p>
        <p id='title'>{props.title}</p>
        <p>{props.school}</p>
        <p id='contact'>Contact</p>
      </div>
    </div>
  );
}

export default ProfileCard;
