TP 2: Système de Gestion de Portefeuille 

d’Investissement en Python (POO) 
Contexte 
Une société de gestion financière souhaite développer une application permettant de :
 Gérer différents types d’actifs financiers 
 Calculer la valeur d’un portefeuille 
 Simuler des rendements 
 Générer des rapports d’investissement 
Vous devez concevoir ce système en utilisant les principes de la Programmation Orientée 
Objet (POO) en Python. 
Objectifs pédagogiques 
À la fin de ce TP, l’étudiant devra être capable de : 
 Appliquer les concepts fondamentaux de la POO : 
o Encapsulation 
o Héritage 
o Polymorphisme 
o Abstraction 
 Modéliser un problème réel en classes 
 Concevoir un système extensible 
 Implémenter des cas d’usage métier 
 Structurer un projet Python proprement 
Concepts POO à mettre en œuvre 
1 Encapsulation 
 Attributs privés 
 Méthodes d’accès (getters / setters si nécessaires) 
2 Héritage 
 Classe mère Actif 
 Classes filles : 
o Action 
o Obligation 
o Crypto 
3 Polymorphisme 
 Méthode commune calculer_rendement() 
 Chaque type d’actif implémente sa propre logique 
4 Abstraction 
 Utilisation de classes abstraites (abc.ABC) 
Travail demandé 
Étape 1 : Modélisation des Actifs 
Créer une classe abstraite : 
class Actif(ABC): 
def __init__(self, nom, valeur): 
pass 
@abstractmethod 
def calculer_rendement(self): 
pass 
Implémenter ensuite : 
Classe Action 
 Attributs : nom, prix d’achat, prix actuel, dividende, quantité 
 Calcul du rendement basé sur variation + dividende 
Classe Obligation 
 Attributs : nom, valeur nominale, taux d’intérêt, durée 
 Calcul du rendement basé sur intérêts 
Classe Crypto 
 Attributs : nom, prix d’achat, prix actuel, quantité 
 Rendement basé uniquement sur volatilité 
Étape 2 : Classe Portefeuille 
Créer une classe Portefeuille permettant : 
 Ajouter un actif 
 Supprimer un actif 
 Calculer la valeur totale 
 Calculer le rendement global 
 Afficher un résumé du portefeuille 
Cas d’usage à implémenter 
Cas d’usage 1 : Création d’un portefeuille 
L’utilisateur peut créer un portefeuille vide. 
Cas d’usage 2 : Ajout d’actifs 
L’utilisateur peut ajouter plusieurs types d’actifs. 
Cas d’usage 3 : Calcul du rendement global 
Le système calcule automatiquement le rendement total du portefeuille. 
Cas d’usage 4 : Simulation 
Simuler une variation de marché (+5%, -3%, etc.) et recalculer la valeur. 
Cas d’usage 5 : Rapport synthétique 
Afficher : 
 Valeur totale investie 
 Valeur actuelle 
 Rendement par actif 
 Rendement global 
Analyse demandée 
Les étudiants doivent expliquer : 
1. Pourquoi utiliser une classe abstraite ? 
2. Où observe-t-on le polymorphisme ? 
3. En quoi l’encapsulation protège les données ? 
4. Comment rendre le système extensible (ajout futur : ETF, Fonds, etc.) ? 
Bonus (optionnel) 
 Implémenter une sauvegarde en fichier JSON 
 Ajouter une gestion des exceptions 
 Implémenter un système de logging 
 Ajouter une interface CLI simple 
 Appliquer un Design Pattern (ex : Factory pour créer les actifs) 
Livrables attendus 
1 Code source 
 Projet structuré : 
/portfolio_project 
actif.py 
action.py 
obligation.py 
crypto.py 
portefeuille.py 
main.py 
2 Rapport PDF (3–5 pages) 
Contenant : 
 Diagramme UML des classes 
 Explication des concepts POO utilisés 
 Description des cas d’usage 
 Captures d’écran d’exécution 
 Analyse critique (forces / limites) 
3 Démonstration 
Présentation orale de 5–10 minutes : 
 Architecture choisie 
 Difficultés rencontrées 
 Améliorations possibles 