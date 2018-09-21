# Modulos
import pygame
import settings
import os
import thread

#clases
import background
import button
import cursor
import img
import bgm
import text
import s1

#funciones
pygame.init()

#funcion principal
def main():

    #creacion de objetos para el programa
    bg = background.background(settings.pantalla,'00.jpg',posicion = (settings.WIDTH/2,settings.HEIGHT/2))
    negro = background.background(settings.pantalla,"black.png",posicion = (settings.WIDTH/2,settings.HEIGHT/2),alpha = True)
    
    #configuramos boton principal
    boton = button.button(settings.pantalla,posicion=(170,470))
    boton.add('00.png')
    boton.add('01.png')
    boton.add('02.png')
    
    boton2 = button.button(settings.pantalla,posicion=(600,470))
    boton2.add("03.png")
    boton2.add("04.png")
    boton2.add("05.png")
    l2 = text.text(settings.pantalla,linea = u"Controles",posicion = (600,470),color = (0,0,0),tamano = 30,rectangulo = True)
    l3 = text.text(settings.pantalla,linea = u"Salir",posicion = (600,470),color = (0,0,0),tamano = 30,rectangulo = True)
    indicador = False
    
    l0 = text.text(settings.pantalla,linea = u"Controles",posicion = (70,50),nombre = "COOPBL.TTF",color = (255,255,255))
    l1 = text.text(settings.pantalla,linea = "Pulza Z para avanzar los textos",posicion = (70,100),color = (255,255,255))
    
    mouse = cursor.cursor()
    bgmusic = bgm.bgm("001.mp3")
    running = True
    directorio = os.getcwd()

    #acciones de uso unico
    bgmusic.play()

    #bucle principal
    while running:
        #variables que se comprueban cada bucle
            

        #lista que contiene todos los eventos que se ejecutaron
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if boton.rect.left < mouse.posicion[0] < boton.rect.right and boton.rect.top < mouse.posicion[1] < boton.rect.bottom and not(indicador):
                        s1.main()
                        running = False
                    if boton2.rect.left < mouse.posicion[0] < boton2.rect.right and boton2.rect.top < mouse.posicion[1] < boton2.rect.bottom:
                        aux = not(indicador)
                        indicador = aux
                        
            if evento.type == pygame.QUIT:
                running = False


        #opciones de posicion del mouse
        if mouse.posicion[0] > boton.rect.right or \
           mouse.posicion[0] < boton.rect.left or \
           mouse.posicion[1] > boton.rect.bottom or \
           mouse.posicion[1] < boton.rect.top:
            boton.current(0)
        else:
            if mouse.estado[0] and not(indicador):
                boton.current(2)
            if not(mouse.estado[0]) and not(indicador):
                boton.current(1)

        if mouse.posicion[0] > boton2.rect.right or \
           mouse.posicion[0] < boton2.rect.left or \
           mouse.posicion[1] > boton2.rect.bottom or \
           mouse.posicion[1] < boton2.rect.top:
            boton2.current(0)
        else:
            if mouse.estado[0]:
                boton2.current(2)
            if not(mouse.estado[0]):
                boton2.current(1)
                
        #Actualizamos posicion de las cosas
        bg.update()
        boton.update()
        boton2.update()
        l2.update()
        mouse.update()
        if indicador:
            negro.update()
            boton2.update()
            l0.update()
            l1.update()
            l3.update()
        if not(running): bgmusic.stop()
        
        #actualizamos la pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)                     #60 frames por segundo
    