import pygame

#Variables Globales entre archivos
WIDTH = 800
HEIGHT = 600
screen_center = (WIDTH/2,HEIGHT/2)

#variables texto

text_speed_1 = 45             #45
text_speed_2 = 20             #20
text_speed_credits = 60             #60

text_tamano_1 = 30          #30
text_tamano_2 = 30          #30
text_tamano_credits_title = 20          #20
text_tamano_credits_normal = 30      #30



#reloj global
reloj = pygame.time.Clock()

#pantalla global
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("La marmota mistica - Episodio 1")
icon = pygame.image.load("img/icon.png").convert_alpha()
pygame.display.set_icon(icon)
