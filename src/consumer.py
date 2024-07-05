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
from json import loads

# THIRD PARTY LIBRARY IMPORTS
from kafka import KafkaConsumer
from pydantic import ValidationError

# LOCAL LIBRARY IMPORTS
from src.environment import Environment, EnvironmentVariableKeys
from src.metric_model import MetricModel


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
            if message.value:
                print(message.value)

    def _get_kafka_consumer(self) -> KafkaConsumer:
        """
        A method to get the Kafka consumer
        """

        return KafkaConsumer(
            Environment.get_environment_variable(EnvironmentVariableKeys.METRIC_TOPIC),
            bootstrap_servers=Environment.get_environment_variable(
                EnvironmentVariableKeys.BOOTSTRAP_SERVERS
            ),
            auto_offset_reset="earliest",  # Start reading at the earliest message
            group_id=Environment.get_environment_variable(
                EnvironmentVariableKeys.METRIC_TOPIC_GROUP_ID
            ),
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
            value_deserializer=self.deserialize_user_message,  # Use the custom deserializer
        )

    def deserialize_user_message(self, message: bytes) -> MetricModel | None:
        """
        A method to deserialize the user message
        """

        try:
            data = loads(message.decode("utf-8"))
            return MetricModel(**data)

        except ValidationError as e:
            print(f"Message validation error: {e}")
            return None
