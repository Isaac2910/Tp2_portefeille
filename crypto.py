# -*- coding: utf-8 -*-
"""
Created on 2026

@author: Newton10
"""
from actif import Actif



class Crypto (Actif):
    def __init__(self, nom, valeur, prixAchat, prixActuel, quantite):
        super().__init__(nom , valeur)
        self.prixAchat = prixAchat;
        self.prixActuel = prixActuel;
        self.quantite = quantite
        
    def calculer_rendement (self):
        
        gain_prix = (self.prixActuel - self.prixAchat) * self.quantite  
        
        investissement = self.prixAchat * self.quantite ; 
        
       
        
        return (gain_prix / investissement) * 100 ;