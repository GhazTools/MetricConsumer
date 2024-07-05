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

# THIRD PARTY LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL LIBRARY IMPORTS


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
    timestamp: str
    additional_metadata: Optional[AdditinalMetadata] = None
