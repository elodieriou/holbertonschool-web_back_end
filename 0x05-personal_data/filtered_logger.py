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
        """Filter values in incoming log records using filter_datum method
        """
        message_format = filter_datum(self.fields,
                                      RedactingFormatter.REDACTION,
                                      super().format(record),
                                      RedactingFormatter.SEPARATOR)

        return message_format


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated by 'redaction' argument
    """
    for i in fields:
        message = re.sub(i + '=.+?' + separator,
                         i + '=' + redaction + separator,
                         message)
    return message


def get_logger() -> logging.Logger:
    """This method get a logger with the 4 steps following :
    - Create a logger,
    - Create handler
    - Create formatters and add it to handler,
    - Aad handler to the logger
    Return the logger object
    """

    logger = logging.getLogger()
    logger.name = 'user_name'
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()

    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """This methode get connexion to a database. It is necessary to give some
    information like : host, database, user, password.
    """

    connexion = connection.MySQLConnection(
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'),
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', '')
    )

    return connexion


def main() -> None:
    """The main method :
    - Create a connexion to the database,
    - Create a logger,
    - Create a cursor object to traversal all elements in the database,
    - The cursor execute a query into the database
    - The cursor fetch all data, the answer to the query,
    - Browse the data return by the cursor
    - Give to the logger.info the message build
    - Close the cursor object and connexion
    """

    connexion = get_db()
    logger = get_logger()

    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    for column in rows:
        message = "name={}; email={}; phone={}; ssn={}; password={}; \
        ip={}; last_login={}; user_agent={};".format(column[0], column[1],
                                                     column[2], column[3],
                                                     column[4], column[5],
                                                     column[6], column[7])
        logger.info(message)

    cursor.close()
    connexion.close()


if __name__ == "__main__":
    """Call the main function
    """
    main()
