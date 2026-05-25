# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:49:29 2026

@author: HP
"""

class Portefeuille ():
    def __init__(self, nom ):
        
        self.nom = nom
        self.actifs = []
        
    def ajouter_actif(self , actif):
        self.actifs.append(actif)
        
    def supprimer_actif(self, actif):
        
        self.actifs.remove(actif)
        
        
    def valeur_totale(self):
        total = 0
        for actif in self.actifs:
            total += actif.valeur
        return total
    
    def rendement_global(self):
        
        total = 0
        for actif in self.actifs:
            total += actif.calculer_rendement()
            
        return total / len(self.actifs) 

        
    
    def afficher_resume(self):
        print(self.nom)
        for actif in self.actifs:
            print(actif.nom, actif.calculer_rendement())
        print(self.valeur_totale())
        print("total", self.rendement_global())
        
        
        
        
        
    
    
    