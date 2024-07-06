"""
file_name = metrics_repository.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from sqlalchemy.orm import Session

# LOCAL LIBRARY IMPORTS
from database.database_setup import SESSION_MAKER
from database.models.metrics_model import MetricsTableModel
from src.models.metric_model import MetricModel


class MetricsRepository:
    """
    A class to handle the metrics repository
    """

    def __init__(self) -> None:
        """
        Creates a new MetricsRepository object and initializes an SQLAlchemy session.
        """

        self.session: Session = SESSION_MAKER()

    def __enter__(self):
        """
        Called when the object is used as a context manager.

        This function is called when the `with` statement is used to create a context
        for the EndpointDiagnosticsRepository object. Returns the current object as the context
        manager value.
        """

        return self  # pylint: disable=unnecessary-pass

    def __exit__(self, type, value, traceback):  # pylint: disable=redefined-builtin
        """
        Called when the context manager is exited.

        This function is called when the `with` block created by the `with` statement
        that created this context manager is exited. This function closes the SQLAlchemy
        session.
        """

        self.session.close()

    def insert_metric(self, metric_model: MetricModel) -> None:
        """
        Inserts a new metric into the database.

        Args:
            metric_model (MetricModel): The metric to insert into the database.
        """

        metric_row: MetricsTableModel = MetricsTableModel(metric_model)

        self.session.add(metric_row)
        self.session.commit()
