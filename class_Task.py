class Task:
    def __init__(self, titre, description, date_limite=None, priorité='moyenne'):
        self.titre = titre
        self.description = description
        self.date_limite = date_limite
        self.priorité = priorité
        self.completée = False

    def marquer_comme_complétée(self):
        self.completée = True
