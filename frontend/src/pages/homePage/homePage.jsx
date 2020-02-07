import React from 'react';
import './homePage.css';
import Header from '../../components/header/header';
import AboutUs from '../../components/aboutUs/aboutUs';
import AboutProject from '../../components/aboutProject/aboutProject';
import Footer from '../../components/footer/footer';
import { Parallax, ParallaxLayer } from '../../../node_modules/react-spring/renderprops-addons';

const HomePage = () => (
  <div>
    <Parallax pages={2.8} scrolling>
      <ParallaxLayer offset={0} speed={0.5}>
        <Header />
        <AboutProject />
        <AboutUs />
        <Footer />
      </ParallaxLayer>
    </Parallax>
  </div>
);

export default HomePage;
