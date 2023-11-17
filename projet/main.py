import pygame
from math import *
pygame.init()

class InfoGame:
    def __init__(self):
        self.InGame = True ##variable pour la boucle while
        self.tuto = True ##affichage du tuto du demarage
        self.win = False
        self.menu = 1  ##variable pour savoir si on est dans le menu (1 = menu base 2 = choix niveau 3 = partie demarer)
        self.difficulter = 1 ## 1 = starter / 2 = junior / 3 = master / 4 = expert
        self.level = 1 ## quelle est le niveau choisi
        self.choix = 1 ##utile pour le menu
        self.map = [[0, 1, 0, 1, 0, 1, 0], ##representation du plateau
                    [1, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0, 1, 0]]
        self.total_piece = [] ##lors du menu3 contient toute les piece sur le plateau



def quitter():
    '''
    a son appel stop le programm
    '''
    Game.InGame = False
    pygame.quit()
    print("Jeu fermé")
    quit()


class img:
    '''
    permet de stocker les image avec des information utile
    '''
    list = [] ##list contenant toute les immage instaler
    def __init__(self,name,x=0,y=0,scale=1,active = False,when = None):
        image = pygame.image.load(f"assets/{name}.png")
        largeur = image.get_width()
        hauteur = image.get_height()
        self.image = pygame.transform.scale(image,(int(largeur*scale),int(hauteur*scale)))
        largeur *= scale
        hauteur *= scale
        x= int(x-(largeur/2))
        y = int(y)
        self.taille = (largeur,hauteur)
        self.topleft = (x,y)
        self.activ = active
        self.name = name
        self.when = when ##contient un chiffre corespondant a qu'elle menu nous somme
        img.list.append(self)




    def rotate(self, angle):
        ## dois normalement renvoyer les nouvel coordonée apres la rotation de l'img
        return (self.topleft)




