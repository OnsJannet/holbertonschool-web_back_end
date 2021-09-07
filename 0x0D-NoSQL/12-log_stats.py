#!/usr/bin/env python3
"""  provides some stats about
Nginx logs stored in MongoDB """

from pymongo import MongoClient


def log_stats(log_dict: dict) -> int:
    """ provides some stats about Nginx logs stored in MongoDB
        - Database: logs
        - Collection: nginx
        - Methods ["GET", "POST", "PUT", "PATCH", "DELETE"]
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    data = client.logs.nginx
    logs = data.count_documents({log_dict})
    message = f"\
              { log_stats({logs}) } logs\n\
              Methods:\n\
              \tmethod GET: { log_stats({'method': 'GET'}) }\n\
              \tmethod POST: { log_stats({'method': 'POST'}) }\n\
              \tmethod PUT: {log_stats({'method': 'PUT'})}\n\
              \tmethod PATCH: {log_stats({'method': 'PATCH'})}\n\
              \tmethod DELETE: {log_stats({'method': 'DELETE'})}\n\
              {status} status check\
            "
    print(message)

    if __name__ == "__main__":
        log_stats()
