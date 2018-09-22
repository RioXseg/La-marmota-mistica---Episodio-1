import pygame
import thread

#imagenes -> list(surface)
#actual -> surface
#pantalla -> surface
#directorio -> str
#posicion -> (int int)
#rect -> Rect
class sprites:

    def __init__(self,pantalla = None,directorio = "sprites/", posicion = (0,0)):
        
        self.imagenes = []
        self.actual = None
        self.pantalla = pantalla
        self.directorio = directorio
        self.posicion = posicion
        self.rect = pygame.Rect(posicion,(0,0))

        if self.posicion != (0,0): self.position(posicion)
        
    #screen: self surface -> None
    #coloca pantalla como la surface principal sobre la cual estara el sprite
    def screen(self,pantalla):
        self.pantalla = pantalla

    #directory: self str -> None
    #cambia el directorio en el cual estan ubicadas las imagenes
    def directory(self,directorio):
        self.directorio = directorio

    #add: self str bool -> None
    #anade la imagen a la lista de imagenes del objeto (self.imagenes)
    #si solo hay una imagen esta se colocara como imagen actual
    def add(self,imagen,alpha = True):
        if alpha:
            aux1 = pygame.image.load(self.directorio + imagen)
            aux2 = aux1.convert_alpha()
            self.imagenes.append(aux2)
        if not(alpha):
            aux1 = pygame.image.load(self.directorio + imagen)
            aux2 = aux1.convert()
            self.imagenes.append(aux2)

        if len(self.imagenes) == 1: self.current(0)

    #current: self int -> None
    #cambia la imagen actual por una de la lista de imagenes
    def current(self,indice):
        self.actual = self.imagenes[indice]
        
        self.rect = self.actual.get_rect()
        self.rect.center = self.posicion

    #pop: self int -> surface
    #elimina de la lista de imagenes una imagen (y la retorna)
    def pop(self,indice):
        self.imagenes.pop(indice)

    #position: self (int int) -> None
    #modifica la posicion del sprite
    def position(self,tupla):
        self.posicion = tupla
        self.rect.center = self.posicion

    #update: self -> None
    #funcion que recarga la imagen en la pantalla asiganada al objeto
    def update(self):
        self.pantalla.blit(self.actual,self.rect)

    
class personaje(sprites):
    def __init__(self,pantalla = None,directorio = "sprites/",posicion = (0,0)):
        sprites.__init__(self,pantalla,directorio,posicion)
        self.isVisible = True
        self.isAnim01 = False
        self.reloj = pygame.time.Clock()
        
    #move_ip: self (int int) -> None
    #mueve la posicion de un personaje de forma relativa
    def move_ip(self,tupla):
        x = self.posicion[0]
        y = self.posicion[1]
        self.position((x + tupla[0],y + tupla[1]))
        
    #move_anim: self (int int) int -> None
    #crea la animacion de movimiento de un personaje (traslacion)
    def anim_01(self,tupla,velocidad):
        thread.start_new_thread(self.anim_01_True,(tupla,velocidad))
        
    #end_move_anim: self -> None
    #termina la animacion de movimiento dejando al personaje en el lugar final
    def end_anim_01(self):
        self.Anim01 = False
        
    #move_anim_True: self (int int) int -> none
    #crea la animacion de movimiento de un personaje (traslacion)
    def anim_01_True(self,tupla,velocidad):
        termino = False
        self.isAnim01 = True
        
        while not(termino):
            if self.isAnim01 == False:
                self.position(tupla)
                termino = True
                
            if self.posicion == tupla:
                termino = True
                self.Anim01 = False
                
            if self.posicion[0] < tupla[0]:
                self.move_ip((1,0))
            if self.posicion[0] > tupla[0]:
                self.move_ip((-1,0))
                
            if self.posicion[1] < tupla[1]:
                self.move_ip((0,1))
            if self.posicion[1] > tupla[1]:
                self.move_ip((0,-1))
                
            self.reloj.tick(velocidad)
       
    #update: self -> None
    #actualiza los objetos en pantalla (si es que estan visibles)
    def update(self):
        if self.isVisible:
            self.pantalla.blit(self.actual,self.rect)
        
        

        
        
        
        
        
        
        
        
        
        
        
