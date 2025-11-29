# Fonction pour convertir l'heure en secondes
def heure_en_secondes(heure_str):
    h, m, s = map(int, heure_str.split(':'))
    return h * 3600 + m * 60 + s

# Fonction pour convertir les secondes en heure au format h : m : s
def secondes_en_heure(secondes):
    heures = secondes // 3600
    reste_secondes = secondes % 3600
    minutes = reste_secondes // 60
    secondes = reste_secondes % 60
    return f"{heures:02d}:{minutes:02d}:{secondes:02d}"

# Demander à l'utilisateur d'entrer l'heure au format h : m : s
heure_input = input("Entrez l'heure au format h:m:s : ")

# Convertir l'heure en secondes
secondes = heure_en_secondes(heure_input)

# Ajouter une seconde
secondes += 1

# Convertir les secondes en heure au format h : m : s
nouvelle_heure = secondes_en_heure(secondes)

# Afficher la nouvelle heure
print("Nouvelle heure après avoir ajouté une seconde :", nouvelle_heure)
