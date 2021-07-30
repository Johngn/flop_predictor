# Flop predictor

<img src="https://raw.githubusercontent.com/Johngn/portfolio/master/src/images/flopimg.png" width="500" />



<!-- ABOUT THE PROJECT -->
## About The Project

Flop predictor is a machine learning application that will predict box office takings of a film based on the director, lead actor, genre, budget, and runtime.


### Built With

* [React](https://reactjs.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [scikit learn](https://scikit-learn.org/stable/index.html)



<!-- GETTING STARTED -->
## Getting Started

The project is divided up into three different main folders: client, server, and model. The model folder contains the data cleaning and manipulation, as well as the training of the model itself. The data is from a freely available IMDB dataset on Kaggle (https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). The server folder contains the flask server that is hosted on Heroku, while the client folder hold the React front end.


<!-- USAGE EXAMPLES -->
## Usage

To use Flop Predictor simply select the director, actor, genre, budget and runtime from the options available. The model is linear, so negative values are possible. However they will only show as making less than $10 million. What will become clear is that the biggest indicator of how money a film will make is how much was spent on it.



