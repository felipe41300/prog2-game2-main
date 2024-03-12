import pygame
import sys
import player

# Inicializa o jogo
pygame.init()

# Configura o display
width = 500
height = 800
screen = pygame.display.set_mode((width, height))

# Configurações do jogador
p = player.Player()
g = pygame.sprite.Group()
g.add(p)

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

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed() 

    # Muda a posição baseado na tecla pressionado
    p.move(keys)

    # Desenha o jogador
    g.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()