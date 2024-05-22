import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URI = str(os.getenv("MONGO_URI"))
    APP_PORT = int(os.getenv("APP_PORT", 3000))
    CORS_ORIGIN = str(os.getenv("CORS_ORIGIN"))
    CORS_ORIGIN_FRONT = str(os.getenv("CORS_ORIGIN_FRONT"))
    CORS_ORIGIN_PROD = str(os.getenv("CORS_ORIGIN_PROD"))
<<<<<<< HEAD
    HOST = str(os.getenv("HOST"))
=======
>>>>>>> af30212a66c0f1111080efec4748a6642ef7843f
