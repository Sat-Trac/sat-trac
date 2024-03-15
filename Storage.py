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