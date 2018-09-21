# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import text
import cursor
import bgm
import s2

#funciones
pygame.init()


#funcion principal
def main():
    
    
    #creacion de objetos para la pantalla
    bg = background.background(settings.pantalla,"02.png",posicion = settings.screen_center)
    
    l0 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 100),linea = u"Hace 30 años, un cazador furtivo llamado",velocidad = settings.text_speed_2) 
    l05 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 150),linea = u"Marcelo Salas, fue al mar índico a",velocidad = settings.text_speed_2)
    l1 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 200),linea = u"permutar transgénicos.  ",velocidad = settings.text_speed_2) 
    l2 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 0),linea = "                                                             ",velocidad = settings.text_speed_2) 
    l3 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 300),linea = u"Estuvo allí durante eones (Si, leiste bien:",velocidad = settings.text_speed_2) 
    l35 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 350),linea = u"EONES) y no pudo permutar ningún",velocidad = settings.text_speed_2) 
    l4 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 400),linea = u"transgénico. ",velocidad = settings.text_speed_2) 
    l5 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20,0),linea = "                                                             ",velocidad = settings.text_speed_2) 
    lis = [l0,l05,l1,l2,l3,l35,l4,l5]
    
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
        
        #actualizacion de objetos en pantalla
        bg.update()
        text.texto_lista_update(lis)
        
        #paso a la siguiente pantalla
        if l5.renderizado == True:
            running = False
            bgmusic.fadeout(1000)
            s2.main()
        
        #actualizamos pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)


