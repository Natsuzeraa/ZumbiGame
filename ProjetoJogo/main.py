import pygame
from intrucoes import Tela_instrucoes
from settings import Config
from jogo import Jogo



cor_de_fundo = (255, 203, 219)
pygame.init()
tela = pygame.display.set_mode((1000, 900)) #Tela onde o jogo irá aparecer


# ================ CARREGAMENTOS DA TELA INICIAL =====================

largura_do_botao = 300
altura_do_botao = 70

mapa1 = pygame.image.load('Image/mapa1.png').convert()
mapa1 = pygame.transform.scale(mapa1, (1216, 6400))
mapa2 = pygame.image.load('Image/mapa2.jpg').convert()
mapa2 = pygame.transform.scale(mapa2, (1216, 6400))
mapa3 = pygame.image.load('Image/mapa3.png').convert()
mapa3 = pygame.transform.scale(mapa3,(1216, 6400))

botao_jogar = pygame.image.load('Image/jogar.png').convert_alpha()
botao_jogar = pygame.transform.scale(botao_jogar, (largura_do_botao, altura_do_botao))

botao_opcao = pygame.image.load('Image/config.png').convert_alpha()
botao_opcao = pygame.transform.scale(botao_opcao, (largura_do_botao, altura_do_botao))

botao_int = pygame.image.load('Image/instrucoes.png').convert_alpha()
botao_int = pygame.transform.scale(botao_int, (largura_do_botao, altura_do_botao))

botao_creditos = pygame.image.load('Image/creditos.png').convert_alpha()
botao_creditos = pygame.transform.scale(botao_creditos, (200, 60))

botao_voltar = pygame.image.load('Image/voltar.png').convert_alpha()
botao_voltar = pygame.transform.scale(botao_voltar, (200, 60))

botao_proximo = pygame.image.load('Image/proximo.png').convert_alpha()
botao_proximo = pygame.transform.scale(botao_proximo, (200, 60))

tela_vitoria = pygame.image.load('Image/vitoria.png').convert()
tela_vitoria = pygame.transform.scale(tela_vitoria, (1000, 900))

tela_derrota = pygame.image.load('Image/derrota.png').convert()
tela_derrota = pygame.transform.scale(tela_derrota, (1000, 900))

p1 = pygame.image.load('Image/PM1.png').convert_alpha()
p1 = pygame.transform.scale(p1,(100, 170))
p2 = pygame.image.load('Image/PM2.png').convert_alpha()
p2 = pygame.transform.scale(p2,(100, 170))
p3 = pygame.image.load('Image/FM1.png').convert_alpha()
p3 = pygame.transform.scale(p3,(100, 170))
p4 = pygame.image.load('Image/FM2.png').convert_alpha()
p4 = pygame.transform.scale(p4,(100, 170))


# ==============================================================================
background = pygame.image.load('Image/fundo2.png').convert()
background = pygame.transform.scale(background, (1000, 900))
carla = pygame.image.load('Image/carla.png').convert_alpha()
carla = pygame.transform.scale(carla,(300, 235))
daniel = pygame.image.load('Image/daniel.png').convert_alpha()
daniel = pygame.transform.scale(daniel,(300, 235))
bcreditos = pygame.image.load('Image/bcreditos.png').convert()
bcreditos = pygame.transform.scale(bcreditos, (1000, 900))
som_do_botao = pygame.mixer.Sound('Sounds/pass.wav')
musica = pygame.mixer.music.load('Sounds/musica.flac')
som_vitoria = pygame.mixer.Sound('Sounds/victory.wav')
som_derrota = pygame.mixer.Sound('Sounds/derrota.wav')

t=0
zombie_sprites = []            
for x in range(8):
    zombie_sprites.append(pygame.image.load(f'Image/zombie/{t}.png').convert_alpha())
    t+=1

#================================================================================


font = pygame.font.Font('Font/rubik.ttf', 21) #Cria uma fonte de letra para ser ultilizada em futuros textos
font2 = pygame.font.Font('Font/rubik.ttf', 30)
font3 = pygame.font.Font('Font/rubik.ttf', 16)
text = font.render('SOM: LIGAR / DESLIGAR', True, (255,0,0))
texto_nome = font.render('DIGITE O NOME DO SEU PERSONAGEM: ', True, (255, 0, 0))
texto_personagem = font.render('ESCOLHA SEU PERSONAGEM: ',True,(255,0,0))



