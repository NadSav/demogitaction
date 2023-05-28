chaine = "Pierre, Julien, Anne, Marie, Lucien"
def chaine_en_ordre(chaine:str):
    liste_nom = chaine.split(", ")
    liste_nom.sort()
    return ", ".join(liste_nom)

print(chaine_en_ordre(chaine))
