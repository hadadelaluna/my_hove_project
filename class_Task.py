    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.completée = False

    def marquer_comme_complétée(self):
        self.completée = True