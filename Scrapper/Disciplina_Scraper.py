import requests

url = {}
url['cursos'] = 'https://dados-ufma.herokuapp.com/liveapi/v01/curso/'

def get_Cursos(url):

    page = requests.get(url).text
    json = json.loads(page)