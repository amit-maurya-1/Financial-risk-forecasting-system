# 💹 Financial Risk & Forecasting System

A complete Streamlit-based AI-powered financial intelligence suite with 4 ML models.

## 🚀 Setup & Run

```bash
# 1. Place your model files in the models/ folder
#    Required files:
#    - models/stock_model.pkl       (LinearRegression - Stock Price)
#    - models/loan_model.pkl        (LogisticRegression - Loan Approval)
#    - models/loan_scaler.pkl       (StandardScaler - Loan features)
#    - models/fraud_model.pkl       (RandomForestClassifier - Fraud Detection)
#    - models/kmeans_model.pkl      (KMeans - Customer Segmentation)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

## 📊 Models & Features

| Module | Model | Features | Output |
|--------|-------|----------|--------|
| Stock Predictor | Linear Regression | Current price | Next-day price |
| Loan Approval | Logistic Regression | Income, CIBIL, Loan Amount, Term, Education, Employment | Approved / Rejected |
| Fraud Detection | Random Forest | Time, V1–V28, Amount (30 features) | Fraud / Legitimate |
| Customer Segments | K-Means (4 clusters) | Spending Score | Segment ID (0–3) |

## 🗂️ Project Structure

```
financial_risk_app/
├── app.py              ← Main Streamlit application
├── requirements.txt    ← Python dependencies
├── README.md
└── models/
    ├── stock_model.pkl
    ├── loan_model.pkl
    ├── loan_scaler.pkl
    ├── fraud_model.pkl
    └── kmeans_model.pkl
```
