from flask import Flask , render_template
import os 
from flask_cors import CORS
from src.api.routes import api_blueprint
from src.modeling.prophet_model import train_model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def create_app():
    app = Flask(__name__,  
                template_folder=os.path.join(BASE_DIR, "templates"))

    CORS(app)
    train_model(
        data_path=r"C:\Users\Pratibha\OneDrive\Desktop\DATA SCIENCE RESOURCES\revenue-forecasting-scenario-planning\revenue-forecasting-scenario-planning\data\processed\monthly_revenue_processed_ALL_YEARS_CORRECT.csv"
    )
    
    app.register_blueprint(api_blueprint, url_prefix="/api")


    # Serve frontend
    @app.route("/")
    def home():
        return render_template("index.html")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
