"""
file_name = metrics_model.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from sqlalchemy import Integer, String, DateTime, JSON
from sqlalchemy.orm import mapped_column

# LOCAL LIBRARY IMPORTS
from database.database_setup import BASE
from src.models.metric_model import MetricModel


class MetricsTableModel(BASE):
    """
    A class to represent the metrics model
    """

    __tablename__ = "metrics"

    row_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    application = mapped_column(String)
    metric_name = mapped_column(String)
    timestamp = mapped_column(DateTime)
    additional_metadata = mapped_column(JSON)

    def __init__(self, metric_model: MetricModel) -> None:
        """
        A method to initialize the metrics table model
        """

        self.application = metric_model.application
        self.metric_name = metric_model.metric_name
        self.timestamp = metric_model.timestamp
        self.additional_metadata = (
            metric_model.additional_metadata.dict()
            if metric_model.additional_metadata
            else {}
        )
