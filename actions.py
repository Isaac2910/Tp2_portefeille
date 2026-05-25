# -*- coding: utf-8 -*-
"""
Created on 2026

@author:Newton
"""
from actif import Actif

class Action(Actif):
    def __init__(self, nom,valeur, prixAchat, prixActuel , dividende, quantite):
        super().__init__(nom,valeur);
        self.prixAchat= prixAchat;
        self.prixActuel = prixActuel;
        self.dividende = dividende
        self.quantite = quantite
        
    def calculer_rendement(self):
        gain_prix = (self.prixActuel - self.prixAchat) * self.quantite ;      
        gain_dividende = self.dividende * self.quantite;             
        gain_total = gain_prix + gain_dividende ;
        investissement = self.prixAchat * self.quantite ;       
        return (gain_total / investissement) * 100 ;