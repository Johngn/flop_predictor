from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/get_directors')
def get_directors():
    response = jsonify({
        'directors': utils.get_director_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_boxoffice', methods=['POST'])
def predict_boxoffice():
    duration = float(request.form['duration'])
    avg_vote = float(request.form['avg_vote'])
    budget = float(request.form['budget'])
    actor = request.form['actor']
    director = request.form['director']
    genre = request.form['genre']
    
    response = jsonify({
        'estimated_boxoffice': utils.get_estimated_boxoffice(duration,avg_vote,budget,actor,director,genre)
        })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == "__main__":
    print("Starting python flask server")
    utils.load_saved_assets()
    app.run()