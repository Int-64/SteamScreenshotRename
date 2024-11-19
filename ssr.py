import os
import yaml
from steam_web_api import Steam

def nidname(gameid):
    appdata = steam.apps.get_app_details(gameid)
    gamename = appdata.get(gameid).get("data").get("name")
    return gamename

def id2code(filename):
    text = filename.split('_')
    id = nidname(text[0])
    id = wsafetext(id)
    result = id + "_" + text[1] + "_" + text[2]
    return result

def wsafetext(text):
    for i in range(len(illegal)):
        text = text.replace(illegal[i], "")
    return text

def rename_files(path):
    count = 0   
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if filename[0].isdigit():
            newname = id2code(filename)
            os.rename(filepath, os.path.join(path, id2code(filename)))
            count += 1
            print(f"{count}) {filename} -> {newname}")
            continue
    if count == 0:
        count = "No"
    print(f"{count} file names changed!")

with open("config.yml", "r") as file:
    config_var = yaml.safe_load(file)

yml_api_key = config_var["steam_api_key"]
yml_path = config_var["path"]

api_key = os.environ.get(str(yml_api_key))
steam = Steam(api_key)
illegal = config_var["remove_char"]
path = str(yml_path)

rename_files(path)