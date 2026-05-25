# -*- coding: utf-8 -*-
"""
@author: Newton10
"""
from abc import ABC, abstractmethod 

class Actif(ABC): 
    def __init__(self, nom, valeur): 
        self.nom = nom
        self.valeur = valeur
    
    @abstractmethod 
    def calculer_rendement(self): 
        pass 