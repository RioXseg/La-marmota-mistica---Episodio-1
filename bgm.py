import pygame


#nombre -> str
#direccion -> str
class bgm():
    #inciializa el objeto de tipo bgm.
    #solo puede haber un objeto del tipo bgm existiendo
    def __init__(self,nombre = "",direccion="bgm/"):
        self.nombre = nombre
        self.direccion = direccion
        
        if nombre != "": self.load(nombre)

    #carga una nueva cancion en el mismo objeto bgm
    def load(self, nombre):
        pygame.mixer.music.load(self.direccion + nombre)

    #reproduce el bgm actualmente cargado
    def play(self, loop = -1, inicio = 0.0):
        pygame.mixer.music.play(loop,inicio)

    #resetea el bgm cargado y lo reproduce desde el inicio
    def replay(self):
        pygame.mixer.music.rewind()

    #detiene el bgm que se reproduce en el momento, comenzara luego desde cero
    def stop(self):
        pygame.mixer.music.stop()

    #pause el bgm reproduciendose, no lo vuelve al inicio
    def pause(self):
        pygame.mixer.music.pause()

    #quita el pause puesto y continua la reproduccion del bgm
    def unpause(self):
        pygame.mixer.music.unpause()

    #detiene el bgm haciendo un fadeout, se debe especificar la
    #cantidad de milisegundos que dura el fadeout
    def fadeout(self,milisegs):
        assert 0 < milisegs
        pygame.mixer.music.fadeout(milisegs)

    #modifica el valor del volumen del bgm actual
    #debe ser un valor entre 0 y 1
    def set_volume(self,volumen):
        assert 0 <= volumen <= 1
        pygame.mixer.music.set_volume(volumen)

    #devuelve el volumen actual del bgm cargado
    def  get_volume(self):
        return pygame.mixer.music.get_volume()

    #devuelve un bool indicando si el bgm esta siendo reproducido
    def get_busy(self):
        return pygame.mixer.music.get_busy()

    #devuelve la cantidad de tiempo que el bgm a estado activo en milisegundos
    def get_time(self):
        return pygame.mixer.music.get_pos()

    #anade una cancion en la cola de la principal del objeto
    #la cancion se reproducira luego de que la primera termine
    #todos sus loops
    def queue(self,nombre,direccion = "bgm/"):
        pygame.mixer.music.queue(direccion+nombre)

    #funcion que creara un evento cada vez que la cancion se detenga
    #el parametro es el tipo de evento, un parametro vacio quitara el evento
    #que ya estaba puesto
    def set_event(self,tipo = pygame.NOEVENT):
        pygame.mixer.music.set_endevent(tipo)

    #devuelve el tipo de evento puesto en set_event
    def get_event(self):
        return pygame.mixer.music.get_endevent()
        
        

    
    

    
