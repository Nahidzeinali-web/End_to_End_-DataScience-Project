# ====================== MODULE IMPORTS ======================

# Built-in Python libraries
import os  # To interact with the file system (e.g., create directories)
import yaml  # To read YAML configuration files (commonly used in ML projects)
import json  # For reading and writing JSON data files
import joblib  # For saving and loading binary objects (like trained models)

# Logger from the main project module to track activities consistently
from src.datascience import logger

# External helper libraries
from ensure import ensure_annotations  # Ensures that function annotations are respected at runtime
from box import ConfigBox  # Converts dictionaries to objects with dot notation (e.g., config.model.name)
from box.exceptions import BoxValueError  # Custom exception for empty config handling

# Type hinting and path handling
from pathlib import Path  # More powerful and safer path operations than strings
from typing import Any  # Allows any type to be passed or returned (e.g., for joblib objects)


# ============================================================
# 🧰  Utility-Function Cheat-Sheet
# ============================================================
# | Function             | Purpose                                   | Why Use It?                                                       |
# |----------------------|-------------------------------------------|-------------------------------------------------------------------|
# | read_yaml()          | Read configuration in YAML format         | YAML is clean & human-readable; `ConfigBox` gives dot-access.     |
# | create_directories() | Ensure required folders are available     | Prevents “folder not found” errors in data/ML pipelines.          |
# | save_json()          | Save a Python dict to a JSON file         | Perfect for config outputs, metadata, and experiment logs.        |
# | load_json()          | Load JSON and return a `ConfigBox`        | Dot-access (`cfg.key`) is cleaner in large configs.               |
# | save_bin()           | Persist any object as a binary file       | Efficient for models, vectorizers, or large NumPy arrays.         |
# | load_bin()           | Restore object from binary file           | Quickly reload trained models for inference or further training.  |
# ============================================================

# =============================================================
# @ensure_annotations decorator (from `ensure` library)
# -------------------------------------------------------------
# 🧠 Purpose:
# Enforces that function input/output types match their annotations at runtime.
#
# ✅ Helps catch bugs early
# ✅ Ensures that types like Path, dict, str, etc., are correctly used
# ✅ Makes Python functions behave more like statically typed languages
#
# 🔍 Example:
# @ensure_annotations
# def greet(name: str) -> str:
#     return f"Hello, {name}"
#
# greet(123)  ❌ Raises TypeError: name must be str
# =============================================================
# =============================================================
# ConfigBox (from `python-box` library)
# -------------------------------------------------------------
# 🧠 Purpose:
# Converts standard Python dicts into objects that allow dot notation access
#
# 🔍 Example:
# from box import ConfigBox
# config = ConfigBox({"model": {"name": "BERT"}})
# print(config.model.name)  # ✅ Access like an attribute: "BERT"
#
# ✅ More readable and maintainable than nested dictionary indexing
# ✅ Especially useful for loading and using YAML or JSON configs
# ✅ Automatically converts nested dicts into nested ConfigBox instances
# =============================================================


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Why:
    - YAML is often used for config files in ML and data projects.
    - Using ConfigBox enables `dot access` (config.model.name instead of config["model"]["name"]).
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Safely parse YAML
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Convert dict to dot-accessible object
    except BoxValueError:
        raise ValueError("yaml file is empty")  # Custom error for empty YAML
    except Exception as e:
        raise e  # Re-raise any other exceptions



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories if they don’t already exist.

    Why:
    - Ensures required folders like 'artifacts/', 'logs/', or 'models/' are created.
    - `verbose=True` enables logging to help debug directory creation steps.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Does nothing if directory exists
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a Python dictionary as a JSON file.

    Why:
    - Useful for saving configurations, results, experiment metadata, etc.
    - JSON is human-readable and easy to parse.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Write with pretty indentation
    logger.info(f"json file saved at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns a ConfigBox.

    Why:
    - Allows dot-access to keys after loading.
    - Helpful for structured experiment results or settings.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves Python object as a binary file using joblib.

    Why:
    - More efficient than pickle for saving large numpy arrays, sklearn models, etc.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary file and returns the stored object.

    Why:
    - Used to restore trained models, vectorizers, or intermediate pipelines.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



