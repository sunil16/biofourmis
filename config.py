import os
import configparser

APP_ENV = 'env'
INI_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)
                    ), "conf/{}.ini".format(APP_ENV)
)

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

REPORT = CONFIG["reporttime"]
INTERVAL_M = REPORT['interval_minutes']
INTERVAL_H = REPORT['interval_hours']

SIMULATOR = CONFIG["simulator"]
START_TIME = SIMULATOR['start_time']
