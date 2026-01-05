# 📊 Revenue Forecasting & Scenario Planning System

**Live Demo:** https://revenue-forecasting-scenario-planning-1.onrender.com/ 
It might take sometime to load 
---

## 🔥 Executive Summary

This project delivers an **end-to-end forecasting system** that goes beyond point predictions to quantify **uncertainty, downside risk, and revenue-at-risk** — empowering business decisions under macroeconomic volatility.

Unlike standard forecasting projects, this system:

- Provides **multi-scenario revenue forecasts** (base, upside, downside)
- Simulates **stress scenarios** (e.g., −5%, −10%, −15% demand shocks)
- Converts outputs into **business-actionable insights**
- Offers a **live interactive dashboard**
- Serves REST APIs and supports controlled batch retraining

👉 This is a **production-ready analytics system** built with real deployment, not just a notebook.

---

## 📈 Why This Matters (Business Impact)

In uncertain economic environments, leadership needs answers to questions like:

- What’s the expected revenue over the next 12 months?
- How much revenue is at risk if demand weakens?
- What happens under mild, moderate, or severe stress?
- How should we adjust operations or cost strategy accordingly?

This system turns forecasting into **decision support**, not just prediction.

---

## 🧠 Key Features

| Feature | Description |
|---------|-------------|
| Base/Scenario Forecasts | Generates base, upside, and downside forecasts with uncertainty bands |
| Revenue-at-Risk | Quantifies potential loss under adverse scenarios |
| Stress Testing | Applies macroeconomic stress multipliers (e.g., −10%) post-forecast |
| REST APIs | Endpoints for forecast, scenarios, retraining |
| Controlled Retraining | Batch retraining endpoint (`POST /api/retrain`) |
| Live Deployment | Hosted service with interactive UI and API |

---

## 🧩 Architecture Overview

User (Browser)
↓
Frontend (Dashboard UI)
↕
Flask API (REST)
↕
Prophet Model (trained once at startup)
↕
Stress Scenario Logic
↕
CSV Revenue Dataset


---

## 🚀 Live Demo Screenshots

(*Include these after you capture them locally* — see below for instructions)



---

## 📦 What’s Inside the Repo

├── data/
│ └── processed/
│ └── monthly_revenue_…csv # Clean revenue dataset
| └── raw/
│ └── monthly_revenue_…csv # dataset
├── src/
│ ├── api/
│ │ ├── app.py # Flask app entrypoint
│ │ ├── routes.py # API routes
│ │ └── templates/index.html # Frontend dashboard
│ ├── modeling/
│ │ └── prophet_model.py # Forecast training & caching
│ └── utils/
│ └── stress_testing.py # Stress scenario helpers
├── Procfile # Render deployment config
├── requirements.txt # Python deps
└── README.md


---

## 🚀 Live API Endpoints

Use these to integrate or test:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/` | GET | Health check |
| `/api/forecast` | GET | Full forecast (base + upside + downside arrays) |
| `/api/scenario-summary` | GET | 12-month aggregate revenue scenarios |
| `/api/stress-scenario` | GET | Exogenous stress outcomes |
| `/api/retrain` | POST | Retrain model with updated data |

Examples:

```bash
# Base forecast
curl http://<your-app>.onrender.com/api/forecast

# Scenario totals
curl http://<your-app>.onrender.com/api/scenario-summary

# Stress test
curl http://<your-app>.onrender.com/api/stress-scenario

```

--- 

## 🧠 Technical Decisions

✅ Prophet was chosen due to its ability to model:

trend

yearly seasonality

uncertainty intervals

❌ We did not force stationarity or optimize solely for point accuracy — because business value lies in risk interpretation, not lowest MAE.

👉 We built stress scenarios post-forecast to realistically assess sensitivity under macro conditions.

---

🛠 Run Locally (Quick Start)

Clone the repo:

`git clone https://github.com/pratibha131/revenue-forecasting-scenario-planning.git
cd revenue-forecasting-scenario-planning`


Create a virtual environment & install deps:

`python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt `


Run the app:

`python -m src.api.app`


Open in browser:

`http://127.0.0.1:5000`

---

## 🧠 Future Improvements

✔ Add exogenous macro drivers (e.g., CPI, pricing)
✔ Schedule automated retraining jobs
✔ Add user authentication for retrain endpoint
✔ Add CI/CD (GitHub Actions → Render)

---

## 📝 Final Takeaway

This project demonstrates end-to-end analytics capability, combining:

Statistical modeling

Risk awareness

System design

Deployment & productization

Business communication