def wrap_text(text, font, max_width):
    # Divise le texte en lignes pour s'adapter à la largeur maximale
    lines = []
    words = text.split(" ")
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        test_size = font.size(test_line)

        if test_size[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines

def afficher_texte(texte, position, taille=30, color=(0, 0, 0), max_width=860):
    '''
    permet d'aficher du texte a la position voulue
    '''
    font = pygame.font.Font(None, taille)
    lines = texte.split("\n")  # Divise le texte en lignes à chaque "\n"

    y = position[1]
    for line in lines:
        # Découpe la ligne si une largeur maximale est spécifiée
        wrapped_lines = wrap_text(line, font, max_width)
        for wrapped_line in wrapped_lines:
            texte_rendu = font.render(wrapped_line, True, color)
            texte_rect = texte_rendu.get_rect()
            texte_rect.center = (position[0], y)
            screen.blit(texte_rendu, texte_rect)
            y += font.get_linesize()



def affiche():
    '''
    fonction principal permettant de gérer tout l'affichage a son appel selon dans qu'elle menu nous somme
    '''
    screen.blit(image_fond, (0, 0)) ##afiche le font
    l = img.list
    for i in l: ##affiche les img "basic"
        if i.when == Game.menu:
            screen.blit(i.image,i.topleft)
        elif i.activ:
            screen.blit(i.image,i.topleft)
    if Game.menu == 1: ##affichage particuler du menu1
        if Game.choix == 1:
            im = pygame.transform.rotate(eguille.image,-80)
            co = eguille.rotate(-80)
            screen.blit(im,co)
        elif Game.choix ==2:
            im = pygame.transform.rotate(eguille.image,-100)
            co = eguille.rotate(-100)
            screen.blit(im,co)
        elif Game.choix == 3:
            im = pygame.transform.rotate(eguille.image,100)
            co = eguille.rotate(100)
            screen.blit(im,co)
        elif Game.choix == 4:
            im = pygame.transform.rotate(eguille.image,80)
            co = eguille.rotate(80)
            screen.blit(im,co)
    if Game.menu == 2: ##affichage particulier du menu2
        compte = 0
        for i in l:
            if i.name[:-1] == "button":
                compte += 1
                afficher_texte(("level "+str(compte)),(i.topleft[0]+i.taille[0]/2,i.topleft[1]+i.taille[1]/2),taille=50)
            if i.name == "button-gris":
                afficher_texte("retour",(i.topleft[0]+i.taille[0]/2,i.topleft[1]+i.taille[1]/2),taille=50)
        if Game.choix == 1:
            im = pygame.transform.rotate(eguille2.image,-80)
            co = eguille2.rotate(-80)
            screen.blit(im,co)
        elif Game.choix ==2:
            im = pygame.transform.rotate(eguille2.image,-20)
            co = eguille2.rotate(-10)
            screen.blit(im,co)
        elif Game.choix == 3:
            im = pygame.transform.rotate(eguille2.image,20)
            co = eguille2.rotate(10)
            screen.blit(im,co)
        elif Game.choix == 4:
            im = pygame.transform.rotate(eguille2.image,80)
            co = eguille2.rotate(80)
            screen.blit(im,co)
    if Game.menu == 3: ##affichage particulier menu3
        afficher_texte(("retour"),(retour.topleft[0]+retour.taille[0]/2,retour.topleft[1]+retour.taille[1]/2),taille=35)
        afficher_texte(("tuto"),(tuto.topleft[0]+tuto.taille[0]/2,tuto.topleft[1]+tuto.taille[1]/2),taille=35)
        screen.blit(pygame.transform.scale(Game.total_piece[Game.choix].image,(int(Game.total_piece[Game.choix].taille[0]*0.3),int(Game.total_piece[Game.choix].taille[1]*0.3))),(60,65))
        afficher_texte(("pièce sélectionnée"),(75,260),taille=22)
        afficher_texte(("déplacement"),(865,355),taille=30)
        if Game.difficulter == 1:
            a= 'starter'
        elif Game.difficulter ==2:
            a= "junior"
        elif Game.difficulter ==3:
            a = "expert"
        else:
            a = "master"
        afficher_texte((f"dif : {a}\nlv : {Game.level}\n\nRappel :\nLes pièces blanches sont imbougeables.\nL'objectif est de mettre la pièce rouge en haut à gauche.\n\nBon courage !"),(865,30),taille=30,max_width=200)

def ajout_menu3():
    '''
    charge les image utile du menu 3 et reset la liste img.list
    '''
    img.list = []
    global sup,sup2,sup3,retour,tuto,sup4,sup5,p_blanc,p_bleu,p_bleu2,p_jaune,p_orange,p_rose,p_rouge,p_verte,p_verte2,p_violet,p_blanc3,p_blanc2,p_rose2,p_orange2,p_orange3,fg,fd,dep_g,dep_d,dep_h,dep_b
    sup = img("bannerBottom",x=750,y=0,when=3,scale=0.6)
    sup2 = img("bannerBottom",x=150,y=50,when=3,scale=0.6)
    sup3 = img("bannerBottom2",x=0,y=50,when=3,scale=0.6)
    sup4 = img("bannerBottom2",x=0,y=270,when=3,scale=0.6)
    retour = img("button-gris",x=70,y=280,when=3,scale=1)
    tuto = img("button-gris",x=70,y=400,when=3,scale=1)
    p_blanc = img("piece_blance",scale=0.87)
    p_blanc2 = img("piece_blance",scale=0.87)
    p_blanc3 = img("piece_blance",scale=0.87)
    p_bleu = img("piece_bleu",scale=0.87)
    p_bleu2 = img("piece_bleu2",scale=0.87)
    p_jaune = img("piece_jaune",scale=0.87)
    p_orange = img("piece_orange",scale=0.87)
    p_rose = img("piece_rose",scale=0.87)
    p_rouge = img('piece_rouge',scale=0.87)
    p_verte = img("piece_verte",scale=0.87)
    p_verte2 = img("piece_verte2",scale=0.87)
    p_violet = img("piece_violet",scale=0.87)
    p_rose2 = img("piece_rose2",scale=0.87)
    p_orange2 = img("piece_orange2",scale=0.87)
    p_orange3 = img("piece_orange3",scale=0.87)
    fg = img("fleche2",x=25,y=180,when=3,scale=0.6)
    fd = img("fleche",x=120,y=180,when=3,scale=0.6)
    dep_g = img("fleche",x=815,y=370,when=3,scale=1)
    dep_b = img("fleche",x=815,y=450,when=3,scale=1)
    dep_d = img("fleche",x=895,y=450,when=3,scale=1)
    dep_h = img("fleche",x=895,y=370,when=3,scale=1)

    sup5 = sup4 = img("bannerBottom2",x=900,y=325,when=3,scale=0.6)
    dep_g.image = pygame.transform.rotate(fd.image,-225)
    dep_b.image = pygame.transform.rotate(fd.image,-135)
    dep_d.image = pygame.transform.rotate(fd.image,-405)
    dep_h.image = pygame.transform.rotate(fd.image,-315)

def ajout_menu2():
    '''
    charge les image utile du menu 2 et reset la liste img.list
    '''
    img.list = []
    Game.choix = 1
    global lv1,lv2,lv3,retour,eguille2
    lv1 = img("button"+str(Game.difficulter),x=230,y=hauteur_ecran/2.5,when=2,scale=1.5)
    lv2 = img("button"+str(Game.difficulter),x=370,y=hauteur_ecran/1.5,when=2,scale=1.5)
    lv3 = img("button"+str(Game.difficulter),x=largeur_ecran-370,y=hauteur_ecran/1.5,when=2,scale=1.5)
    retour = img("button-gris",x=largeur_ecran-230,y=hauteur_ecran/2.5,when=2,scale=1.5)
    eguille2 = img("eguille",scale=1,x=largeur_ecran/2,y= hauteur_ecran/3)

def ajout_menu1():
    '''
    charge les image utile du menu 1 et reset la liste img.list
    '''
    img.list = []
    Game.choix = 1
    global roue,junior,starter,master,expert,eguille
    roue = img("roue",scale = 1,x=largeur_ecran/2,y=hauteur_ecran/3,when=1)
    junior = img("junior",scale= 1,x=largeur_ecran/2-roue.taille[1]/1.1,y=roue.topleft[1]+roue.taille[1]/4,when=1)
    starter = img("starter",scale= 1,x=largeur_ecran/2-roue.taille[1]/1.1,y=junior.topleft[1]+junior.taille[1]*1.9,when=1)
    master = img("master",scale= 1,x=largeur_ecran/2+roue.taille[1]/1.1,y=junior.topleft[1]+junior.taille[1]*1.9,when=1)
    expert = img("expert",scale= 1,x=largeur_ecran/2+roue.taille[1]/1.1,y=roue.topleft[1]+roue.taille[1]/4,when=1)
    eguille = img("eguille",scale=1,x=largeur_ecran/2,y= roue.topleft[1]+roue.taille[1]/2-50,when=None)

def tuto1():
    '''
    a son appel affiche les information utile lors du tuto1
    '''
    image_fond = pygame.image.load("assets/loading.png")
    image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))
    screen.blit(image_fond, (0, 0)) ##afiche le font
    afficher_texte("Bienvenue dans Anti-Virus Games ! \n\nPour vous déplacer dans le menu, utilisez les flèches droite ou gauche du clavier. \n Pour valider, appuyez sur espace ou entrée ou flèche du haut ou flèche du bas. \n\n Un autre tuto arrivera avant de commencer le jeu.\n\n*** pour continuer appuyez sur espace ou  cliquez ! ***",(largeur_ecran/2,50),taille=45,max_width=860)

