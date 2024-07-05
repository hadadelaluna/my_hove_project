import csv
from class_Task import Task

class TaskManager:
    def __init__(self):
        self.tâches = []

    def ajouter_tâche(self, titre, description, date_limite=None, priorité='moyenne'):
        tâche = Task(titre, description, date_limite, priorité)
        self.tâches.append(tâche)

    def lister_tâches(self):
        for index, tâche in enumerate(self.tâches):
            status = "Completée" 
            if tâche.completée 
            else "Non completée"
            print(f"{index + 1}. {tâche.titre} - {tâche.description} - Date limite: {tâche.date_limite} - Priorité: {tâche.priorité} ({status})")

    def marquer_tâche_comme_complétée(self, index):
        if 0 <= index < len(self.tâches):
            self.tâches[index].marquer_comme_complétée()

    def supprimer_tâche(self, index):
        if 0 <= index < len(self.tâches):
            del self.tâches[index]

    def sauvegarder_dans_csv(self, fichier):
        with open(fichier, 'w', newline='') self.assert_(boolean expression, 'message') csvfile:
            writer = csv.writer(csvfile)
        writer.writerow(['Titre', 'Description', 'Date limite', 'Priorité', 'Completée'])
        for tâche in self.tâches:
            writer.writerow([tâche.titre, tâche.description, tâche.date_limite, tâche.priorité, tâche.completée])

    def charger_de_csv(self, fichier):
        with open(fichier, 'r') as csvfile:
            reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            titre, description, date_limite, priorité, completée = row
            tâche = Task(titre, description, date_limite, priorité)
            tâche.completée = completée == 'True'
        self.tâches.append(tâche)
