# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import text
import cursor
import bgm
import s6

#funciones
pygame.init()


#funcion principal
def main():
    
    
    #creacion de objetos para la pantalla
    bg = background.background(settings.pantalla,"02.png",posicion = settings.screen_center)
    
    l0 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 50),linea = u"",velocidad = settings.text_speed_2) 
    l1 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 100),linea = u"",velocidad = settings.text_speed_2)
    l2 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 150),linea = u"",velocidad = settings.text_speed_2)
    l3 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 200),linea = u"",velocidad = settings.text_speed_2)
    l4 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 250),linea = u"",velocidad = settings.text_speed_2)
    l5 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 300),linea = u"",velocidad = settings.text_speed_2)
    l6 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 350),linea = u"",velocidad = settings.text_speed_2)
    l7 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 400),linea = u"",velocidad = settings.text_speed_2)
    l8 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 450),linea = u"",velocidad = settings.text_speed_2)
    l9 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = 30,posicion = (settings.WIDTH/10 -20, 500),linea = u"",velocidad = settings.text_speed_2)
    lis = [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]
    parrafo = text.group_text(lis)
    
    mouse = cursor.cursor()
    bgmusic = bgm.bgm()
    running = True
    
    while running:
        #variables que se comprueban cada bucle
        
        
        #control de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                bgmusic.fadeout(1000)
            
        #manejo de textos  
        if parrafo.contador == 1 and parrafo.renderizado == True:
        
            parrafo.void()
            
            #modificamos textos
            l2.line(u"Jesucristo le hizo un hechizo y Marcelo ")
            l3.line(u"Salas se transformó en Dante Allighieri,")
            l4.line(u"                          ")
            l5.line(u"pero aún no sabe que aventuras le ")
            l6.line(u"esperarán con su nuevo cuerpo y sus ")
            l7.line(u"nuevas Divinas Comedias.")
            l8.line(u"                                  ")
            
        if parrafo.contador == 2 and parrafo.renderizado:
        
            parrafo.void()
            
            #modificamos textos
            l5.isRect = True
            l5.position(settings.screen_center)
            l5.velocidad = 2
            l5.line(u" Continuará...")
            
 
 
         #paso a la siguiente pantalla
        if parrafo.contador == 3:
            running = False
            s6.main()
        
        #actualizacion de objetos en pantalla
        bg.update()
        parrafo.update()
        
        
        #actualizamos pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)
