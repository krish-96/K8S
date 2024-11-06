from flask import Flask
from logger_service import logger

# Log an info message to indicate that the application has started
logger.info("Application started.")

app = Flask(__name__)

no_of_hits = 0


@app.route('/')
def welcome_page():
    global no_of_hits
    logger.debug(f"Request received!")

    msg = f"""<h1 style="color:red;text-align:center;">Welcome to Flask Application Tutorial!</h1><br><p style="background-color:black;color:yellow;text-align:center; padding: 25px;border: 2px solid blue;">We're going to learn something new from here</p><p style="background-color:black;color:yellow;text-align:center; padding: 25px;border: 2px solid blue;">Recevied {no_of_hits} requests</p>"""

    logger.info(msg)

    logger.debug(f"Response returned!")
    no_of_hits += 1

    return msg


@app.route('/req_count')
def request_count():
    global no_of_hits
    logger.info(f"Request Count received!")
    msg = f"""<h1 style="color:red;text-align:center;">Welcome to Flask Application Tutorial!<br>(We're going to learn something new from here)</h1><br><p style="background-color:black;color:yellow;text-align:center; padding: 25px;border: 2px solid blue;">Recevied {no_of_hits} requests</p>"""
    logger.info(msg)
    logger.debug(f"Returning the count!")
    return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
