import json

# read the config file
with open("config.json", "r") as file:
    configFile = file.read()
    file.close()

# apply the parser to the file
configFile = json.loads(configFile)

# print contents of the config file
print(configFile)

