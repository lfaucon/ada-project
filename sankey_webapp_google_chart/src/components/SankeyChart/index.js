import React, { Component } from 'react';
import { Chart } from 'react-google-charts';
import './styles.css';
import dataset1 from './dataset1.json';
import dataset2 from './dataset2.json';

class SankeyChart extends Component {
  constructor(props) {
    super(props);

    this.state = { data: dataset1.data };

    this.handleResize = this.handleResize.bind(this);
    this.setData = this.setData.bind(this);
  }

  componentDidMount() {
    window.addEventListener('resize', this.handleResize);
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.handleResize);
  }

  setData(index) {
    switch (index) {
      case 1:
        this.setState({ data: dataset1.data });
        break;
      case 2:
        this.setState({ data: dataset2.data });
        break;
      default:
        this.setState({ data: dataset1.data });
        break;
    }
  }

  handleResize() {
    this.forceUpdate();
  }

  render() {
    return (
      <div className="container">
        <div className="chart-container">
          <Chart
            chartType="Sankey"
            data={this.state.data}
            options={{}}
            graph_id="ScatterChart"
            width="100%"
            height="400px"
            legend_toggle
          />
        </div>
        <div className="buttons-container">
          <button onClick={() => this.setData(1)}>Dataset 1</button>
          <button onClick={() => this.setData(2)}>Dataset 2</button>
        </div>
      </div>
    );
  }
}

export default SankeyChart;
