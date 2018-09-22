import pygame
import thread

#posicion -> (int int)
#tipo -> str
#color -> (int int int)
#tamano -> int
#imagen -> surface
#fuente -> Font
#linea -> str
#isRender -> bool
#pantalla -> surface
#renderizado -> bool
#rect -> Rect
#isRect -> bool
#rect_center -> (int int)
#terminado -> bool
#comenzado -> bool
class text:
    def __init__(self,pantalla = "",tipo = "Arial",color = (0,0,0),tamano = 24,posicion = (0,0),linea = "",directorio = "font/",nombre="",rectangulo = False,fuente = ""):
	
        self.pantalla = pantalla
        self.posicion = posicion
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
        self.linea = linea
        self.rect = pygame.Rect(self.posicion,(0,0))                        #No se dee utilizar este para mover el rectangulo sino la siguiente
        self.rect_center = self.rect.center                                     #debe utilizarse esta variable para mover al rectangulo     (asi es, falta crear funciones y proteger variables)
        self.fuente = pygame.font.SysFont(self.tipo,self.tamano)
        self.imagen = self.fuente.render("",True,self.color)                #valor inicial
        self.comenzado = False
        self.renderizado = False                                                #indica si el texto esta actualizado con todos los datos mas actuales
        self.terminado = False                                                  #indica si el texto esta en sus condiciones finales
        self.directorio = directorio
        self.nombre = nombre
        self.isSystem = True
        self.isRect = rectangulo
        
        if self.nombre != "":
            self.fuente = pygame.font.Font(self.directorio + self.nombre,self.tamano)
            self.isSystem = False
            
        if fuente != "":
            self.fuente = fuente

    #typ: self str bool -> None
    #modifica el tipo de letra que tendra la fuente del texto (requiere nuevo render), sys sirve para indicar si es una fuente del sistema o no
    def typ(self,tipo,sys = True):
        if sys:
            self.tipo = tipo
            self.isSystem = True
            self.fuente = pygame.font.SysFont(self.tipo,self.tamano)
            self.comenzado = False
            self.renderizado = False
            self.terminado = False
        if not(sys):
            self.nombre = tipo
            self.isSystem = False
            self.fuente = pygame.font.Font(self.directorio + self.nombre,self.tamano)
            self.comenzado = False
            self.renderizado = False
            self.terminado = False

    #colors: self (int int int (int)) -> None
    #modifica el color de el texto (requiere nuevo render)
    def colors(self,color):
        self.color = color
        self.comenzado = False
        self.renderizado = False
        self.terminado = False

    #position: self (int int) -> None
    #modifica la posicion en la que se ubicara el texto
    def position(self,tupla):
        if not(self.isRect):
            self.posicion = tupla
        if self.isRect:
            self.rect_center = tupla

    #line: self str -> None
    #modifica la linea de texto que contiene el objeto (requiere nuevo render)
    def line(self, linea):
        self.linea = linea
        self.comenzado = False
        self.renderizado = False
        self.terminado = False

    #size: self int -> None
    #modifica el tamano de la fuente del texto del objeto (requiere nuevo render)
    def size(self, tamano):
        if self.isSystem:
            self.tamano = tamano
            self.fuente = pygame.font.SysFont(self.tipo,self.tamano)
            self.comenzado = False
            self.renderizado = False
            self.terminado = False
        if not(self.isSystem):
            self.tamano = tamano
            self.fuente = pygame.font.Font(self.directorio + self.nombre,self.tamano)
            self.comenzado = False
            self.renderizado = False
            self.terminado = False
          
    #void: self -> None
    #vacia el objeto quitadole el texto y cambiandole la imagen (self.imagen)
    def void(self):
        self.imagen = self.fuente.render("",True,self.color)
        self.line("")
        self.comenzado = False
        self.renderizado = False
        self.terminado = False
        
    #render: self -> None
    #crea la superficie que contendra el texto
    def render(self):
        self.comenzado = True
        self.imagen = self.fuente.render(self.linea,True,self.color)
        self.renderizado = True
        self.terminado = True

    #update: self -> None
    #actualiza la caja de texto en la pantalla principal
    def update(self):
        if not(self.renderizado):self.render()
        if self.isRect:
            self.rect = self.imagen.get_rect()
            self.rect.center = self.rect_center
            self.pantalla.blit(self.imagen,self.rect)
        if not(self.isRect):
            self.pantalla.blit(self.imagen,self.posicion)
	

