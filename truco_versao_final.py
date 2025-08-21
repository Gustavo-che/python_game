import random
import pygame
from time import sleep
from pygame import mixer

#print("Regras")
#print("Voce eh o jogador A")
#print("Jogo de truco, aperte 1 e enter para jogar a primeira carta, aperte 2 e enter para jogar a segunda carta, aperte 3 e enter para jogar a terceira carta na sua vez")
#colocar deck receber no update

def partida():
    fim = 0
    pontos1 = 0
    pontos2 = 0
    
    
    while fim  == 0:
        a = 0
        b = 0
        saiu = 1
        valor = 1
        quempediu = 0
        d = 1
        c = 1
        #print (pontos1, pontos2,"Total")
    

        baralho = [*range(0, 39, 1)]
        baralho2 =["4our","4esp","4cop","4paus","5our", "5esp","5cop","5paus","6our", "6esp","6cop","6paus","7our", "7esp","7cop","7paus","Qour", "Qesp","Qcop","Qpaus","Jour", "Jesp","Jcop","Jpaus","Kour", "Kesp","Kcop","Kpaus","Aour", "Aesp","Acop","Apaus","2our","2esp","2cop","2paus","3our","3esp","3cop","3paus",]
        numeroale = random.randrange(0, 39)
        m = baralho[numeroale]
        
        
        mnd = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9]
        if m == 38 or m == 39 or m == 37 or m == 36:
            baralho2.append(baralho2[0])
            baralho2.append(baralho2[1])
            baralho2.append(baralho2[2])
            baralho2.append(baralho2[3])
            
            baralho[0] = 40
            baralho[1] = 41
            baralho[2] = 42
            baralho[3] = 43
            
        else:
            if m == 35 or m == 34 or m == 33 or m == 32:
                x = 1
            else:
                f = m//4 + 1
                g = 0
                t = 0
                n = 0
                while f != mnd[t]:
                    t = t + 1
                
                while baralho[n] != t:
                    n = n + 1
                baralho2.append(baralho2[t])
                baralho2.append(baralho2[t+1])
                baralho2.append(baralho2[t+2])
                baralho2.append(baralho2[t+3])
                
                
                baralho[n] = 40
                baralho[n+1] = 41
                baralho[n+2] = 42
                baralho[n+3] = 43
                

            
        random.shuffle(baralho)
        
        
        mn1 = [baralho[0], baralho[1], baralho[2]]
        mao1 = [baralho2[baralho[0]],baralho2[baralho[1]],baralho2[baralho[2]]]
        

        mao2 = [baralho2[baralho[3]],baralho2[baralho[4]],baralho2[baralho[5]]]
        print (mao2)
        mn2 = [baralho[3], baralho[4], baralho[5]]
        mao3 = [baralho2[baralho[6]],baralho2[baralho[7]],baralho2[baralho[8]]]
        #print(mao3)
        mn3 = [baralho[6], baralho[7], baralho[8]]
        mao4 = [baralho2[baralho[9]],baralho2[baralho[10]],baralho2[baralho[11]]]
        mn4 = [baralho[9], baralho[10], baralho[11]]
        #print(mao4)
        

        
        if mn1[0] == m:
            mn1[0] = baralho[12]
            mao1[0] = baralho2[mn1[0]]
        if mn1[1] == m:
            mn1[1] = baralho[12]
            mao1[1] = baralho2[mn1[1]]
        if mn1[2] == m:
            mn1[2] = baralho[12]
            mao1[2] = baralho2[mn1[2]]
        if mn2[0] == m:
            mn2[0] = baralho[12]
            mao2[0] = baralho2[mn2[0]]
        if mn2[1] == m:
            mn2[1] = baralho[12]
            mao2[1] = baralho2[mn2[1]]
        if mn2[2] == m:
            mn2[2] = baralho[12]
            mao2[2] = baralho2[mn2[2]]
        if mn3[0] == m:
            mn3[0] = baralho[12]
            mao3[0] = baralho2[mn3[0]]
        if mn3[1] == m:
            mn3[1] = baralho[12]
            mao3[1] = baralho2[mn3[1]]    
        if mn3[2] == m:
            mn3[2] = baralho[12]
            mao3[2] = baralho2[mn3[2]]
        if mn4[0] == m:
            mn4[0] = baralho[12]
            mao4[0] = baralho2[mn4[0]]
        if mn4[1] == m:
            mn4[1] = baralho[12]
            mao4[1] = baralho2[mn4[1]]
        if mn4[2] == m:
            mn4[2] = baralho[12]
            mao4[2] = baralho2[mn4[2]]
        cartaa = []
        cartab = []
        cartac = []
        cartad = []
        if mn1[0] >= 40:
            cartaa.append(mn1[0]/4)
        else:
            cartaa.append(mn1[0]//4)
        if mn1[1] >= 40:
            cartaa.append(mn1[1]/4)
        else:
            cartaa.append(mn1[1]//4)
        if mn1[2] >= 40:
            
            cartaa.append(mn1[2]/4)
        else:
            cartaa.append(mn1[2]//4)
        if mn2[0] >= 40:
            cartab.append(mn2[0]/4)
        else:
            cartab.append(mn2[0]//4)
        if mn2[1] >= 40:
            cartab.append(mn2[1]/4)
        else:
            cartab.append(mn2[1]//4)
        if mn2[2] >= 40:
            cartab.append(mn2[2]/4)
        else:
            cartab.append(mn2[2]//4)
        if mn3[0] >= 40:
            cartac.append(mn3[0]/4)
        else:
            cartac.append(mn3[0]//4)
        if mn3[1] >= 40:
            cartac.append(mn3[1]/4)
        else:
            cartac.append(mn3[1]//4)
        if mn3[2] >= 40:
            cartac.append(mn3[2]/4)
        else:
            cartac.append(mn3[2]//4)
        if mn4[0] >= 40:
            cartad.append(mn4[0]/4)
        else:
            cartad.append(mn4[0]//4)
        if mn4[1] >= 40:
            cartad.append(mn4[1]/4)
        else:
            cartad.append(mn4[1]//4)
        if mn4[2] >= 40:
            cartad.append(mn4[2]/4)
        else:
            cartad.append(mn4[2]//4)
        
        #sleep(2)
        
        #sleep(2)
        a = 0
        b = 0
        c = 0
        maom = [baralho2[m]]
        
        ca = 0
        cb = 0
        cc = 0
        cd = 0
        e = "a"
        jogadaa = []
        jogadab = []
        jogadac = []
        jogadad = []
        pygame.init()
        mixer.music.load("LAB.wav")
        mixer.music.play(-1)
        screen = pygame.display.set_mode((800, 600))
        jj = 0
        zz = 270
        cartas2 = {0:pygame.image.load("4_of_diamonds.png"),1:pygame.image.load("4_of_spades.png"),2:pygame.image.load("4_of_hearts.png"),3:pygame.image.load("4_of_clubs.png"),4:pygame.image.load("5_of_diamonds.png"),5:pygame.image.load("5_of_spades.png"),6:pygame.image.load("5_of_hearts.png"),7:pygame.image.load("5_of_clubs.png"),8:pygame.image.load("6_of_diamonds.png"),9:pygame.image.load("6_of_spades.png"),10:pygame.image.load("6_of_hearts.png"),11:pygame.image.load("6_of_clubs.png"),12:pygame.image.load("7_of_diamonds.png"),13:pygame.image.load("7_of_spades.png"),14:pygame.image.load("7_of_hearts.png"),15:pygame.image.load("7_of_clubs.png"),16:pygame.image.load("queen_of_diamonds.png"),17:pygame.image.load("queen_of_spades.png"),18:pygame.image.load("queen_of_hearts.png"),19:pygame.image.load("queen_of_clubs.png"),20:pygame.image.load("jack_of_diamonds.png"),21:pygame.image.load("jack_of_spades.png"),22:pygame.image.load("jack_of_hearts.png"),23:pygame.image.load("jack_of_clubs.png"),24:pygame.image.load("king_of_diamonds.png"),25:pygame.image.load("king_of_spades.png"),26:pygame.image.load("king_of_hearts.png"),27:pygame.image.load("king_of_clubs.png"),28:pygame.image.load("ace_of_diamonds.png"),29:pygame.image.load("ace_of_spades.png"),30:pygame.image.load("ace_of_hearts.png"),31:pygame.image.load("ace_of_clubs.png"),32:pygame.image.load("2_of_diamonds.png"),33:pygame.image.load("2_of_spades.png"),34:pygame.image.load("2_of_hearts.png"),35:pygame.image.load("2_of_clubs.png"),36:pygame.image.load("3_of_diamonds.png"),37:pygame.image.load("3_of_spades.png"),38:pygame.image.load("3_of_hearts.png"),39:pygame.image.load("3_of_clubs.png")}
        if m == 39 or m == 38 or m == 37 or m == 36 :
            cartas = {0:pygame.image.load("4_of_diamonds.png"),1:pygame.image.load("4_of_spades.png"),2:pygame.image.load("4_of_hearts.png"),3:pygame.image.load("4_of_clubs.png"),4:pygame.image.load("5_of_diamonds.png"),5:pygame.image.load("5_of_spades.png"),6:pygame.image.load("5_of_hearts.png"),7:pygame.image.load("5_of_clubs.png"),8:pygame.image.load("6_of_diamonds.png"),9:pygame.image.load("6_of_spades.png"),10:pygame.image.load("6_of_hearts.png"),11:pygame.image.load("6_of_clubs.png"),12:pygame.image.load("7_of_diamonds.png"),13:pygame.image.load("7_of_spades.png"),14:pygame.image.load("7_of_hearts.png"),15:pygame.image.load("7_of_clubs.png"),16:pygame.image.load("queen_of_diamonds.png"),17:pygame.image.load("queen_of_spades.png"),18:pygame.image.load("queen_of_hearts.png"),19:pygame.image.load("queen_of_clubs.png"),20:pygame.image.load("jack_of_diamonds.png"),21:pygame.image.load("jack_of_spades.png"),22:pygame.image.load("jack_of_hearts.png"),23:pygame.image.load("jack_of_clubs.png"),24:pygame.image.load("king_of_diamonds.png"),25:pygame.image.load("king_of_spades.png"),26:pygame.image.load("king_of_hearts.png"),27:pygame.image.load("king_of_clubs.png"),28:pygame.image.load("ace_of_diamonds.png"),29:pygame.image.load("ace_of_spades.png"),30:pygame.image.load("ace_of_hearts.png"),31:pygame.image.load("ace_of_clubs.png"),32:pygame.image.load("2_of_diamonds.png"),33:pygame.image.load("2_of_spades.png"),34:pygame.image.load("2_of_hearts.png"),35:pygame.image.load("2_of_clubs.png"),36:pygame.image.load("3_of_diamonds.png"),37:pygame.image.load("3_of_spades.png"),38:pygame.image.load("3_of_hearts.png"),39:pygame.image.load("3_of_clubs.png"),40:cartas2[0],41:cartas2[1],42:cartas2[2],43:cartas2[3]}
        else:
            cartas = {0:pygame.image.load("4_of_diamonds.png"),1:pygame.image.load("4_of_spades.png"),2:pygame.image.load("4_of_hearts.png"),3:pygame.image.load("4_of_clubs.png"),4:pygame.image.load("5_of_diamonds.png"),5:pygame.image.load("5_of_spades.png"),6:pygame.image.load("5_of_hearts.png"),7:pygame.image.load("5_of_clubs.png"),8:pygame.image.load("6_of_diamonds.png"),9:pygame.image.load("6_of_spades.png"),10:pygame.image.load("6_of_hearts.png"),11:pygame.image.load("6_of_clubs.png"),12:pygame.image.load("7_of_diamonds.png"),13:pygame.image.load("7_of_spades.png"),14:pygame.image.load("7_of_hearts.png"),15:pygame.image.load("7_of_clubs.png"),16:pygame.image.load("queen_of_diamonds.png"),17:pygame.image.load("queen_of_spades.png"),18:pygame.image.load("queen_of_hearts.png"),19:pygame.image.load("queen_of_clubs.png"),20:pygame.image.load("jack_of_diamonds.png"),21:pygame.image.load("jack_of_spades.png"),22:pygame.image.load("jack_of_hearts.png"),23:pygame.image.load("jack_of_clubs.png"),24:pygame.image.load("king_of_diamonds.png"),25:pygame.image.load("king_of_spades.png"),26:pygame.image.load("king_of_hearts.png"),27:pygame.image.load("king_of_clubs.png"),28:pygame.image.load("ace_of_diamonds.png"),29:pygame.image.load("ace_of_spades.png"),30:pygame.image.load("ace_of_hearts.png"),31:pygame.image.load("ace_of_clubs.png"),32:pygame.image.load("2_of_diamonds.png"),33:pygame.image.load("2_of_spades.png"),34:pygame.image.load("2_of_hearts.png"),35:pygame.image.load("2_of_clubs.png"),36:pygame.image.load("3_of_diamonds.png"),37:pygame.image.load("3_of_spades.png"),38:pygame.image.load("3_of_hearts.png"),39:pygame.image.load("3_of_clubs.png"),40:cartas2[m-(m%4) + 4],41:cartas2[m-(m%4) + 5],42:cartas2[m-(m%4) + 6],43:cartas2[m-(m%4) + 7]}
            
        cartaa1Img = cartas[mn1[0]]
        
        DEFAULT_IMAGE_SIZE = (60,87)

        cartaa1Img = pygame.transform.scale(cartaa1Img,DEFAULT_IMAGE_SIZE)
        
        cartaa1X = 290
        cartaa1Y = 480
        cartaa2Img = cartas[mn1[1]]
        DEFAULT_IMAGE_SIZE = (60,87)

        cartaa2Img = pygame.transform.scale(cartaa2Img,DEFAULT_IMAGE_SIZE)
        
        cartaa2X = 360
        cartaa2Y = 480

        cartaa3Img = cartas[mn1[2]]
        DEFAULT_IMAGE_SIZE = (60,87)

        cartaa3Img = pygame.transform.scale(cartaa3Img,DEFAULT_IMAGE_SIZE)
        
        cartaa3X = 430
        cartaa3Y = 480
        manilhaImg = cartas[numeroale]
        DEFAULT_IMAGE_SIZE = (60,87)

        manilhaImg = pygame.transform.scale(manilhaImg,DEFAULT_IMAGE_SIZE)
        
        manilhaX = 570
        manilhaY = 250
        cartab1Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartab1Img = pygame.transform.scale(cartab1Img,DEFAULT_IMAGE_SIZE)
        cartab1Img = pygame.transform.rotate(cartab1Img,90)
        cartab1X = 70
        cartab1Y = 210

        cartab2Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
        cartab2Img = pygame.transform.rotate(cartab2Img,90)
        cartab2X = 70
        cartab2Y = 280

        cartab3Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartab3Img = pygame.transform.scale(cartab3Img,DEFAULT_IMAGE_SIZE)
        cartab3Img = pygame.transform.rotate(cartab3Img,90)
        cartab3X = 70
        cartab3Y = 350

        cartac1Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartac1Img = pygame.transform.scale(cartac1Img,DEFAULT_IMAGE_SIZE)
        cartac1X = 290
        cartac1Y = 50

        cartac2Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
        cartac2X = 360
        cartac2Y = 50

        cartac3Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartac3Img = pygame.transform.scale(cartac3Img,DEFAULT_IMAGE_SIZE)
        cartac3X = 430
        cartac3Y = 50

        cartad1Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartad1Img = pygame.transform.scale(cartad1Img,DEFAULT_IMAGE_SIZE)
        cartad1Img = pygame.transform.rotate(cartad1Img,90)
        cartad1X = 650
        cartad1Y = 210

        cartad2Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
        cartad2Img = pygame.transform.rotate(cartad2Img,90)
        cartad2X = 650
        cartad2Y = 280

        cartad3Img = pygame.image.load("cartavirada.png")
        DEFAULT_IMAGE_SIZE = (60,87)

        cartad3Img = pygame.transform.scale(cartad3Img,DEFAULT_IMAGE_SIZE)
        cartad3Img = pygame.transform.rotate(cartad3Img,90)
        cartad3X = 650
        cartad3Y = 350
        x = 0
        ca = 0
        cb = 0
        cc = 0
        cd = 0
        deck = [0,0,0,0,0,0,0,0,0,0,0,0]
        jogadab1 = 0
        jogadac1 = 0
        jogadad1 = 0
        truco = 3
        font = pygame.font.Font("freesansbold.ttf",20)
        truco_txt = font.render("",True,(255,255,255))
        quempediu = 0
        

        update_screen(screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        sleep(5)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        jogadaa1 = 1

                        print (a,b)
                        aa = 1
                        
                        e, jogadab1,jogadac1, jogadad1,cartab1X, cartab1Y, cartab1Img, cartab2X, cartab2Y, cartab2Img,cartab3X, cartab3Y, cartab3Img,cartac1X, cartac1Y, cartac1Img,cartac2X, cartac2Y, cartac2Img,cartac3X, cartac3Y, cartac3Img,cartad1X, cartad1Y, cartad1Img,cartad2X, cartad2Y, cartad2Img,cartad3X, cartad3Y, cartad3Img,truco,truco_txt,valor,a,b,c,pontos1,pontos2,quempediu,fim,ca,cb,cc,cd,d = jogada(mao1,mao2,mao3,mao4,mn1,m,mn2,mn3,mn4,ca,cb,cc,cd,valor,quempediu,a,b,saiu,e,cartaa,cartab,cartac,cartad,jogadaa1,c,aa,maom,pontos1,pontos2,cartas,
                                   screen, manilhaX, manilhaY, manilhaImg,
                                   cartaa1X, cartaa1Y, cartaa1Img,
                                   cartaa2X, cartaa2Y, cartaa2Img,
                                   cartaa3X, cartaa3Y, cartaa3Img,
                                   cartab1X, cartab1Y, cartab1Img,
                                   cartab2X, cartab2Y, cartab2Img,
                                   cartab3X, cartab3Y, cartab3Img,
                                   cartac1X, cartac1Y, cartac1Img,
                                   cartac2X, cartac2Y, cartac2Img,
                                   cartac3X, cartac3Y, cartac3Img,
                                   cartad1X, cartad1Y, cartad1Img,
                                   cartad2X, cartad2Y, cartad2Img,
                                   cartad3X, cartad3Y, cartad3Img, deck,jogadaa,jogadab,jogadac,jogadad,jogadab1,jogadac1,jogadad1,truco,truco_txt,fim,d
                                   )
                        
                        
                        sleep(3)
                    if event.key == pygame.K_2:
                        jogadaa1 = 2

                        
                        aa = 1
                        e, jogadab1,jogadac1, jogadad1,cartab1X, cartab1Y, cartab1Img, cartab2X, cartab2Y, cartab2Img,cartab3X, cartab3Y, cartab3Img,cartac1X, cartac1Y, cartac1Img,cartac2X, cartac2Y, cartac2Img,cartac3X, cartac3Y, cartac3Img,cartad1X, cartad1Y, cartad1Img,cartad2X, cartad2Y, cartad2Img,cartad3X, cartad3Y, cartad3Img,truco,truco_txt,valor,a,b,c,pontos1,pontos2,quempediu,fim,ca,cb,cc,cd,d = jogada(mao1,mao2,mao3,mao4,mn1,m,mn2,mn3,mn4,ca,cb,cc,cd,valor,quempediu,a,b,saiu,e,cartaa,cartab,cartac,cartad,jogadaa1,c,aa,maom,pontos1,pontos2,cartas,
                                   screen, manilhaX, manilhaY, manilhaImg,
                                   cartaa1X, cartaa1Y, cartaa1Img,
                                   cartaa2X, cartaa2Y, cartaa2Img,
                                   cartaa3X, cartaa3Y, cartaa3Img,
                                   cartab1X, cartab1Y, cartab1Img,
                                   cartab2X, cartab2Y, cartab2Img,
                                   cartab3X, cartab3Y, cartab3Img,
                                   cartac1X, cartac1Y, cartac1Img,
                                   cartac2X, cartac2Y, cartac2Img,
                                   cartac3X, cartac3Y, cartac3Img,
                                   cartad1X, cartad1Y, cartad1Img,
                                   cartad2X, cartad2Y, cartad2Img,
                                   cartad3X, cartad3Y, cartad3Img, deck,jogadaa,jogadab,jogadac,jogadad,jogadab1,jogadac1,jogadad1,truco,truco_txt,fim,d
                                   )
                        
                        
                        sleep(3)
                    if event.key == pygame.K_3:
                        jogadaa1 = 3

                        
                        aa = 1
                        e, jogadab1,jogadac1, jogadad1,cartab1X, cartab1Y, cartab1Img, cartab2X, cartab2Y, cartab2Img,cartab3X, cartab3Y, cartab3Img,cartac1X, cartac1Y, cartac1Img,cartac2X, cartac2Y, cartac2Img,cartac3X, cartac3Y, cartac3Img,cartad1X, cartad1Y, cartad1Img,cartad2X, cartad2Y, cartad2Img,cartad3X, cartad3Y, cartad3Img,truco,truco_txt,valor,a,b,c,pontos1,pontos2,quempediu,fim,ca,cb,cc,cd,d = jogada(mao1,mao2,mao3,mao4,mn1,m,mn2,mn3,mn4,ca,cb,cc,cd,valor,quempediu,a,b,saiu,e,cartaa,cartab,cartac,cartad,jogadaa1,c,aa,maom,pontos1,pontos2,cartas,
                                   screen, manilhaX, manilhaY, manilhaImg,
                                   cartaa1X, cartaa1Y, cartaa1Img,
                                   cartaa2X, cartaa2Y, cartaa2Img,
                                   cartaa3X, cartaa3Y, cartaa3Img,
                                   cartab1X, cartab1Y, cartab1Img,
                                   cartab2X, cartab2Y, cartab2Img,
                                   cartab3X, cartab3Y, cartab3Img,
                                   cartac1X, cartac1Y, cartac1Img,
                                   cartac2X, cartac2Y, cartac2Img,
                                   cartac3X, cartac3Y, cartac3Img,
                                   cartad1X, cartad1Y, cartad1Img,
                                   cartad2X, cartad2Y, cartad2Img,
                                   cartad3X, cartad3Y, cartad3Img, deck,jogadaa,jogadab,jogadac,jogadad,jogadab1,jogadac1,jogadad1,truco,truco_txt,fim,d
                                   )
                    if event.key == pygame.K_4:
                        if quempediu == 1:
                            if valor == 1:
                                truco_txt = font.render("Nao pode pedir truco",True,(255,255,255))
                                
                                
                            else:
                                truco_txt = font.render("Nao pode pedir",valor + 3,True,(255,255,255))
                            x = 0
                            while x == 0:
                                    truco = 1
                                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                                    truco = 0
                                    x = 1
                        else:
                            valor, quempediu, saiu, a,jogadaa1 = trucoA(mn2, mn4, valor, saiu, a,ca,cb ,cc, cd,e,screen, manilhaX, manilhaY, manilhaImg,
    cartaa1X, cartaa1Y, cartaa1Img,
    cartaa2X, cartaa2Y, cartaa2Img,
    cartaa3X, cartaa3Y, cartaa3Img,
    cartab1X, cartab1Y, cartab1Img,
    cartab2X, cartab2Y, cartab2Img,
    cartab3X, cartab3Y, cartab3Img,
    cartac1X, cartac1Y, cartac1Img,
    cartac2X, cartac2Y, cartac2Img,
    cartac3X, cartac3Y, cartac3Img,
    cartad1X, cartad1Y, cartad1Img,
    cartad2X, cartad2Y, cartad2Img,
    cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)   
                        sleep(3)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        x = 0
            if c == 3:
                running = False
                print("oioi")
        print("oi")
        pygame.display.quit()
        pygame.quit()
        
        
    return screen

def update_screen(screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2                 ):
    screen.fill((0, 0, 0))
    cartaa1(manilhaX, manilhaY, screen, manilhaImg)
    
    if deck[0] == 0 :
        cartaa1(cartaa1X, cartaa1Y, screen, cartaa1Img)
    if  deck[1] == 0 :
        cartaa1(cartaa2X, cartaa2Y, screen, cartaa2Img)
    if deck[2] == 0:
        cartaa1(cartaa3X, cartaa3Y, screen, cartaa3Img)
    if deck[3] == 0:
        cartaa1(cartab1X, cartab1Y, screen, cartab1Img)
    if deck[4] == 0:
        cartaa1(cartab2X, cartab2Y, screen, cartab2Img)
    if deck[5] == 0:
        cartaa1(cartab3X, cartab3Y, screen, cartab3Img)
    if deck[6] == 0 :
        cartaa1(cartac1X, cartac1Y, screen, cartac1Img)
    if deck[7] == 0:
        cartaa1(cartac2X, cartac2Y, screen, cartac2Img)
    if deck[8] == 0:
        cartaa1(cartac3X, cartac3Y, screen, cartac3Img)
    if deck[9] == 0:
        cartaa1(cartad1X, cartad1Y, screen, cartad1Img)
    if deck[10] == 0:
        cartaa1(cartad2X, cartad2Y, screen, cartad2Img)
    if deck[11] == 0:
        cartaa1(cartad3X, cartad3Y, screen, cartad3Img)
    if truco == 1 or truco == 2:
        truco_texto(screen,truco_txt)
    inicio_texto(screen)
    placar(screen,pontos1,pontos2)
    A(screen)
    B(screen)
    C(screen)
    D(screen)
    manilha(screen)
    pygame.display.update()
    return deck
def cartaa1(x,y,screen,cartaa1Img):
    screen.blit(cartaa1Img, (x, y))

def truco_texto(screen,truco_txt):
    font = pygame.font.Font("freesansbold.ttf",20)
    screen.blit(truco_txt, (100, 100))
def inicio_texto(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    inicio_txt = font.render("Aperte 1, 2 ou 3 na sua vez, para jogar as cartas 1,2 e 3, 4 para pedir truco ou 6 ou 9",True,(255,255,255))
    screen.blit(inicio_txt, (10, 10))
def placar(screen,pontos1,pontos2):
    font = pygame.font.Font("freesansbold.ttf",18)
    pontos1str = str(pontos1)
    pontos2str = str(pontos2)
    placar_txt = font.render("Dupla 1:"+pontos1str+"Dupla 2:"+pontos2str,True,(255,255,255))
    screen.blit(placar_txt, (10, 500))
def A(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    A_txt = font.render("A",True,(255,255,255))
    screen.blit(A_txt, (360, 450))
def B(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    B_txt = font.render("B",True,(255,255,255))
    screen.blit(B_txt, (170, 280))
def C(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    C_txt = font.render("C",True,(255,255,255))
    screen.blit(C_txt, (360, 150))
def D(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    D_txt = font.render("D",True,(255,255,255))
    screen.blit(D_txt, (750, 280))
def manilha(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    manilha_txt = font.render("Manilha",True,(255,255,255))
    screen.blit(manilha_txt, (570, 230))

def jogada(mao1,mao2,mao3,mao4,mn1,m,mn2,mn3,mn4,ca,cb,cc,cd,valor,quempediu,a,b,saiu,e,cartaa,cartab,cartac,cartad,jogadaa1,c,aa,maom,pontos1,pontos2,cartas,screen, manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img,deck,jogadaa,jogadab,jogadac,jogadad,jogadab1,jogadac1,jogadad1,truco,truco_txt,fim,d):
    
    
    
    if 1 == 1:
        
        #print(valor)
            
        
        
        if e == "a" and aa == 1:
            print("manilha",maom)
            print("A",mao1)
            if saiu != 0 and b != 2 and a != 2:
                ca,mao1,mn1,valor, quempediu,a,saiu,cartaa1X,cartaa1Y,cartaa2X,cartaa2Y,cartaa3X,cartaa3Y,deck,jogadaa1,jogadaa,truco_txt = jogadorA(mao1,mn1,m,mn2,mn3,mn4,cb,cc,cd,valor, quempediu,a,saiu,e,cartaa,jogadaa1,cartas,screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao2,mao3, mao4, deck,jogadaa,truco,truco_txt,pontos1, pontos2)
                
                sleep(1)
            if saiu != 0 and b != 2 and a != 2:
                cb, mao2,mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                
                sleep(1)
            if saiu != 0 and b != 2 and a != 2:
                cc, mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                sleep(1)
            if saiu != 0 and b != 2 and a != 2:
                cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                
                sleep(1)
                
            if saiu != 0:
                a, b, e, deck = fimjogada(a,b,e,ca,cb,cc,cd,valor,quempediu,pontos1,pontos2,saiu,jogadaa1,jogadab1,jogadac1,jogadad1,deck,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,jogadaa,jogadab,jogadac,jogadad,truco,truco_txt)
            aa = 0  
                    
        
            if e == "b" and aa == 0:
                print("manilha",maom)
                print("A", mao1)
                if saiu != 0 and b != 2 and a != 2:
                    cb, mao2, mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                if saiu != 0 and b != 2 and a != 2:
                    cc, mao3, mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                if saiu != 0 and b != 2 and a != 2:
                    cd, mao4, mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                    aa = 1
            if e == "c" and aa == 0:
                print("manilha",maom)
                print("A", mao1)
                if saiu != 0 and b != 2 and a != 2:
                    cc,mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                if saiu != 0 and b != 2 and a != 2:
                    cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                    aa = 1
                
            if e == "d" and aa == 0:
                print("manilha",maom)
                print("A", mao1)
                if saiu != 0 and b != 2 and a != 2:
                    cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                    aa = 1
                
                    
                
        else:
            if e == "b" and aa == 1:
                if saiu != 0 and b != 2 and a != 2:
                    ca,mao1,mn1,valor,quempediu,a,saiu,cartaa1X,cartaa1Y,cartaa2X,cartaa2Y,cartaa3X,cartaa3Y,deck,jogadaa1,jogadaa,truco_txt = jogadorA(mao1,mn1,m,mn2,mn3,mn4,cb,cc,cd,valor,quempediu,a,saiu,e,cartaa,jogadaa1,cartas,screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img,mao2,mao3, mao4, deck,jogadaa,truco,truco_txt,pontos1, pontos2)
                    sleep(1)
                print(jogadaa1,jogadab1,jogadac1,jogadad1)
                if saiu != 0 and b != 2 and a != 2:
                    a, b, e, deck =  fimjogada(a,b,e,ca,cb,cc,cd,valor,quempediu,pontos1,pontos2,saiu,jogadaa1,jogadab1,jogadac1,jogadad1,deck,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,jogadaa,jogadab,jogadac,jogadad,truco,truco_txt)

                aa = 0
                if e == "b" and aa == 0:
                    print("manilha",maom)
                    print("A", mao1)
                    if saiu != 0 and b != 2 and a != 2:
                        cb, mao2, mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                    if saiu != 0 and b != 2 and a != 2:
                        cc, mao3, mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                    if saiu != 0 and b != 2 and a != 2:
                        cd, mao4, mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                        aa = 1
                if e == "c" and aa == 0:
                    print("manilha",maom)
                    print("A", mao1)
                    if saiu != 0 and b != 2 and a != 2:
                        cc,mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                    if saiu != 0 and b != 2 and a != 2:
                        cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                        aa = 1
                if e == "d" and aa == 0:
                    print("manilha",maom)
                    print("A", mao1)
                    if saiu != 0 and b != 2 and a != 2:
                        cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                        aa = 1
            
                
                                         
            else:
                if e == "c" and aa == 1:
                    if saiu != 0 and b != 2 and a != 2:
                        ca,mao1,mn1,valor,quempediu,a,saiu,cartaa1X,cartaa1Y,cartaa2X,cartaa2Y,cartaa3X,cartaa3Y,deck,jogadaa1,jogadaa,truco_txt = jogadorA(mao1,mn1,m,mn2,mn3,mn4,cb,cc,cd,valor,quempediu,a,saiu,e,cartaa,jogadaa1,cartas,screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img,mao2,mao3, mao4, deck,jogadaa,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                    if saiu != 0 and b != 2 and a != 2:
                        cb,mao2,mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                        sleep(1)
                                
                    print(jogadaa1,jogadab1,jogadac1,jogadad1)
                    if saiu != 0 and b != 2 and a != 2:
                        a, b, e, deck = fimjogada(a,b,e,ca,cb,cc,cd,valor,quempediu,pontos1,pontos2,saiu,jogadaa1,jogadab1,jogadac1,jogadad1,deck,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,jogadaa, jogadab,jogadac,jogadad,truco,truco_txt)
                    aa = 0
                    if e == "b" and aa == 0:
                        print("manilha",maom)
                        print("A", mao1)
                        if saiu != 0 and b != 2 and a != 2:
                            cb, mao2, mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                        if saiu != 0 and b != 2 and a != 2:
                            cc, mao3, mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                        if saiu != 0 and b != 2 and a != 2:
                            cd, mao4, mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt= jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                            aa = 1
                    if e == "c" and aa == 0:
                        print("manilha",maom)
                        print("A", mao1)
                        if saiu != 0 and b != 2 and a != 2:
                            cc,mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                        if saiu != 0 and b != 2 and a != 2:
                            cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                            aa = 1
                            
                    if e == "d" and aa == 0:
                        print("manilha",maom)
                        print("A", mao1)
                        print("ola")
                        if saiu != 0 and b != 2 and a != 2:
                            cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                            sleep(1)
                            aa = 1
            
                else:
                    if e == "d" and aa == 1:
                            if saiu != 0 and b != 2 and a != 2:
                                ca,mao1,mn1,valor, quempediu,a,saiu,cartaa1X,cartaa1Y,cartaa2X,cartaa2Y,cartaa3X,cartaa3Y,deck,jogadaa1,jogadaa,truco_txt = jogadorA(mao1,mn1,m,mn2,mn3,mn4,cb,cc,cd,valor,quempediu,a,saiu,e,cartaa,jogadaa1,cartas,screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao2,mao3, mao4, deck,jogadaa,truco,truco_txt,pontos1, pontos2)
                                sleep(1)
                            if saiu != 0 and b != 2 and a != 2:
                                cb,mao2,mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                                sleep(1)
                                    
                            if saiu != 0 and b != 2 and a != 2:
                                cc,mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                                sleep(1)
                            print(jogadaa1,jogadab1,jogadac1,jogadad1)
                            if saiu != 0 and b != 2 and a != 2:
                                a, b, e, deck = fimjogada(a,b,e,ca,cb,cc,cd,valor,quempediu,pontos1,pontos2,saiu,jogadaa1,jogadab1,jogadac1,jogadad1,deck,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,jogadaa,jogadab,jogadac,jogadad,truco,truco_txt)
                                aa = 0
                            if e == "b" and aa == 0:
                                print("manilha",maom)
                                print("A", mao1)
                                if saiu != 0 and b != 2 and a != 2:
                                    cb, mao2, mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt = jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1, mao3, mao4, deck,jogadab,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                            
                                if saiu != 0 and b != 2 and a != 2:
                                    cc, mao3, mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                if saiu != 0 and b != 2 and a != 2:
                                    cd, mao4, mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                    aa = 1
                            if e == "c" and aa == 0:
                                print("manilha",maom)
                                print("A", mao1)
                                if saiu != 0 and b != 2 and a != 2:
                                    cc,mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt = jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4, deck,jogadac,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                if saiu != 0 and b != 2 and a != 2:
                                    cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                    aa = 1
                            if e == "d" and aa == 0:
                                print("manilha",maom)
                                print("A", mao1)
                                if saiu != 0 and b != 2 and a != 2:
                                    cd,mao4,mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt = jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2)
                                    sleep(1)
                                    aa = 1
                                    
                                 
        if a == 2 and d != 0:
            print ("Dupla 1 ganhou")
                
            c = 3
            
            
                
            pontos1 = pontos1 + valor
            d = 0
            print("d",d)
        if b == 2 and d != 0 :
            print ("Dupla 2 ganhou")
            c = 3
            
            
            
            
            pontos2 = pontos2 + valor
            d = 0
            print("d",d)
        #if saiu == 0 and quempediu == 1:
         #   a = 0
          #  b = 0
           # c = 3
            #pontos1 = pontos1 + valor
        #if saiu == 0 and quempediu == 2:
         #   a = 0
          #  b = 0
           # c = 3
            #pontos2 = pontos2 + valor    
    if pontos1 >= 12:
        fim = 1
        font = pygame.font.Font("freesansbold.ttf",40)
        truco_txt = font.render("DUPLA 1 GANHOU O JOGO ! ",True,(255,255,255))
        truco = 1
        
        print(pontos1, pontos2)
        print ("DUPLA 1 GANHOU O JOGO!!")
    if pontos2 >= 12:
        fim = 1
        font = pygame.font.Font("freesansbold.ttf",40)
        truco_txt = font.render("DUPLA 2 GANHOU O JOGO ! ",True,(255,255,255))
        truco = 1
        
        print(pontos1, pontos2)
        print ("DUPLA 2 GANHOU O JOGO!!")
    print("score",pontos1, pontos2)
    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
    sleep(3)
    return e, jogadab1,jogadac1, jogadad1,cartab1X, cartab1Y, cartab1Img, cartab2X, cartab2Y, cartab2Img,cartab3X, cartab3Y, cartab3Img,cartac1X, cartac1Y, cartac1Img,cartac2X, cartac2Y, cartac2Img,cartac3X, cartac3Y, cartac3Img,cartad1X, cartad1Y, cartad1Img,cartad2X, cartad2Y, cartad2Img,cartad3X, cartad3Y, cartad3Img,truco,truco_txt,valor,a,b,c,pontos1,pontos2,quempediu,fim,ca,cb,cc,cd,d
                         
            
def jogadorA(mao1,mn1,m,mn2,mn3,mn4,cb,cc,cd,valor, quempediu,a,saiu,e,cartaa,jogadaa1,cartas,screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img,mao2,mao3, mao4,deck,jogadaa,truco,truco_txt,pontos1, pontos2):
    
    ca = 0
    
            
    jogadaa.append(jogadaa1)
    print(jogadaa)
    if saiu == 0:
        jogadaa1 = 0
    
        
    if jogadaa1 == 1:
        ca = cartaa[0]
        print("Jogador A jogou",mao1[0])
        
        del mao1[0]
                
        del mn1[0]
        del cartaa[0]
    if jogadaa1 == 2:
        ca = cartaa[1]
        print("Jogador A jogou",mao1[1])
        del mao1[1]
                
        del mn1[1]
        del cartaa[1]
    if jogadaa1 == 3:
        ca = cartaa[2]
        print("Jogador A jogou",mao1[2] )
        del mao1[2]
               
        del mn1[2]
        del cartaa[2]
    print(ca)
    if len(jogadaa) == 1:
        
        if jogadaa1 == 1:
                
            
            cartaa1X = 290
            cartaa1Y = 290
            
                
            
                
                
        if jogadaa1 == 2:
                

            
            cartaa2X = 290
            cartaa2Y = 290
            
            
                
        if jogadaa1 == 3:
                
            
            cartaa3X = 290
            cartaa3Y = 290
            
                
        
    if len(jogadaa) == 2:
        if jogadaa[0] == 1 and jogadaa[1] == 1:
            
            cartaa2X = 290
            cartaa2Y = 290
            
        if (jogadaa[0] == 2 or jogadaa[0] == 3) and jogadaa[1] == 1:
            cartaa1X = 290
            cartaa1Y = 290
            
        if (jogadaa[0] == 1 or jogadaa[0] == 2) and jogadaa[1] == 2:
            cartaa3X = 290
            cartaa3Y = 290
                
        if jogadaa[0] == 3   and jogadaa[1] == 2:
            cartaa2X = 290
            cartaa2Y = 290
    if len(jogadaa) == 3:
        if (jogadaa[0] == 1 or jogadaa[0] == 2) and jogadaa[1] == 1:
            cartaa3X = 290
            cartaa3Y = 290
        if jogadaa[0] == 1 and jogadaa[1] == 2:
            cartaa2X = 290
            cartaa2Y = 290
        if (jogadaa[0] == 2 or jogadaa[0] == 3) and jogadaa[1] == 2:
            cartaa1X = 290
            cartaa1Y = 290
        if jogadaa[0] == 3 and jogadaa[1] == 1:
            cartaa2X = 290
            cartaa2Y = 290
    
    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1,mao2,mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        #parte de pedir truco
    if jogadaa1 == 4 and quempediu == 1:
        if valor == 1:
            print("nao pode pedir truco")
        else:
            print("nao pode pedir",valor+3)
    else:
        if jogadaa1 == 4:
            if valor == 1:
                print("JogadorA pediu truco")
            else:
                print("JogadorA pediu",valor+3)
            valor, quempediu, saiu, a = trucoA(mn2, mn4, valor, saiu, a,ca,cb ,cc, cd,e)
                
                

    return ca,mao1, mn1, valor,quempediu,a,saiu,cartaa1X,cartaa1Y,cartaa2X,cartaa2Y,cartaa3X,cartaa3Y,deck,jogadaa1,jogadaa,truco_txt

def jogadorB(mao2,mn2,m,ca,cb,cc,cd,valor, quempediu,b,saiu,cartab,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao3, mao4,deck,jogadab,truco,truco_txt,pontos1, pontos2):
    #jogadab1 = int(input("jogar carta 1, 2 ou 3"))
    jogadab1 = 0
    if len(mn2) == 3:
        
        if ca == 0 and cc == 0 and cd == 0:
            if mn2[0]>=mn2[1] and mn2[0]>= mn2[2]:
                jogadab1 = 1
            if mn2[1]>=mn2[2] and mn2[1]>= mn2[0]:
                jogadab1 = 2
            if mn2[2]>=mn2[1] and mn2[2]>= mn2[0]:
                jogadab1 = 3
            
        else:
            
            if (cd<= ca or cd <= cc):
                
                if cartab[0] > ca and cartab[0] > cc and cartab[1] > ca and cartab[1] > cc and cartab[2] > ca and cartab[2]> cc:
                    if mn2[0]<=mn2[1] and mn2[0]<= mn2[2]:
                        jogadab1 = 1
                    if mn2[1]<=mn2[2] and mn2[1]<= mn2[0]:
                        jogadab1 = 2
                    if mn2[2]<=mn2[1] and mn2[2]<= mn2[0]:
                        jogadab1 = 3
                    
                else:
                    if cartab[0] > ca and cartab[0] > cc and cartab[1] > ca and cartab[1] > cc:
                        if mn2[0]<=mn2[1] :
                            jogadab1 = 1
                        if mn2[1]<=mn2[0] :
                            jogadab1 = 2
                    else:
                        if cartab[0] > ca and cartab[0] > cc and cartab[2] > ca and cartab[2] > cc:
                            if mn2[0]<=mn2[2] :
                                jogadab1 = 1
                            if mn2[2]<=mn2[0] :
                                jogadab1 = 3
                        else:
                            if cartab[1] > ca and cartab[1] > cc and cartab[2] > ca and cartab[2] > cc:
                                if mn2[1]<=mn2[2] :
                                    jogadab1 = 2
                                if mn2[2]<=mn2[1] :
                                    jogadab1 = 3
                            else:
                                if cartab[0] >= ca and cartab[0] >= cc:
                                    jogadab1 = 1
                                else:
                                    if cartab[1] >= ca and cartab[1] >= cc:
                                        jogadab1 = 2
                                    else:
                                        if cartab[2] >= ca and cartab[2] >= cc:
                                            jogadab1 = 3
                                        else:
                                            if mn2[0]<=mn2[1] and mn2[0]<= mn2[2]:
                                                jogadab1 = 1
                                            if mn2[1]<=mn2[2] and mn2[1]<= mn2[0]:
                                                jogadab1 = 2
                                            if mn2[2]<=mn2[1] and mn2[2]<= mn2[0]:
                                                jogabab1 = 3

            else:
                if mn2[0]<=mn2[1] and mn2[0]<= mn2[2]:
                    jogadab1 = 1
                if mn2[1]<=mn2[2] and mn2[1]<= mn2[0]:
                    jogadab1 = 2
                if mn2[2]<=mn2[1] and mn2[2]<= mn2[0]:
                    jogabab1 = 3
    print(valor)
    
    if len(mn2) == 2:
        quempediu, cb, valor, saiu, b, truco,aceita,truco_txt = trucoB(mn2,b,valor,saiu,quempediu,cb,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if saiu != 0:
            if cd == 0 and ca == 0 and cc == 0:
                if mn2[0]>=mn2[1] :
                    jogadab1 = 1
                if mn2[1]>= mn2[0]:
                    jogadab1 = 2
            else:
                if cd<= ca or cd <= cc:
                    if cartab[0] > ca and cartab[0] > cc or cartab[1] > ca and cartab[1] > cc:
                        if mn2[0]<=mn2[1] :
                            jogadab1 = 1
                        if mn2[1]<=mn2[0] :
                            jogadab1 = 2
                    else:
                        if cartab[0] >= ca and cartab[0] >= cc:
                            jogadab1 = 1
                        else:
                            if cartab[1] >= ca and cartab[1] >= cc:
                                jogadab1 = 2
                            else:
                                if mn2[0]<=mn2[1] :
                                    jogadab1 = 1
                                if mn2[1]<=mn2[0] :
                                    jogadab1 = 2
                else:
                    if mn2[0]<=mn2[1] :
                        jogadab1 = 1
                    if mn2[1]<=mn2[0] :
                        jogadab1 = 2
                    

            
    if len(mn2) == 1:
        quempediu, cb, valor, saiu, b, truco,aceita,truco_txt = trucoB(mn2,b,valor,saiu,quempediu,cb,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if saiu != 0:
            jogadab1 = 1
        
    jogadab.append(jogadab1)    
    
        
    
    if len(jogadab) == 1:
        if jogadab[0] == 1:
            cartab1Img = cartas[mn2[0]]
        
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab1Img = pygame.transform.scale(cartab1Img,DEFAULT_IMAGE_SIZE)
            cartab1Img = pygame.transform.rotate(cartab1Img,90)
            cartab1X = 230
            cartab1Y = 280
        
        
        
        
        if jogadab[0] == 2:
            cartab2Img = cartas[mn2[1]]
            
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
            cartab2Img = pygame.transform.rotate(cartab2Img,90)
            cartab2X = 230
            cartab2Y = 280

        
        
        if jogadab[0] == 3:
            cartab3Img = cartas[mn2[2]]
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab3Img = pygame.transform.scale(cartab3Img,DEFAULT_IMAGE_SIZE)
            cartab3Img = pygame.transform.rotate(cartab3Img,90)
            cartab3X = 230
            cartab3Y = 280
    if len(jogadab) == 2:
        if jogadab[0] == 1 and jogadab[1] == 1:
            cartab2Img = cartas[mn2[0]]
            
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
            cartab2Img = pygame.transform.rotate(cartab2Img,90)
            cartab2X = 230
            cartab2Y = 280
        if (jogadab[0] == 1 or jogadab[0] == 2) and jogadab[1] == 2:
            cartab3Img = cartas[mn2[1]]
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab3Img = pygame.transform.scale(cartab3Img,DEFAULT_IMAGE_SIZE)
            cartab3Img = pygame.transform.rotate(cartab3Img,90)
            cartab3X = 230
            cartab3Y = 280
        if (jogadab[0] == 2 or jogadab[0] == 3) and jogadab[1] == 1:
            cartab1Img = cartas[mn2[0]]
        
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab1Img = pygame.transform.scale(cartab1Img,DEFAULT_IMAGE_SIZE)
            cartab1Img = pygame.transform.rotate(cartab1Img,90)
            cartab1X = 230
            cartab1Y = 280
        if jogadab[0] == 3 and jogadab[1] == 2:
            cartab2Img = cartas[mn2[1]]
            
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
            cartab2Img = pygame.transform.rotate(cartab2Img,90)
            cartab2X = 230
            cartab2Y = 280
    if len(jogadab) == 3:
        if (jogadab[0] == 1 or jogadab[0] == 2) and jogadab[1] == 1:
            cartab3Img = cartas[mn2[0]]
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab3Img = pygame.transform.scale(cartab3Img,DEFAULT_IMAGE_SIZE)
            cartab3Img = pygame.transform.rotate(cartab3Img,90)
            cartab3X = 230
            cartab3Y = 280
        if jogadab[0] == 1 and jogadab[1] == 2:
            cartab2Img = cartas[mn2[0]]
            
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
            cartab2Img = pygame.transform.rotate(cartab2Img,90)
            cartab2X = 230
            cartab2Y = 280
        if jogadab[0] == 2 or jogadab[0] == 3 and jogadab[1] == 2:
            cartab1Img = cartas[mn2[0]]
        
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab1Img = pygame.transform.scale(cartab1Img,DEFAULT_IMAGE_SIZE)
            cartab1Img = pygame.transform.rotate(cartab1Img,90)
            cartab1X = 230
            cartab1Y = 280
        if jogadab[0] == 3 and jogadab[1] == 1:
            cartab2Img = cartas[mn2[0]]
            
            DEFAULT_IMAGE_SIZE = (60,87)

            cartab2Img = pygame.transform.scale(cartab2Img,DEFAULT_IMAGE_SIZE)
            cartab2Img = pygame.transform.rotate(cartab2Img,90)
            cartab2X = 230
            cartab2Y = 280
    
    if jogadab1 == 1:
        
        
        
        
        cb = cartab[0]
        #sleep(2)
        print("Jogador B jogou",mao2[0])
        mao2 [0] = "já usada"
        del cartab[0]
        del mao2[0]
        del mn2[0]
    if jogadab1 == 2:
        

        
        cb = cartab[1]
        #sleep(2)
        print("Jogador B jogou",mao2[1])
        del cartab[1]
        del mao2[1]
        del mn2[1]
    if jogadab1 == 3:
        cb = cartab[2]
        #sleep(2)
        print("Jogador B jogou",mao2[2])
        del cartab[2]
        del mao2[2]
        del mn2[2]    
    print(cb)
    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
    return cb, mao2, mn2,valor, quempediu,b,saiu,cartab1Img,cartab1X,cartab1Y,cartab2Img,cartab2X,cartab2Y,cartab3Img,cartab3X,cartab3Y,deck,jogadab1,jogadab,truco_txt
def jogadorC(mao3,mn3,m,ca,cb,cc,cd,mn2,mn4,a,valor,quempediu,e,saiu,cartac,cartas,screen,manilhaX, manilhaY, manilhaImg,
                              cartaa1X, cartaa1Y, cartaa1Img,
                              cartaa2X, cartaa2Y, cartaa2Img,
                              cartaa3X, cartaa3Y, cartaa3Img,
                              cartab1X, cartab1Y, cartab1Img,
                              cartab2X, cartab2Y, cartab2Img,
                              cartab3X, cartab3Y, cartab3Img,
                              cartac1X, cartac1Y, cartac1Img,
                              cartac2X, cartac2Y, cartac2Img,
                              cartac3X, cartac3Y, cartac3Img,
                              cartad1X, cartad1Y, cartad1Img,
                              cartad2X, cartad2Y, cartad2Img,
                              cartad3X, cartad3Y, cartad3Img, mao1,  mao2, mao4,deck,jogadac,truco,truco_txt,pontos1, pontos2):
    #jogadac1 = int(input("jogar carta 1, 2 ou 3"))
    #30
    font = pygame.font.Font("freesansbold.ttf",20)
    jogadac1 = 0
    
    if sum(mn3)/len(mn3) > 40  and quempediu != 1  :
        quempediu = 1
        print("jogadorC pediu truco")
        tamanhob = len(mn2)
        tamanhod = len(mn4)
        if tamanhob == 0:
            tamanhob = 1
        if tamanhod == 0:
            tamanhod = 1
        somab = sum(mn2)/tamanhob
        somad = sum(mn4)/tamanhod
        if e == "a":
            somab = sum(mn2)/tamanhob
            somad = sum(mn4)/tamanhod
        if e == "b":
            somab = (sum(mn2)+cb)/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        if e == "c":
            somab = (sum(mn2))/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        if e == "d":
            somab = (sum(mn2))/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        
        x = 1
        while x == 1:
            truco = 1
            valorstr = str(valor + 3)
            if valor == 1: 
                truco_txt = font.render("Dupla 1 pediu truco !",True,(255,255,255))
                print(valor)
            else:
                truco_txt = font.render("Dupla 1 pediu "+valorstr,True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            x = 0
        if  valor == 1:
            if somab +somad > 46:
                #46
                    
                quempediu = 1
                                
                truco = 1
                truco_txt = font.render("Dupla 2 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                
                
                valor = 3
            else:
                print("Dupla 2 saiu")
                saiu = 0
                jogadad1 = 0
                quempediu = 1
                a = 2
                truco = 1
                truco_txt = font.render("Dupla 2 saiu.Dupla 1 ganhou !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        else:
                           
            if somab + somad > 56 :
                #56
                quempediu = 1
                valor = valor + 3
                truco = 1
                truco_txt = font.render("Dupla 2 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                
                
                
                    
                                            
                
            else:
                print("Dupla 2 saiu")
                saiu = 0
                jogadad1 = 0
                quempediu = 1
                a = 2
                truco = 1
                truco_txt = font.render("Dupla 2 saiu.Dupla 1 ganhou !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                
        
        
            #if somab +somad > 46:                    
                
                                        
            #if somab + somad > 56 :
         
        #33
    
    if sum(mn3)/len(mn3) > 40 and a == 1 and quempediu != 1 and valor != 1 :
        quempediu = 1
        print("jogadorC pediu",valor+3)
        tamanhob = len(mn2)
        tamanhod = len(mn4)
        if tamanhob == 0:
            tamanhob = 1
        if tamanhod == 0:
            tamanhod = 1
        somab = sum(mn2)/tamanhob
        somad = sum(mn4)/tamanhod
        if e == "a":
            somab = sum(mn2)/tamanhob
            somad = sum(mn4)/tamanhod
        if e == "b":
            somab = (sum(mn2)+cb)/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        if e == "c":
            somab = (sum(mn2))/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        if e == "d":
            somab = (sum(mn2))/tamanhob
            somad = (sum(mn4)+cd)/tamanhod
        
        
        if  valor == 1:
            if somab +somad > 46:                    
                #46
                quempediu = 1
                            
                print ("vamos")
                valor = 3
            else:
                print("Dupla 2 saiu")
                saiu = 0
                quempediu = 1
                a = 2
                 
        else:
                                        
            if somab + somad > 56 :
                valor = valor + 3
                #56
                    
                                            
                
            else:
                print("Dupla 2 saiu")
                saiu = 0
                quempediu = 1
                a = 2    
        
    if saiu != 0:
        if len(mn3) == 3:
            if ca == 0 and cb == 0 and cd == 0:
                if mn3[0]>=mn3[1] and mn3[0]>= mn3[2]:
                    jogadac1 = 1
                if mn3[1]>=mn3[2] and mn3[1]>= mn3[0]:
                    jogadac1 = 2
                if mn3[2]>=mn3[1] and mn3[2]>= mn3[0]:
                    jogadac1 = 3
            else:
                if (ca<= cb or ca <= cd):
                    if cartac[0] > cb and cartac[0] > cd and cartac[1] > cb and cartac[1] > cd and cartac[2] > cb and cartac[2]> cd:
                        if mn3[0]<=mn3[1] and mn3[0]<= mn3[2]:
                            jogadac1 = 1
                        if mn3[1]<=mn3[2] and mn3[1]<= mn3[0]:
                            jogadac1 = 2
                        if mn3[2]<=mn3[1] and mn3[2]<= mn3[0]:
                            jogadac1 = 3
                    else:
                        if cartac[0] > cb and cartac[0] > cd and cartac[1] > cb and cartac[1] > cd:
                            if mn3[0]<=mn3[1] :
                                jogadac1 = 1
                            if mn3[1]<=mn3[0] :
                                jogadac1 = 2
                        else:
                            if cartac[0] > cb and cartac[0] > cd and cartac[2] > cb and cartac[2] > cd:
                                if mn3[0]<=mn3[2] :
                                    jogadac1 = 1
                                if mn3[2]<=mn3[0] :
                                    jogadac1 = 3
                            else:
                                if cartac[1] > cb and cartac[1] > cd and cartac[2] > cb and cartac[2] > cd:
                                    if mn3[1]<=mn3[2] :
                                        jogadac1 = 2
                                    if mn3[2]<=mn3[1] :
                                        jogadac1 = 3
                                else:
                                    if cartac[0] >= cb and cartac[0] >= cd:
                                        jogadac1 = 1
                                    else:
                                        if cartac[1] >= cb and cartac[1] >= cd:
                                            jogadac1 = 2
                                        else:
                                            if cartac[2] >= cb and cartac[2] >= cd:
                                                jogadac1 = 3
                                            else:
                                                if mn3[0]<=mn3[1] and mn3[0]<= mn3[2]:
                                                    jogadac1 = 1
                                                if mn3[1]<=mn3[2] and mn3[1]<= mn3[0]:
                                                    jogadac1 = 2
                                                if mn3[2]<=mn3[1] and mn3[2]<= mn3[0]:
                                                    jogadac1 = 3
                else:
                    if mn3[0]<=mn3[1] and mn3[0]<= mn3[2]:
                        jogadac1 = 1
                    if mn3[1]<=mn3[2] and mn3[1]<= mn3[0]:
                        jogadac1 = 2
                    if mn3[2]<=mn3[1] and mn3[2]<= mn3[0]:
                        jogadac1 = 3
        if len(mn3) == 2:    
            if ca == 0 and cb == 0 and cd == 0:
                if mn3[0]>=mn3[1] :
                    jogadac1 = 1
                if mn3[1]>= mn3[0]:
                    jogadac1 = 2
            else:
                if ca<= cb or ca <= cd:
                    if cartac[0] > cb and cartac[0] > cd and cartac[1] > cb and cartac[1] > cd:
                        if mn3[0]<=mn3[1] :
                            jogadac1 = 1
                        if mn3[1]<=mn3[0] :
                            jogadac1 = 2
                    else:
                        if cartac[0] >= cb and cartac[0] >= cd:
                            jogadac1 = 1
                        else:
                            if cartac[1] >= cb and cartac[1] >= cd:
                                jogadac1 = 2
                            else:
                                if mn3[0]<=mn3[1] :
                                    jogadac1 = 1
                                if mn3[1]<=mn3[0] :
                                    jogadac1 = 2
                else:
                    if mn3[0]<=mn3[1] :
                        jogadac1 = 1
                    if mn3[1]<=mn3[0] :
                        jogadac1 = 2
                        
        
       
        if len(mn3) == 1:
            jogadac1 = 1
        jogadac.append(jogadac1)
        if len(jogadac) == 1:
            if jogadac[0] == 1:
                cartac1Img = cartas[mn3[0]]
        
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac1Img = pygame.transform.scale(cartac1Img,DEFAULT_IMAGE_SIZE)
                
                cartac1X = 280
                cartac1Y = 250
            if jogadac[0] == 2:
                cartac2Img = cartas[mn3[1]]
        
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
            
                cartac2X = 280
                cartac2Y = 250
            if jogadac[0] == 3:
                cartac3Img = cartas[mn3[2]]
        
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac3Img = pygame.transform.scale(cartac3Img,DEFAULT_IMAGE_SIZE)
                
                cartac3X = 280
                cartac3Y = 250
        

        if len(jogadac) == 2:
            if jogadac[0] == 1 and jogadac[1] == 1:
                cartac2Img = cartas[mn3[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
                cartac2X = 280
                cartac2Y = 250
            if (jogadac[0] == 1 or jogadac[0] == 2) and jogadac[1] == 2:
                cartac3Img = cartas[mn3[1]]
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac3Img = pygame.transform.scale(cartac3Img,DEFAULT_IMAGE_SIZE)
                cartac3X = 280
                cartac3Y = 250
            if (jogadac[0] == 2 or jogadac[0] == 3) and jogadac[1] == 1:
                cartac1Img = cartas[mn3[0]]
            
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac1Img = pygame.transform.scale(cartac1Img,DEFAULT_IMAGE_SIZE)
                cartac1X = 280
                cartac1Y = 250
            if jogadac[0] == 3 and jogadac[1] == 2:
                cartac2Img = cartas[mn3[1]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
                cartac2X = 280
                cartac2Y = 250
        if len(jogadac) == 3:
            if (jogadac[0] == 1 or jogadac[0] == 2) and jogadac[1] == 1:
                cartac3Img = cartas[mn3[0]]
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac3Img = pygame.transform.scale(cartac3Img,DEFAULT_IMAGE_SIZE)
                cartac3X = 280
                cartac3Y = 250
            if jogadac[0] == 1 and jogadac[1] == 2:
                cartac2Img = cartas[mn3[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
                
                cartac2X = 280
                cartac2Y = 250
            if jogadac[0] == 2 or jogadac[0] == 3 and jogadac[1] == 2:
                cartac1Img = cartas[mn3[0]]
            
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac1Img = pygame.transform.scale(cartac1Img,DEFAULT_IMAGE_SIZE)
                cartac1X = 280
                cartac1Y = 250
            if jogadac[0] == 3 and jogadac[1] == 1:
                cartac2Img = cartas[mn3[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartac2Img = pygame.transform.scale(cartac2Img,DEFAULT_IMAGE_SIZE)
                cartac2X = 280
                cartac2Y = 250

        print("valor= ",valor)    
        if jogadac1 == 1:
            

            cc = cartac[0]
            
            
            
            #sleep(2)
            print("Jogador C jogou",mao3[0])
            
            del mao3[0]
            del mn3[0]
            del cartac[0]
        if jogadac1 == 2:
            cc = cartac[1]
            
            
            
            #sleep(2)
            print("Jogador C jogou",mao3[1])
            mao3 [1] = "já usada"
            del mao3[1]
            del mn3[1]
            del cartac[1]
        if jogadac1 == 3:
            
            cc = cartac[2]
            #sleep(2)
            print("Jogador c jogou",mao3[2])
            mao3 [2] = "já usada"
            del mao3[2]
            del mn3[2]
            del cartac[2]
        print(cc)
        deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
    return cc, mao3,mn3,valor, quempediu,a,saiu,cartac1Img,cartac1X,cartac1Y,cartac2Img,cartac2X,cartac2Y,cartac3Img,cartac3X,cartac3Y,deck,jogadac1,jogadac,truco_txt
def jogadorD(mao4,mn4,m,ca,cb,cc,cd,valor,quempediu, saiu, b,cartad,cartas,screen, manilhaX, manilhaY, manilhaImg,
                      cartaa1X, cartaa1Y, cartaa1Img,
                      cartaa2X, cartaa2Y, cartaa2Img,
                      cartaa3X, cartaa3Y, cartaa3Img,
                      cartab1X, cartab1Y, cartab1Img,
                      cartab2X, cartab2Y, cartab2Img,
                      cartab3X, cartab3Y, cartab3Img,
                      cartac1X, cartac1Y, cartac1Img,
                      cartac2X, cartac2Y, cartac2Img,
                      cartac3X, cartac3Y, cartac3Img,
                      cartad1X, cartad1Y, cartad1Img,
                      cartad2X, cartad2Y, cartad2Img,
                      cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, deck,jogadad,truco,truco_txt,pontos1, pontos2):
    #jogadad1 = int(input("jogar carta 1, 2 ou 3"))
    #23
    font = pygame.font.Font("freesansbold.ttf",20)
    if sum(mn4)/len(mn4) > 23 and b == 1 and quempediu != 2 and valor == 1 :
        quempediu = 2
        truco = 1
        print("jogador D pediu truco")
        #aceita = int(input("jogador D pediu truco, cai ou sai?Para cair aperte 1 e enter para sair 2 e enter"))
        while truco == 1:
            #screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        truco = 0
                        aceita = 1
                
                    if event.key == pygame.K_n:
                        truco = 0
                        aceita = 2
            
            
            truco_txt = font.render("Dupla 2 pediu truco, para aceitar aperte s para sair aperte n",True,(255,255,255))
    
       
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if aceita == 1:
            valor = 3
            print("inicio",valor)
            while aceita == 1:
                truco = 1
                truco_txt = font.render("Dupla 1 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                aceita = 3
        else:
            if aceita == 2:
                jogadad1 = 0
                print("Dupla 1 saiu")
                saiu = 0
                quempediu = 2
                b = 2
                while aceita == 2:
                    truco = 1
                    truco_txt = font.render("Dupla 1 saiu.Dupla 2 ganhou !",True,(255,255,255))
                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                    sleep(3)
                    truco = 0
                    aceita = 3
    if sum(mn4)/len(mn4) > 33 and b == 1 and quempediu != 2 and valor != 1 :
        quempediu = 2
        #33
        print("jogador D pediu",valor+3)
        valorstr = str(valor + 3)
        truco = 1
        #aceita = int(input("jogador D pediu "+ valorstr+" cai ou sai?Para cair aperte 1 e enter para sair 2 e enter"))
        while truco == 1:
            #screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        truco = 0
                        aceita = 1
                
                    if event.key == pygame.K_n:
                        truco = 0
                        aceita = 2
            
            
            truco_txt = font.render("Dupla 2 pediu "+ valorstr+", para aceitar aperte s para sair aperte n",True,(255,255,255))
    
       
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if aceita == 1:
            valor = valor + 3
            while aceita == 1:
                truco = 1
                truco_txt = font.render("Dupla 1 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                aceita = 3
        else:
            if aceita == 2:
                print("Dupla 1 saiu")
                jogadad1 = 0
                saiu = 0
                quempediu = 2
                b = 2
                while aceita == 2:
                    truco = 1
                    truco_txt = font.render("Dupla 1 saiu.Dupla 2 ganhou !",True,(255,255,255))
                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                    sleep(3)
                    truco = 0
                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                    aceita = 3
    if saiu != 0:
        if len(mn4) == 3:
            if cb == 0 and ca == 0 and cc == 0:
                if mn4[0]>=mn4[1] and mn4[0]>= mn4[2]:
                    jogadad1 = 1
                if mn4[1]>=mn4[2] and mn4[1]>= mn4[0]:
                    jogadad1 = 2
                if mn4[2]>=mn4[1] and mn4[2]>= mn4[0]:
                    jogadad1 = 3
            else:
                if cb<= ca or cb <= cc:
                    if cartad[0] > ca and cartad[0] > cc and cartad[1] > ca and cartad[1] > cc and cartad[2] > ca and cartad[2]> cc:
                        if mn4[0]<=mn4[1] and mn4[0]<= mn4[2]:
                            jogadad1 = 1
                        if mn4[1]<=mn4[2] and mn4[1]<= mn4[0]:
                            jogadad1 = 2
                        if mn4[2]<=mn4[1] and mn4[2]<= mn4[0]:
                            jogadad1 = 3
                    else :
                        if cartad[0] > ca and cartad[0] > cc and cartad[1] > ca and cartad[1] > cc:
                            if mn4[0]<=mn4[1] :
                                jogadad1 = 1
                            if mn4[1]<=mn4[0] :
                                jogadad1 = 2
                        else:
                            if cartad[0] > ca and cartad[0] > cc and cartad[2] > ca and cartad[2] > cc:
                                if mn4[0]<=mn4[2] :
                                    jogadad1 = 1
                                if mn4[2]<=mn4[0] :
                                    jogadad1 = 3
                            else:
                                if cartad[2] > ca and cartad[2] > cc and cartad[1] > ca and cartad[1] > cc:
                                    if mn4[2]<=mn4[1] :
                                        jogadad1 = 3
                                    if mn4[1]<=mn4[2] :
                                        jogadad1 = 2
                                else:
                                    if cartad[0] >= ca and cartad[0] >= cc:
                                        jogadad1 = 1
                                    else:
                                        if cartad[1] >= ca and cartad[1] >= cc:
                                            jogadad1 = 2
                                        else:
                                            if cartad[2] >= ca and cartad[2] >= cc:
                                                jogadad1 = 3
                                            else:
                                                if mn4[0]<=mn4[1] and mn4[0]<= mn4[2]:
                                                    jogadad1 = 1
                                                if mn4[1]<=mn4[2] and mn4[1]<= mn4[0]:
                                                    jogadad1 = 2
                                                if mn4[2]<=mn4[1] and mn4[2]<= mn4[0]:
                                                    jogadad1 = 3            
                else:
                    if mn4[0]<=mn4[1] and mn4[0]<= mn4[2]:
                        jogadad1 = 1
                    if mn4[1]<=mn4[2] and mn4[1]<= mn4[0]:
                        jogadad1 = 2
                    if mn4[2]<=mn4[1] and mn4[2]<= mn4[0]:
                        jogadad1 = 3
        if len (mn4) == 2:
            if cb == 0 and ca == 0 and cc == 0:
                if mn4[0]>=mn4[1] :
                    jogadad1 = 1
                if mn4[1]>= mn4[0]:
                    jogadad1 = 2
            else:
                if cb<= ca or cb <= cc:
                    if cartad[0] > ca and cartad[0] > cc and cartad[1] > ca and cartad[1] > cc:
                        if mn4[0]<=mn4[1] :
                            jogadad1 = 1
                        if mn4[1]<=mn4[0] :
                            jogadad1 = 2
                    else:
                        if cartad[0] >= ca and cartad[0] >= cc:
                            jogadad1 = 1
                        else:
                            if cartad[1] >= ca and cartad[1] >= cc:
                                jogadad1 = 2
                            else:
                                if mn4[0]<=mn4[1] :
                                    jogadad1 = 1
                                if mn4[1]<=mn4[0] :
                                    jogadad1 = 2
                else:
                    if mn4[0]<=mn4[1] :
                        jogadad1 = 1
                    if mn4[1]<=mn4[0] :
                        jogadad1 = 2
        
        if len(mn4) == 1:
            jogadad1 = 1
        
        jogadad.append(jogadad1)    
    
        
        
        if len(jogadad) == 1:
            if jogadad[0] == 1:
                cartad1Img = cartas[mn4[0]]
            
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad1Img = pygame.transform.scale(cartad1Img,DEFAULT_IMAGE_SIZE)
                cartad1Img = pygame.transform.rotate(cartad1Img,90)
                cartad1X = 340
                cartab1Y = 280
            
            
            
            
            if jogadad[0] == 2:
                cartad2Img = cartas[mn4[1]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
                cartad2Img = pygame.transform.rotate(cartad2Img,90)
                cartad2X = 340
                cartad2Y = 280

            
            
            if jogadad[0] == 3:
                cartad3Img = cartas[mn4[2]]
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad3Img = pygame.transform.scale(cartad3Img,DEFAULT_IMAGE_SIZE)
                cartad3Img = pygame.transform.rotate(cartad3Img,90)
                cartad3X = 340
                cartad3Y = 280
        if len(jogadad) == 2:
            if jogadad[0] == 1 and jogadad[1] == 1:
                cartad2Img = cartas[mn4[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
                cartad2Img = pygame.transform.rotate(cartad2Img,90)
                cartad2X = 340
                cartad2Y = 280
            if (jogadad[0] == 1 or jogadad[0] == 2) and jogadad[1] == 2:
                cartad3Img = cartas[mn4[1]]
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad3Img = pygame.transform.scale(cartad3Img,DEFAULT_IMAGE_SIZE)
                cartad3Img = pygame.transform.rotate(cartad3Img,90)
                cartad3X = 340
                cartad3Y = 280
            if (jogadad[0] == 2 or jogadad[0] == 3) and jogadad[1] == 1:
                cartad1Img = cartas[mn4[0]]
            
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad1Img = pygame.transform.scale(cartad1Img,DEFAULT_IMAGE_SIZE)
                cartad1Img = pygame.transform.rotate(cartad1Img,90)
                cartad1X = 340
                cartad1Y = 280
            if jogadad[0] == 3 and jogadad[1] == 2:
                cartad2Img = cartas[mn4[1]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
                cartad2Img = pygame.transform.rotate(cartad2Img,90)
                cartad2X = 340
                cartad2Y = 280
        if len(jogadad) == 3:
            if (jogadad[0] == 1 or jogadad[0] == 2) and jogadad[1] == 1:
                cartad3Img = cartas[mn4[0]]
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad3Img = pygame.transform.scale(cartad3Img,DEFAULT_IMAGE_SIZE)
                cartad3Img = pygame.transform.rotate(cartad3Img,90)
                cartad3X = 340
                cartad3Y = 280
            if jogadad[0] == 1 and jogadad[1] == 2:
                cartad2Img = cartas[mn4[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
                cartad2Img = pygame.transform.rotate(cartad2Img,90)
                cartad2X = 340
                cartad2Y = 280
            if (jogadad[0] == 2 or jogadad[0] == 3) and jogadad[1] == 2:
                cartad1Img = cartas[mn4[0]]
            
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad1Img = pygame.transform.scale(cartad1Img,DEFAULT_IMAGE_SIZE)
                cartad1Img = pygame.transform.rotate(cartad1Img,90)
                cartad1X = 340
                cartad1Y = 280
            if jogadad[0] == 3 and jogadad[1] == 1:
                cartad2Img = cartas[mn4[0]]
                
                DEFAULT_IMAGE_SIZE = (60,87)

                cartad2Img = pygame.transform.scale(cartad2Img,DEFAULT_IMAGE_SIZE)
                cartad2Img = pygame.transform.rotate(cartad2Img,90)
                cartad2X = 340
                cartad2Y = 280
                
            
        print("valor= ",valor)
       
        if jogadad1 == 1:
                
            cd = cartad[0]
            print("Jogador D jogou",mao4[0])
                
            mao4 [0] = "erro tente novamente"
            del mao4[0]
            del cartad[0]
            del mn4[0]
            
        if jogadad1 == 2:
            cd = cartad[1]    
            
            print("Jogador D jogou",mao4[1])
            del mao4[1]
            del cartad[1]
            del mn4[1]
        if jogadad1 == 3:
                
            cd = cartad[2]
            
            print("Jogador D jogou",mao4[2])
            mao4 [2] = "erro tente novamente"
            del mao4[2]
            del cartad[2]
            del mn4[2]
        print(cd)
        deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)

       
    return cd, mao4, mn4,valor, quempediu,b,saiu,cartad1Img,cartad1X,cartad1Y,cartad2Img,cartad2X,cartad2Y,cartad3Img,cartad3X,cartad3Y,deck,jogadad1,jogadad,truco_txt
def trucoA(mn2, mn4, valor, saiu, a,ca,cb ,cc, cd,e,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2):
    font = pygame.font.Font("freesansbold.ttf",20)
    
    jogadaa1 = 0
    tamanhob = len(mn2)
    tamanhod = len(mn4)
    if tamanhob == 0:
        tamanhob = 1
    if tamanhod == 0:
        tamanhod = 1
    somab = sum(mn2)/tamanhob
    somad = sum(mn4)/tamanhod
    if e == "a":
        somab = sum(mn2)/tamanhob
        somad = sum(mn4)/tamanhod
    if e == "b":
        somab = (sum(mn2)+cb)/tamanhob
        somad = (sum(mn4)+cd)/tamanhod
    if e == "c":
        somab = (sum(mn2))/tamanhob
        somad = (sum(mn4)+cd)/tamanhod
    if e == "d":
        somab = (sum(mn2))/tamanhob
        somad = (sum(mn4)+cd)/tamanhod
    x = 1
    while x == 1:
        truco = 1
        valorstr = str(valor + 3)
        if valor == 1: 
            truco_txt = font.render("Dupla 1 pediu truco !",True,(255,255,255))
            print(valor)
        else:
            truco_txt = font.render("Dupla 1 pediu "+valorstr,True,(255,255,255))
        deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                        cartaa1X, cartaa1Y, cartaa1Img,
                        cartaa2X, cartaa2Y, cartaa2Img,
                        cartaa3X, cartaa3Y, cartaa3Img,
                        cartab1X, cartab1Y, cartab1Img,
                        cartab2X, cartab2Y, cartab2Img,
                        cartab3X, cartab3Y, cartab3Img,
                        cartac1X, cartac1Y, cartac1Img,
                        cartac2X, cartac2Y, cartac2Img,
                        cartac3X, cartac3Y, cartac3Img,
                        cartad1X, cartad1Y, cartad1Img,
                        cartad2X, cartad2Y, cartad2Img,
                        cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        sleep(3)
        truco = 0
        x = 0
        
        
    if  valor == 1:
        if somab +somad > 46:
            #46
                
            quempediu = 1
                            
            truco = 1
            truco_txt = font.render("Dupla 2 cai !",True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            
            
            valor = 3
        else:
            print("Dupla 2 saiu")
            saiu = 0
            jogadaa1 = 0
            quempediu = 1
            a = 2
            truco = 1
            truco_txt = font.render("Dupla 2 saiu.Dupla 1 ganhou !",True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
    else:
                       
        if somab + somad > 56 :
            #56
            quempediu = 1
            valor = valor + 3
            truco = 1
            truco_txt = font.render("Dupla 2 cai !",True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            
            
            
                
                                        
            
        else:
            print("Dupla 2 saiu")
            saiu = 0
            jogadaa1 = 0
            quempediu = 1
            a = 2
            truco = 1
            truco_txt = font.render("Dupla 2 saiu.Dupla 1 ganhou !",True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            
            
            
    return valor, quempediu, saiu, a,jogadaa1
def trucoB(mn2,b,valor,saiu,quempediu,cb,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2):
    font = pygame.font.Font("freesansbold.ttf",20)
    cb = 0
    aceita = 0
    if sum(mn2)/len(mn2) > 30 and b == 1 and quempediu != 2 and valor == 1 :
        quempediu = 2
        truco = 1
            
        print("jogador B pediu truco")
        #aceita = int(input("jogadorB pediu truco, cai ou sai?Para cair aperte 1 e enter para sair 2 e enter"))
        while truco == 1:
            #screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        truco = 0
                        aceita = 1
                
                    if event.key == pygame.K_n:
                        truco = 0
                        aceita = 2
            
            
            truco_txt = font.render("Dupla 2 pediu truco, para aceitar aperte s para sair aperte n",True,(255,255,255))
    
       
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if aceita == 1:
            valor = 3
            print("inicio",valor)
            while aceita == 1:
                truco = 1
                truco_txt = font.render("Dupla 1 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                aceita = 3
        else:
            if aceita == 2:
                print("Dupla 1 saiu")
                saiu = 0
                quempediu = 2
                b = 2
                while aceita == 2:
                    truco = 1
                    truco_txt = font.render("Dupla 1 saiu.Dupla 2 ganhou !",True,(255,255,255))
                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                    sleep(3)
                    truco = 0
                    aceita = 3
    if sum(mn2)/len(mn2) > 33 and b == 1 and quempediu != 2 and valor != 1 :
        #33
        quempediu = 2
        truco = 2
        print("jogador B pediu",valor+3)
        valorstr = str(valor + 3)
        #aceita = int(input("jogador B pediu "+ valorstr+" cai ou sai?Para cair aperte 1 e enter para sair 2 e enter"))
        while truco == 2:
            #screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        truco = 0
                        aceita = 1
                
                    if event.key == pygame.K_n:
                        truco = 0
                        aceita = 2
            
            
            truco_txt = font.render( "jogador B pediu "+ valorstr+" cai ou sai?Para cair aperte s para sair n e enter",True,(255,255,255))
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
        if aceita == 1:
            valor = valor + 3
            while aceita == 1:
                truco = 1
                truco_txt = font.render("Dupla 1 cai !",True,(255,255,255))
                deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                cartaa1X, cartaa1Y, cartaa1Img,
                                cartaa2X, cartaa2Y, cartaa2Img,
                                cartaa3X, cartaa3Y, cartaa3Img,
                                cartab1X, cartab1Y, cartab1Img,
                                cartab2X, cartab2Y, cartab2Img,
                                cartab3X, cartab3Y, cartab3Img,
                                cartac1X, cartac1Y, cartac1Img,
                                cartac2X, cartac2Y, cartac2Img,
                                cartac3X, cartac3Y, cartac3Img,
                                cartad1X, cartad1Y, cartad1Img,
                                cartad2X, cartad2Y, cartad2Img,
                                cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                sleep(3)
                truco = 0
                aceita = 3
             
        else:
            if aceita == 2:
                print("Dupla 1 saiu")
                saiu = 0
                quempediu = 2
                b = 2
                while aceita == 2:
                    truco = 1
                    truco_txt = font.render("Dupla 1 saiu.Dupla 2 ganhou !",True,(255,255,255))
                    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                                    cartaa1X, cartaa1Y, cartaa1Img,
                                    cartaa2X, cartaa2Y, cartaa2Img,
                                    cartaa3X, cartaa3Y, cartaa3Img,
                                    cartab1X, cartab1Y, cartab1Img,
                                    cartab2X, cartab2Y, cartab2Img,
                                    cartab3X, cartab3Y, cartab3Img,
                                    cartac1X, cartac1Y, cartac1Img,
                                    cartac2X, cartac2Y, cartac2Img,
                                    cartac3X, cartac3Y, cartac3Img,
                                    cartad1X, cartad1Y, cartad1Img,
                                    cartad2X, cartad2Y, cartad2Img,
                                    cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
                    sleep(3)
                    truco = 0
                    aceita = 3
                
    return quempediu, cb, valor, saiu, b, truco,aceita,truco_txt
        
def fimjogada(a,b,e,ca,cb,cc,cd,valor,quempediu,pontos1,pontos2,saiu,jogadaa1,jogadab1,jogadac1,jogadad1,deck,screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,jogadaa, jogadab,jogadac,jogadad,truco,truco_txt):
    if len(jogadaa) == 1:
        
        if jogadaa1 == 1:
            deck[0] = 1
        if jogadaa1 == 2:    
            deck[1] = 1
        if jogadaa1 == 3:
            deck[2] = 1
    if len(jogadaa) == 2:
        if jogadaa[0] == 1 and jogadaa[1] == 1:
            deck[1] = 1
            
        if (jogadaa[0] == 2 or jogadaa[0] == 3) and jogadaa[1] == 1:
            deck[0] = 1
            
        if (jogadaa[0] == 1 or jogadaa[0] == 2) and jogadaa[1] == 2:
            deck[2] = 1
                
        if jogadaa[0] == 3   and jogadaa[1] == 2:
            deck[1] = 1
    if len(jogadaa) == 3:
        if (jogadaa[0] == 1 or jogadaa[0] == 2) and jogadaa[1] == 1:
            deck[2] = 1
        if jogadaa[0] == 1 and jogadaa[1] == 2:
            deck[1] = 1
        if (jogadaa[0] == 2 or jogadaa[0] == 3) and jogadaa[1] == 2:
            deck[0] = 1
        if jogadaa[0] == 3 and jogadaa[1] == 1:
            deck[1] = 1
    if len(jogadab) == 1:
        if jogadab[0] == 1:
            deck[3] = 1
        if jogadab[0] == 2:
           deck[4] = 1 
        if jogadab[0] == 3:
            deck[5] = 1
    if len(jogadab) == 2:
        if jogadab[0] == 1 and jogadab[1] == 1:
            deck[4] = 1
        if (jogadab[0] == 1 or jogadab[0] == 2) and jogadab[1] == 2:
            deck[5] = 1
        if (jogadab[0] == 2 or jogadab[0] == 3) and jogadab[1] == 1:
            deck[3] = 1
        if jogadab[0] == 3 and jogadab[1] == 2:
            deck[4] = 1
    if len(jogadab) == 3:
        if (jogadab[0] == 1 or jogadab[0] == 2) and jogadab[1] == 1:
            deck[5] = 1
        if jogadab[0] == 1 and jogadab[1] == 2:
            deck[4] = 1
        if jogadab[0] == 2 or jogadab[0] == 3 and jogadab[1] == 2:
            deck[3] = 1
        if jogadab[0] == 3 and jogadab[1] == 1:
            deck[4] = 1
    if len(jogadac) == 1:
        if jogadac[0] == 1:
            deck[6] = 1
        if jogadac[0] == 2:
            deck[7] = 1
        if jogadac[0] == 3:
            deck[8] = 1
                
        

    if len(jogadac) == 2:
        if jogadac[0] == 1 and jogadac[1] == 1:
            deck[7] = 1
        if (jogadac[0] == 1 or jogadac[0] == 2) and jogadac[1] == 2:
            deck[8] = 1
        if (jogadac[0] == 2 or jogadac[0] == 3) and jogadac[1] == 1:
            deck[6] = 1
        if jogadac[0] == 3 and jogadac[1] == 2:
            deck[7] = 1
    if len(jogadac) == 3:
        if (jogadac[0] == 1 or jogadac[0] == 2) and jogadac[1] == 1:
            deck[8] = 1
        if jogadac[0] == 1 and jogadac[1] == 2:
            deck[7] = 1
        if jogadac[0] == 2 or jogadac[0] == 3 and jogadac[1] == 2:
            deck[6] = 1
        if jogadac[0] == 3 and jogadac[1] == 1:
            deck[7] = 1
    if len(jogadad) == 1:
        if jogadad[0] == 1:
            deck[9] = 1
            
        if jogadad[0] == 2:
            deck[10] = 1

            
            
        if jogadad[0] == 3:
            deck[11] = 1
    if len(jogadad) == 2:
        if jogadad[0] == 1 and jogadad[1] == 1:
            deck[10] = 1
        if (jogadad[0] == 1 or jogadad[0] == 2) and jogadad[1] == 2:
            deck[11] = 1
        if (jogadad[0] == 2 or jogadad[0] == 3) and jogadad[1] == 1:
            deck[9] = 1
        if jogadad[0] == 3 and jogadad[1] == 2:
            deck[10] = 1
    if len(jogadad) == 3:
        if (jogadad[0] == 1 or jogadad[0] == 2) and jogadad[1] == 1:
            deck[11] = 1
        if jogadad[0] == 1 and jogadad[1] == 2:
            deck[10] = 1
        if (jogadad[0] == 2 or jogadad[0] == 3) and jogadad[1] == 2:
            deck[9] = 1
        if jogadad[0] == 3 and jogadad[1] == 1:
            deck[10] = 1
        
    
    print(deck)
    deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
cartaa1X, cartaa1Y, cartaa1Img,
cartaa2X, cartaa2Y, cartaa2Img,
cartaa3X, cartaa3Y, cartaa3Img,
cartab1X, cartab1Y, cartab1Img,
cartab2X, cartab2Y, cartab2Img,
cartab3X, cartab3Y, cartab3Img,
cartac1X, cartac1Y, cartac1Img,
cartac2X, cartac2Y, cartac2Img,
cartac3X, cartac3Y, cartac3Img,
cartad1X, cartad1Y, cartad1Img,
cartad2X, cartad2Y, cartad2Img,
cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
    font = pygame.font.Font("freesansbold.ttf",40)
            

    if quempediu == 1 and saiu == 0:
        pontos1 = pontos1 + 1
        
    else:
        if quempediu == 2 and saiu == 0:
            pontos2 = pontos2 + 1
            
        else:
            
            if ca > cb and ca > cc and ca> cd:
                print ("A ganhou")
                a = a + 1
                e = "a"
                truco_txt = font.render( "A ganhou",True,(255,255,255))
                print(a,b)
                
            if cb > ca and cb> cc and cb > cd:
                print ("B ganhou")
                b = b + 1
                e = "b"
                truco_txt = font.render( "b ganhou",True,(255,255,255))
                print(a,b)

                
            if cc >ca and cc > cb and cc> cd:
                print ("C ganhou")
                a = a + 1
                e = "c"
                truco_txt = font.render( "C ganhou",True,(255,255,255))
                print(a,b)       
                
            if cd > cb and cd> cc and cd > ca:
                print ("D ganhou")
                b = b + 1
                e = "d"
                truco_txt = font.render( "D ganhou",True,(255,255,255))
                print(a,b)        
                
            if ca == cc and ca > cb and ca > cd:
                print ("dupla 1 ganhou a rodada")
                a = a + 1
                print(a, b)
                truco_txt = font.render( "dupla 1 ganhou a rodada",True,(255,255,255))
                if e == "a"or e == "d":
                    e = "c"
                else:
                    if e == "b" or e == "c":
                        e = "a"
            if cb == cd and cb > ca and cb > cc:
                print ("dupla 1 ganhou a rodada")
                b = b + 1
                print(a, b)
                truco_txt = font.render( "dupla 1 ganhou a rodada",True,(255,255,255))
                if e == "a"or e == "b":
                    e = "d"
                else:
                    if e == "c" or e == "d":
                        e = "b"
                
            if ca == cb and ca > cc and ca > cd:
                print("Empate")
                a = a + 1
                b = b + 1
                i = 1
                truco_txt = font.render( "Empate",True,(255,255,255))
                print(a, b)
                if e == "a"or e == "c":
                    e = "b"
                else:
                    if e == "b" or e == "d":
                        e = "a"
                    
                
            if ca == cd and ca > cb and ca > cc:
                print("Empate")
                a = a + 1                         
                b = b + 1
                print(a, b)
                truco_txt = font.render( "Empate",True,(255,255,255))
                if e == "a"or e == "d":
                    e = "d"
                else:
                    if e == "b" or e == "c":
                        e = "a"
                
                
            if cc == cb and cc> ca and cc > cd:
                print("Empate")
                a = a + 1
                b = b + 1
                print(a, b)
                truco_txt = font.render( "Empate",True,(255,255,255))
                if e == "a"or e == "b" or e == "d":
                    e = "c"
                else:
                    if e == "c" :
                        e = "b"
                
            if cc == cd and cc > cb and cc > ca:
                print("Empate")
                a = a + 1
                b = b + 1
                print(a, b)
                truco_txt = font.render( "Empate",True,(255,255,255))
                                
                if e == "a"or e == "b" or e == "c":
                    e = "d"
                else:
                    if e == "c" :
                        e = "c"

            truco = 1                     
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            sleep(3)
            truco = 0
            deck = update_screen(screen, manilhaX, manilhaY, manilhaImg,
                            cartaa1X, cartaa1Y, cartaa1Img,
                            cartaa2X, cartaa2Y, cartaa2Img,
                            cartaa3X, cartaa3Y, cartaa3Img,
                            cartab1X, cartab1Y, cartab1Img,
                            cartab2X, cartab2Y, cartab2Img,
                            cartab3X, cartab3Y, cartab3Img,
                            cartac1X, cartac1Y, cartac1Img,
                            cartac2X, cartac2Y, cartac2Img,
                            cartac3X, cartac3Y, cartac3Img,
                            cartad1X, cartad1Y, cartad1Img,
                            cartad2X, cartad2Y, cartad2Img,
                            cartad3X, cartad3Y, cartad3Img, mao1, mao2, mao3, mao4,deck,truco,truco_txt,pontos1, pontos2)
            return a,b,e,deck
screen = partida()
            
