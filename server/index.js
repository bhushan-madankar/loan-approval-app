const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config();

const app = express();
const PORT = 4000;

app.use(cors());
app.use(bodyParser.json());

app.post('/predict', async (req, res) => {
  try {
    // const response = await axios.post('http://localhost:5000/predict', req.body);
    // const response = await axios.post('https://loan-approval-app-dtej.onrender.com/', req.body)

    const FLASK_URL = process.env.FLASK_URL || 'http://localhost:5000';
    const response = await axios.post(`${FLASK_URL}/predict`, req.body);

    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});