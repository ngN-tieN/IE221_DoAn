from abc import ABC, abstractmethod
import mysql.connector
import config


class AbstractDBService(ABC):
    def __init__(self):
        self._mydb = mysql.connector.connect(
            host=config.mysql['host'],
            user=config.mysql['user'],
            password=config.mysql['passwd'],
            database=config.mysql['database'])