def tuto2():
    '''
    a son appel affiche les information utile lors du tuto2
    '''
    image_fond = pygame.image.load("assets/loading.png")
    image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))
    screen.blit(image_fond, (0, 0)) ##afiche le font
    screen.blit(pygame.image.load("assets/help1.jpg"),(710,290))
    screen.blit(pygame.image.load("assets/help2.jpg"),(710,40))
    afficher_texte("L'objectif est de déplacer la pièce rouge en haut à gauhe.\nToutes les pièces se déplacent en diagonale sauf les pièces blanches.\nPour déplacer une pièce il vous faut la sélectionner en haut à gauche et ensuite la déplacer soit via les flèches du clavier soit en cliquant sur les flèches en bas à droite. \n\n Bonne chance !\n\n\n\n\n\n\n*** pour continuer appuyez sur espace ou cliquez ! ***",(370,50),taille=35,max_width=700)

def souris_clic(event):
    '''
    lors du menu 3 gere tout les clic recu pour joué aux jeux
    '''
    if event.button == 1:
        x,y = event.pos
        print(x,y)
        if retour.topleft[0] <= x <= retour.topleft[0]+retour.taille[0] and retour.topleft[1] <= y <= retour.topleft[1]+retour.taille[1]: ##si le clic est sur le bouton retour
            Game.menu =2
            ajout_menu2()
        elif tuto.topleft[0] <= x <= tuto.topleft[0]+tuto.taille[0] and tuto.topleft[1] <= y <= tuto.topleft[1]+tuto.taille[1]:
            Game.tuto = True
        elif fd.topleft[0] <= x <= fd.topleft[0]+fd.taille[0] and fd.topleft[1] <= y <= fd.topleft[1]+fd.taille[1]:
            if Game.choix != len(Game.total_piece)-1:
                Game.choix = Game.choix +1
            else:
                Game.choix = 0
        elif fg.topleft[0] <= x <= fg.topleft[0]+fg.taille[0] and fg.topleft[1] <= y <= fg.topleft[1]+fg.taille[1]:
            if Game.choix != 0:
                Game.choix = Game.choix -1
            else:
                Game.choix = len(Game.total_piece)-1
        elif dep_h.topleft[0] <= x <= dep_h.topleft[0]+dep_h.taille[0] and dep_h.topleft[1] <= y <= dep_h.topleft[1]+dep_h.taille[1]:
            deplacement("h")
        elif dep_b.topleft[0] <= x <= dep_b.topleft[0]+dep_b.taille[0] and dep_b.topleft[1] <= y <= dep_b.topleft[1]+dep_b.taille[1]:
            deplacement("b")
        elif dep_d.topleft[0] <= x <= dep_d.topleft[0]+dep_d.taille[0] and dep_d.topleft[1] <= y <= dep_d.topleft[1]+dep_d.taille[1]:
            deplacement("d")
        elif dep_g.topleft[0] <= x <= dep_g.topleft[0]+dep_g.taille[0] and dep_g.topleft[1] <= y <= dep_g.topleft[1]+dep_g.taille[1]:
            deplacement("g")


