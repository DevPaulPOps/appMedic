from flask import Flask

from config import Config
from db.mongodb import get_mongo_client
from route.SignalementRoutes import SignalementRoutes
from flask_cors import CORS
<<<<<<< HEAD
from analytics.analytics_routes import AnalyticsRoutes
=======
>>>>>>> af30212a66c0f1111080efec4748a6642ef7843f

app = Flask(__name__)
initialized = False

CORS(
    app,
    origins=[
        Config.CORS_ORIGIN,
        Config.CORS_ORIGIN_FRONT,
        Config.CORS_ORIGIN_PROD,
    ],
)


# @app.before_request
def initialize_database():
    global initialized
    if not initialized:
        client = get_mongo_client()
        try:
            client.admin.command("ping")
            print("MongoDB connection established successfully")
            initialized = True
        except Exception as e:
            print(f"MongoDB connection failed: {e}")


AnalyticsRoutes.init_app(app)
SignalementRoutes.init_app(app)
if __name__ == "__main__":
    initialize_database()
<<<<<<< HEAD
    app.run(host=Config.HOST, debug=True, port=Config.APP_PORT)
=======
    app.run(debug=True, port=Config.APP_PORT)
>>>>>>> af30212a66c0f1111080efec4748a6642ef7843f
