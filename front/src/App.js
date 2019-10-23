import React from 'react'
import './App.css'

export default class App extends React.Component {
  state = {
    currencies: [],
    fr: '',
    to: '',
    amount: '',
    result: '',
  }

  constructor (props) {
    super(props)

    fetch('http://0.0.0.0:8000/converter/currencies/')
    .then(response => response.json())
    .then(json => {
      this.setState({currencies: json})
    })
  }

  onChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value
    }, () => {
      let fr = this.state.fr
      let to = this.state.to
      let amount = this.state.amount

      if (!fr || !to || !amount) return

      fetch(`http://0.0.0.0:8000/converter/${fr}/${to}/${amount}/`)
        .then(response => response.json())
        .then(json => {
          this.setState({result: json.result})
        })
    })
  }

  render() {
    let options = c => {
      return <option key={c.code} value={c.code}>{c.code} {c.name}</option>
    }
    let result = r => {
      if (this.state.result) {
        return <h3 className="uk-text-muted">
          <strong>{this.state.amount}</strong> {this.state.fr}
          <span>=</span>
          <strong>{this.state.result.toFixed(2)}</strong> {this.state.to}
        </h3>
      } else {
        return ''
      }
    }

    if (!this.state.currencies.length) {
      return <div className="App">
        <p className="loading">...</p>
      </div>
    }

    return (
      <div className="App">
        <div className="uk-container">
          <form>

            <label>
              From:
              <select className="uk-select" name="fr" onChange={this.onChange}>
                <option></option>
                {this.state.currencies.map(options)}
              </select>
            </label>

            <label>
              To:
              <select className="uk-select" name="to" onChange={this.onChange}>
                <option></option>
                {this.state.currencies.map(options)}
              </select>
            </label>

            <label>
              Amount:
              <input className="uk-input" name="amount" onChange={this.onChange} />
            </label>

          </form>

          {result()}

        </div>
      </div>
    )
  }
}
