import pygame
import main

def tela_creditos():
    
    main.tela.fill(main.cor_de_fundo)

    main.tela.blit(main.carla, (50, 200))
    main.tela.blit(main.daniel, (600, 200))
    main.tela.blit(main.text1, (130, 420))
    main.tela.blit(main.text2, (680, 420))
    main.tela.blit(main.text3, (820, 820))
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX > 820 and mouseX < 960 and mouseY > 820 and mouseY < 850:
        pygame.draw.rect(main.tela,(255,0,0),((810, 815), (155, 40)), 4, 50)
    text = main.font.render(f'A posicao de x é {mouseX} e y é: {mouseY}', True, (0, 0, 0))
    main.tela.blit(text,(650,700))
    
    

    pygame.display.update()