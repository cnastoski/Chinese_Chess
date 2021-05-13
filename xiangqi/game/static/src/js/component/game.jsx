import React from "react";

class Board extends React.component {
    renderRow(i) {
        return <Row value={i} />;
    }

    render() {

    }
}

class Square extends React.component {
    render() {
        return (
            <div className='square' />
        )
    }
}

class Row extends React.component {
    render() {
        var ret = ''
        for (var i = 0; i < 8; i++) {
            ret += Square
        }
    }
}

class Game extends React.component{
    render(){
        <div className="game" />
    }
}