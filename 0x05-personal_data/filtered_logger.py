#!/usr/bin/env python3
"""
filter_datum
"""

from typing import List
import re


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
