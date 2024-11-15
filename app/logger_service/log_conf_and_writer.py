import logging

# Configure logging
# Create handlers for file and console
file_handler = logging.FileHandler(r'app_logs.log')
console_handler = logging.StreamHandler()

# Set the logging format
formatter = logging.Formatter('[%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Set the logging level for handlers
file_handler.setLevel(logging.DEBUG)  # or any level you need
console_handler.setLevel(logging.DEBUG)  # or any level you need

# Get the logger
logger = logging.getLogger('flask_app')
logger.setLevel(logging.DEBUG)  # Set the overall logger level
logger.addHandler(file_handler)  # Add file handler to the logger
logger.addHandler(console_handler)  # Add console handler to the logger
