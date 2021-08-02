#!/usr/bin/env python3
"""
filter_datum
"""
from typing import List
import re
import logging
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class.
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Constructor
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using `filter_datum`
        """
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