def setup_map():
    '''
    fonction utile
    a son appel crée la map selon la dificulter et le lv choisis
    '''
    Game.map = [[0, 1, 0, 1, 0, 1, 0],[1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0],[1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0],[1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0]]
    Game.total_piece = []

    largeur_initial = 218
    hauteur_initial = 38
    ecart_largeur = 73
    ecart_hauteur = 63

    if Game.difficulter == 1: #starter
        if Game.level == 1:
            Game.map[4][4],Game.map[5][5] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.total_piece.append(p_rouge)
        elif Game.level ==2:
            Game.map[4][4],Game.map[5][5] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.map[3][3] = p_blanc.name
            p_blanc.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_blanc])
        elif Game.level ==3:
            Game.map[3][5],Game.map[4][6] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+5*ecart_hauteur)
            Game.map[2][4],Game.map[4][4] = p_rose.name,p_rose.name
            p_rose.topleft = (largeur_initial+2*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_rose])
    elif Game.difficulter == 2:
        if Game.level == 1:
            Game.map[5][1],Game.map[6][2] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+5*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[1][1],Game.map[3][1] = p_rose.name,p_rose.name
            p_rose.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[1][3] = p_blanc.name
            p_blanc.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[5][3] = p_blanc2.name
            p_blanc2.topleft = (largeur_initial+5*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_rose,p_blanc,p_blanc2])
        elif Game.level == 2:
            Game.map[5][3],Game.map[6][4] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+5*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[4][2] = p_blanc.name
            p_blanc.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[1][5] = p_blanc2.name
            p_blanc2.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+5*ecart_hauteur)
            Game.map[3][1],Game.map[3][3],Game.map[4][4] = p_verte2.name, p_verte2.name, p_verte2.name
            p_verte2.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_verte2,p_blanc,p_blanc2])
        elif Game.level ==3:
            Game.map[5][1],Game.map[6][2] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+5*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[3][1] = p_blanc.name
            p_blanc.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[3][3] = p_blanc2.name
            p_blanc2.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[0][2],Game.map[1][1] = p_bleu.name,p_bleu.name
            p_bleu.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_bleu,p_blanc,p_blanc2])
    elif Game.difficulter == 3:
        if Game.level ==1:
            Game.map[4][4],Game.map[5][5] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.map[4][2] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[0][4] = p_blanc2.name
            p_blanc2.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.map[1][3],Game.map[3][3],Game.map[3][5] = p_violet.name,p_violet.name,p_violet.name
            p_violet.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_violet,p_blanc2,p_blanc])
        elif Game.level == 2:
            Game.map[4][2],Game.map[5][3] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[3][3] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[4][4],Game.map[4][6] = p_rose2.name,p_rose2.name
            p_rose2.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.map[4][0],Game.map[3][1],Game.map[5][1]=p_orange.name,p_orange.name,p_orange.name
            p_orange.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+0*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_orange,p_rose2,p_blanc])
        elif Game.level == 3:
            Game.map[4][0],Game.map[5][1] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+0*ecart_hauteur)
            Game.map[3][1] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[1][1],Game.map[0][2],Game.map[1][3]=p_orange2.name,p_orange2.name,p_orange2.name
            p_orange2.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.map[1][6] =  p_blanc2.name
            p_blanc2.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+5*ecart_hauteur)
            Game.map[3][3],Game.map[4][2] = p_bleu.name, p_bleu.name
            p_bleu.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_orange2,p_blanc2,p_bleu,p_blanc])
    elif Game.difficulter == 4:
        if Game.level == 1:
            Game.map[4][0],Game.map[5][1] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+0*ecart_hauteur)
            Game.map[6][0],Game.map[6][2] = p_rose2.name, p_rose2.name
            p_rose2.topleft = (largeur_initial+6*ecart_largeur,hauteur_initial+0*ecart_hauteur)
            Game.map[2][2],Game.map[4][2] = p_verte.name, p_verte.name
            p_verte.topleft = (largeur_initial+2*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[3][3] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+3*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[0][4] =  p_blanc2.name
            p_blanc2.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_verte,p_rose2,p_blanc,p_blanc2])
        elif Game.level == 2:
            Game.map[4][4],Game.map[5][5] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+4*ecart_hauteur)
            Game.map[0][6] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+6*ecart_hauteur)
            Game.map[4][2] =  p_blanc2.name
            p_blanc2.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[0][2],Game.map[0][4],Game.map[1][5] = p_verte2.name,p_verte2.name,p_verte2.name
            p_verte2.topleft = (largeur_initial+0*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.map[1][3],Game.map[2][4],Game.map[3][3] = p_orange3.name,p_orange3.name,p_orange3.name
            p_orange3.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[6][2],Game.map[6][4],Game.map[6][6] = p_bleu2.name,p_bleu2.name,p_bleu2.name
            p_bleu2.topleft = (largeur_initial+6*ecart_largeur,hauteur_initial+2*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_verte2,p_orange3,p_bleu2,p_blanc,p_blanc2])
        elif Game.level == 3:
            Game.map[5][3],Game.map[6][4] = p_rouge.name, p_rouge.name
            p_rouge.topleft = (largeur_initial+5*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[1][3] =  p_blanc.name
            p_blanc.topleft = (largeur_initial+1*ecart_largeur,hauteur_initial+3*ecart_hauteur)
            Game.map[2][6] =  p_blanc2.name
            p_blanc2.topleft = (largeur_initial+2*ecart_largeur,hauteur_initial+6*ecart_hauteur)
            Game.map[5][1],Game.map[4][2],Game.map[4][4] = p_jaune.name,p_jaune.name,p_jaune.name
            p_jaune.topleft = (largeur_initial+4*ecart_largeur,hauteur_initial+1*ecart_hauteur)
            Game.total_piece.extend([p_rouge,p_jaune,p_blanc,p_blanc2])

    ##ici on active les image de la map et on retire toute les piece blanche de Game.total_piece car elle ne peuvent pas etre deplacé
    new = []
    for i in range(len(Game.total_piece)):
        Game.total_piece[i].activ = True
        if Game.total_piece[i].name != "piece_blance" :
            new.append(Game.total_piece[i])
    Game.total_piece = new



def deplacement(direction):
    """
    deplace les piece selon la quelle est selection et le deplacement voulu"""
    coordoner = []
    new_coordoner = []
    selection = Game.total_piece[Game.choix]
    for ligne in range(7):
        for colone in range(7):
            if Game.map[ligne][colone] == selection.name:
                coordoner.append([ligne,colone])
    ##coordonner contient les coordoné de tout les point de la piece selectioné
    if direction == "d":
        for i in coordoner:
            if i[0] != 6 and i[1] !=6 and (Game.map[i[0]+1][i[1]+1]==0 or Game.map[i[0]+1][i[1]+1]== selection.name):
                new_coordoner.append([i[0]+1,i[1]+1])
            else:
                new_coordoner = []
                break
    elif direction == "b":
        for i in coordoner:
            if i[0] != 0 and i[1] !=6 and (Game.map[i[0]-1][i[1]+1]==0 or Game.map[i[0]-1][i[1]+1]== selection.name):
                new_coordoner.append([i[0]-1,i[1]+1])
            else:
                new_coordoner = []
                break
    elif direction == "g":
        if Game.map[0][0] == "piece_rouge": ##verifie si la partie est gagné
            Game.win = True
        for i in coordoner:
            if i[0] !=0 and i[1] != 0 and (Game.map[i[0]-1][i[1]-1]==0 or Game.map[i[0]-1][i[1]-1]== selection.name):
                new_coordoner.append([i[0]-1,i[1]-1])
            else:
                new_coordoner = []
                break
    elif direction == "h":
        for i in coordoner:
            if i[0] != 6 and i[1] != 0 and (Game.map[i[0]+1][i[1]-1]==0 or Game.map[i[0]+1][i[1]-1]== selection.name):
                new_coordoner.append([i[0]+1,i[1]-1])
            else:
                new_coordoner = []
                break

    ##new_coordoner contient les co du deplacement, si il est vide alors le deplacement a etait imposible
    if new_coordoner != []:
        for i in coordoner:
            Game.map[i[0]][i[1]] = 0
        for i in new_coordoner:
            Game.map[i[0]][i[1]] = selection.name
    else:
        return ##si deplacement impossible sa sert a rien de continuer la fonction

    ##maintenant le deplacement a etait enregistrer dans le Game.map
    ecart_largeur = 73
    ecart_hauteur = 63

    if direction == 'b':
        selection.topleft = (selection.topleft[0]-ecart_largeur,selection.topleft[1]+ecart_hauteur)
    elif direction == "g":
        selection.topleft = (selection.topleft[0]-ecart_largeur,selection.topleft[1]-ecart_hauteur)
    elif direction == "h":
        selection.topleft = (selection.topleft[0]+ecart_largeur,selection.topleft[1]-ecart_hauteur)
    elif direction == "d":
        selection.topleft = (selection.topleft[0]+ecart_largeur,selection.topleft[1]+ecart_hauteur)

    ##maintenant l'aspet visuel est modifier



def win():
    """
    comme les fonction tuto, gére l'affichage lors d'une partie gagner
    """
    image_fond = pygame.image.load("assets/loading.png")
    image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))
    screen.blit(image_fond, (0, 0)) ##afiche le font
    afficher_texte("Félicitations\n\n C'est gagné :)",taille=100,position=(largeur_ecran/2,50))
    afficher_texte("*** pour continuer appuyez sur espace ou cliquez ! ***",taille=45,position=(largeur_ecran/2,500))
    pass

