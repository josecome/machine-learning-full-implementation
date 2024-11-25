from app import app
from flask import request, jsonify
from machine_learning import MLModels


@app.route("/api/train_test_evaluate_model/", methods=["POST"])
def train_test_evaluate_model():
    data_type = float(request.form['data_type'])
    new_data = False

    if(data_type == "1"):
        new_data = True
    
    MLModels.test_and_evaluate(new_data)
    test = MLModels.ml_model.predict([[2.4, 1.8, 5.1, 4.2]])
    print('Prediction test: ', test)
    params = ""

    return jsonify({"test:": test, "params": params})


@app.route("/api/ml_predict/", methods=["POST"])
def api():
    v1 = float(request.form['v1'])
    v2 = float(request.form['v2'])
    v3 = float(request.form['v3'])
    v4 = float(request.form['v4'])

    if all(v is not None for v in [v1, v2, v3, v4]):
        MLModels.load_model()
        return MLModels.ml_model.predict([[v1, v2, v3, v4]])
    
    return "Please, fill all fields!"
    