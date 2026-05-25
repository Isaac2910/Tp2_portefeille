# -*- coding: utf-8 -*-
"""
Created on 2026

@author: Newton10
"""
from actif import Actif

class Obligation(Actif):
    def __init__(self, nom, valeur,tauxInteret, dure):
        super().__init__(nom , valeur)
      
        self.tauxInteret = tauxInteret;
        self.dure = dure
        
    def calculer_rendement(self):
        gain_annuel = self.valeur * self.tauxInteret
        
        gain_total = gain_annuel * self.dure
        
        return (gain_total / self.valeur) * 100
        
        
     