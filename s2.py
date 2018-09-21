# -*- coding: utf-8 -*-

#modulos
import pygame
import settings

#clases
import background
import button
import img
import text
import sprites
import cursor
import bgm
import s3

#funciones
pygame.init()

#funcion principal
def main():

    #creacion de objetos para el programa
    bg = background.background(settings.pantalla,"01.png",alpha = True, posicion = settings.screen_center)
    barra = img.img(settings.pantalla,"001.png",posicion=settings.screen_center)

    #control de los textos
    l0 = text.text(settings.pantalla,color = (255,255,255),nombre = "COOPBL.ttf",tamano = settings.text_tamano_1,posicion = (40,405),linea = u"Marcelo")
    l1 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,455), linea = u"Puta, y ahora como chucha voy a permutar ")
    l2 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,495), linea = u"transgénicos...")
    l3 = text.text_anim_01(settings.pantalla,nombre = "ARLRDBD.ttf",tamano = settings.text_tamano_1,velocidad = settings.text_speed_1,color = (255,255,255), posicion = (25,535), linea = "")
    lista = [l1,l2,l3]
    
    #marcelo
    marcelo = sprites.personaje(settings.pantalla,posicion = (-300,450))
    marcelo.add("marcelo.png")
    marcelo.add("marcelo01.png")
    x2 = pygame.transform.scale2x(marcelo.imagenes[0])
    marcelo.imagenes[0] = x2
    x3 = pygame.transform.scale2x(marcelo.imagenes[1])
    marcelo.imagenes[1] = x3
    marcelo.current(0)
    marcelo.anim_01((150,450),180)
    
    #marmota
    marmota = sprites.personaje(settings.pantalla,posicion = (1000,450))
    marmota.add("marmota.png")
    marmota.add("marmota01.png")
    
    #utiles
    indicador = 0
    
    mouse = cursor.cursor()
    bgmusic = bgm.bgm("003.mp3")
    running = True

    #acciones de uso unico
    bgmusic.play(inicio = 2.0)

    #bucle principal
    while running:
        #variables que se comprueban cada bucle
        
        
        #lista de los eventos que se ejecutaron
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_z:
                    marcelo.end_anim_01()
                    marmota.end_anim_01()
                    if not(l3.renderizado):
                        for linea in lista:
                            linea.velocidad = 5000      
                    else:
                        indicador += 1
                        
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_z:
                    for linea in lista:
                        if indicador ==16:
                            break
                        linea.velocidad = settings.text_speed_1
                          
            if evento.type == pygame.QUIT:
                running = False
        
        #manejo de textos
        if indicador == 1:
            indicador += 1
            marcelo.current(1)
            marmota.current(0)
            #modificamos textos
            l0.line(u"Voz Sexona")
            lista[0].void_line(u"Solo tienes que viajar hacia el mar Atlántico")
            lista[1].void_line("")
            lista[2].void_line("")
            
        if indicador == 3:
            indicador += 1
            marcelo.current(0)
            marmota.current(1)
            #modificamos textos
            l0.line(u"Marcelo")
            lista[0].void_line(u"Ohh! Pero que sorpresa!")
            lista[1].void_line("")
            lista[2].void_line("")
        
        if indicador == 5:
            indicador +=1
            marmota.anim_01((600,450),180)
            
            #modificamos los textos
            l0.line(u"Marcelo")
            lista[0].void_line(u"Es una marmota sexona índica magnética leedora ")
            lista[1].void_line(u"de mentes transversales impulsadas hacia el ")
            lista[2].void_line(u"infinito y lo desconocido!")
            
        if indicador == 7:
            indicador +=1
            marcelo.current(1)
            marmota.current(0)
            #modificamos los textos
            l0.line(u"Marmota Sexona")
            lista[0].void_line(u"No tienes porque sorpenderte hijo mio")
            lista[1].void()
            lista[2].void()
            
        if indicador == 9:
            indicador +=1
            marcelo.current(0)
            marmota.current(1)
            #modificamos los textos
            l0.line(u"Marcelo")
            lista[0].void_line(u"Dame una buena razón para no sorpenderme")
            lista[1].void()
            lista[2].void()
            
        if indicador == 11:
            indicador += 1
            marcelo.current(1)
            marmota.current(0)
            #modificamos los textos
            l0.line(u"Jesucristo")
            lista[0].void_line(u"Lo que pasa es que soy Jesucristo, pero se me")
            lista[1].void_line(u"perdió mi gorro y tengo que ir a buscarlo")
            lista[2].void_line(u"")
            
        if indicador == 13:
            indicador += 1
            marmota.anim_01((1000,-200),60)
            
            #modificamos los textos
            l0.line(u"Jesucristo")
            lista[0].void_line(u"así que chaoo chaoo nos vemos, no olviden")
            lista[1].void_line(u"rendirme culto y subscribirse a la iglesia católica,")
            lista[2].void_line(u"soy Jesucristo y te deseo buenas noches.")
            
        if indicador == 15:
            indicador += 1
            marcelo.current(0)
            marmota.current(1)
            #modificamos textos
            l0.line(u"Marcelo")
            lista[0].velocidad = 2
            lista[0].void_line(u". . .")
            if lista[0].renderizado: lista[0].velocidad = settings.text_speed_1
            lista[1].void()
            lista[2].void()
            
        #termino de la pantalla
        if indicador == 17:
            running = False
            s3.main()
            
        
        #actualizacion de objetos en pantalla
        bg.update()
        mouse.update()
        marcelo.update()
        marmota.update()
        barra.update()
        l0.update()
        text.texto_lista_update(lista)
        if not(running): bgmusic.stop()
    
        #actualizamos la pantalla
        if running: pygame.display.flip()
        settings.reloj.tick(60)
