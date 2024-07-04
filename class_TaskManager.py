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
            status = "Completée" si tâche.completée sinon "Non completée"
            print(f"{index + 1}. {tâche.titre} - {tâche.description} - Date limite: {tâche.date_limite} - Priorité: {tâche.priorité} ({status})")

    def marquer_tâche_comme_complétée(self, index):
        si 0 <= index < len(self.tâches):
            self.tâches[index].marquer_comme_complétée()

    def supprimer_tâche(self, index):
        si 0 <= index < len(self.tâches):
            del self.tâches[index]

    def sauvegarder_dans_csv(self, fichier):
        avec open(fichier, 'w', newline='') comme csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Titre', 'Description', 'Date limite', 'Priorité', 'Completée'])
            pour tâche dans self.tâches:
                writer.writerow([tâche.titre, tâche.description, tâche.date_limite, tâche.priorité, tâche.completée])

    def charger_de_csv(self, fichier):
        avec open(fichier, 'r') comme csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            pour row dans reader:
                titre, description, date_limite, priorité, completée = row
                tâche = Task(titre, description, date_limite, priorité)
                tâche.completée = completée == 'True'
                self.tâches.append(tâche)
