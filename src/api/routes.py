from flask import Blueprint, jsonify
from src.modeling.prophet_model import get_forecast

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Revenue Forecasting API is running"
    })


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
