import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("TOKEN")
username=os.getenv("GITHUB_USERNAME")
URL = "https://api.github.com/users/"+username

response = requests.get(URL).json()

def generate_resume():
    data = []
    datatype=["login","name","avatar_url","followers","following","public_repos"]
    for i in datatype:
        if (i in datatype):
            data.append(response[i])
    print(data)

    data_hash = {
        "login" : data[0],
        "name" : data[1],
        "avatar_url" : data[2],
        "followers" : data[3],
        "following" : data[4],
        "public_repos" : data[5]
    }
    return data_hash