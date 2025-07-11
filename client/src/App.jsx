import React, { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [form, setForm] = useState({
    age: '',
    income: '',
    credit_score: '',
    loan_amount: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   try {
  //     const res = await axios.post('http://localhost:4000/predict', form);
  //     setResult(res.data.result);
  //   } catch (err) {
  //     setResult("Error predicting result");
  //   }
  // };

  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    const payload = {
      Age: parseInt(form.age),
      Income: parseFloat(form.income),
      CreditScore: parseInt(form.credit_score),
      LoanAmount: parseFloat(form.loan_amount)
    };

    // const res = await axios.post('http://localhost:5000/predict', payload); // also fix port
    const res = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/predict`, payload)

    setResult(res.data.result);
  } catch (err) {
    setResult("Error predicting result");
  }
};


  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <form className="bg-white p-8 rounded-xl shadow-md w-96" onSubmit={handleSubmit}>
        <h1 className="text-2xl font-bold mb-4">Loan Approval Checker</h1>
        {['age', 'income', 'credit_score', 'loan_amount'].map((field) => (
          <div className="mb-4" key={field}>
            <label className="block mb-1 capitalize">{field.replace('_', ' ')}</label>
            <input
              type="number"
              name={field}
              value={form[field]}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>
        ))}
        <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
          Check
        </button>
        {result && (
          <p className="mt-4 text-lg font-semibold text-center">
            Result: {result}
          </p>
        )}
      </form>
    </div>
  );
}
