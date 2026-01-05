import pandas as pd
from prophet import Prophet
from datetime import datetime

MODEL = None
FORECAST = None
LAST_TRAINED_AT = None


def train_model(data_path: str):
    """
    Train Prophet model and cache forecast
    """
    global MODEL, FORECAST, LAST_TRAINED_AT

    df = pd.read_csv(data_path)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df = df.sort_values("Date")

    prophet_df = df.rename(columns={
        "Date": "ds",
        "Revenue": "y"
    })

    train = prophet_df[prophet_df["ds"] <= "2018-12"]

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False,
        interval_width=0.8
    )

    model.fit(train)

    future = model.make_future_dataframe(
        periods=12,
        freq="MS"
    )

    forecast = model.predict(future)

    MODEL = model
    FORECAST = forecast
    LAST_TRAINED_AT = datetime.utcnow()


def get_forecast():
    if FORECAST is None:
        raise RuntimeError("Model not trained yet")
    return FORECAST


def get_training_metadata():
    return {
        "last_trained_at": LAST_TRAINED_AT.isoformat() if LAST_TRAINED_AT else None
    }
