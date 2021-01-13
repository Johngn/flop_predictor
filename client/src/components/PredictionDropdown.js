import React from "react";

export default function PredictionDropdown(props) {
    return (
        <div className="form-item select-container">
            <label className="form-slider-label">{props.name}</label>
            <select className="select-item" onChange={props.setOption}>
                <option></option>
                {props.options.map((item, i) => (
                    <option key={i} value={item}>
                        {item.replace(/\w\S*/g, w =>
                            w.replace(/^\w/, c => c.toUpperCase())
                        )}
                    </option>
                ))}
            </select>
        </div>
    );
}
