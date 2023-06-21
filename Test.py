
import glob

def lister_fichiers(dossier):
    fichiers = glob.glob(dossier + '\\**\\*', recursive=True)
    return fichiers

# Exemple d'utilisation :
dossier = r"C:\Users\clement.slowik\Desktop\Intershop\FR"  # Remplacez par le chemin de votre dossier
fichiers = lister_fichiers(dossier)

print(len(fichiers))

import os

def lister_fichiers(dossier):
    fichiers = []
    for dossier_racine, sous_dossiers, fichiers_dans_dossier in os.walk(dossier):
        for fichier in fichiers_dans_dossier:
            chemin_complet = os.path.join(dossier_racine, fichier)
            fichiers.append(chemin_complet)
    return fichiers

# Exemple d'utilisation :
dossier =r"C:\Users\clement.slowik\Desktop\Intershop\FR"  # Remplacez par le chemin de votre dossier
fichiers = lister_fichiers(dossier)

# Affichage des fichiers
print(len(fichiers))



import os
path = r"C:\Users\clement.slowik\Desktop\Intershop\FR"
def find_files(path : str) -> list:
    documents = os.listdir(path)
    return documents


