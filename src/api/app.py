from flask import Flask
from flask_cors import CORS
from src.api.routes import api_blueprint
from src.modeling.prophet_model import load_and_train_model

def create_app():
    app = Flask(__name__)

    CORS(app)
    # Load model ONCE at startup
    load_and_train_model(
        data_path=r"C:\Users\Pratibha\OneDrive\Desktop\DATA SCIENCE RESOURCES\revenue-forecasting-scenario-planning\revenue-forecasting-scenario-planning\data\processed\monthly_revenue_processed_ALL_YEARS_CORRECT.csv"
    )

    app.register_blueprint(api_blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
