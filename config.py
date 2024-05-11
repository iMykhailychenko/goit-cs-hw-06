from pathlib import Path

from dotenv import dotenv_values

config = dotenv_values(".env")


DB_URI = config["DB_URI"]
FRONT_FOLDER = config["FRONT_FOLDER"]
BASE_DIR = Path(__file__).parent / config["FRONT_FOLDER"]
CHUNK_SIZE = int(config["CHUNK_SIZE"]) or 1024
HTTP_PORT = int(config["HTTP_PORT"]) or 3000
SOCKET_PORT = int(config["SOCKET_PORT"]) or 5000
HTTP_HOST = config["HTTP_HOST"]
SOCKET_HOST = config["SOCKET_HOST"]
