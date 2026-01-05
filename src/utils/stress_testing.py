import pandas as pd


def apply_demand_stress(forecast_df: pd.DataFrame, stress_pct: float):
    """
    Apply demand stress to forecast.

    stress_pct: e.g. 0.10 for 10% downside
    """
    stressed = forecast_df.copy()

    stressed["yhat_stressed"] = stressed["yhat"] * (1 - stress_pct)
    stressed["yhat_upper_stressed"] = stressed["yhat_upper"] * (1 - stress_pct)
    stressed["yhat_lower_stressed"] = stressed["yhat_lower"] * (1 - stress_pct)

    return stressed
