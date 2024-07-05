# ToDoList_CLI.py

from class_Task import Task
from class_TaskManager import TaskManager

def afficher_menu():
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme complétée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

def main():
    gestionnaire = TaskManager()
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        if choix == '1':
            titre = input("Titre de la tâche : ")
            description = input("Description de la tâche : ")
            date_limite = input("Date limite (YYYY-MM-DD) : ")
            priorité = input("Priorité (haute, moyenne, basse) : ")
            gestionnaire.ajouter_tâche(titre, description, date_limite, priorité)
        elif choix == '2':
            gestionnaire.lister_tâches()
        elif choix == '3':
            index = int(input("Numéro de la tâche à marquer comme complétée : ")) - 1
            gestionnaire.marquer_tâche_comme_complétée(index)
        elif choix == '4':
            index = int(input("Numéro de la tâche à supprimer : ")) - 1
            gestionnaire.supprimer_tâche(index)
        elif choix == '5':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
