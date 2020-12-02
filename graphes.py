# Algorithmes de recherche de chemin
import queue
import time

# définition du graphe
monGraphe = {
    0: [1, 2],
    1: [0, 5],
    2: [4, 0, 3],
    3: [2],
    4: [2],
    5: [1, 7],
    6: [8],
    7: [5, 8],
    8: [6, 7, 9],
    9: [8],
}


def trouver_chemin(graphe, depart, arrivee):
    """
    Algorithme de recherche d'un chemin méthode parcours en profondeur
    """
    prochains = queue.LifoQueue()
    prochains.put(depart)
    predecesseurs = {
        depart: None
    }
    courant = depart
    while (not prochains.empty()) and (courant != arrivee):
        courant = prochains.get()
        for voisin in graphe[courant]:
            if voisin not in predecesseurs.keys():
                predecesseurs[voisin] = courant
                prochains.put(voisin)
    if arrivee not in predecesseurs.keys():
        return None
    else:
        chemin = [arrivee]
        pred = arrivee
        while pred != depart:
            pred = predecesseurs[pred]
            chemin.insert(0, pred)
        return chemin


# calcul du temps d'execution (en demandant 100000 fois la recherche)
t0 = time.time()
for i in range(100000):
    ch1 = trouver_chemin(monGraphe, 9, 3)
t1 = time.time() - t0
print(ch1)
print("Temps de recherche chemin du grand graphe : ", t1)


def find_path(graph, start, end, path=[]):
    """
    Algorithme de recherche d'un chemin méthode récursive
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


t0 = time.time()
for i in range(100000):
    ch2 = find_path(monGraphe, 9, 3)
t1 = time.time() - t0
print(ch2)
print("Temps de recherche chemin du grand graphe : ", t1)


# Recherche d'un cycle dans le graphe
def recherche_cycle(graphe):
    source = 0
    file = queue.Queue()
    file.put(source)
    drapeaux = []
    for sommet in graphe.keys():
        drapeaux.append(-1)
    cycle = False

    while not file.empty():
        courant = file.get()
        drapeaux[courant] = 1
        for voisin in graphe[courant]:
            if drapeaux[voisin] == 0:
                cycle = True
            if drapeaux[voisin] == -1:
                file.put(voisin)
                drapeaux[voisin] = 0
    return cycle


t0 = time.time()
for i in range(100000):
    cycle = recherche_cycle(monGraphe)
t1 = time.time() - t0
print(cycle)
print("Temps de recherche cycle du grand graphe : ", t1)


graphe2 = {
    0: [1, 2],
    1: [1, 5],
    2: [0, 5],
    3: [5],
    4: [2],
    5: [1, 3, 2]
}

t0 = time.time()
for i in range(100000):
    ch1 = trouver_chemin(graphe2, 0, 5)
t1 = time.time() - t0
print(ch1)
print("Temps de recherche chemin du petit graphe : ", t1)

t0 = time.time()
for i in range(100000):
    ch2 = find_path(graphe2, 0, 5)
t1 = time.time() - t0
print(ch2)
print("Temps de recherche chemin du petit graphe : ", t1)

t0 = time.time()
for i in range(100000):
    cycle = recherche_cycle(graphe2)
t1 = time.time() - t0
print(cycle)
print("Temps de recherche cycle petit graphe : ", t1)
