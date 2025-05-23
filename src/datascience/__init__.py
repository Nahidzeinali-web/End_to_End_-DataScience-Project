# Import the 'os' module for interacting with the operating system, especially for path and directory handling
import os

# Import 'sys' to access system-specific parameters and functions (used here to direct logs to stdout)
import sys

# Import 'logging' to configure logging across the application
import logging

# Define a custom logging format including timestamp, log level, module name, and the actual message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where the log file will be stored
log_dir = "logs"

# Full path of the log file
log_filepath = os.path.join(log_dir, "logging.log")

# Create the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (can be DEBUG, WARNING, etc.)
    format=logging_str,  # Use the custom logging format defined earlier
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages will be written to a file
        logging.StreamHandler(sys.stdout)   # Log messages will also be printed to the console (stdout)
    ]
)

# Create a logger instance named "datasciencelogger" for reuse across modules
logger = logging.getLogger("datasciencelogger")
