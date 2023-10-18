import pygame
pygame.init()

def MenuAcceuil(event):
    select = 0
    menu_items = ["Démarrer", "Options", "Quitter"]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            select = (select +1) %len(menu_items)
        elif event.key == pygame.K_UP:
            select = (select -1) %len(menu_items)
        elif event.key == pygame.K_RETURN:
            if select == 0:  # Démarrer  
                print("Démarrer le jeu")
                Game.StartGame = True
            elif select == 1:  # Options
                print("Afficher les options")         
            elif select == 2:  # Quitter
                Game.InGame = False
        

class InfoGame:
    def __init__(self):
        self.StartGame = False
        self.InGame = True
Game = InfoGame


pygame.display.set_caption("Anti-Virus")
screen = pygame.display.set_mode(1080,720)

background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))


while Game.InGame:
    screen.blit(background,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.InGame = False
            pygame.quit()
            print("jeu fermer")
    if not Game.StartGame :
        MenuAcceuil(event)
pygame.quit()
print("jeu fermer")
    




