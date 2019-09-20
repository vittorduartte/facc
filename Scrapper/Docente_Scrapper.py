# -*- coding: utf-8 -*-

import requests
import json

def getDocentes(qtdd):
    
    docentes = {}
    url = 'http://www.wjr.eti.br/nameGenerator/index.php?q='+str(qtdd)+'&o=json'
    response = json.loads(requests.get(url).text)

    return response



