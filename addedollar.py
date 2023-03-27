import requests
import json as _json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

source = "https://lbprate.com/"

body      = requests.get(source, headers=headers).content.decode()
body      = body[body.find("Market Rate")::]
_price    = re.search(r"USD at\s+([\d,]+)", body).group(1)
body      = body[body.find("Sayrafa")::]
_sayrafa  = re.search(r"USD at\s+([\d,]+)", body).group(1)
data      = {"price":str(_price), "sayrafa":str(_sayrafa)}

def update():
    body      = requests.get(source, headers=headers).content.decode()
    body      = body[body.find("Market Rate")::]
    _price    = re.search(r"USD at\s+([\d,]+)", body).group(1)
    body      = body[body.find("Sayrafa")::]
    _sayrafa  = re.search(r"USD at\s+([\d,]+)", body).group(1)
    data      = {"price":_price, "sayrafa":_sayrafa}

def price():
    return _price
    
def sayrafa():
    return _sayrafa
    
def json():
    return _json.dumps(data)
