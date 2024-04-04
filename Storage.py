import os
import dotenv  # pip install python-dotenv
dotenv.load_dotenv(".env")

class Storage:
    def __init__(self):
        pass

    def testConfig(self):
        requiredKeys = ["APIKey", "AnotherKey", "BadKey"]

        for key in requiredKeys:
            try:
                os.environ[key]
            except(KeyError):
                print("Bad Key")

    def getKey(self, key):
        return os.environ[key]

    def setKey(self, key, value):
        dotenv.set_key(dotenv_path=".env", key_to_set=key, value_to_set=value)
        os.environ[key] = value