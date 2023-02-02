#!/usr/bin/env python3
"""
Regex-ing
"""
import logging
import re
from typing import List, Tuple
from mysql.connector import connection
from os import getenv

PII_FIELDS: Tuple = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated by 'redaction' argument"""
    for i in fields:
        message = re.sub(i + '=.+?' + separator,
                         i + '=' + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records using filter_datum method"""
        message_format = filter_datum(self.fields,
                                      RedactingFormatter.REDACTION,
                                      super().format(record),
                                      RedactingFormatter.SEPARATOR)
        return message_format


def get_logger() -> logging.Logger:
    """Create a logger"""

    # Create a custom logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)

    # Create formatters and add it to handler
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """Connect to secure database"""

    connexion = connection.MySQLConnection(
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'),
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', '')
    )

    return connexion
