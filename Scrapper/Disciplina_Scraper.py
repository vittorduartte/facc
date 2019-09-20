# -*- coding: utf-8 -*-

import requests, json
from bs4 import BeautifulSoup as BS
from DataClass.Disciplina import Disciplina

def getViewState(r):

    text = r.text
    page = BS(text, 'lxml')
    input = page.find('input', id='javax.faces.ViewState')

    return input.get("value")

def parser_Row(rows):
    
    elements = []
    
    for row in rows:
    
        cols = row.find_all('td')

        codigo = cols[0].text.strip()
        nome = cols[1].text.strip()
        tipo = cols[2].text.strip()
        ch = cols[4].text.strip()

        disciplina = Disciplina(codigo, nome, tipo, ch).getDisciplina_JSON()
        
        elements.append(disciplina)

    return elements

def parser_Table(table):

    disciplinas = {}
    rowsI = table.find_all('tr', class_='linhaImpar')
    rowsP = table.find_all('tr', class_='linhaPar')
    
    disciplinas['data'] = (parser_Row(rowsI) + parser_Row(rowsP))
    
    return disciplinas
    
def getDisciplinas():

    url = 'https://sigaa.ufma.br/sigaa/public/componentes/busca_componentes.jsf'

    try:
        page_response = requests.get(url)

        id = getViewState(page_response)
        cookies = dict(JSESSIONID=page_response.cookies['JSESSIONID'])
        payload = {'form': 'form', 'form:nivel': 'G', 'form:checkTipo': 'on', 'form:tipo': 2, 'form:j_id_jsp_449987817_11': '', 'form:j_id_jsp_449987817_13': '',
                   'form:checkUnidade': 'on', 'form:unidades': 1396, 'form:btnBuscarComponentes': 'Buscar Componentes', 'javax.faces.ViewState': id}

        response = requests.post(url, data=payload, cookies=cookies)

        print(response.status_code, " ~ \n\n")
        tabela = BS(response.text, 'lxml').find('table', class_='listagem')
        
        return parser_Table(tabela)

    except Exception as e:
        print('Erro ao recuperar os dados das disciplinas: ', e)
