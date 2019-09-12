# coding: utf-8

class Disciplina:

    def __init__ (self, codigo, nome, tipo, ch):
    
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.ch = ch
    
    def getDisciplina_JSON(self):
        
        saida = {"codigo":self.codigo, "nome":self.nome, "tipo":self.tipo, "ch":self.ch}

        return saida