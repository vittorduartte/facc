import requests
import json

def getDocentes(qtdd):
    
    url = 'http://www.wjr.eti.br/nameGenerator/index.php?q='+str(qtdd)+'&o=json'
    response = requests.get(url)
    content = response.text

    return json.loads(content)