pygame.display.set_caption('ZOMBIE APOCALYPSE') #Nome do jogo que irá aparecer na borda
clock = pygame.time.Clock()

def borda():
    vermelho = (255,0,0)
    mouseX, mouseY = pygame.mouse.get_pos() #Retorna a posição que o mouse esta localizado
    
    #botão jogar
    if mouseX > 350 and mouseX < 350+300 and mouseY > 430 and mouseY < 430+70: #Verifica se o mouse está no botão
        pygame.draw.rect(tela,vermelho,((345, 425),(312, 82)), 4, 50) #Desenha um retagulo em volta do botão quando o mosue está em cima
        
    #botão opções
    if mouseX > 350 and mouseX < 350+300 and mouseY > 530 and mouseY < 530+70: 
        pygame.draw.rect(tela,vermelho,((345, 525), (312, 82)), 4, 50)
    #botão instruções
    if mouseX > 350 and mouseX < 350+300 and mouseY > 630 and mouseY < 630+70:
        pygame.draw.rect(tela,vermelho,((345, 625),(312, 82)), 4, 50)
    #botão creditos
    if mouseX > 40 and mouseX < 40+200 and mouseY > 795 and mouseY < 795+60:
        pygame.draw.rect(tela,vermelho,((35, 790), (212, 72)), 4, 50)
    #botão sair
    #if mouseX > 770 and mouseX < 770+200 and mouseY > 820 and mouseY < 820+60:
       # pygame.draw.rect(tela,vermelho,((765, 815),(212, 72)), 4, 50)
       
op = Config() #Inicia a clase de configurações
#TELA PRINCIPAL
def tela_menu():
        
        tela.fill(cor_de_fundo)
        tela.blit(background, (0, 0))
        tela.blit(botao_jogar,(350, 430))
        tela.blit(botao_opcao,(350, 530))
        tela.blit(botao_int,(350, 630))
        tela.blit(botao_creditos, (40, 795))
        #tela.blit(botao_sair, (770, 820))
        #x, y = pygame.mouse.get_pos()
        #text = font.render(f'A posicao de x é {x} e y é: {y}', True, (0, 0, 0))
        #tela.blit(text, (200, 200))
        borda()


        pygame.display.update()


def tela_creditos():
    
    tela.fill(cor_de_fundo)
    tela.blit(bcreditos, (0,0))
    tela.blit(carla, (70, 200))
    tela.blit(daniel, (600, 500))
    tela.blit(text_nome_carla, (380, 250))
    tela.blit(texto_funcao_carla,(380, 280))
    tela.blit(texto_curso, (380, 315))
    tela.blit(texto_uf,(380, 345))
    tela.blit(text_nome_daniel, (295, 570))
    tela.blit(texto_funcao_daniel,(295, 600))
    tela.blit(texto_curso, (295, 635))
    tela.blit(texto_uf,(295, 665))

    tela.blit(botao_voltar, (760, 820))
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880:
        pygame.draw.rect(tela,(255,0,0),((755, 816), (210, 68)), 4, 50)
    #text = font.render(f'A posicao de x é {mouseX} e y é: {mouseY}', True, (0, 0, 0))
    #tela.blit(text,(650,700))
    
    

    pygame.display.update()


