# Loan Approval Application

A complete loan approval application with React frontend, Express.js server, and Python ML model.

## Project Structure

```
loan-approval-app/
├── client/          # React frontend (Port 3000)
├── server/          # Express.js API server (Port 4000)
├── ml-model/        # Python Flask ML service (Port 5000)
└── package.json     # Root package.json for managing the entire project
```

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm

## Quick Start

1. **Install all dependencies and setup the project:**
   ```bash
   npm run setup
   ```

2. **Start all services:**
   ```bash
   npm run dev
   ```

This will start:
- ML Model service on http://localhost:5000
- Express server on http://localhost:4000
- React client on http://localhost:3000

## Manual Setup

If you prefer to set up components individually:

### 1. Install Node.js dependencies
```bash
npm run install:all
```

### 2. Install Python dependencies
```bash
npm run install:python
```

### 3. Train the ML model
```bash
npm run train:model
```

### 4. Start individual services

Start ML model service:
```bash
npm run start:ml
```

Start Express server:
```bash
npm run start:server
```

Start React client:
```bash
npm run start:client
```

## Usage

1. Open your browser and go to http://localhost:3000
2. Fill in the loan application form:
   - Age
   - Income
   - Credit Score
   - Loan Amount
3. Click "Check" to get the loan approval prediction

## API Endpoints

- `POST /predict` - Predicts loan approval based on input data

## Technologies Used

- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: Express.js, Node.js
- **ML Model**: Python, Flask, Scikit-learn
- **Other**: Axios for API calls, CORS for cross-origin requests
