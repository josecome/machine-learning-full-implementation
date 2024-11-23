from app import app
from flask import request, jsonify
from machine_learning import MLModels


def train_test_evaluate_model():
    MLModels.test_and_evaluate()
    print('Prediction test: ', MLModels.ml_model.predict([[2.4, 1.8, 5.1, 4.2]]))


@app.route("/api/ml_predict/", methods=["POST"])
def api():
    v1 = float(request.form['v1'])
    v2 = float(request.form['v2'])
    v3 = float(request.form['v3'])
    v4 = float(request.form['v4'])

    if all(v is not None for v in [v1, v2, v3, v4]):
        return MLModels.ml_model.predict([[v1, v2, v3, v4]])
    
    return "Please, fill all fields!"
    