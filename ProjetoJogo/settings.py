import pygame
#============================== CARREGAMENTO DAS IMAGENS ===========================================
bconfig = pygame.image.load('Image/bconfig.png')
bconfig = pygame.transform.scale(bconfig, (1000, 900))
simb_som = pygame.image.load('Image/som.png')
simb_som = pygame.transform.scale(simb_som, (84, 84))
#==================================================================================================




class Config:
    def __init__(self):
        self.name = ""
        self.nome = "Fulano"
        t=0
        
        self.lista_sprites = []
        for x in range(6):
            self.lista_sprites.append(pygame.image.load(f'Image/FM1/{t}.png'))
            t+=1
        

    def nome_personagem(self, evt, mouseX, mouseY, tela):
        
        if evt.type == pygame.KEYDOWN:
            if evt.unicode.isalpha():
                    self.name += evt.unicode
            elif evt.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
            elif evt.key == pygame.K_RETURN:
                self.nome = self.name[:]
                self.name = ""
        if evt.type == pygame.MOUSEBUTTONDOWN:
            #PM1
            if mouseX > 600 and mouseX < 700 and mouseY > 260 and mouseY < 430:
                t=0
                self.lista_sprites = []
                pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
                for x in range(6):
                    self.lista_sprites.append(pygame.image.load(f'Image/PM1/{t}.png').convert_alpha())
                    t+=1
            #FM1
            elif mouseX > 600 and mouseX < 700 and mouseY > 460 and mouseY < 630:
                t=0
                self.lista_sprites = []
                pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
                for x in range(6):
                    self.lista_sprites.append(pygame.image.load(f'Image/FM1/{t}.png').convert_alpha())
                    t+=1
            #FM2
            elif mouseX > 800 and mouseX < 900 and mouseY > 460 and mouseY < 630:
                t=0
                self.lista_sprites = []
                pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
                for x in range(6):
                    self.lista_sprites.append(pygame.image.load(f'Image/FM2/{t}.png').convert_alpha())
                    t+=1
            #PM20
            elif mouseX > 800 and mouseX < 900 and mouseY > 260 and mouseY < 430:
                t=0
                self.lista_sprites = []
                pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
                for x in range(6):
                    self.lista_sprites.append(pygame.image.load(f'Image/PM2/{t}.png').convert_alpha())
                    t+=1
            
            
    
    def mostrar_nome(self):
        return self.nome
    
    def sprite(self):
        return self.lista_sprites
        

    
    
    def Som(self, textoB, TextoP, personagem, p1, p2, p3, p4):
        self.texto_do_botao = textoB
        self.nome_texto = TextoP
        self.Tpersonagem = personagem
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    
    
    
    
    
    #DESENHA A TELA DE CONFIGURAÇÕES
    def tela_settings(self, tela, cor, botao, mouseX, mouseY, fonte):
        self.fonte = fonte
        tela.fill(cor)
        tela.blit(bconfig, (0,0))
        tela.blit(botao, (760, 820))
        tela.blit(simb_som, (150, 250))
        tela.blit(self.texto_do_botao, (50, 230))
        tela.blit(self.nome_texto, (50, 430))
        tela.blit(self.Tpersonagem, (600, 230))
        
        tela.blit(self.p1, (600, 260))
        tela.blit(self.p2, (800, 260))
        tela.blit(self.p3, (600, 460))
        tela.blit(self.p4, (800, 460))
        
        nick = self.fonte.render(self.name, True, (255,255,255))
        pygame.draw.rect(tela,(0,0,0),((50, 460), (410, 50)), 0, 10)
        tela.blit(nick, (55, 465))
        
        if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880: #botão voltar
            pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
        elif mouseX > 600 and mouseX < 700 and mouseY > 260 and mouseY < 430: #PM1
            pygame.draw.rect(tela,(255,0,0),((595, 256),(110, 178)), 4, 50)
        elif mouseX > 600 and mouseX < 700 and mouseY > 460 and mouseY < 630: #FM1
            pygame.draw.rect(tela,(255,0,0),((595, 456),(110, 178)), 4, 50)
        elif mouseX > 800 and mouseX < 900 and mouseY > 460 and mouseY < 630: #FM2
            pygame.draw.rect(tela,(255,0,0),((795, 465),(110,178)), 4, 50)
        elif mouseX > 800 and mouseX < 900 and mouseY > 260 and mouseY < 430: #PM2
            pygame.draw.rect(tela,(255,0,0),((795, 256),(110,178)), 4, 50)
        
        if pygame.mixer.music.get_busy() == False:
            pygame.draw.line(tela,(255,0,0),(150, 260),(214, 324),8)
        
        
        pygame.display.update()

   
   
   
   
   #RESPONSAVEL POR LIGAR E DESLIGAR A MUSICA
    def config_som(self):

        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play(-1)
            
        elif pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()
            
        
