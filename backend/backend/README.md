# Asthma AI Predictor

## Project Overview
Asthma AI Predictor is a machine learning based web application that predicts asthma risk using patient health and environmental data.

## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy

## Machine Learning Algorithm
Random Forest Classifier

## Steps to Run the Project

1. Clone the repository

git clone <repository-link>

2. Open project folder

cd Astma_predictor

3. Go to backend folder

cd backend

4. Create virtual environment

python -m venv .venv

5. Activate virtual environment

For PowerShell:
.\.venv\Scripts\Activate.ps1

For Command Prompt:
.venv\Scripts\activate

6. Install required libraries

pip install fastapi uvicorn numpy pandas scikit-learn

7. Run the backend server

python -m uvicorn app:app --reload

8. Open browser

http://127.0.0.1:8000/docs

## Features
- Asthma risk prediction
- AI based analysis
- Environmental data integration
- Interactive frontend UI
- REST API backend

## Author
Rajeshwari N
