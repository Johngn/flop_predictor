import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import rootReducer from './redux/reducers';

const composedEnhancers = composeWithDevTools(applyMiddleware(thunk));

const store = createStore(rootReducer, {}, composedEnhancers);

export default store;
