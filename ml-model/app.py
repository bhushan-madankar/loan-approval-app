# Content is in ChatGPT canvas.
from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = np.array([
            data['age'],
            data['income'],
            data['credit_score'],
            data['loan_amount']
        ]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({'result': 'Approved' if prediction == 1 else 'Rejected'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)