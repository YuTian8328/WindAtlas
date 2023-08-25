
import React, { useState } from 'react';
import axios from 'axios';
import Map from './Map';
import Circle from './components/Circle';
const apiKey = process.env.REACT_APP_GOOGLE_API_KEY;
const initStatus = {
  zoom: 6,
  center: {
    lat: 65.25,
    lng: 24.75,
  },
};
export default function MaxTolerance({ apiUrl,
}) {

  const [formData, setFormData] = useState({
    waitingTime: '',
    batteryCapacity: '10000',
    windTurbine: '2',
    totalEnergy: ''
  });
  const [fractions, setFractions] = useState([]);
  //const [calculatedResult, setCalculatedResult] = useState(null);//

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('Form submitted with data:', formData);

    const url = `${apiUrl}/api/suitability`;

    const config = {
      headers: {
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryTorHrryEzMAgU0CD'
        // 'content-type': 'application/json',
      },
    };
    try {
      const response = await axios.post(url, formData, config);
      console.log(response.data);
      setFractions(response.data.suitability);
    } catch (error) {
      console.error('Error while submitting:', error);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  // console.log(formData);//

  return (
    <div className="MaxTolerance">
      <h2>Available Fractions of Year 2021 to Run Your Process</h2>
      <form method="post" onSubmit={handleSubmit}>
        <label htmlFor="name">Total energy needed to run your process (integer): </label>
        <input type="number" step="0.01" name="totalEnergy" id="floatingInput" onChange={handleChange} />
        <span className="unit">Wh</span>
        <br></br>
        <br></br>
        <label htmlFor="name">The max waiting time you can tolerate (integer): </label>
        <input id="ticketNum" type="number" name="waitingTime" list="defaultNumbers" onChange={handleChange} />
        <span className="unit">h</span>
        <datalist id="defaultNumbers">
          <option value="1"></option>
          <option value="2"></option>
          <option value="3"></option>
          <option value="4"></option>
          <option value="5"></option>
          <option value="6"></option>
          <option value="7"></option>
          <option value="8"></option>
        </datalist>
        <br></br>
        <br></br>
        <label htmlFor="name">Virtual wind turbine to use: </label>
        <select name="windTurbine" onChange={handleChange} defaultValue="2">
          <option value="1">Rutland 50w Wind Turbine (Windcharger)</option>
          <option value="2">Automaxx Windmill 1500W Wind Turbine (Home-use)</option>
          <option value="3">Nordex N100 2500kW Wind Turbine (High-yield)</option>
        </select>
        <br></br>
        <br></br>
        <button type="submit" onSubmit={handleSubmit}>Submit</button>
      </form>

      <br></br>

      <div>
        <Map
          apiKey={apiKey}
          initStatus={initStatus}
          Component={Circle}
          data={fractions}
        /> </div >
    </div>
  );
}