import pygame

#imagen -> surface
#posicion -> (int, int)
#rect -> Rect
#pantalla -> surface (principal)
#directorio -> str
class img:
    def __init__(self,pantalla = None,imagen = "",alpha = True,directorio = 'img/', posicion=(0,0)):
        self.imagen = None
        self.rect = pygame.Rect(0,0,0,0)
        self.posicion = posicion
        self.pantalla = pantalla
        self.directorio = directorio

        if posicion != (0,0): self.position(posicion)
        if imagen != "": self.image(imagen,alpha)

    #screen: self surface -> None
    #coloca pantalla como la surface principal sobre la cual estara el background
    def screen(self,pantalla):
        self.pantalla = pantalla

    #directory: self str -> None
    #cambia el directorio en el cual estan ubicadas las imagenes
    def directory(self, directorio):
        self.directorio = directorio

    #position: self (int int) -> None
    #modifica la posicion del background
    def position(self,tupla):
        self.posicion = tupla
        self.rect.center = self.posicion

    #image: self str bool -> None
    #carga la imagen que contendra el background
    def image(self, nombre = "", alpha = False):
        if alpha:
            self.imagen = pygame.image.load(self.directorio + nombre).convert_alpha()
        if not(alpha):
            self.imagen = pygame.image.load(self.directorio + nombre).convert()

        self.rect = self.imagen.get_rect()
        self.rect.center = self.posicion

    #update: self -> None
    #funcion que recarga la imagen en la pantalla asiganada al objeto
    def update(self):
        self.pantalla.blit(self.imagen,self.rect)
   

        


