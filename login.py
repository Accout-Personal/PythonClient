from _typeshed import Self
import requests

class login:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self.impostazioni = "application/json"
        self.token = False

    def get_token(self):
        return self.token
"""
    @staticmethod
    def prova_static():
        return """

