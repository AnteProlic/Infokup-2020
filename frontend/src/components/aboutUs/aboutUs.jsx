import React from 'react';
import './aboutUs.css';
import ProfileCard from './components/profileCard';

const AboutUs = () => (
  <div id='aboutUs__container'>
    <ProfileCard image='https://picsum.photos/500/500' name='Augustin Čavka' title='(Overrated) AI Expert' school='III. gimnazija' />
    <ProfileCard image='https://picsum.photos/500/500' name='Ante Prolić' title='Backend Expert' school='III. gimnazija' />
    <ProfileCard image='https://picsum.photos/500/500' name='Goran Prolić' title='Frontend Expert' school='III. gimnazija' />
  </div>
);

export default AboutUs;
