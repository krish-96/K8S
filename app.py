from flask import Flask
from logger_service import logger

# Log an info message to indicate that the application has started
logger.info("Application initialized")

app = Flask(__name__)

welcome_message = """
    <h1 style="color:red;text-align:center;padding:25px;">Welcome to Kubernetes - Flask Tutorial!</h1>
    <p style="text-align:center;padding:22px;font-size:22px;">
        We're going to learn something new from here
    </p>
    <div style="text-align:center;padding:20px;font-size:20px;">  
        So far we processed 
            <span style="color:blue;font-size:55px;">
                {no_of_hits:02}
            </span>
             {requests}
    </div>
    """


class Cache(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.__count = 0
        return cls.__instance

    @staticmethod
    def get(increase=False):
        """This method will return the current count
        If the increase value is given, it's True, then it'll increase the value by 1
        """
        current_count = Cache.__instance.__count
        if increase is True:
            Cache.__instance.__count += 1
        return current_count


@app.route('/')
def welcome_page():
    no_of_hits = Cache().get(increase=True) + 1
    logger.debug(f"Request received!")
    logger.info(f"Processing the {no_of_hits} request")
    logger.debug(f"Response returned!")
    return welcome_message.format(no_of_hits=no_of_hits, requests="request" if no_of_hits == 1 else "requests")


@app.route('/stats')
def request_count():
    logger.info(f"Request Count received!")
    no_of_hits = Cache().get()
    logger.info(f"Processed fetching the count request")
    logger.debug(f"Returning the count!")
    return welcome_message.format(no_of_hits=no_of_hits, requests="request" if no_of_hits == 1 else "requests")


if __name__ == '__main__':
    logger.info("Application running...")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