def run_game():
    jogando = True
    screen = 1
    ativo = 0
    dicas = 1
    
    op.config_som()
    op.Som(text, texto_nome, texto_personagem, p1, p2, p3, p4)
    dica = Tela_instrucoes(tela,cor_de_fundo, botao_voltar, font3) #Inicia a classe de Instrucoes
    jogo = Jogo(tela, cor_de_fundo, font, som_vitoria, som_derrota) #Inicia a tela do jogo
    
    while jogando:
        mouseX, mouseY = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
            if screen == 1:
                #================================   SOM  DOS BOTÕES  =====================================================
                if (mouseX > 350 and mouseX < 350+300 and mouseY > 430 and mouseY < 430+70) or (mouseX > 350 and mouseX < 350+300 and mouseY > 530 and mouseY < 530+70) or (mouseX > 350 and mouseX < 350+300 and mouseY > 630 and mouseY < 630+70) or (mouseX > 40 and mouseX < 40+200 and mouseY > 795 and mouseY < 795+60):
                    if ativo == 0:
                        pygame.mixer.Sound.play(som_do_botao)
                        ativo = 1
                if not(mouseX > 350 and mouseX < 350+300 and mouseY > 430 and mouseY < 430+70) and not (mouseX > 350 and mouseX < 350+300 and mouseY > 530 and mouseY < 530+70) and not (mouseX > 350 and mouseX < 350+300 and mouseY > 630 and mouseY < 630+70) and not (mouseX > 40 and mouseX < 40+200 and mouseY > 795 and mouseY < 795+60):
                    ativo = 0
                #===========================================================================================
            #TROCA AS TELAS COM O CLICK
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 40 and mouseX < 40+200 and mouseY > 795 and mouseY < 795+60:
                        screen = 2
                    if mouseX > 350 and mouseX < 350+300 and mouseY > 630 and mouseY < 630+70:
                        dicas = 1
                        screen = 3
                    if mouseX > 350 and mouseX < 350+300 and mouseY > 530 and mouseY < 530+70:
                        screen = 4
                    if mouseX > 350 and mouseX < 350+300 and mouseY > 430 and mouseY < 430+70:
                        screen = 5
            
            #CLICKS NA TELA 2
            elif screen == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880:
                        screen = 1
            
            #CLICKS NA TELA 3
            elif screen == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880:
                        screen = 1
            
            #CLICKS NA TELA 4
            elif screen == 4:
                op.nome_personagem(event, mouseX, mouseY, tela)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 760 and mouseX < 960 and mouseY > 820 and mouseY < 880:
                        screen = 1
                    if mouseX > 150 and mouseX < 150+64 and mouseY > 250 and mouseY < 250+64:
                        op.config_som()
            elif screen == 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                        jogo.reset()
                        screen = 6
            elif screen == 6:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseX > 760 and mouseX < 960 and mouseY > 100 and mouseY < 160:
                        jogo.reset()
                        screen = 7
                
            
                        
    #RESPONSAVEIS POR DESENHAR NA TELA
        if screen == 1:
            tela_menu()
        elif screen == 2:
            tela_creditos()
        elif screen == 3:
            dica.tela_instrucoes(mouseX, mouseY)
        elif screen == 4:
            op.tela_settings(tela, cor_de_fundo, botao_voltar, mouseX, mouseY, font2)
        elif screen == 5:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                screen = 1
            nickname = op.mostrar_nome()
            lista_sprites = op.sprite()
            jogo.fase1(mapa1, lista_sprites, nickname, botao_proximo, tela_vitoria, mouseX, mouseY, zombie_sprites, tela_derrota)
            jogo.movimento()
        elif screen == 6:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                screen = 1
            nickname = op.mostrar_nome()
            lista_sprites = op.sprite()
            jogo.fase2(mapa2, lista_sprites, nickname, botao_proximo, tela_vitoria, mouseX, mouseY, zombie_sprites, tela_derrota)
            jogo.movimento()
        elif screen == 7:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                screen = 1
            nickname = op.mostrar_nome()
            lista_sprites = op.sprite()
            jogo.fase2(mapa3, lista_sprites, nickname, botao_proximo, tela_vitoria, mouseX, mouseY, zombie_sprites, tela_derrota)
            jogo.movimento()


    
#TEXTO DOS CREDTIOS 

text_nome_carla = font.render('NOME: Carla Beatriz', True, (255,255,255))
texto_curso = font.render('CURSO: Ciências e Tecnológia',True,(255,255,255))
texto_uf = font.render('INSTITUIÇÃO: ECT/UFRN',True,(255,255,255))
texto_funcao_carla = font.render('FUNÇÃO: Desenvolvedora/Designer',True,(255,255,255))
text_nome_daniel = font.render('NOME: Daniel Moura', True, (255,255,255))
texto_funcao_daniel = font.render('FUNÇÃO: Desenvolvedor',True,(255,255,255))





run_game()


