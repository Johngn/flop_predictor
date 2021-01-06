import React from "react";

export default function PredictionContainer() {
    return (
        <div className="predictioncontainer">
            <div className="predictioncontainer-form-container">
                <form className="predictioncontainer-form">
                    <div className="form-item">
                        <input
                            type="range"
                            className="predictioncontainer-form-input"
                        ></input>
                    </div>
                    <div className="form-item">
                        <input
                            type="range"
                            className="predictioncontainer-form-input"
                        ></input>
                    </div>
                    <div className="form-item">
                        <label htmlFor="budget"></label>
                        <input
                            name="budget"
                            type="range"
                            className="predictioncontainer-form-input"
                        ></input>
                    </div>
                    <div className="form-item select-container">
                        <select className="select-item">
                            <option value="western">Western</option>
                            <option value="horror">Horror</option>
                            <option value="action">Action</option>
                        </select>
                    </div>
                    <div className="form-item select-container">
                        <select className="select-item">
                            <option value="david lynch d">David Lynch</option>
                            <option value="james cameron d">
                                James Cameron
                            </option>
                            <option value="steven spielberg d">
                                Steven Spielberg
                            </option>
                        </select>
                    </div>
                    <div className="form-item select-container">
                        <select className="select-item">
                            <option value="tom cruise">Tom Cruise</option>
                            <option value="clint eastwood">
                                Clint Eastwood
                            </option>
                            <option value="jeremy renner">Jeremy Renner</option>
                        </select>
                    </div>
                </form>
            </div>
        </div>
    );
}
