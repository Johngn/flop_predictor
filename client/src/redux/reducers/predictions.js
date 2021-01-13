import {
    GET_PREDICTION,
    PREDICTION_LOADING,
    GET_OPTIONS,
} from "../actions/types";

const initialState = {
    loading: false,
    options: {
        actors: [],
        directors: [],
        genres: [],
    },
    prediction: {},
};

export default function predictionReducer(state = initialState, action) {
    switch (action.type) {
        case GET_PREDICTION:
            return {
                ...state,
                prediction: action.payload,
                loading: false,
            };
        case GET_OPTIONS:
            return {
                ...state,
                options: action.payload,
                loading: false,
            };
        case PREDICTION_LOADING:
            return {
                ...state,
                loading: true,
            };
        default:
            return state;
    }
}
