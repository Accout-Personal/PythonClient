<<<<<<< HEAD

from typing import final
=======
>>>>>>> 6143f5f3993e3d87dfd7d90925ff31f0f4140dea
import requests

class login:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        self.impostazioni = "application/json"
        self.token = False
    

    def get_token(self):
        return self.token

    @staticmethod
    def get_Host():
        return "pippo"

