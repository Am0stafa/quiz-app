import requests

def getData():
    res = requests.get('https://opentdb.com/api.php?amount=15&category=18&type=boolean')
    que = res.json()
    return que["results"]


question_data = getData()
