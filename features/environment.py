import json
import logging

def before_all(context):
    with open('features/conf.json') as f:
        context.settings = json.load(f)

    context.config.setup_logging(filename="results/logs/APIPOC.log", level=logging.INFO,
                                 format='%(asctime)s - [%(name)-7s] - %(levelname)s::%(message)s',
                                 datefmt='%Y-%m-%d %H:%M:%S',filemode='w')

def after_scenario(context,scenario):
    logging.info("====== Scenario {} ======".format(scenario.status))