def clic_menu(event):
    """
    gére tout les clic de la souris pour naviguer de le menu 1 et 2
    """
    x,y = event.pos
    if Game.menu ==1 and event.button ==1:
        if junior.topleft[0] <= x <= junior.topleft[0]+junior.taille[0] and junior.topleft[1] <= y <= junior.topleft[1]+junior.taille[1]:
            Game.menu = 2
            Game.difficulter = 2
            ajout_menu2()

        elif starter.topleft[0] <= x <= starter.topleft[0]+starter.taille[0] and starter.topleft[1] <= y <= starter.topleft[1]+starter.taille[1]:
            Game.menu = 2
            Game.difficulter = 1
            ajout_menu2()
        elif expert.topleft[0] <= x <= expert.topleft[0]+expert.taille[0] and expert.topleft[1] <= y <= expert.topleft[1]+expert.taille[1]:
            Game.menu = 2
            Game.difficulter = 3
            ajout_menu2()
        elif master.topleft[0] <= x <= master.topleft[0]+master.taille[0] and master.topleft[1] <= y <= master.topleft[1]+master.taille[1]:
            Game.menu = 2
            Game.difficulter = 4
            ajout_menu2()
    elif Game.menu == 2 and event.button ==1:
        if lv1.topleft[0] <= x <= lv1.topleft[0]+lv1.taille[0] and lv1.topleft[1] <= y <= lv1.topleft[1]+lv1.taille[1]:
            Game.tuto = True
            ajout_menu3()
            Game.menu = 3
            Game.level = 1
            Game.choix = 0
            setup_map()
        elif lv2.topleft[0] <= x <= lv2.topleft[0]+lv2.taille[0] and lv2.topleft[1] <= y <= lv2.topleft[1]+lv2.taille[1]:
            Game.tuto = True
            ajout_menu3()
            Game.menu = 3
            Game.level = 2
            Game.choix = 0
            setup_map()
        elif lv3.topleft[0] <= x <= lv3.topleft[0]+lv3.taille[0] and lv3.topleft[1] <= y <= lv3.topleft[1]+lv3.taille[1]:
            Game.tuto = True
            ajout_menu3()
            Game.menu = 3
            Game.level = 3
            Game.choix = 0
            setup_map()
        elif retour.topleft[0] <= x <= retour.topleft[0]+retour.taille[0] and retour.topleft[1] <= y <= retour.topleft[1]+retour.taille[1]:
            Game.menu = 1
            ajout_menu1()

