import { PREDICTION_LOADING, GET_PREDICTION, GET_OPTIONS } from "./types";
import axios from "axios";
import FormData from "form-data";

export const setPredictionLoading = () => {
    return {
        type: PREDICTION_LOADING,
    };
};

export const getOptions = () => dispatch => {
    axios
        .get(
            process.env.NODE_ENV === "development"
                ? process.env.REACT_APP_API_URL_DEVELOPMENT
                : process.env.REACT_APP_API_URL_PRODUCTION
        )
        .then(res => dispatch({ type: GET_OPTIONS, payload: res.data }))
        .catch(err => console.log(err));
};

export const getPrediction = params => dispatch => {
    dispatch(setPredictionLoading());

    const formData = new FormData();

    formData.append("director", params.director);
    formData.append("actor", params.actor);
    formData.append("genre", params.genre);
    formData.append("budget", params.budget * 1e6);
    formData.append("duration", params.duration);
    formData.append("avg_vote", params.score);

    axios
        .post(
            `${
                process.env.NODE_ENV === "development"
                    ? process.env.REACT_APP_API_URL_DEVELOPMENT
                    : process.env.REACT_APP_API_URL_PRODUCTION
            }/predict_boxoffice`,
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        )
        .then(res =>
            dispatch({
                type: GET_PREDICTION,
                payload: res.data,
            })
        );
};
