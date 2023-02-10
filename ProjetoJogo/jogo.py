import pygame
from settings import Config


class Jogo:
    def __init__(self, tela, cor, fonte, som_vitoria, som_derrota):
        self.tela = tela
        self.fonte = fonte
        self.cor = cor
        self.som = som_vitoria
        self.som_d = som_derrota
        self.image_x = 100
        self.image_y = 5500
        self.character_x = 470
        self.character_y = 700
        self.pista_esquerda = 390
        self.pista_direita = 570
        self.value = 0
        self.repet = 0
        self.pontuação = 0
        self.zombie_x = 200
        self.zombie1_x = 100
        self.zombie2_x = 300
        self.zombie_y = 50
        self.zombie1_y = 100
        self.zombie2_y = 150
        self.colisao = False
    
    def reset(self):
        self.image_x = 100
        self.image_y = 5500
        self.pista_esquerda = 390
        self.pista_direita = 570
        self.character_y = 700
        self.character_x = 470

    def fase1(self, mapa1, lista_sprites, nick, proximo, vitoria, mouseX, mouseY, zombie_sprites, derrota):
        self.tela.fill(self.cor)
        if self.image_y > 0 and self.colisao == False:
            
            self.tela.blit(mapa1, (0,0), (self.image_x, self.image_y, 1280, 6400))
            #self.tela.blit(personagem, (self.character_x, self.character_y))
            self.value +=1
            if self.value >= len(lista_sprites):
                self.value = 0
            self.personagem = lista_sprites[self.value]
            self.personagem = pygame.transform.scale(self.personagem, (50, 65))
            self.heroi = self.personagem.get_rect(topleft = (self.character_x, self.character_y))
            self.tela.blit(self.personagem, (self.character_x, self.character_y))
            #print(self.character_y)
            #print(teste)
            nickname = self.fonte.render(nick, True, (255,255,255))
            self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            #print(self.image_y)
            self.zombie = zombie_sprites[self.value]
            self.zombie = pygame.transform.scale(self.zombie, (50, 65))
            self.monstro = self.zombie.get_rect(topleft=(self.zombie_x, self.zombie_y))

            self.zombie1 = zombie_sprites[self.value]
            self.zombie1 = pygame.transform.scale(self.zombie1, (50, 65))
            self.monstro1 = self.zombie.get_rect(topleft=(self.zombie1_x, self.zombie1_y))

            self.zombie2 = zombie_sprites[self.value]
            self.zombie2 = pygame.transform.scale(self.zombie2, (50, 65))
            self.monstro2 = self.zombie.get_rect(topleft=(self.zombie2_x, self.zombie2_y))
            
            if self.image_y > 1:
                self.tela.blit(self.zombie, (self.zombie_x, self.zombie_y))
                self.tela.blit(self.zombie1, (self.zombie1_x, self.zombie1_y))
                self.tela.blit(self.zombie2, (self.zombie2_x, self.zombie2_y))
                self.zombie_x += 0.1
                self.zombie1_x += 0.2
                self.zombie2_x += 0.3
                self.zombie_y += 0.4
                self.zombie1_y += 0.6
                self.zombie2_y += 0.5
                if self.heroi.colliderect(self.monstro) or self.heroi.colliderect(self.monstro1) or self.heroi.colliderect(self.monstro2):
                    print('Colidiu')
                    pygame.mixer.Sound.play(self.som_d)
                    self.pontuação -= 100
                    self.colisao = True
                if self.image_y == 4000 or self.image_y == 3000 or self.image_y == 1200 or self.image_y == 100:
                    self.zombie_x = 200
                    self.zombie1_x = 100
                    self.zombie2_x = 300
                    self.zombie_y = 50
                    self.zombie1_y = 100
                    self.zombie2_y = 150
        
        elif self.repet < 0:
            self.repet += 1
            self.image_y = 5500
            self.zombie_x = 200
            self.zombie_y = 50
            print(self.repet)
        elif self.colisao == False:
            if self.character_y > 0:
                self.character_y -=0.5
                self.tela.blit(mapa1, (0,0), (self.image_x, self.image_y, 1280, 6400))
                #print(self.character_y)
                if self.character_y == 0.5:
                    self.pontuação += 100
                    pygame.mixer.Sound.play(self.som)
            
                self.value +=1
                if self.value >= len(lista_sprites):
                    self.value = 0
                self.personagem = lista_sprites[self.value]
                self.personagem = pygame.transform.scale(self.personagem, (50, 65))
                self.tela.blit(self.personagem, (self.character_x, self.character_y))
        
                nickname = self.fonte.render(nick, True, (255,255,255))
                self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            else:
                self.tela.blit(vitoria, (0,0))
                self.tela.blit(proximo, (760, 100))
                pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
                self.tela.blit(pontuação, (50, 70))
                if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                    pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        elif self.colisao == True:
            self.tela.blit(derrota, (0,0))
            self.tela.blit(proximo, (760, 100))
            pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
            self.tela.blit(pontuação, (50, 70))
            if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        
        pygame.display.update()
    
    def fase2(self, mapa2, lista_sprites, nick, proximo, vitoria, mouseX, mouseY, zombie_sprites, derrota):
        self.tela.fill(self.cor)
        if self.image_y > 0 and self.colisao == False:
            
            self.tela.blit(mapa2, (0,0), (self.image_x, self.image_y, 1280, 6400))
            #self.tela.blit(personagem, (self.character_x, self.character_y))
            self.value +=1
            if self.value >= len(lista_sprites):
                self.value = 0
            self.personagem = lista_sprites[self.value]
            self.personagem = pygame.transform.scale(self.personagem, (50, 65))
            self.heroi = self.personagem.get_rect(topleft = (self.character_x, self.character_y))
            self.tela.blit(self.personagem, (self.character_x, self.character_y))
            #print(self.character_y)
            #print(teste)
            nickname = self.fonte.render(nick, True, (255,255,255))
            self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            #print(self.image_y)
            self.zombie = zombie_sprites[self.value]
            self.zombie = pygame.transform.scale(self.zombie, (50, 65))
            self.monstro = self.zombie.get_rect(topleft=(self.zombie_x, self.zombie_y))

            self.zombie1 = zombie_sprites[self.value]
            self.zombie1 = pygame.transform.scale(self.zombie1, (50, 65))
            self.monstro1 = self.zombie.get_rect(topleft=(self.zombie1_x, self.zombie1_y))

            self.zombie2 = zombie_sprites[self.value]
            self.zombie2 = pygame.transform.scale(self.zombie2, (50, 65))
            self.monstro2 = self.zombie.get_rect(topleft=(self.zombie2_x, self.zombie2_y))
            
            if self.image_y > 1:
                self.tela.blit(self.zombie, (self.zombie_x, self.zombie_y))
                self.tela.blit(self.zombie1, (self.zombie1_x, self.zombie1_y))
                self.tela.blit(self.zombie2, (self.zombie2_x, self.zombie2_y))
                self.zombie_x += 0.1
                self.zombie1_x += 0.2
                self.zombie2_x += 0.3
                self.zombie_y += 0.4
                self.zombie1_y += 0.6
                self.zombie2_y += 0.5
                if self.heroi.colliderect(self.monstro) or self.heroi.colliderect(self.monstro1) or self.heroi.colliderect(self.monstro2):
                    print('Colidiu')
                    pygame.mixer.Sound.play(self.som_d)
                    self.colisao = True
                if self.image_y == 4000 or self.image_y == 3000 or self.image_y == 1200 or self.image_y == 100:
                    self.zombie_x = 200
                    self.zombie1_x = 100
                    self.zombie2_x = 300
                    self.zombie_y = 50
                    self.zombie1_y = 100
                    self.zombie2_y = 150
        
        elif self.repet < 0:
            self.repet += 1
            self.image_y = 5500
            self.zombie_x = 200
            self.zombie_y = 50
            print(self.repet)
        elif self.colisao == False:
            if self.character_y > 0:
                self.character_y -=0.5
                self.tela.blit(mapa2, (0,0), (self.image_x, self.image_y, 1280, 6400))
                #print(self.character_y)
                if self.character_y == 0.5:
                    self.pontuação += 100
                    pygame.mixer.Sound.play(self.som)
            
                self.value +=1
                if self.value >= len(lista_sprites):
                    self.value = 0
                self.personagem = lista_sprites[self.value]
                self.personagem = pygame.transform.scale(self.personagem, (50, 65))
                self.tela.blit(self.personagem, (self.character_x, self.character_y))
        
                nickname = self.fonte.render(nick, True, (255,255,255))
                self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            else:
                self.tela.blit(vitoria, (0,0))
                self.tela.blit(proximo, (760, 100))
                pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
                self.tela.blit(pontuação, (50, 70))
                if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                    pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        elif self.colisao == True:
            self.tela.blit(derrota, (0,0))
            self.tela.blit(proximo, (760, 100))
            pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
            self.tela.blit(pontuação, (50, 70))
            if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        
        pygame.display.update()
    
    def fase3(self, mapa3, lista_sprites, nick, proximo, vitoria, mouseX, mouseY, zombie_sprites, derrota):
        self.tela.fill(self.cor)
        if self.image_y > 0 and self.colisao == False:
            
            self.tela.blit(mapa3, (0,0), (self.image_x, self.image_y, 1280, 6400))
            #self.tela.blit(personagem, (self.character_x, self.character_y))
            self.value +=1
            if self.value >= len(lista_sprites):
                self.value = 0
            self.personagem = lista_sprites[self.value]
            self.personagem = pygame.transform.scale(self.personagem, (50, 65))
            self.heroi = self.personagem.get_rect(topleft = (self.character_x, self.character_y))
            self.tela.blit(self.personagem, (self.character_x, self.character_y))
            #print(self.character_y)
            #print(teste)
            nickname = self.fonte.render(nick, True, (255,255,255))
            self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            #print(self.image_y)
            self.zombie = zombie_sprites[self.value]
            self.zombie = pygame.transform.scale(self.zombie, (50, 65))
            self.monstro = self.zombie.get_rect(topleft=(self.zombie_x, self.zombie_y))

            self.zombie1 = zombie_sprites[self.value]
            self.zombie1 = pygame.transform.scale(self.zombie1, (50, 65))
            self.monstro1 = self.zombie.get_rect(topleft=(self.zombie1_x, self.zombie1_y))

            self.zombie2 = zombie_sprites[self.value]
            self.zombie2 = pygame.transform.scale(self.zombie2, (50, 65))
            self.monstro2 = self.zombie.get_rect(topleft=(self.zombie2_x, self.zombie2_y))
            
            if self.image_y > 1:
                self.tela.blit(self.zombie, (self.zombie_x, self.zombie_y))
                self.tela.blit(self.zombie1, (self.zombie1_x, self.zombie1_y))
                self.tela.blit(self.zombie2, (self.zombie2_x, self.zombie2_y))
                self.zombie_x += 0.1
                self.zombie1_x += 0.2
                self.zombie2_x += 0.3
                self.zombie_y += 0.4
                self.zombie1_y += 0.6
                self.zombie2_y += 0.5
                if self.heroi.colliderect(self.monstro) or self.heroi.colliderect(self.monstro1) or self.heroi.colliderect(self.monstro2):
                    print('Colidiu')
                    pygame.mixer.Sound.play(self.som_d)
                    self.colisao = True
                if self.image_y == 4000 or self.image_y == 3000 or self.image_y == 1200 or self.image_y == 100:
                    self.zombie_x = 200
                    self.zombie1_x = 100
                    self.zombie2_x = 300
                    self.zombie_y = 50
                    self.zombie1_y = 100
                    self.zombie2_y = 150
        
        elif self.repet < 0:
            self.repet += 1
            self.image_y = 5500
            self.zombie_x = 200
            self.zombie_y = 50
            print(self.repet)
        elif self.colisao == False:
            if self.character_y > 0:
                self.character_y -=0.5
                self.tela.blit(mapa3, (0,0), (self.image_x, self.image_y, 1280, 6400))
                #print(self.character_y)
                if self.character_y == 0.5:
                    self.pontuação += 100
                    pygame.mixer.Sound.play(self.som)
            
                self.value +=1
                if self.value >= len(lista_sprites):
                    self.value = 0
                self.personagem = lista_sprites[self.value]
                self.personagem = pygame.transform.scale(self.personagem, (50, 65))
                self.tela.blit(self.personagem, (self.character_x, self.character_y))
        
                nickname = self.fonte.render(nick, True, (255,255,255))
                self.tela.blit(nickname, (self.character_x-10, self.character_y - 25))
            else:
                self.tela.blit(vitoria, (0,0))
                self.tela.blit(proximo, (760, 100))
                pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
                self.tela.blit(pontuação, (50, 70))
                if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                    pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        elif self.colisao == True:
            self.tela.blit(derrota, (0,0))
            self.tela.blit(proximo, (760, 100))
            pontuação = self.fonte.render(f'SUA PONTUAÇÃO: {self.pontuação}', True, (255,255,255))
            self.tela.blit(pontuação, (50, 70))
            if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                pygame.draw.rect(self.tela,(255,0,0),((755, 96), (210, 68)), 4, 50)
        
        pygame.display.update()
        
        
    
    def movimento(self):
        keys = pygame.key.get_pressed()
        if self.image_y > 0:
            self.image_y -= 0.5
        if keys[pygame.K_LEFT] and self.character_x > self.pista_esquerda:
            self.character_x -= 0.5
            self.image_x -= 0.5
        if keys[pygame.K_RIGHT] and self.character_x < self.pista_direita:
            self.character_x += 0.5
            self.image_x += 0.5
    
        



        
        
        

