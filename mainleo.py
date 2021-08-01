import requests
import env
from login import login

log = login('user4','password')
print(env.token)