import random

class Tiles:
    def __init__(self, mode, niveau,nb_tiles):

        # Dictionnaire associant un chiffre à une flèche du clavier
        self.dict_arrow = {
            0: 'gauche',
            1: 'bas',
            2: 'haut',
            3: 'droite'
        }
        self.score = 0
        self.mode = mode #mode de jeu
        self.niveau = niveau #niveaux du mode 1
        self.nb_tiles = nb_tiles #nombre de combinaison par partie


    # Fonction qui génère les combinaisons
    def get_tiles(self):

        # Création du tableau contenant les combinaisons
        tiles = []

        # Mode 1 : classique
        if self.mode == 1:
            # Niveau 1 : combinaisons d'une seule flèche
            if self.niveau == 1:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Mélanger la liste de manière aléatoire
                    random.shuffle(sequence1)
                    # Ajout de la liste à notre tableau de combinaisons
                    tiles.append(sequence1)

            # Niveau 2 : combinaisons d'une ou deux flèches
            elif self.niveau == 2:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence2 = [0, 0, 1, 1]
                    # Mélanger les listes de manière aléatoire
                    random.shuffle(sequence1)
                    random.shuffle(sequence2)
                    # Probabilités d'obtenir les séquences
                    probabilities = [0.6, 0.4]
                    # Choix de la séquence à ajouter, au hasard entre les deux
                    sequence = random.choices([sequence1, sequence2], probabilities)
                    # Ajout de la liste à notre tableau de combinaisons
                    tiles.append(sequence[0])
            # Niveau 3 : combinaisons d'une, deux ou trois flèches
            elif self.niveau == 3:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence2 = [0, 0, 1, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence3 = [0, 1, 1, 1]
                    # Mélanger les listes de manière aléatoire
                    random.shuffle(sequence1)
                    random.shuffle(sequence2)
                    random.shuffle(sequence3)
                    # Probabilités d'obtenir les séquences
                    probabilities = [0.4, 0.3, 0.3]
                    # Choix de la séquence à ajouter, au hasard entre les trois
                    sequence = random.choices([sequence1, sequence2, sequence3], probabilities)
                    # Ajout de la liste à notre tableau de combinaisons
                    tiles.append(sequence[0])

                # Séléction d'un niveau n'existant pas
                else:
                    print("Ce niveau n'existe pas.")

        # Mode 2 : multiflèche
        elif self.mode == 2:
            for i in range(self.nb_tiles):
                tile = random.choice(0, 1, 2, 3, dtype=int)
                tiles.append(tile)

        # Mode 3 : contre la montre
        elif self.mode == 3:
            for i in range(self.nb_tiles):
                tile = random.choice(0, 1, 2, 3, dtype=int)
                tiles.append(tile)

        # Séléction d'un mode n'existant pas
        else:
            print("Ce mode n'existe pas.")

        return tiles

    # Fonction qui génère le délai entre chaque combinaison
    def get_tiles_delay(self):

        # Création du tableau contenant le délai entre chaque combinaison
        tiles_delay = []

        # Mode 1 : classique
        if self.mode == 1:

            # Niveau 1 : combinaisons d'une seule flèche
            if self.niveau == 1:
                delai=0
                for i in range(self.nb_tiles):
                    # Ajout du délai
                    tiles_delay.append((round(2.3+delai, 1)))
                    delai+=2.3

            # Niveau 2 : combinaisons d'une ou deux flèches
            elif self.niveau == 2:
                delai=0
                for i in range(self.nb_tiles):
                    # Ajout du délai
                    tiles_delay.append((round(2.0+delai, 1)))
                    delai+=2.0

            # Niveau 3 : combinaisons d'une, deux ou trois flèches
            elif self.niveau == 3:
                delai=0
                for i in range(self.nb_tiles):
                    # Ajout du délai
                    tiles_delay.append((round(1.7+delai, 1)))
                    delai+=1.7

            # Séléction d'un niveau n'existant pas
            else:
                print("Ce niveau n'existe pas.")

        # Mode 2 : multiflèche
        elif self.mode == 2:
            delai=0
            for i in range(self.nb_tiles):
                # Ajout du délai
                tiles_delay.append((round(2.0+delai, 1)))
                delai+=2

        # Séléction d'un mode n'existant pas
        else:
            print("Ce mode n'existe pas.")


        return tiles_delay

    def add_score(self,points):
        self.score+=points

    def wich_label(self,points):
        if points < 25:
            return 0
        elif points >= 25 and points <= 50:
            return 1
        elif points >= 50 and points <=75:
            return 2
        elif points >= 75 and points < 100:
            return 3
        elif points == 100 :
            return 4

