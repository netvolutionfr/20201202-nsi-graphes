class Vehicule():
    couleur = "rouge"
    roues = 2
    nom = ""
    son = "Tutut"

    def __init__(self, nom="", roues=4):
        if roues > 0:
            self.roues = roues
        if nom == "":
            self.nom = "Mon véhicule"
        else:
            self.nom = nom

    def klaxonne(self, son=""):
        if (son == ""):
            print(self.son)
        else:
            print(son)

    def montrer_couleur(self):
        return self.couleur

    def repeindre(self, couleur):
        self.couleur = couleur


mon_vehicule = Vehicule()
print(mon_vehicule.nom)
print(mon_vehicule.roues)
mon_vehicule.klaxonne()

mon_vehicule2 = Vehicule("Vélo", 2)
print(mon_vehicule2.nom)
print(mon_vehicule2.roues)

mon_vehicule2.klaxonne("Pouetpouet")

print(mon_vehicule.montrer_couleur())
mon_vehicule.repeindre("vert")
print(mon_vehicule.montrer_couleur())
