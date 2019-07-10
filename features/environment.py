import json
import logging
import os

FWHOME= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(FWHOME,'logging_config.ini')
print(config_file)


def before_all(context):
    with open('features/conf.json') as f:
        context.settings = json.load(f)

    context.config.setup_logging(configfile=config_file)


def after_scenario(context,scenario):
    logging.info("============ Scenario : {} ===========".format(scenario.status.upper()))