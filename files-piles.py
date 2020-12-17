class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        if len(self.contenu) == 0:
            return True
        else:
            return False

    def empiler(self, element):
        self.contenu.append(element)

    def depiler(self):
        element = self.contenu.pop()
        return element

    def afficher(self):
        print(self.contenu)




class File:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        if len(self.contenu) == 0:
            return True
        else:
            return False

    def enfiler(self, element):
        self.contenu.append(element)

    def defiler(self):
        element = self.contenu.pop(0)
        return element

    def afficher(self):
        print(self.contenu)


P = File()
P.enfiler(8)
P.enfiler(5)
P.enfiler(2)
P.enfiler(4)
P.afficher()

Q = File()
while not P.est_vide():
    Q.enfiler(P.defiler())

Q.afficher()
P.afficher()


