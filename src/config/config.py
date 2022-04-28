import os

class Config(object):
    POKE_API_URL = os.environ.get("POKE_API_URL")