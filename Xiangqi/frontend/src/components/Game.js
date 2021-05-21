import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return(<h1>React Test</h1>)
    }
}

const gameDiv = document.getElementById('game')
render(<Game />, gameDiv)