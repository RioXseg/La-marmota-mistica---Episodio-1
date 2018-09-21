# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import text
import cursor
import bgm
import s0

#funciones
pygame.init()


#funcion principal
def main():
    
    
    #creacion de objetos para la pantalla
    bg = background.background(settings.pantalla,"03.jpg",posicion = settings.screen_center)
    
    l0 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],600),linea = u"Gracias por jugar",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True) 
    l1 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_title,posicion = (settings.screen_center[0],1300),linea = u"Programación",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l2 = text.text_anim_02(pantalla = settings.pantalla,nombre = "ARLRDBD.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],1350),linea = u"Sergio Álvarez",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l3 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_title,posicion = (settings.screen_center[0],1450),linea = u"Historia",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l4 = text.text_anim_02(pantalla = settings.pantalla,nombre = "ARLRDBD.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],1500),linea = u"Felix Cerda",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l5 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_title,posicion = (settings.screen_center[0],1600),linea = u"Arte y fondos",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l6 = text.text_anim_02(pantalla = settings.pantalla,nombre = "ARLRDBD.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],1650),linea = u"Alguien en internet",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l7 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_title,posicion = (settings.screen_center[0],1750),linea = u"Especialmente gracias",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l8 = text.text_anim_02(pantalla = settings.pantalla,nombre = "ARLRDBD.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],1800),linea = u"Marcelo Salas",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    l9 = text.text_anim_02(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_credits_normal,posicion = (settings.screen_center[0],2400),linea = u"Nos vemos en el capitulo 2",direccion = (0,-1),velocidad = settings.text_speed_credits,rectangulo = True)
    parrafo = text.group_text_02([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9])
    
    l10 = text.text(settings.pantalla,color = (255,255,255),tamano = 15, linea = u"Pulsa cualquier tecla para adelantar",posicion = (685,580),rectangulo = True)
    
    mouse = cursor.cursor()
    bgmusic = bgm.bgm()
    
    marcador = 0
    
    running = True
    
    while running:
        #variables que se comprueban cada bucle
        tiempo = pygame.time.get_ticks()/1000
        
        #control de eventos
        for evento in pygame.event.get():   
            if evento.type == pygame.KEYDOWN:
                for linea in parrafo.lista:
                    linea.velocidad = 200
        
            if evento.type == pygame.QUIT:
                running = False
                bgmusic.fadeout(1000)
                
        #manejo de textos
        if l9.rect_center[1] <= settings.screen_center[1] :
            parrafo.stop()
            if marcador ==0: marcador = tiempo
            
        #actualizacion de objetos en pantalla
        bg.update()
        parrafo.update()
        l10.update()
        
        #paso a la siguiente pantalla
        if tiempo == marcador + 3 and marcador != 0:
            running = False
            bgmusic.fadeout(1000)
            s0.main()
        
        #actualizamos pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)

