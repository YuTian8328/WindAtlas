import React, { useState } from 'react';
import GoogleMapReact from 'google-map-react';
import { COORDINATES } from './coordinates';

export default function Map({
  apiKey,
  initStatus,
  Component,
  data,
}){
  const [zoom, setZoom] = useState(initStatus.zoom);

  const { center } = initStatus;

  const handleZoomChange = ({ zoom }) => {
    setZoom(zoom);
  };

  const buildComponent = (data) => {
    const { city } = data;
    const { lat, lng } = COORDINATES[city];
    const newData = { ...data, zoom: zoom }
    return (
      <Component
        key={ city }
        lat={ lat }
        lng={ lng }
        data={ newData }
      />
    );
  }

  return (
    // Important! Always set the container height explicitly
    <div style={{ height: '100vh', width: '100%' }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: apiKey }}
        defaultCenter={ center }
        zoom={ zoom }
        onChange={ handleZoomChange }
      >
        { data.map((x) => buildComponent(x)) }
      </GoogleMapReact>
    </div>
  );
}
