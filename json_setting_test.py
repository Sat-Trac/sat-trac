import json

with open("settings.json", "r") as jsonsettings:
    settings = json.load(jsonsettings)

print(settings)
