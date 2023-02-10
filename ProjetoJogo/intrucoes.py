import pygame

#============================ carregamento das imagens =======================================================
part1 = pygame.image.load('Image/binstrucoes.png')
part1 = pygame.transform.scale(part1,(1000, 900))

#=============================================================================================================


class Tela_instrucoes:
    def __init__(self, tela, cor, botao, font):
        self.tela = tela
        self.cor = cor
        self.botao = botao
        self.text_int = font.render('=> MOVA O PERSONAGEM HORIZONTALMENTE E EVITE SER PEGO PELOS ZUMBIS', True, (255,0,0))
        
    #DESENHA A 1ª TELA DE INSTRUÇÕES
    def tela_instrucoes(self, mouseX, mouseY, ):
        self.tela.fill(self.cor)
        self.tela.blit(part1, (0,0))
        self.tela.blit(self.botao, (760, 820))
        self.tela.blit(self.text_int, (60, 190))
        
        
        if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880:
            pygame.draw.rect(self.tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
        
        
        pygame.display.update()
    


