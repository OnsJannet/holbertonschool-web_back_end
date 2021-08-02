#!/usr/bin/env python3
"""
filter_datum
"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    '''Redacting Formatter class.
    '''
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Constructor
        '''
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        '''
        Filters values in incoming log records using `filter_datum`
        '''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''
        returns the log message obfuscated:
            - fields: a list of strings representing all fields to obfuscate
            - redaction: a string representing by what the field will
              be obfuscated
            - message: a string representing the log line
            - separator: a string representing by which character is
              separating all fields in the log line (message)
    '''
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:

    ''' Creates Logger
    Logger: user_data
    Level: INFO
    Doesn't Propagate msgs to other loggers
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:

    '''
    returns a MySQL Database connector
    '''
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    connector = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)

    return connector


def main():
    '''
    a main function that takes no arguments and
    returns nothing.
    '''
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    for row in data:
        for coloumn in row:
            print(coloumn)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