def choix(event):
    """
    lors du deplacement aux clavier gere les choix actuelle pour le menu 1 et 2
    """
    if Game.choix >4 or Game.choix <1:
        Game.choix =1
    if event.key == pygame.K_LEFT:
        if Game.choix != 1:
            Game.choix = Game.choix -1
        else:
            Game.choix = 4
    elif event.key == pygame.K_RIGHT:
        if Game.choix != 4:
            Game.choix = Game.choix +1
        else:
            Game.choix = 1
    elif ((event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)) and (Game.menu == 1):
        Game.menu = 2
        Game.difficulter = Game.choix
        ajout_menu2()
    elif ((event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)) and (Game.menu == 2):
        if Game.choix !=4:
            Game.tuto = True
            ajout_menu3()
            Game.menu = 3
            Game.level = Game.choix
            Game.choix = 0
            setup_map()
            ##ici rajouter les image du menu3
        else:
            Game.menu = 1
            ajout_menu1()

# Récupérer la largeur et la hauteur de l'écran
largeur_ecran = 960
hauteur_ecran = 540

pygame.display.set_caption("Anti-Virus")
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) ##taille de la fenetre


Game = InfoGame() ##game contiendra toute les information du jeux

roue,junior,starter,master,expert,eguille = None,None,None,None,None,None ##contiendra les image pour la phase du menu 1
lv1,lv2,lv3,retour,eguille2 = None,None,None,None,None ##contiendra les bulle pour la phase de menu2
sup,retour,tuto,sup2,sup3,sup4,p_blanc,p_bleu,p_bleu2,sup5,p_jaune,p_orange,dep_g,dep_d,dep_h,dep_b,p_rose,p_rouge,p_verte,p_verte2,p_violet,p_blanc3,p_blanc2,p_rose2,p_orange2,p_orange3,fg,fd = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None ##contien image pour menu 3

