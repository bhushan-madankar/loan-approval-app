# ml_model/app.py

from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(f"📥 Received data: {data}")
    try:
        features = np.array([
            data['Age'],
            data['Income'],
            data['CreditScore'],
            data['LoanAmount']
        ]).reshape(1, -1)

        # Optional: If using a scaler, include this line
        # features = scaler.transform(features)

        prediction = model.predict(features)[0]
        return jsonify({'result': 'Approved' if prediction == 1 else 'Rejected'})
    except Exception as e:
        print(f"❌ Error in /predict: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
