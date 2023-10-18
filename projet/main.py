import pygame
pygame.init()


class InfoGame:
    def __init__(self):
        self.StartGame = False
        self.InGame = True

def quiter():
    Game.InGame = False
    pygame.quit()
    print("jeu fermer")
    exit()

pygame.display.set_caption("Anti-Virus")
screen = pygame.display.set_mode((1080,720))

bouton_vert = pygame.image.load("assets/button_vert.png")
bouton_orange = pygame.image.load("assets/button_orange.png")
bouton_rouge = pygame.image.load("assets/button_rouge.png")
bouton_bleu = pygame.image.load("assets/button_bleu.png")
bouton_violer = pygame.image.load("assets/button_violer.png")


Game = InfoGame()
while Game.InGame == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quiter()
    screen.fill((60,120,240))
    pygame.display.flip()
pygame.quit()
print("jeu fermer")