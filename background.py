import pygame
import img

#imagen -> surface
#pantalla -> surface (principal)
#posicion -> (int, int)
#directorio -> str
class background(img.img):
    #__init__: self surface str str bool tupla -> background
    #crea objeto del tipo background, se recomienda tener solo uno de estos por pantalla
    def __init__(self, pantalla = None, imagen = "",alpha = False, directorio = "bg/", posicion = (0,0)):
        img.img.__init__(self,pantalla,imagen,alpha,directorio,posicion)
        

