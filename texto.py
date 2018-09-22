import pygame

fuente = pygame.font.SysFont("Arial",24)

text_sup_01 = fuente.render("",True,(0,0,0))
text_sup_02 = fuente.render("",True,(0,0,0))
text_sup_03 = fuente.render("",True,(0,0,0))
text_sup_04 = fuente.render("",True,(0,0,0))

def mensaje():      
    texto_running = True
    reloj = pygame.time.Clock()
    state = 0
  
    line_01 = "Pulsa comenzar para iniciar el juego"
    line_02 = "controles: flechas -> movimiento"
    line_03 = "                  z -> disparar"
    line_04 = "                  shift -> bombas"

    #indicamos que queremos modificar los globales
    global text_sup_01
    global text_sup_02
    global text_sup_03
    global text_sup_04
    
    vel_char = 30
	

    while texto_running:
        
        if state == 0:
            for i in range(len(line_01)):
                text_sup_01 = fuente.render(line_01[0:i+1],True,(0,0,0))
                reloj.tick(vel_char)
            state = 1
             
        if state == 1:
            for i in range(len(line_02)):
                text_sup_02 = fuente.render(line_02[0:i+1],True,(0,0,0))
                reloj.tick(vel_char)
            state = 2
        if state == 2:
            for i in range(len(line_03)):
                text_sup_03 = fuente.render(line_03[0:i+1],True,(0,0,0))
                reloj.tick(vel_char)
            state = 3
        if state == 3:
            for i in range(len(line_04)):
                text_sup_04 = fuente.render(line_04[0:i+1],True,(0,0,0))
                reloj.tick(vel_char)
            state = 4
        if state == 4:
            break
    
    return 0
