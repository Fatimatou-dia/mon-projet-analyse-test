
# analyse_donnees.py
# Ce script lit un fichier CSV contenant des données fictives de recherche et affiche des statistiques de base

import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("donnees_exemple.csv")

# Afficher les 5 premières lignes
print("Aperçu des données :")
print(df.head())

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe())

# Comptage des valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())
