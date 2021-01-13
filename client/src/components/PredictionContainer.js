import React, { Component } from "react";
import { connect } from "react-redux";
import { getOptions, getPrediction } from "../redux/actions/predictions";
import PropTypes from "prop-types";
import PredictionRangeSlider from "./PredictionRangeSlider";
import PredictionDropdown from "./PredictionDropdown";

class PredictionContainer extends Component {
    state = {
        selectedActor: "",
        selectedDirector: "",
        selectedGenre: "",
        budget: 0,
        duration: 0,
        score: 0,
    };

    componentDidMount() {
        this.props.getOptions();
    }

    setActor = e => {
        console.log(e.target.value);
        this.setState({
            selectedActor: e.target.value,
        });
    };

    setDirector = e => {
        console.log(e.target.value);
        this.setState({
            selectedDirector: e.target.value,
        });
    };

    setGenre = e => {
        console.log(e.target.value);
        this.setState({
            selectedGenre: e.target.value,
        });
    };

    setBudget = e => {
        console.log(e.target.value);
        this.setState({
            budget: e.target.value,
        });
    };

    setDuration = e => {
        console.log(e.target.value);
        this.setState({
            duration: e.target.value,
        });
    };

    setScore = e => {
        console.log(e.target.value);
        this.setState({
            score: e.target.value,
        });
    };

    getPrediction = () => {
        const params = {
            actor: this.state.selectedActor,
            director: this.state.selectedDirector,
            genre: this.state.selectedGenre,
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
                            name="Budget"
                            min="0"
                            max="500"
                            step="1"
                            setNumber={this.setBudget}
                        />
                        <PredictionRangeSlider
                            text2=" mins"
                            number={this.state.duration}
                            name="Duration"
                            min="0"
                            max="200"
                            step="1"
                            setNumber={this.setDuration}
                        />
                        <PredictionRangeSlider
                            number={this.state.score}
                            name="Score"
                            min="0"
                            max="10"
                            step="0.1"
                            setNumber={this.setScore}
                        />
                        <PredictionDropdown
                            name="Actor"
                            setOption={this.setActor}
                            options={actors}
                        />
                        <PredictionDropdown
                            name="Director"
                            setOption={this.setDirector}
                            options={directors}
                        />
                        <PredictionDropdown
                            name="Genre"
                            setOption={this.setGenre}
                            options={genres}
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
