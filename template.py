# Import the 'os' module to interact with the operating system, such as file and directory handling
import os

# Import 'Path' from 'pathlib' for convenient and readable file path manipulation
from pathlib import Path

# Import 'logging' to log messages, useful for tracking the script’s execution and debugging
import logging

# Configure logging to show messages with time stamps and a custom format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name for dynamic folder generation
project_name = "datascience"

# List of files and their paths that should exist in the project structure
# This structure includes modules, configuration files, a web template, a research notebook, and app setup
list_of_files = [
    ".gthub/workflows/.gitkeep",  # Keeps the workflows directory in Git even if it's empty
    f"src/{project_name}/__init__.py",  # Marks 'datascience' as a Python package
    f"src/{project_name}/components/__init__.py",  # Component-level Python package
    f"src/{project_name}/utils/__init__.py",  # Utility-level Python package
    f"src/{project_name}/utils/common.py",  # Utility script for shared helper functions
    f"src/{project_name}/config/__init__.py",  # Configuration-level Python package
    f"src/{project_name}/config/configuration.py",  # Configuration handling logic
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline-level Python package
    f"src/{project_name}/entity/__init__.py",  # Entity-level Python package
    f"src/{project_name}/entity/config_entity.py",  # Entity definition for configs (often using dataclasses)
    f"src/{project_name}/constants/__init__.py",  # Constants package for global static values
    "config/config.yaml",  # Configuration file for storing global configs
    "params.yaml",  # File for hyperparameters and experiment configs
    "schema.yaml",  # Schema definition (e.g., input data format)
    "main.py",  # Main entry point of the application
    "Dockerfile",  # Docker configuration for containerizing the app
    "setup.py",  # For packaging and installing the module
    "research/research.ipynb",  # Jupyter notebook for experimentation
    "templates/index.html",  # Web template (likely for a Flask or similar web app)
    "app.py"  # Main Flask (or other framework) web application entry point
]

# Iterate through each file path to ensure the structure exists
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object for platform-independent handling
    filedir, filename = os.path.split(filepath)  # Split into directory and file name

    # If the directory part is not empty, create the directory structure (if not already present)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # 'exist_ok=True' prevents error if directory already exists
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create the file without writing anything
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log that the file already exists
        logging.info(f"{filename} is already exists")
