import turtle
turtle.tracer(0, 0)
turtle.screensize(2000, 2000)
turtle.pu()
turtle.goto(-500, 0)
turtle.pd()


def dessiner(tapis, longueur, angle):
    for caractere in tapis:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


def regleSierpinsky(chaine):
    nouvelleChaine = ''
    for lettre in chaine:
        if lettre == 'F':
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'
        else:
            if lettre == 'G':
                nouvelleChaine = nouvelleChaine + 'GG'
            else:
                nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine


def tapisSierpinsky(motifInitial, niter):
    tapis = motifInitial
    for i in range(niter):
        nouveauMotif = regleSierpinsky(tapis)
        tapis = nouveauMotif
    return tapis


def fractale(motifInitial, niter):
    tapis = tapisSierpinsky(motifInitial, niter)
    fractale = ''
    for _ in range(3):
        fractale += tapis
        fractale += '--'
    return fractale


longueur = 10
angle = 120
niter = 6

dessiner(tapisSierpinsky('F−G−G', niter), longueur, angle)
