""" Module to access configuration params """
import json
from pathlib import Path

CONFIG_FILENAME = "config.json" 

ROOT_DIR = Path(__file__).parent.parent
config_file_path = Path(ROOT_DIR, "config", CONFIG_FILENAME)
with open(config_file_path) as f:
    config_params = json.load(f)


class Config(object):
    TwilioAccountSid = config_params["TwilioAccountSid"]
    TwilioAuthToken = config_params["TwilioAuthToken" ]
    TwilioServiceSid  = config_params["TwilioServiceSid" ]

class DBConfig():
    """Base class to hold configurations to connect to Database"""

    DBSERVER = config_params["DBServer"]
    DBNAME = config_params["DBName"]
    DBSCHEMA = config_params["DBSchema"]
    DBUSERNAME = config_params["DBUsername"]
    DBPASSWORD = config_params["DBPassword"]
    DBPORT = int(config_params["DBPort"])

    def get_connection_str(self) -> str:
        """Returns connection for DB"""
        return f"""postgresql+psycopg2://{self.DBUSERNAME}:{self.DBPASSWORD}@{self.DBSERVER}:{self.DBPORT}/{self.DBNAME}"""

