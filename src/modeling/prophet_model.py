import pandas as pd
from prophet import Prophet

MODEL = None
FORECAST = None


def load_and_train_model(data_path: str):
    """
    Train Prophet model once and cache forecast
    """
    global MODEL, FORECAST

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


def get_forecast():
    """
    Return cached forecast
    """
    if FORECAST is None:
        raise RuntimeError("Model not loaded")

    return FORECAST
