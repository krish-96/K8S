import os
import time
from datetime import datetime

from flask import Flask, jsonify
from utils import get_db_version, get_cache_db_version
from db_setup import SetTestDataBase

from logs_configs import logger

# Module constants
HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
USE_RELOADER = False

app = Flask(__name__)

stdt = SetTestDataBase()
if not stdt.set_test_tables():
    stdt.set_test_data()
stdt.verify_test_data()


@app.route('/', methods=['GET'])
def home():
    logger.info("Home page Accessed")
    logger.info("Home page Accessed requested")
    return jsonify(dict(message="Welcome to Flask Application, To check the DB connection, goto /db-connection"))


@app.route('/db-connection', methods=['GET'])
def db_connection():
    logger.info("DB version page Accessed requested")
    postgres_details = get_db_version()
    time.sleep(2)
    logger.info("DB version page Accessed")
    return jsonify(
        dict(message="Db Connection is valid",
             is_response_from_cache=False,
             connection=postgres_details)
    )


@app.route('/cache/db-connection', methods=['GET'])
def cache_db_connection():
    logger.info("DB version (Cache) page Access requested")
    postgres_details = get_cache_db_version()
    logger.info("DB version (Cache) page Accessed")
    return jsonify(
        dict(
            message="Db Connection is valid",
            is_response_from_cache=True,
            connection=postgres_details
        )
    )


if __name__ == '__main__':
    logger.info("App Starting")
    app.run(debug=DEBUG, host=HOST, port=PORT, use_reloader=USE_RELOADER)
