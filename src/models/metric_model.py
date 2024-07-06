"""
file_name = metric_model.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import Optional
from datetime import datetime

# THIRD PARTY LIBRARY IMPORTS
from pydantic import BaseModel, validator

# LOCAL LIBRARY IMPORTS
from utils.app_logger import AppLogger


class AdditinalMetadata(BaseModel):
    """
    A class to represent the additional metadata
    """

    latency: Optional[float] = None


class MetricModel(BaseModel):
    """
    A class to represent the metric model
    """

    application: str
    metric_name: str
    timestamp: datetime
    additional_metadata: Optional[AdditinalMetadata] = None

    @validator("timestamp", pre=True, allow_reuse=True)
    def convert_timestamp(cls, value):  # pylint: disable=no-self-argument
        """
        A validator to convert the timestamp string to a datetime object
        """

        # Assuming the timestamp string is in 'YYYY-MM-DD HH:MM:SS' format
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

        raise ValueError("Timestamp must be a string in 'YYYY-MM-DD HH:MM:SS' format")
