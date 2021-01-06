import { Provider } from "react-redux";
import store from "./store";
import "./App.css";
import PredictionContainer from "./components/PredictionContainer";
import Title from "./components/Title";

function App() {
    return (
        <Provider store={store}>
            <div className="App">
                <Title />
                <PredictionContainer />
            </div>
        </Provider>
    );
}

export default App;
