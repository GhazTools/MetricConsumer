"""
file_name = environment.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from enum import Enum
from pathlib import Path
from os import getenv

# THIRD PARTY LIBRARY IMPORTS
from dotenv import load_dotenv

# LOCAL LIBRARY IMPORTS


class EnvironmentVariableKeys(Enum):
    """
    An Enum class to specify the environment variable keys.
    """

    BOOTSTRAP_SERVERS = "BOOTSTRAP_SERVERS"
    SECURITY_PROTOCOL = "SECURITY_PROTOCOL"
    SASL_MECHANISM = "SASL_MECHANISM"
    SASL_PLAIN_USERNAME = "SASL_PLAIN_USERNAME"
    SASL_PLAN_PASSWORD = "SASL_PLAN_PASSWORD"
    METRIC_TOPIC = "METRIC_TOPIC"
    METRIC_TOPIC_GROUP_ID = "METRIC_TOPIC_GROUP_ID"
    SQL_TYPE = "SQL_TYPE"
    SQL_HOST = "SQL_HOST"
    SQL_PORT = "SQL_PORT"
    SQL_USERNAME = "SQL_USERNAME"
    SQL_PASSWORD = "SQL_PASSWORD"
    SQL_DATABASE = "SQL_DATABASE"


class Environment:
    """
    A class to handle the environment variables
    """

    is_loaded: bool = False

    @staticmethod
    def load_environment_variables() -> None:
        """
        A method to load the environment variables
        """

        if Environment.is_loaded:
            return

        app_path: Path = Path(__file__).resolve().parents[1]
        env_path = app_path / ".env"

        load_dotenv(dotenv_path=env_path)

        Environment.verify_environment_variables()
        Environment.is_loaded = True

    @staticmethod
    def verify_environment_variables() -> None:
        """
        A method to verify the environment
        """

        missing_keys = []
        for key in EnvironmentVariableKeys:
            key_value = key.value

            if getenv(key_value) is None:
                missing_keys.append(key_value)

        if missing_keys:
            raise ValueError("Missing environment variables:", ", ".join(missing_keys))

    @staticmethod
    def get_environment_variable(key: EnvironmentVariableKeys):
        """
        A method to get the environment variable
        """

        Environment.load_environment_variables()

        return getenv(key.value)
