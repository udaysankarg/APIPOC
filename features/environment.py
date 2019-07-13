import json
import logging
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(root_dir, 'logging_config.ini')


def before_all(context):
    context.config.setup_logging(configfile=config_file)
    try:
        with open('features/conf.json') as f:
            context.settings = json.load(f)
    except Exception as e:
        logging.exception("JSON Error : {}".format(e))


def before_scenario(context, scenario):
    logging.info("Starting scenario: {} ".format(scenario.name))


def after_scenario(context, scenario):
    logging.info("\t============= Scenario {} ============".format(scenario.status.name.upper()))
