
import React, { Component } from "react";
import Chart from "react-apexcharts";

class MyChart extends Component {
  constructor(props) {
    super(props);

    this.state = {
      options: {
        chart: {
          id: "basic-bar"
        },
        xaxis: {
          categories: Array.from(Array(props.data.length).keys())
        }
      },
      series: [
        {
          name: "series-1",
          data: props.data
        }
      ]
    };
  }

  render() {
    return (
      <div className="app">
        <div className="row">
          <div className="mixed-chart">
            <Chart
              options={this.state.options}
              series={this.state.series}
              type="bar"
              width="500"
            />
          </div>
        </div>
      </div>
    );
  }
}

export default MyChart;