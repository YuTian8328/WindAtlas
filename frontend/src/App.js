import './App.css';

import React, { useState, useEffect } from 'react';

import axios from 'axios';
// import $ from 'jquery';
import MyChart from './Chart';
import MaxTolerance from './MaxTolerance'
import Map from './Map';
import Circle from './components/Circle';

const apiUrl = process.env.REACT_APP_API_URL;
//const apiUrl = "http://localhost:8000";//
const apiKey = process.env.REACT_APP_GOOGLE_API_KEY;

axios.get(apiUrl)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });

const initStatus = {
  zoom: 6,
  center: {
    lat: 65.25,
    lng: 24.75,
  },
}

function App() {
  let chart = null;

  const [file, setFile] = useState(0);
  const [tg, setTG] = useState(1);
  const [process, setProcess] = useState([]);
  const [chartstate, setChartstate] = useState(false);
  // const [mapstate, setMapstate] = useState(null);
  const [fractions, setFractions] = useState([]);
  const [datastate, setDatastate] = useState(false);





  return (

    <div className="App">
      <h1>Wind Power Atlas of Finland</h1>

      <MaxTolerance apiUrl={apiUrl} />

    </div>

  );

}

export default App;