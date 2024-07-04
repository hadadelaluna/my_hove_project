    def __init__(self):
        self.tâches = []

    def ajouter_tâche(self, titre, description):
        tâche = Task(titre, description)
        self.tâches.append(tâche)

    def lister_tâches(self):
        for index, tâche in enumerate(self.tâches):
            status = "Completée" if tâche.completée else "Non completée"
            print(f"{index + 1}. {tâche.titre} - {tâche.description} ({status})")

    def marquer_tâche_comme_complétée(self, index):
        if 0 <= index < len(self.tâches):
            self.tâches[index].marquer_comme_complétée()

    def supprimer_tâche(self, index):
        if 0 <= index < len(self.tâches):
            del self.tâches[index]