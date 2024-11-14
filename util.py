import os
import yaml
import configparser


def get_file_path(file_path):
    try:
        abs_path = os.path.normpath(os.path.join(os.path.dirname(__file__), file_path))
        return abs_path
    except:
        return file_path


def check_file_existence(file_path) -> bool:
    try:
        if os.path.exists(file_path):
            return True
        return False
    except:
        return False


def return_file_not_exists(file_path):
    from logger_service import logger
    logger.critical(f"File doesn't exist: {file_path}")
    return {}


def get_yaml_data(file_path, property=None):
    file_path = get_file_path(file_path)
    if not check_file_existence(file_path):
        return return_file_not_exists(file_path)
    with open(file_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file.read())
    if yaml_content and property and property in yaml_content:
        return yaml_content.get(property)
    return yaml_content


def get_properties(file_path, section, property=None):
    file_path = get_file_path(file_path)
    if not check_file_existence(file_path):
        return return_file_not_exists(file_path)
    cfg = configparser.ConfigParser(file_path)
    cfg.read(file_path)
    if cfg.has_section(section):
        if property is not None:
            if cfg.has_option(section=section, option=property):
                return cfg.get(section, option=property)
        return cfg[section]
    return {}