ajout_menu1() ##charge les image du menu1
while Game.InGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:##verif que la fenetre n'est pas fermer
            quitter()
        elif (Game.menu ==1 or Game.menu ==2) and event.type == pygame.KEYDOWN and Game.tuto == False: ##active la fonction choix si nous somme dans le menu 1 ou 2 et qu'une touche de clavier est saisie
            choix(event)
        elif (Game.menu ==1 or Game.menu ==2) and event.type == pygame.MOUSEBUTTONDOWN and Game.tuto == False: ##active la fonction clic_menu si nous somme dans le menu 1 ou 2 et que la sourie est presser
            clic_menu(event)
        elif Game.tuto and ((event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE ) or event.type == pygame.MOUSEBUTTONDOWN): ##desactive game tuto s'il est actif et qu'on apuie sur espace ou un clic souris
            Game.tuto = False
        elif Game.win and ((event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE ) or event.type == pygame.MOUSEBUTTONDOWN):##desactive game win et retourne dans le menu1 s'il est actif et qu'on apuie sur espace ou un clic souris
            Game.win = False
            Game.menu = 1
            ajout_menu1()
            Game.choix = 1
        elif Game.tuto == False and Game.menu ==3 and event.type == pygame.MOUSEBUTTONDOWN: ##active la fonction souris clic si nous somme dans le menu3 et qu'un clic souris survien
            souris_clic(event)
        elif Game.tuto == False and Game.menu == 3 and event.type == pygame.KEYDOWN: ##active la fonction deplacement si nous somme dans le menu 3 et qu'une fleche est presser
            if event.key == pygame.K_LEFT:
                deplacement("g")
            elif event.key == pygame.K_RIGHT:
                deplacement("d")
            elif event.key == pygame.K_UP:
                deplacement("h")
            elif event.key == pygame.K_DOWN:
                deplacement("b")

    if Game.menu == 2 or Game.menu == 1 and Game.tuto == False: ## change le font selon si on est dans le menu ou non
        image_fond = pygame.image.load("assets/bgLevelSelect.jpg")
        image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))
    elif Game.menu == 3 and Game.tuto == False:
        image_fond = pygame.image.load("assets/backgroundPlay.jpg")
        image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))

    ##active les different affichage selon si des tuto ou win son actif
    if Game.tuto and Game.menu ==1:
        tuto1()
    elif Game.tuto and Game.menu ==3:
        tuto2()
    elif Game.win:
        win()
    else:
        affiche() #fonction qui verifie l'etat du jeux et affiche toute les immage
    pygame.display.flip() ##active les modification d'image
