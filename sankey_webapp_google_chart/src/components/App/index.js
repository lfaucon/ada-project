import React from 'react';
import './styles.css';
import SankeyChart from '../SankeyChart';

function App() {
  return (
    <div className="app">
      <div className="app-header">
        <h2>ADA Project</h2>
      </div>
      <SankeyChart />
    </div>
  );
}

export default App;
