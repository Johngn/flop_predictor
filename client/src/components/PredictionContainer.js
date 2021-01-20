import React, { Component } from "react";
import { connect } from "react-redux";
import { getOptions, getPrediction } from "../redux/actions/predictions";
import PropTypes from "prop-types";
import PredictionRangeSlider from "./PredictionRangeSlider";
import PredictionDropdown from "./PredictionDropdown";

class PredictionContainer extends Component {
    state = {
        actor: "",
        director: "",
        genre: "",
        budget: 0,
        duration: 0,
        score: 0,
    };

    componentDidMount() {
        this.props.getOptions();
    }

    onChange = e => {
        console.log(e.target.value);

        this.setState({ [e.target.name]: e.target.value });
    };

    getPrediction = () => {
        const params = {
            actor: this.state.actor,
            director: this.state.director,
            genre: this.state.genre,
            budget: this.state.budget,
            duration: this.state.duration,
            score: this.state.score,
        };

        console.log(params);
        this.props.getPrediction(params);
    };

    render() {
        const { actors, directors, genres } = this.props.options;
        const { estimated_boxoffice } = this.props.prediction;

        return (
            <div className="predictioncontainer">
                <div className="predictioncontainer-form-container">
                    <form className="predictioncontainer-form">
                        <PredictionRangeSlider
                            text1="$ "
                            text2=" million"
                            number={this.state.budget}
                            title="Budget"
                            name="budget"
                            min="0"
                            max="500"
                            step="1"
                            onChange={this.onChange}
                        />
                        <PredictionRangeSlider
                            text2=" mins"
                            number={this.state.duration}
                            title="Duration"
                            name="duration"
                            min="0"
                            max="200"
                            step="1"
                            onChange={this.onChange}
                        />
                        <PredictionRangeSlider
                            number={this.state.score}
                            title="Score"
                            name="score"
                            min="0"
                            max="10"
                            step="0.1"
                            onChange={this.onChange}
                        />
                        <PredictionDropdown
                            title="Actor"
                            name="actor"
                            options={actors}
                            onChange={this.onChange}
                        />
                        <PredictionDropdown
                            title="Director"
                            name="director"
                            options={directors}
                            onChange={this.onChange}
                        />
                        <PredictionDropdown
                            title="Genre"
                            name="genre"
                            options={genres}
                            onChange={this.onChange}
                        />
                    </form>
                    <button
                        className="prediction-button"
                        onClick={this.getPrediction}
                    >
                        Get Prediction
                    </button>
                    <div className="prediction-amount">
                        $ {parseInt(parseFloat(estimated_boxoffice) / 1e6)}{" "}
                        million
                    </div>
                </div>
            </div>
        );
    }
}

PredictionContainer.propTypes = {
    getOptions: PropTypes.func.isRequired,
    getPrediction: PropTypes.func.isRequired,
    options: PropTypes.object.isRequired,
    prediction: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
    options: state.predictions.options,
    prediction: state.predictions.prediction,
});

export default connect(mapStateToProps, { getOptions, getPrediction })(
    PredictionContainer
);
