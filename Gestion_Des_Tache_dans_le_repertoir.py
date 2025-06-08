# PROJET : Gestionnaire de tâche en ligne de commande

# Objectif : construire une application en ligne de commande pour gerer les tâche en utilisant des pratique pythonique.
# Certaines des fonctionnalités que nous ajouterons a ce gestionnaire de tâche particuliers sont : 
#	 Ajouter des tâches, pour voir toutes les tâches qui sont là.
#	Marquer une tâche comme terminé et vous pouvez egalement supprimé une tâche.


# importons le module os

import os
#  le fichier de stockage des tâche 
FILE_NAME = "tâche.txt"

# Charger la tâche depuit le fichier

def charger_tache():
	taches = {}

	# Verifions qu'une tâche existe
	if os.path.exists(FILE_NAME):
		with open(FILE_NAME, "r") as file :
			for line in file:
				tache_id, titre, status = line.strip().split(" | ")
				taches[int(tache_id)] = {"titre" : titre, "statut" : status}
	return taches

# Sauvegarder la tâche 

def sauvegarde(taches):
	with open(FILE_NAME, "w") as file :
		for tache_id, tache in taches.items() :
			file.write(f"{tache_id} | {tache['titre']} |{tache['statut']}\n")
			

# Ajouter une nouvelle tâche :

def ajouter_tache(taches):

	titre = input("Veuillez saisir le titre de la tâche : ") 
	tache_id = max(taches.keys(), default=0) + 1
	taches[tache_id] = {"titre" : titre, "statut" : "Incomplète"}
	print(f"Tâche '{titre}' ajoutée.")

# Fonction pour voir toutes les tâches

def voir_tache(taches):
	if not taches:
		print("Il n'y a pas de tâche disponible")
	else:
		for tache_id, tache in taches.items() :
			print(f"[{tache_id}] {tache['titre']} - {tache['statut']}")

# Marquer la tâche comme complète
 
def tache_complete(taches):
	tache_id = int(input("Entrez l'Id de la tâche marquer complète :"))
	if tache_id in taches:
		taches[tache_id]["statut"] = "complete"
		print(f"tâche'{taches[tache_id]['titre']}' marqué comme complète")
	else:
		print(" La tâche n'existe pas veuillez en créer une")

# Supprimer une tache

def supprimer_tache(taches):
	tache_id = int(input("Entrez l'Id de la tâche marquer complète :"))
	if tache_id in taches:
                supprimer_tache = taches.pop(tache_id)
                print(f"tâche '{supprimer_tache['titre']}' supprimé.") 
	else:
                print(f" La tâche n'existe pas veuillez en créer une") 

 # Menu principale 

def main() :

	taches = charger_tache()
	while True :
		print("\nMenu de gestion des tâches: ")
		print("1. Ajouter une tâche")
		print("2. Voir les tâches")
		print("3. Marqué tâche comme complète")
		print("4. Supprimé la tâche")
		print("5. Quitter")
		
		choix = input("Entrez votre choix: ")
		
		if choix == "1" :
			ajouter_tache(taches)
		elif choix == "2" :
			voir_tache(taches)
		elif choix == "3" :
			tache_complete(taches)
		elif choix == "4" :
			supprimer_tache(taches)
		elif choix == "5" :
			sauvegarde(taches)

			print("À bientôt")
			break
		else :
			print("Choix invalide, veuillez reéssayer")
			
# Executons la fonction principale

if __name__ == "__main__" :
	main()
