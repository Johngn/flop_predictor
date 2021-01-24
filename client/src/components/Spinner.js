import React, { Component } from "react";
import RingLoader from "react-spinners/ClipLoader";

export default class Spinner extends Component {
    render() {
        return (
            <div className="spinner-container">
                <RingLoader size={30} color={"#000"} loading />
            </div>
        );
    }
}
