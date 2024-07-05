"""
file_name = consumer.py
Created On: 2024/07/05
Lasted Updated: 2024/07/05
Description: _FILL OUT HERE_
Edit Log:
2024/07/05
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from kafka import KafkaConsumer

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from src.environment import Environment, EnvironmentVariableKeys


class Consumer:
    """
    A class to handle the Kafka consumer
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        A method to create a singleton instance of the class
        """

        if cls._instance is None:
            cls._instance = super(Consumer, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self) -> None:
        """
        A method to initialie the consumer class
        """

        self._kafka_consumer = self._get_kafka_consumer()

    def consume(self) -> None:
        """
        A method to consume the messages from the Kafka topic
        """

        for message in self._kafka_consumer:
            print(message.value.decode())

    def _get_kafka_consumer(self) -> KafkaConsumer:
        """
        A method to get the Kafka consumer
        """

        return KafkaConsumer(
            "metric_consumer_topic",
            bootstrap_servers=Environment.get_environment_variable(
                EnvironmentVariableKeys.BOOTSTRAP_SERVERS
            ),
            auto_offset_reset="earliest",  # Start reading at the earliest message
            group_id="metric_consumer_group",  # Consumer group ID
            security_protocol=Environment.get_environment_variable(
                EnvironmentVariableKeys.SECURITY_PROTOCOL
            ),
            sasl_mechanism=Environment.get_environment_variable(
                EnvironmentVariableKeys.SASL_MECHANISM
            ),
            sasl_plain_username=Environment.get_environment_variable(
                EnvironmentVariableKeys.SASL_PLAIN_USERNAME
            ),
            sasl_plain_password=Environment.get_environment_variable(
                EnvironmentVariableKeys.SASL_PLAN_PASSWORD
            ),
        )
