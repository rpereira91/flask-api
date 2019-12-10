import React, { Component } from 'react';
import Warehouse from './components/warehouse'
class App extends Component {
  state = {
    warehouses: []
  }
  componentDidMount() {
    fetch('http://127.0.0.1:5000/api/v1/warehouse/all')
      .then(res => res.json())
      .then((data) => {
        this.setState({ warehouses: data })
      })
      .catch(console.log)
  }
  render() {
    console.log(this.state.warehouses)
    return (
      <Warehouse warehouses={this.state.warehouses}/>
    );
  }
}

export default App;