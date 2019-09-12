# -*- coding: utf-8 -*-

from DataClass.Disciplina import Disciplina
from DataClass.Docente import Docente

from Scrapper import Disciplina_Scraper, Docente_Scrapper
import json

def write_Data(data, name):
    
    file = open(name+'.json', 'w')

    try:
        file.write(data)
        file.close()
    except Exception as e:
        print('Erro ao escrever os dados: ', e)


disciplinas = Disciplina_Scraper.getDisciplinas()
write_Data(json.dumps(disciplinas), 'data_disciplina')

docentes = Docente_Scrapper.getDocentes(40)
write_Data(docentes, 'data_docentes') 


    