class text_anim_01(text):
    def __init__(self,pantalla = "",tipo = "Arial",color = (0,0,0),tamano = 24,posicion = (0,0),linea = "",velocidad = 15, directorio = "font/",nombre = "", rectangulo = False, fuente =""):
    
        text.__init__(self,pantalla,tipo,color,tamano,posicion,linea,directorio,nombre,rectangulo,fuente)
        
        self.reloj = pygame.time.Clock()
        self.velocidad = velocidad
    
    #render: self -> None
    #renderiza el texto en un thread aparte para dejar ejecutarse la animacion
    def render(self):
        thread.start_new_thread(self.render_True,())
    
    #render_True: self -> None
    #funcion que sera llamada por render en un nuevo thread 
    def render_True(self):
        self.comenzado = True
        self.renderizado = False
        self.terminado = False
        for i in range(len(self.linea)):
            self.imagen = self.fuente.render(self.linea[0:i+1],True,self.color)
            self.reloj.tick(self.velocidad)
        self.renderizado = True
        self.terminado = True
    
    #void_line: self str -> None
    #ejecuta las funciones void y line
    #sirve para modificar el mensaje de un cuadro de texto de manera limpia
    def void_line(self,linea):
        self.void()
        self.line(linea)
    
    #update: self -> None
    #actualiza la caja de texto en la pantalla principal
    def update(self):
        if not(self.comenzado): self.render()
        if not(self.isRect):
            self.pantalla.blit(self.imagen,self.posicion)
        if self.isRect:
            self.rect = self.imagen.get_rect()
            self.rect.center = self.rect_center
            self.pantalla.blit(self.imagen,self.rect)
        
        
class text_anim_02(text):
    def __init__(self,pantalla = "",tipo = "Arial",color = (0,0,0),tamano = 24,posicion = (0,0),linea = "",directorio = "font/",nombre="",velocidad = 60, direccion = (0,1),rectangulo = False,fuente = ""):
        text.__init__(self,pantalla,tipo,color,tamano,posicion,linea,directorio,nombre,rectangulo,fuente)

        self.direccion = direccion
        self.velocidad = velocidad
        self.reloj = pygame.time.Clock()
        
    #movimiento: self -> None
    #comienza el movimiento en un nuevo thread
    def movimiento(self):
        self.comenzado = True
        thread.start_new_thread(self.movimiento_True,())
        
    #movimiento_True: self -> None
    #comienza el movimiento del texto, (notar que las variables se pueden cambiar mientras se ejecuta)
    #debe indicarse cuando el texto acabe (self.terminado).
    def movimiento_True(self):
        while not(self.terminado):
            if self.isRect:
                aux1 = self.rect_center[0] + self.direccion[0]
                aux2 = self.rect_center[1] + self.direccion[1]
                
            if not(self.isRect):
                aux1 = self.posicion[0] + self.direccion[0]
                aux2 = self.posicion[1] + self.direccion[1]
                
            self.position((aux1,aux2))
            self.reloj.tick(self.velocidad)
    
    #stop: self -> None
    #Detiene el movimiento del texto
    def stop(self):
        self.direccion = (0,0)
    
    #render: self -> None
    #crea la superficie que contendra el texto
    def render(self):
        self.imagen = self.fuente.render(self.linea,True,self.color)
        self.renderizado = True
    
    #end: self -> None
    #termina el texto (cambia el parametro self.terminado)
    def end(self):
        self.terminado = True
        
    #update: self -> None
    #updatea el texto en la pantalla y comienza la funiones de movimiento
    def update(self):
        if not(self.renderizado): self.render()
        if not(self.comenzado): self.movimiento()
        if self.isRect:
            self.rect = self.imagen.get_rect()
            self.rect.center = self.rect_center
            self.pantalla.blit(self.imagen,self.rect)
        if not(self.isRect):
            self.pantalla.blit(self.imagen,self.posicion)
        

   
#clase para agrupar textos en general
class group_text:
    def __init__(self, lista = []):
        self.lista = lista
        self.comenzado = False
        self.renderizado = False
        self.terminado = False
        self.contador =0
        
    #void: self -> None
    #aplica la funcion void a todos los textos del grupo (textos deben poseerla)
    def void(self):
        for textos in self.lista:
            textos.void()
        self.comenzado = False
        self.renderizado = False
        self.terminado = False
        
    #texto_lista_update: self -> None
    #updatea todos los textos y guarda los datos necesarios
    def update(self):
        self.comenzado = True
        for i in range(len(self.lista)):
            if i==0:
                self.lista[i].update()
            elif self.lista[i-1].terminado:
                self.lista[i].update()
        
        if not(self.renderizado):
            if self.lista[-1].renderizado:
                self.renderizado = True
                
        if not(self.terminado):
            if self.lista[-1].terminado:
                self.contador += 1   
                self.terminado = True
            

#clase para agrupar textos de la clase text_anim_02
class group_text_02(group_text):
    def __init_(self,lista):
        group_text.__init__(self,lista)

    def stop(self):
        for i in self.lista:
            i.stop()
        
    def update(self):
        for i in range(len(self.lista)):
            self.lista[i].update()
                
        if not(self.renderizado):
            if self.lista[-1].terminado:
                self.renderizado = True
                
        if not(self.terminado):
            if self.lista[-1].terminado:
                self.contador += 1   
                self.terminado = True
    
    
    
    
#texto_inferior_update: list(text)
#updatea los textos que se le pasen en una lista en un orden especifico
#espera a que se termine de updatear uno para pasar al otro        
def texto_lista_update(lista):
    for i in range(len(lista)):
        if i==0:
            lista[i].update()
        elif lista[i-1].renderizado:
            lista[i].update()
            
