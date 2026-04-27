# 💹 Financial Risk & Forecasting System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

**A multi-module for real-time risk analysis and forecasting.**

</div>

---

## 📌 Overview

The **Financial Risk & Forecasting System** (FINRISK) is a production-ready, interactive web application built with Streamlit that brings together four machine learning models under a single, elegant dark-themed dashboard. It enables users to make real-time predictions across stock markets, loan approvals, fraud detection, and customer segmentation — all without writing a single line of code.

> Designed for analysts, fintech developers, and data science enthusiasts looking to explore applied ML in the financial domain.

---

## ✨ Features

- 🌗 **Modern dark UI** — Glassmorphism design with animated gradients and glowing components
- ⚡ **Real-time predictions** — Instant results powered by pre-trained `.pkl` models
- 📊 **Interactive charts** — Plotly-powered visualizations including gauges, pie charts, and scatter plots
- 📂 **Bulk CSV upload** — Batch analysis for fraud detection with downloadable results
- 🧠 **4 independent AI modules** — Each module tackles a distinct financial problem
- 📱 **Responsive layout** — Clean sidebar navigation with live model status indicators

---

## 🧩 Modules

### 📈 1. Stock Price Predictor
> **Algorithm:** Linear Regression

Forecasts the next day's stock closing price based on the current day's price. Provides:
- Predicted closing price with directional indicator (bullish / bearish)
- Percentage change estimate
- Interactive candlestick-style visualization
- A simulated 30-day trend chart

**Input:** Current stock price

---

### 🏦 2. Loan Approval System
> **Algorithm:** Logistic Regression + Standard Scaler

Predicts whether a loan application will be **Approved** or **Rejected** using key financial and personal attributes. Provides:
- Binary approval decision with confidence probability
- Risk breakdown across income, CIBIL score, and loan metrics
- Color-coded result badge (green = Approved, red = Rejected)

**Inputs:**

| Parameter | Description |
|---|---|
| Annual Income | Applicant's yearly income (₹) |
| CIBIL Score | Credit score (300–900) |
| Loan Amount | Requested loan value (₹) |
| Loan Term | Duration in months |
| Employment Status | Employed / Self-Employed / Unemployed |
| Loan Purpose | Home / Education / Personal / Business |
| Number of Dependents | Financial dependents count |
| Assets Value | Total collateral assets (₹) |

---

### 🔍 3. Credit Card Fraud Detection
> **Algorithm:** Random Forest Classifier

Detects fraudulent credit card transactions using 30 PCA-transformed features (V1–V28, Amount, Time). Supports both:
- **Single transaction** analysis with fraud probability gauge
- **Bulk CSV upload** for batch prediction with downloadable results

**Inputs:** 30 PCA-transformed numerical features (V1–V28, Amount, Time)

**Output:** Fraud / Legitimate prediction + probability score + visual breakdown

---

### 👥 4. Customer Segmentation
> **Algorithm:** K-Means Clustering (k=4)

Classifies customers into behavioral segments based on their spending score for targeted marketing. Supports both single-customer and bulk analysis.

**Segments:**

| Cluster | Segment | Description | Strategy |
|---|---|---|---|
| 0 | 🛒 Budget Shoppers | Low spending, value-focused | Discount campaigns, loyalty points |
| 1 | 🛍️ Standard Customers | Moderate spending, balanced | Seasonal promotions, email campaigns |
| 2 | 💎 Premium Spenders | High spending, brand-conscious | VIP events, personalized offers |
| 3 | 👑 Ultra Premium | Highest spenders, luxury buyers | Exclusive memberships, concierge service |

**Input:** Spending Score (1–100)

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/financial-risk-forecasting-system.git
cd financial-risk-forecasting-system
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📦 Dependencies

```txt
streamlit
numpy
pandas
scikit-learn
plotly
joblib
```

> Create a `requirements.txt` by running: `pip freeze > requirements.txt`

---

## 🚀 Usage

1. **Launch** the app using `streamlit run app.py`
2. **Navigate** using the sidebar to select a module
3. **Input** the required financial parameters for your chosen module
4. **Click Predict** to run the ML model instantly
5. **Analyze** the result using the visual charts and metric cards

---

## 📁 Project Structure

```
financial-risk-forecasting-system/
│
├── app.py                    # Main Streamlit application
│
├── models/                   # Pre-trained ML model files
│   ├── stock_model.pkl       # Linear Regression — Stock price predictor
│   ├── loan_model.pkl        # Logistic Regression — Loan approval classifier
│   ├── loan_scaler.pkl       # Standard Scaler — Feature normalizer for loan model
│   ├── fraud_model.pkl       # Random Forest — Fraud detection classifier
│   └── kmeans_model.pkl      # K-Means — Customer segmentation model
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🤖 ML Models

| Module | Algorithm | Input Features | Output |
|---|---|---|---|
| Stock Predictor | Linear Regression | 1 (Current Price) | Next-day price |
| Loan Approval | Logistic Regression | 8 financial/personal | Approved / Rejected |
| Fraud Detection | Random Forest | 30 PCA features | Fraud / Legitimate |
| Customer Segments | K-Means (k=4) | 1 (Spending Score) | Segment 0–3 |

All models are pre-trained, serialized using `joblib`, and loaded at runtime via `@st.cache_resource` for optimal performance.

---



## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

Please keep code clean, well-commented, and consistent with the existing style. For major changes, open an issue first to discuss your proposal.

---

## 📄 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/amit-kumar-maurya-b23281253) or reach out if you have questions or feedback!
Test update from responsiveness branch
---



<div align="center">


**⭐ Star this repo if you found it useful!**
</div>


