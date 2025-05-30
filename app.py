from flask import Flask, request, jsonify
from predict import predict_churn

app = Flask(__name__)

@app.route('/')
def index():
    return "Churn Prediction API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    output = predict_churn(data)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
