import React from "react";

export default function PredictionRangeSlider(props) {
    return (
        <div className="form-item">
            <label className="form-slider-label">{props.title}</label>
            <input
                value={props.number}
                name={props.name}
                type="range"
                onChange={props.onChange}
                className="predictioncontainer-form-input"
                min={props.min}
                max={props.max}
                step={props.step}
            ></input>
            <div>
                {props.text1}
                {props.number}
                {props.text2}
            </div>
        </div>
    );
}
