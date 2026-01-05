from flask import Blueprint, jsonify
from src.modeling.prophet_model import (
    get_forecast,
    train_model,
    get_training_metadata
)
from src.utils.stress_testing import apply_demand_stress


api_blueprint = Blueprint("api", __name__)

# Health check

@api_blueprint.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Revenue Forecasting API is running"
    })


# Forecast endpoint
@api_blueprint.route("/forecast", methods=["GET"])
def forecast():
    forecast_df = get_forecast()

    response = {
        "dates": forecast_df["ds"].astype(str).tolist(),
        "base": forecast_df["yhat"].tolist(),
        "upside": forecast_df["yhat_upper"].tolist(),
        "downside": forecast_df["yhat_lower"].tolist()
    }

    return jsonify(response)


# Scenario summary endpoint

@api_blueprint.route("/scenario-summary", methods=["GET"])
def scenario_summary():
    forecast_df = get_forecast().tail(12)

    base = forecast_df["yhat"].sum()
    upside = forecast_df["yhat_upper"].sum()
    downside = forecast_df["yhat_lower"].sum()

    return jsonify({
        "base_12m": float(base),
        "upside_12m": float(upside),
        "downside_12m": float(downside),
        "revenue_at_risk": float(base - downside)
    })

@api_blueprint.route("/stress-scenario", methods=["GET"])
def stress_scenario():
    """
    Simulate exogenous demand shock scenarios
    """
    forecast_df = get_forecast().tail(12)

    stress_levels = {
        "mild": 0.05,
        "moderate": 0.10,
        "severe": 0.15
    }

    results = {}

    for name, pct in stress_levels.items():
        stressed = apply_demand_stress(forecast_df, pct)
        results[name] = {
            "stress_pct": pct,
            "stressed_revenue_12m": float(stressed["yhat_stressed"].sum())
        }

    return jsonify(results)


# Retrain model endpoint

@api_blueprint.route("/retrain", methods=["POST"])
def retrain():
    try:
        train_model(
            data_path=r"C:\Users\Pratibha\OneDrive\Desktop\DATA SCIENCE RESOURCES\revenue-forecasting-scenario-planning\revenue-forecasting-scenario-planning\data\processed\monthly_revenue_processed_ALL_YEARS_CORRECT.csv"
        )

        metadata = get_training_metadata()

        return jsonify({
            "status": "success",
            "message": "Model retrained successfully",
            "last_trained_at": metadata["last_trained_at"]
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
