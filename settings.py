import os
import yaml
import logging

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_PATH, 'config')


def get_config():
    env = os.environ.get('APPLICATION_ENV', 'local')
    config_file_name = os.path.join(CONFIG_PATH, f'{env}.yaml')

    with open(config_file_name, 'r') as f:
        try:
            return yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            logging.error(f'[CONFIG_ERROR] {str(e)}')
    return {}
