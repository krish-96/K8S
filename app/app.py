import socket

from flask import Flask, request, jsonify

from util import get_yaml_data
from logger_service import logger

# Log an info message to indicate that the application has started
logger.info("Application initialized")

# Module Constants
RELEASE_NOTES_PATH = "ReleaseNotes/Releases.yml"
app = Flask(__name__)

welcome_message = """
    <h1 style="color:red;text-align:center;padding:25px;">Welcome to Kubernetes - Flask Tutorial!</h1>
    <p style="text-align:center;padding:22px;font-size:22px;">
        We're going to learn something new from here, Currently we are on V5 version
        Added host name
    </p>
    <div style="text-align:center;padding:20px;font-size:20px;">  
        So far we processed 
            <span style="color:blue;font-size:55px;">
                {no_of_hits:02}
            </span>
             {requests}
    </div>
    """
hostname_message = """
    <div style="text-align:center;padding:20px;font-size:20px;">  
        From Host:
            <span style="color:blue;font-size:55px;">
                {host_name}
            </span>
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


@app.route('/', methods=["GET"])
def welcome_page():
    no_of_hits = Cache().get(increase=True) + 1
    logger.debug("Request received!")
    logger.info(f"Processing the {no_of_hits} request")
    logger.debug("Response returned!")
    logger.debug(f"Processing the request from: {request.host}-(host) | {request.host_url}-(host_url) ")
    logger.debug(f"SubProcess: {socket.gethostname()}")
    message = welcome_message.format(no_of_hits=no_of_hits, requests="request" if no_of_hits == 1 else "requests") \
              + hostname_message.format(host_name=socket.gethostname())
    return message


@app.route('/stats', methods=["GET"])
def stats():
    logger.info("Request Count received!")
    no_of_hits = Cache().get()
    logger.info("Processed fetching the count request")
    logger.debug("Returning the count!")
    return welcome_message.format(no_of_hits=no_of_hits, requests="request" if no_of_hits == 1 else "requests")


@app.route('/is_alive', methods=["GET"])
def is_service_alive():
    logger.info('Requested for server "Life" status!')
    return dict(status=True)


@app.route('/is_healthy', methods=["GET"])
def is_service_healthy():
    logger.info('Requested for server "Health" status!')
    return dict(status=True)


@app.route('/current_version', methods=["GET"])
def current_version():
    logger.info('Requested for server "Current Version"!')
    current_version = get_yaml_data(file_path=RELEASE_NOTES_PATH, property='CurrentRelease')
    # print(request.host_url, request.host)  # http://192.168.29.78:5000/ 192.168.29.78:5000
    releases_url = f"{str(request.host_url).split(request.host, 1)[0]}{request.host}/release_notes"
    return jsonify(currentVersion=current_version, earlierReleases=releases_url)


@app.route('/release_notes', methods=["GET"])
def release_notes():
    logger.info('Requested for server "Current Version"!')
    releases = get_yaml_data(file_path=RELEASE_NOTES_PATH, property='Releases')
    # print(request.host_url, request.host)  # http://192.168.29.78:5000/ 192.168.29.78:5000
    latest_version = f"{str(request.host_url).split(request.host, 1)[0]}{request.host}/current_version"
    return jsonify(currentVersion=latest_version, allReleases=releases)

@app.route('/metrics', methods=["GET"])
def server_metrics():
    logger.info('Requested for server "Current Version"!')
    releases = get_yaml_data(file_path=RELEASE_NOTES_PATH, property='Releases')
    # print(request.host_url, request.host)  # http://192.168.29.78:5000/ 192.168.29.78:5000
    current_version = get_yaml_data(file_path=RELEASE_NOTES_PATH, property='CurrentRelease')
    latest_version = f"{str(request.host_url).split(request.host, 1)[0]}{request.host}/current_version"
    releases_url = f"{str(request.host_url).split(request.host, 1)[0]}{request.host}/release_notes"
    return jsonify(currentVersionRelease=latest_version, currentVersion=current_version, allReleases=releases_url, totalRelases=len(releases) if releases else 0)

@app.route("/urls", methods=["GET"])
def list_urls():
    """Returns a JSON response with all available URLs in the app."""
    routes = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods:  # Include only routes accessible via GET
            routes.append({
                "endpoint": rule.endpoint,
                "methods": list(rule.methods),
                "url": str(rule)
            })
    return jsonify({"available_urls": routes})

if __name__ == '__main__':
    logger.info("Application running...")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
