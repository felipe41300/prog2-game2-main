import pygame
import cv2
import sys
import player

# Inicializa o jogo
pygame.init()

# Configura o display
width = 500
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("criacao")

# Configurações do jogador
p = player.Player()
g = pygame.sprite.Group()
g.add(p)

subway = cv2.VideoCapture("gameplay.mp4")

# Defini a cor branco
white = (255, 255, 255)

# Cria um relógio
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white) # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #capturar frames do subway surfer
    ret, frame = subway.read()
    surface = pygame.surfarray.make_surface(frame)

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed() 

    # Muda a posição baseado na tecla pressionado
    p.move(keys)

    # desenhar o subway 
    screen.blit(surface, (0, 0))
    # Desenha o jogador
    g.draw(screen)

    pygame.display.flip()
    clock.tick(60)

subway.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()
