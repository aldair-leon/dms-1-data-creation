from script.logger import log
import json
import os

logger = log('ENV SETUP')


def load_resources_path():
    verify_path = os.path.exists(os.path.abspath("resources/"))
    # verify_path = os.path.exists(os.path.abspath("../resources"))
    if verify_path:
        # return os.path.abspath("../resources")
        return os.path.abspath("resources/")
    else:
        logger.error('Error env file, please verify your resource file!')


def load_entities_json():
    path = load_resources_path()
    verify_path = os.path.exists(os.path.abspath(path + '/entities'))
    if verify_path:
        with open(path + '/entities') as f:
            env = json.load(f)
        return env
    else:
        logger.error('Error Loading credentials!')


def load_data_path():
    verify_path = os.path.exists(os.path.abspath("data/"))
    # verify_path = os.path.exists(os.path.abspath("../resources"))
    if verify_path:
        # return os.path.abspath("../resources")
        return os.path.abspath("data/")
    else:
        logger.error('Error env file, please verify your resource file!')
