#!/usr/bin/env python3
"""  provides some stats about
Nginx logs stored in MongoDB """

from pymongo import MongoClient


def log_stats(logs_dict: dict) -> int:
    """ provides some stats about Nginx logs stored in MongoDB
        - Database: logs
        - Collection: nginx
        - Methods ["GET", "POST", "PUT", "PATCH", "DELETE"]
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    data = client.logs.nginx
    logs = data.count_documents(logs_dict)
    message = f"\
              {logs} logs\n\
              Methods:\n\
              \tmethod GET: { logger({'method': 'GET'}) }\n\
              \tmethod POST: { logger({'method': 'POST'}) }\n\
              \tmethod PUT: {logger({'method': 'PUT'})}\n\
              \tmethod PATCH: {logger({'method': 'PATCH'})}\n\
              \tmethod DELETE: {logger({'method': 'DELETE'})}\n\
              {status} status check\
            "
    print(message)

    if __name__ == "__main__":
        log_stats()
