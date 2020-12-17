from graphviz import Digraph


class Graphe():
    """Graphe implémenté à l'aide d'un dictionnaire
    Exemple :
    {'A': [('M', 65), ('R', 90), ('T', 80)],
     'G': [('L', 70)],
     'L': [('G', 70), ('P', 230), ('T', 260)],
     'M': [('A', 65), ('P', 95), ('R', 90), ('T', 55)],
     'P': [('L', 230), ('M', 95), ('T', 130)],
     'R': [('A', 90), ('M', 90)],
     'T': [('A', 80), ('L', 260), ('M', 55), ('P', 130)]}
    """

    def __init__(self, noeuds=None):
        """Initialisation avec un graphe vide
        __noeuds est un dictionnaire
        - clé = Valeur du noeud (chaine, entier)
        - valeur = liste d'aretes (clé, poids)"""
        if noeuds is None:
            self.__noeuds = dict()
        else:
            self.__noeuds = noeuds

    def importe_matrice(self, matrice, noms):
        """Importe une matrice d'adjacence"""
        longueur = len(matrice)
        for i in range(longueur):
            self.__noeuds[noms[i]] = []
            for j in range(longueur):
                if matrice[i][j] != 0:
                    self.__noeuds[noms[i]].append((noms[j], matrice[i][j]))

    def ajouter_noeud(self, nd):
        """Ajoute un nouveau noeud au graphe"""
        if not nd in self.__noeuds:
            self.__noeuds[nd] = []

    def ajouter_arete(self, nd1, nd2, poids=1):
        """Ajoute une arête au graphe
        si poids n'est pas renseigné, il prendra la valeur 1"""
        # On s'assure que les arètes existent
        self.ajouter_noeud(nd1)
        self.ajouter_noeud(nd2)
        # On crée la connexion nd1 -> nd2
        self.__noeuds[nd1].append((nd2, poids))

    def ajouter_arete_nonorientee(self, nd1, nd2, poids=1):
        self.ajouter_arete(nd1, nd2, poids)
        self.ajouter_arete(nd2, nd1, poids)

    def liste_noeuds(self):
        """Renvoie la liste des noeuds"""
        nds = list(self.__noeuds.keys())
        nds.sort()
        return nds

    def voisins(self, nd):
        """Renvoie la liste des noeuds voisins de nd"""
        if nd in self.liste_noeuds():
            return [a[0] for a in self.__noeuds[nd]]
        else:
            return []

    def arete(self, nd1, nd2):
        """Renvoie le poids de l'arete nd1->nd2 ou 0 si pas d'arête"""
        if nd2 not in self.voisins(nd1):
            return 0
        for a in self.__noeuds[nd1]:
            if a[0] == nd2:
                return a[1]

    def show(self):
        """Représentation graphique avec graphviz"""
        dot = Digraph(comment="Graphe", format='png')
        for nd in self.liste_noeuds():
            dot.node(nd, nd)
            for a in self.__noeuds[nd]:
                # Teste si l'arête est orientée
                if self.arete(a[0], nd) == self.arete(nd, a[0]):
                    # dessin d'une arête non orientée
                    if a[0] < nd:
                        # On ne dessine qu'une seule arête sur les 2
                        if a[1] != 1:
                            dot.edge(nd, a[0], label=str(a[1]), dir="none")
                        else:
                            dot.edge(nd, a[0], dir="none")
                else:
                    # dessin d'une arête orientée
                    if a[1] != 1:
                        dot.edge(nd, a[0], label=str(a[1]))
                    else:
                        dot.edge(nd, a[0])
        return dot


""" 1er cas : je passe un paramètre au constructeur """

mesnoeuds = {
    "A": [("B", 1), ("C", 1)],
    "B": [("A", 1), ("D", 1)],
    "C": [("A", 1)],
    "D": [("B", 1)]
}

mongraphe3 = Graphe()
matrice = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0]
]
mongraphe3.importe_matrice(matrice, ["A", "B", "C", "D", "E"])

monarbre = Graphe()
matrice_arbre = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
]
monarbre.importe_matrice(matrice_arbre, ["A", "B", "C", "D", "E", "F", "G", "H", "I"])
representation = monarbre.show()
representation.render()
