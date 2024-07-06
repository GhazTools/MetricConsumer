"""
file_name = engine.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine.base import Engine

# LOCAL LIBRARY IMPORTS
from utils.environment import Environment, EnvironmentVariableKeys


def get_engine() -> Engine:
    """
    Creates and returns an SQLAlchemy engine object.

    This function reads environment variables for the connection details to the
    database and uses them to create an SQLAlchemy engine object.

    Returns:
        An SQLAlchemy engine object that can be used to connect to a database.
    """

    sql_type: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_TYPE
    )
    sql_host: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_HOST
    )
    sql_password: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_PASSWORD
    )
    sql_port: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_PORT
    )
    sql_database: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_DATABASE
    )
    sql_username: str = Environment.get_environment_variable(
        EnvironmentVariableKeys.SQL_USERNAME
    )

    engine: Engine = create_engine(
        f"{sql_type}://{sql_username}:{sql_password}@{sql_host}:{sql_port}/{sql_database}",
        pool_size=10,
        max_overflow=20,
        pool_recycle=3600,
    )
    return engine


ENGINE: Engine = get_engine()
BASE = declarative_base()
SESSION_MAKER = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
