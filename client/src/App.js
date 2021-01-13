import { Provider } from "react-redux";
import store from "./store";
import "./App.css";
import PredictionContainer from "./components/PredictionContainer";
import Title from "./components/Title";
// import Intro from "./components/Intro";

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
