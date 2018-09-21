import pygame
import sprites


class button(sprites.sprites):

    def __init__(self,pantalla = "",directorio="sprites/",posicion = (0,0)): 
        sprites.sprites.__init__(self,pantalla,directorio,posicion)
        
        
