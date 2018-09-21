# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import img
import sprites
import text
import bgm
import s5

#funciones
pygame.init()

#funcion principal
def main():

    #creacion de objetos para el programa
    bg = background.background(settings.pantalla,"02.png",alpha = True, posicion = settings.screen_center)
    barra = img.img(settings.pantalla,"001.png",posicion=settings.screen_center)

    #control de los textos
    l0 = text.text(settings.pantalla,color = (255,255,255),nombre = "COOPBL.ttf",tamano = settings.text_tamano_1,posicion = (40,405),linea = u"Voz que parece familiar")
    l1 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,455), linea = u"Marcelo Salas!")
    l2 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,495), linea = u"Activaste mi carta trampa!")
    l3 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,535), linea = "")
    lista = [l0,l1,l2,l3]
    parrafo = text.group_text(lista)
    
    #marcelo
    marcelo = sprites.personaje(settings.pantalla,posicion = (-300,450))
    marcelo.add("marcelo.png")
    marcelo.add("marcelo01.png")
    x2 = pygame.transform.scale2x(marcelo.imagenes[0])
    marcelo.imagenes[0] = x2
    x3 = pygame.transform.scale2x(marcelo.imagenes[1])
    marcelo.imagenes[1] = x3
    marcelo.current(1)
    marcelo.anim_01((150,450),180)
    
    #marmota
    marmota = sprites.personaje(settings.pantalla,posicion = (1000,450))
    marmota.add("marmota.png")
    marmota.add("marmota01.png")
    
    bgmusic = bgm.bgm("004.mp3")
    running = True

    #acciones de uso unico
    bgmusic.play()

    #bucle principal
    while running:
        #variables que se comprueban cada bucle
        
        
        #lista de los eventos que se ejecutaron
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_z:
                    marmota.end_anim_01()
                    marcelo.end_anim_01()
                    if not(parrafo.renderizado):
                        for linea in lista:
                            linea.velocidad = 5000
                    if parrafo.renderizado:
                        parrafo.contador += 1
                        
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_z:
                    for linea in lista:
                        linea.velocidad = settings.text_speed_1
                        
                    
            if evento.type == pygame.QUIT:
                running = False
        
        #manejo de textos
        if parrafo.renderizado and parrafo.contador == 2:
            parrafo.void()
            marcelo.anim_01((150,450),180)
            marcelo.current(0)
            marmota.current(1)
            #modificamos los textos
            l0.line(u"Marcelo")
            l1.line(u"No veo ni mierdas, podrías prender la luz?")
            
        if parrafo.renderizado and parrafo.contador == 4:
            parrafo.void()
            marcelo.current(1)
            marmota.current(0)
            #modificamos textos
            l0.line(u"Voz que parece familiar")
            bg = background.background(settings.pantalla,"03.jpg",alpha = False, posicion = settings.screen_center)
            l1.line(u"En este lugar no hay luz, solo hay Divinas Comedias! ")
            
        if parrafo.renderizado and parrafo.contador == 6:
            parrafo.void()
            marcelo.current(0)
            marmota.current(1)
            #modificamos textos
            l0.line(u"Marcelo")
            l1.line(u"Quien eres?")
            
        if parrafo.renderizado and parrafo.contador == 8:
            parrafo.void()
            marmota.anim_01((600,450),320)
            marmota.current(0)
            marcelo.current(1)
            #modificamos textos
            l0.line(u"Jesucristo")
            l1.line(u"Creías que Jesucristo era una buena persona?")
            l2.line(u"Jesucristo es de la Policía de Investigaciones!")
            l3.line(u"Cagaste culiao!")
            
        if parrafo.renderizado and parrafo.contador == 10:
            parrafo.void()
            #modificamos textos
            l0.line(u"Jesucristo")
            l1.line(u"Soy de la PDI! Quedaste arrestado por ")
            l2.line(u"contrabando y compra de transgénicos ")
            l3.line(u"ilegales!")
            
        if parrafo.renderizado and parrafo.contador == 12:
            parrafo.void()
            marcelo.current(0)
            marmota.current(1)
            #modificamos textos
            l0.line(u"Marcelo")
            l1.line(u"NOOOOOOOOOOOOOO ")

        if parrafo.renderizado and parrafo.contador == 14:
            parrafo.void()
            marmota.current(0)
            marcelo.current(1)
            #modificamos textos
            l0.line(u"Jesucristo")
            l1.line(u"Ajkajakjak y el weon se la cree ajajkakjakjk ")
            l2.line(u"Solo te tendí una trampa para transformarte ")
            l3.line(u"en Dante Allighieri ")
            
        if parrafo.renderizado and parrafo.contador == 16:
            parrafo.void()
            marcelo.current(0)
            marmota.current(1)
            #modificamos textos
            l0.line(u"Marcelo")
            l1.line(u"Ah, de pana igual")
            
        if parrafo.renderizado and parrafo.contador == 18:
            parrafo.void()
            marcelo.current(1)
            marmota.current(0)
            #modificamos textos
            l0.line(u"Jesucristo")
            l1.line(u"Si, ser Allighieri es entrete")
            

        #paso a la siguiente pantalla
        if parrafo.contador == 20:
            running = False
            s5.main()
            
        
        #actualizacion de objetos en pantalla
        bg.update()
        marcelo.update()
        marmota.update()
        barra.update()
        parrafo.update()
        if not(running): bgmusic.stop()
    
        #actualizamos la pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)

