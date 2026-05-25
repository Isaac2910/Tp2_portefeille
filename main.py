# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:49:55 2026

@author: Newton10
"""




from actions import Action

from crypto import Crypto
from obligation import Obligation

from portefeuille import Portefeuille


apple = Action()
bitcoin = Crypto()
oblig = Obligation()


mon_portefeuille = Portefeuille("Mon Portefeuille")

#add les actif
mon_portefeuille.ajouter_actif(apple)
mon_portefeuille.ajouter_actif(bitcoin)
mon_portefeuille.ajouter_actif(oblig)

#rmv les 1 actif
mon_portefeuille.supprimer_actif()

#calcul val total actif
mon_portefeuille.valeur_totale()



#afficher rendement
mon_portefeuille.rendement_global()

#aff... resumer
mon_portefeuille.afficher_resume()
