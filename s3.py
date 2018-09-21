# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import text
import cursor
import bgm
import s4

#funciones
pygame.init()


#funcion principal
def main():
    
    
    #creacion de objetos para la pantalla
    bg = background.background(settings.pantalla,"02.png",posicion = settings.screen_center)
    
    l0 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 50),linea = u"",velocidad = settings.text_speed_2) 
    l1 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 100),linea = u"Marcelo Salas emprendió su viaje hacia el",velocidad = settings.text_speed_2)
    l2 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 150),linea = u"mar Atlántico, donde se encontraban sus",velocidad = settings.text_speed_2)
    l3 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 200),linea = u"transgénicos.",velocidad = settings.text_speed_2)
    l4 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 250),linea = u"                                                          ",velocidad = settings.text_speed_2)
    l5 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 300),linea = u"",velocidad = settings.text_speed_2)
    l6 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 350),linea = u"Su viaje duro 30 años y 2 segundos hasta",velocidad = settings.text_speed_2)
    l7 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 400),linea = u"que llegó al tan anhelado mar Atlántico.",velocidad = settings.text_speed_2)
    l8 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 450),linea = u"                                                            ",velocidad = settings.text_speed_2)
    l9 = text.text_anim_01(pantalla = settings.pantalla,nombre = "COOPBL.ttf",color = (255,255,255),tamano = settings.text_tamano_2,posicion = (settings.WIDTH/10 -20, 500),linea = u"",velocidad = settings.text_speed_2)
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
                
            l2.line(u"Al llegar a este mar, divisó una manzana")
            l3.line(u"gigante que flotaba sobre una ballena que")
            l4.line(u"comía uretras del fósil de un mamut")
            l5.line(u"congelado que data de aproximadamente")
            l6.line(u"30.000 Mickeys.")
            l7.line(u"                                                            ")
            
        if parrafo.contador == 2 and parrafo.renderizado == True:
        
            parrafo.void()
                
            l1.line(u"Marcelo Salas rápidamente fue navegando")
            l2.line(u"hacia el (Por cierto, Marcelo Salas viaja")
            l3.line(u"por el mar con el cuerpo del Padre Pío) ")
            l4.line(u"hasta que finalmente llegó hasta la manzana. ")
            l5.line(u"                                           ")
            l6.line(u"Pero, al llegar a esta manzana fue  ")
            l7.line(u"teletransportado a un lugar oscuro.")
            l8.line(u"                                                  ")
            
            
        #paso a la siguiente pantalla
        if parrafo.contador == 3:
            running = False
            bgmusic.fadeout(1000)
            s4.main()
            
        
        
        #actualizacion de objetos en pantalla
        bg.update()
        parrafo.update()
        
        
        #actualizamos pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)
