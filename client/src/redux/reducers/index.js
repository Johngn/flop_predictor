import { combineReducers } from "redux";
import predictionReducer from "./predictions";

export default combineReducers({
    predictions: predictionReducer,
});
