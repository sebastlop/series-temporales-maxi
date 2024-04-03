import pygame  
import random
import numpy as np

width = 800
height = width
radio = width

# 3 formas de definir los colores

red = pygame.Color ('Red')
cyan = pygame.Color('Cyan')
blue = pygame.Color('blue')
green = (0, 255, 0)
white = (255, 255, 255)
black = (0,0,0)

pygame.init() #inicializa el entorno de pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculo de Pi')

running = True
screen.fill(black) #rellenamos la pantalla de verde
pygame.draw.circle(screen, white, (0,0), radio) 

nPuntos = 0
nDentroCirculo = 0
radio2 = radio*radio

f = open('evo_pi.csv','wt')
f.write('N\tpi_value\n')

pi_true = np.pi
epsilon = 0.001
dif = 1000

while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #      running = False
    if dif < epsilon :
        running = False

    x = random.randint(0,width)
    y = random.randint(0,height)
    nPuntos += 1
    if x*x + y*y <= radio2: #esta dentro del circulo
        screen.set_at((x,y),red)
        nDentroCirculo += 1
    else:
        screen.set_at((x,y),blue) 

    pi = nDentroCirculo * 4 / nPuntos
    dif = abs(pi_true - pi)       
    
    if nPuntos % 1000 == 0:
        sMsg =f'{nPuntos}\t{pi}\n'
        print(sMsg, end='')
        f.write(sMsg) 
        f.flush()

        pygame.display.flip() #actualizamos la pantalla

f.close()
pygame.quit()
    