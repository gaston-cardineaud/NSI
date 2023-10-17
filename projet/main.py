import pygame
pygame.init()

pygame.display.set_caption("Anti-Virus")
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

background = pygame.image.load("assets/background.jpg")

InGame = True
while InGame:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            InGame = False
            pygame.quit()
            print("jeu fermer")




