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
        .get("http://localhost:5000/get_options")
        .then(res => dispatch({ type: GET_OPTIONS, payload: res.data }));
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
        .post("http://localhost:5000/predict_boxoffice", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        })
        .then(res =>
            dispatch(
                {
                    type: GET_PREDICTION,
                    payload: res.data,
                },
                console.log(res.data)
            )
        );
};

// export const addFilm = newFilm => dispatch => {
//     dispatch(setWatchlistLoading());

//     axios.post("/api/films", newFilm).then(
//         () =>
//             dispatch({
//                 type: ADD_FILM,
//             }),
//         dispatch(setAlert("Film added to watchlist", "success"))
//     );
// };
