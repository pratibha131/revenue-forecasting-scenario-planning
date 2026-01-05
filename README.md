# 📊 Revenue Forecasting & Scenario Planning System

**Live Demo: https://revenue-forecasting-scenario-planning-1.onrender.com**

⏳ Initial load may take a few seconds due to cold start on cloud hosting.

---

## 🔥 Executive Summary

This project delivers a production-grade revenue forecasting and scenario planning system designed to support business decision-making under uncertainty.

Rather than optimizing for point predictions alone, the system explicitly models trend, seasonality, uncertainty, and downside risk, enabling leadership to answer “what happens if things go wrong?” — not just “what is the forecast?”.

The final output is a live, deployed dashboard and API that translates machine-learning forecasts into clear, executive-level insights.

---

## 📈 Business Problem

In volatile macroeconomic environments, revenue planning based on single-point forecasts is fragile.

Decision-makers need to understand:

1.Expected revenue over the next 12 months

2.How much revenue is at risk under adverse conditions

3.Sensitivity to demand shocks (mild, moderate, severe)

4.Whether to prioritize growth, cost control, or capacity expansion

This project reframes forecasting as risk-aware planning, not just prediction.

--- 

## 💡 Business Impact

This system enables leaders to:

1.Quantify 12-month revenue uncertainty

2. Measure downside exposure (revenue-at-risk)

3. Compare base vs upside vs downside outcomes

4. Stress-test plans under macro shocks (−5%, −10%, −15%)

5. Make informed decisions on budgeting, staffing, and cost strategy

👉 The output supports strategic planning, not just reporting.

---

## 🧠 Machine Learning & Modeling Approach 

#### Why Time-Series Modeling (Not Generic ML)?

1. Revenue is:

Sequential

Seasonal

Trend-driven

2. Impacted by structural shocks

Using standard regression or black-box ML would obscure interpretability and risk.

Model Choice: Prophet

Prophet was selected because it explicitly models:

i) Long-term trend

ii) Annual seasonality

iii) Uncertainty intervals (prediction bands)

This allows the system to generate probabilistic forecasts, not just point estimates.

Modeling Philosophy

✔ Benchmarked against naive and seasonal baselines

✔ Prioritized interpretability and uncertainty over raw MAE

❌ Did not over-optimize point accuracy at the expense of decision clarity

The goal was business usefulness, not leaderboard metrics.

--- 

### 🧪 Scenario Planning & Stress Testing

Forecasts are converted into decision scenarios:

1. Base case: expected outcome

2. Upside: optimistic demand realization

3. Downside: adverse realization

Additional exogenous stress tests simulate macro shocks:

−10% demand

This allows leadership to quantify:

Revenue-at-risk

Sensitivity to external shocks

Downside exposure before committing resources

---
## 🚀 Live Demo Screenshots
<img width="1402" height="554" alt="image" src="https://github.com/user-attachments/assets/8032a30c-8bfb-4e6d-87c4-a8eab5d3f7de" />
<img width="763" height="552" alt="image" src="https://github.com/user-attachments/assets/510dada6-ff3e-4be7-a6e6-3c517fcb5db0" />
<img width="780" height="580" alt="image" src="https://github.com/user-attachments/assets/c00d7071-7a12-4eb9-ba02-bf3d83090b0c" />
<img width="1382" height="534" alt="image" src="https://github.com/user-attachments/assets/36cdc843-b7db-4c19-8760-53fb05d0f1dd" />
<img width="1382" height="527" alt="image" src="https://github.com/user-attachments/assets/6693c149-409e-46b7-979f-bac934326d36" />
<img width="1089" height="861" alt="image" src="https://github.com/user-attachments/assets/619a4aa7-2d38-46b4-afa6-b72527f617a4" />
<img width="1384" height="536" alt="image" src="https://github.com/user-attachments/assets/0f331f1c-a855-44ac-b8fb-d714853655b1" />

---

## 🧩 System Architecture

User (Browser)
   ↓
Frontend Dashboard (HTML + JS)
   ↕
Flask REST API
   ↕
Cached Prophet Model
   ↕
Stress Scenario Logic
   ↕
Cleaned Monthly Revenue Dataset

The model is trained once at startup and reused for fast inference.

---

## 🚀 Key Features

| Feature               | Description                                           |
| --------------------- | ----------------------------------------------------- |
| Scenario Forecasts    | Base, upside, and downside forecasts with uncertainty |
| Revenue-at-Risk       | Quantifies potential downside exposure                |
| Stress Testing        | Simulates macro demand shocks                         |
| REST APIs             | Forecast, scenarios, retraining                       |
| Controlled Retraining | Batch retrain endpoint                                |
| Live Deployment       | Cloud-hosted dashboard and API                        |

---

## 📦 Repository Structure
├── data/
│   ├── raw/                          # Original dataset
│   └── processed/                    # Cleaned monthly revenue data
├── notebooks/                        # Analysis & modeling workflow
│   ├── 01_eda.ipynb
│   ├── 02_time_series_decomposition.ipynb
│   ├── 03_baseline_forecast.ipynb
│   ├── 04_prophet_forecast.ipynb
│   └── 05_scenario_planning.ipynb
├── src/
│   ├── api/                          # Flask app & routes
│   ├── modeling/                     # Prophet training & inference
│   └── utils/                        # Stress testing logic
├── Procfile                          # Deployment config
├── requirements.txt
└── README.md

---

## 🚀 Live API Endpoints

| Endpoint                | Method | Description                            |
| ----------------------- | ------ | -------------------------------------- |
| `/api/`                 | GET    | Health check                           |
| `/api/forecast`         | GET    | Full forecast (base, upside, downside) |
| `/api/scenario-summary` | GET    | 12-month aggregated scenarios          |
| `/api/stress-scenario`  | GET    | Exogenous stress outcomes              |
| `/api/retrain`          | POST   | Controlled model retraining            |

Example usage:

```bash
# Base forecast
curl https://revenue-forecasting-scenario-planning-1.onrender.com/api/forecast

# Scenario totals
curl https://revenue-forecasting-scenario-planning-1.onrender.com/api/scenario-summary

# Stress test
curl https://revenue-forecasting-scenario-planning-1.onrender.com/api/stress-scenario
```

---

## 🛠 Run Locally

```bash
git clone https://github.com/pratibha131/revenue-forecasting-scenario-planning.git
cd revenue-forecasting-scenario-planning

python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
python -m src.api.app
```

Open:

```cpp
http://127.0.0.1:5000
```

---

## 🔬 Analysis Notebooks (Optional Deep Dive)

The notebooks document the analytical reasoning behind modeling choices:

1. EDA and trend inspection

2. Seasonality decomposition

3. Baseline benchmarking

4. Prophet modeling

5. Scenario aggregation

They support transparency and reproducibility but are not required to run the system.

---

## 🔮 Future Improvements

Add external macro drivers (CPI, pricing indices)

Automated scheduled retraining

Authentication for retraining endpoint

CI/CD pipeline (GitHub Actions → Cloud)

--- 

## 📝 Final Takeaway

This project demonstrates end-to-end data science maturity:

Machine learning grounded in business context

Risk-aware forecasting, not blind prediction

System design and deployment

Executive-level communication of uncertainty
