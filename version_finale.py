from random import randint
import Percolation_sujet as per
import matplotlib.pyplot as plt
import numpy as np

# Question 1
def creation_grille_vierge(n:int):
    return [[0] * n for i in range(n)]

# Question 2
# per.afficher_grille(creation_grille_vierge(3))

# Question 3
# per.afficher_grille([[1, 0, 1], [0, 1, 0], [1, 0, 1]])

# Question 4
def creation_zebreh(n:int):
    """Lignes horizontales"""
    renvoyer = []
    for i in range(n):
        renvoyer.append([not(i % 2)] * n) # not(5 % 2) est pareil que not(1) i.e. not(True) = False = 0

    return renvoyer

# Question 5
def creation_zebrev(n:int):
    """Lignes verticales"""
    renvoyer = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(not(j % 2))
        renvoyer.append(l)
    return renvoyer

# Question 6
def creation_damier(n:int):
    renvoyer = []
    for i in range(n):
        l = []
        for j in range(n):
            if i % 2:
                l.append(j % 2)
            else:
                l.append(not(j % 2))
        renvoyer.append(l)
    return renvoyer

# Question 7
def creation_grille(p:float, n:int):
    grille = creation_grille_vierge(n)
    for i in grille:
        for j, h in enumerate(i): # Ici j est l'indice et h l'élément de la liste i
            generate = per.rand()
            if p > generate:
                i[j] = 1
    return grille

# Question 8
def a_un_voisin_rempli(grille:list, i:int, j:int):
    veracite = False # Tant qu'on n'a pas trouvé de voisin rempli
    tester = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]] # Coordonnées des points adjascents
    for h in tester:
        try:
            if grille[h[0]][h[1]] == 2:
                veracite = True
        except IndexError:
            continue
    return veracite

# Question 9
def percolation(grille):
    # Première ligne
    for i, j in enumerate(grille[0]):
        if j == 0:
            grille[0][i] = 2

    # Le reste
    for i, j in enumerate(grille):
        for h, k in enumerate(j):
            if a_un_voisin_rempli(grille, i, h) and not j[h]:
                j[h] = 2

# Question 10
# On teste
# grille = creation_grille(0.45, 9)
# percolation(grille)
# per.afficher_grille(grille)
# On se rend compte que l'algorithme ne répond
# pas complétement à la problématique
# (voir l'image intitulée figure_1.png)

def percolation(grille):
    # Première ligne
    for i, j in enumerate(grille[0]):
        if j == 0:
            grille[0][i] = 2

    # Le reste
    while True:
        painted = 0
        for i, j in enumerate(grille):
            for h, k in enumerate(j):
                if a_un_voisin_rempli(grille, i, h) and not j[h]:
                    j[h] = 2
                    painted += 1
        if painted == 0:
            break

# On teste
# grille = creation_grille(0.45, 9)
# percolation(grille)
# per.afficher_grille(grille)
# On ne rencontre plus le même problème

# Question 11
# def percolation11(grille:list):
#     ouvertes = []
#     for colonne, i in enumerate(grille[0):
#             if i == 0:
#                 premiere.append(colonne)
#                 grille[0][colonne] = 2
#     ouvertes = [[0, colonne] for colonne in ouvertes]
#     while True:
#         couple = ouvertes.pop()
#         i, j = couple[0], couple[1]
#         voisins_a_remplir = []
#         if a_un_voisin_rempli(grille, i, j):
#             tester = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]] # Coordonnées des points adjascents
#             for h in tester:
#                 try:
#                     grille[h[0]][h[1]]
#                     voisins_a_remplir.append(h)
#                 except IndexError:
#                     continue
#         ouvertes += voisins_a_remplir

# Question 12
# Avant remplissage
# grille = creation_grille(0.45, 60)
# per.afficher_grille(grille)
# percolation(grille)
# per.afficher_grille(grille)

# Question 13
def teste_percolation(p:float, n:int):
    grille = creation_grille(p, n)
    percolation(grille)
    renvoyer = False
    for i in grille[-1]:
        if i == 2:
            renvoyer = True
    return renvoyer

# Question 14
def proba(p:float, k:int, n:int):
    reussi = 0
    for i in range(k):
        if teste_percolation(p, n):
            reussi += 1
    return reussi / k   # Nombre moyen de réussites

def tracer_proba(n):
    x = np.linspace(0,1,21)
    y = []
    for p in x:
        y.append(proba(p,20,n))
    plt.clf()
    plt.plot(x,y)
    plt.show()
    return None

# Test
# tracer_proba(128)
# tracer_proba(9)
grille = creation_grille(0.45, 15)
percolation(grille)
per.afficher_grille(grille)
teste_percolation(0.45, 15)

# Pour tester
# per.afficher_grille(creation_zebreh(3))
# per.afficher_grille(creation_zebrev(3))
# per.afficher_grille(creation_damier(9))
# per.afficher_grille(creation_grille(0.5, 9))