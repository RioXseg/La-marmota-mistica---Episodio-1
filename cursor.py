import pygame
import sprites

#imagenes -> list(surface)
#actual -> surface
#pantalla -> surface
#directorio -> str
#posicion -> (int int)
#rect -> Rect

#posicion -> (int int)
#movimiento -> (int int)
#visible -> bool
#isImage -> bool
class cursor(sprites.sprites):
    def __init__(self,pantalla = "",directorio="sprites/", posicion = (0,0)):
        sprites.sprites.__init__(self,pantalla,directorio,posicion)
        
        self.movimiento = (0,0)
        self.visible = True
        self.estado = (False,False,False)
        self.isImage = False
        

    #visible: self bool -> None
    #selecciona si la imagen del cursor es visible o no
    def visible(self,visible):
        self.visible = visible
        if self.visible: pygame.mouse.set_visible(True)
        else: pygame.mouse.set_visible(False)

    #update: self -> None
    #recarga los datos del cursor
    def update(self):
        
        self.posicion = pygame.mouse.get_pos()
        self.movimiento = pygame.mouse.get_rel()
        self.estado = pygame.mouse.get_pressed()
        
        if self.imagenes != []: isImage = True
        pygame.mouse.set_visible(self.visible)
    
        if self.isImage:
            (self.rectangulo.left,self.rectangulo.top) = self.posicion
            if self.visible:
                self.pantalla.blit(self.actual,self.posicion)
            
            
            
            
