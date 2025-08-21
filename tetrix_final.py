import pygame
from time import sleep
import random

pygame.init()

screen = pygame.display.set_mode((250, 500))
background = pygame.image.load("2.png")
vari = {"blocoImg":[],"blocoX":[], "blocoY":[],"x":100,"y":0,"fim":1,"cont":0,"numalea":0,"neg2": 0,"neg3":0,"bloco":[],"neg4":0}
vari["numalea"] = random.randrange(0, 7)
t = 0
vira = 0
posicX = [0,25,50,75,100,125,150,175,200,225]
posicY = [500,500,500,500,500,500,500,500,500,500]
for vari1 in range(20):
    posicY.append(vari1*25)
    posicX.append(-25)
for vari2 in range(20):
    posicY.append(vari2*25)
    posicX.append(250)
neg = 0
altura = 0
compl = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qq = 0
def bloco1(vari,t,neg):
    
    vari["x"] = 100
    vari["y"]= -125
    for t in range(512):
        
        if vari["numalea"] == 0:
            
            vari["blocoImg"].append(pygame.image.load("1.png"))
            vari["blocoX"].append(vari["x"])
            vari["blocoY"].append(vari["y"])
        
            vari["y"] += 25
            if t % 4  == 3 and t != 0:
                vari["x"] = 100
                vari["y"] = -125
                vari["bloco"].append(vari["numalea"])
                vari["numalea"] = 1
        else:
            
            if vari["numalea"] == 1:
                
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                
                
                
            
                vari["y"] += 25
                if t % 4 == 1:
                    vari["x"] -= 25
                    vari["y"] -= 25
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                    vari["bloco"].append(vari["numalea"])
                    vari["numalea"] = 0
            elif vari["numalea"] == 2:
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                vari["y"] += 25
                if t % 4 == 1:
                    vari["x"] +=25
                    vari["y"] -= 25
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                        
                    vari["bloco"].append(vari["numalea"])
                    
            elif vari["numalea"] == 3:
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                vari["y"] += 25
                if t % 4 == 0:
                    vari["x"] +=25
                    vari["y"] -= 25
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                        
                    vari["bloco"].append(vari["numalea"])
                    
            elif vari["numalea"] == 4:
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                vari["y"] += 25
                if t % 4 == 0:
                    vari["x"] -=25
                    vari["y"] -= 25
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                        
                    vari["bloco"].append(vari["numalea"])
                    
            elif vari["numalea"] == 5:
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                vari["y"] += 25
                if t % 4 == 1:
                    vari["x"] -=25
                    vari["y"] -= 25
                if t % 4 == 2:
                    vari["x"] += 50
                    vari["y"] -= 25
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                    
                    vari["bloco"].append(vari["numalea"])
                    
            elif vari["numalea"] == 6:
                vari["blocoImg"].append(pygame.image.load("1.png"))
                vari["blocoX"].append(vari["x"])
                vari["blocoY"].append(vari["y"])
                
                if t % 4 == 0:
                    vari["x"] +=25
                    
                if t % 4 == 1:
                    
                    vari["y"] += 25
                if t % 4 == 2:
                    vari["x"] -=25
                    
                if t % 4  == 3 and t != 0:
                    vari["y"] = -125
                    vari["x"] = 100
                        
                    vari["bloco"].append(vari["numalea"])
                    
        if t % 4  == 3 and t != 0:
            vari["numalea"] = random.randrange(0, 7)
            
            
                
            
    
    vari["cont"] += 4
    for i in range(vari["cont"] - 4, vari["cont"]):
        vari["blocoY"][i] += 125 
    neg = 0
    vari["neg2"] = 0
    return vari,t,neg

def bloco(vari,t,neg):
    if vari["fim"] == 1:    
    

        
            
        vari["fim"] = 0
        
        
        
        
            
        vari,t,neg = bloco1(vari,t,neg)
        
           
           
            
            
            
            
                
           
        
    screen.blit(vari["blocoImg"][t], (vari["blocoX"][t], vari["blocoY"][t]))
    return vari,t,neg
def bloco1_change(vari,v,vira):
    
    if v % 4 == 0:
        vira += 1
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 3]
        
        
            
        vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ]+ 25 - (25*(v % 4))
        
            
    if vira == 2:
        vari["blocoX"][v] = vari["blocoX"][vari["cont"]-3]
        if v % 4 == 0:
            
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 4] - 25
            
            
            
        else:
            
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 3] + 25*((v%4)-1)
            
        vari["blocoX"][v] = vari["blocoX"][vari["cont"] - 4]
    if vira == 3:

        vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 3]
        
            
        vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ]- 25 + 25*(v % 4)
    if vira == 0:
        vari["blocoX"][v] = vari["blocoX"][vari["cont"]-3]
        if v % 4 == 0:
            
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 4] - 25
            
            
        else:
            
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] - 3] + 25*((v%4)-1)
        vari["blocoX"][v] = vari["blocoX"][vari["cont"] - 4]
    return vira,vari
            
def bloco2_change(vari,vira,v):
    if v % 4 == 0:
        vira += 1
        #print("tttttt")
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 50
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] + 25
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 25
        
        
            
    if vira == 2:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] -25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] 
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] -25
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ]  - 25

    if vira == 3:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ]
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 50
    if vira == 0:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ]
        
    return vira,vari
def bloco3_change(vari,vira,v):
    if v % 4 == 0:
        vira += 1
        #print("tttttt")
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25 
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] 
        
        
            
    if vira == 2:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] -25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 50

    if vira == 3:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] 
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] + 25 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
    if vira == 0:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 50
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] - 25
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
        
    return vira,vari
def bloco4_change(vari,vira,v):
    if v % 4 == 0:
        vira += 1
        #print("tttttt")
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ]  
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] + 25
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 25
        
        
            
    if vira == 2:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 50

    if vira == 3:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] 
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] - 25 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
    if vira == 0:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 50
        
    return vira,vari
def bloco5_change(vari,vira,v):
    if v % 4 == 0:
        vira += 1
        #print("tttttt")
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 50
        
        
            
    if vira == 2:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] 
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] + 25
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 25

    if vira == 3:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] - 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ]  
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 50
    if vira == 0:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ]
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ]
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] - 25 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] 
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 50
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
        
    return vira,vari
def bloco6_change(vari,vira,v):
    if v % 4 == 0:
        vira += 1
        #print("tttttt")
        
        if vira == 4:
            vira = 0
    
    if vira == 1:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
        
        
            
    if vira == 2:
        
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] + 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ] 
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 25

    if vira == 3:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ] 
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ]  
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] + 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] - 25
    if vira == 0:
        if v % 4 == 0:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -4 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -4 ] - 25
        if v % 4 == 1:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -3 ]
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -3 ]  
        
        if v % 4 == 2:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -2 ] - 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -2 ] - 25
        if v % 4 == 3:
            vari["blocoX"][v] = vari["blocoX"][vari["cont"] -1 ] + 25
            vari["blocoY"][v] = vari["blocoY"][vari["cont"] -1 ] + 25
        
    return vira,vari
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if vari["blocoY"][vari["cont"]-1] != 475:
                    
                    for q in range (vari["cont"] - 4,vari["cont"]):
                        
                        vari["blocoX"][q] -= 25
                        
                        for vari3 in range(len(posicY)):
                            
                            if int(vari["blocoY"][q]) - (int(vari["blocoY"][q])%25)+ 25  == posicY[vari3]:
                                if int(vari["blocoX"][q])-(int(vari["blocoX"][q])%25) == posicX[vari3]:
                                    
                                    for vari4 in range (vari["cont"] - 4,vari["cont"]):
                                        vari["blocoX"][vari4] += 25        
                                        
                            
            if event.key == pygame.K_RIGHT:
                if vari["blocoY"][vari["cont"]-1] != 475:
                    
                    for q in range (vari["cont"] - 4,vari["cont"]):
                        
                        vari["blocoX"][q] += 25
                        
                        for vari3 in range(len(posicY)):
                            
                            if int(vari["blocoY"][q]) - (int(vari["blocoY"][q])%25)+ 25  == posicY[vari3]:
                                if int(vari["blocoX"][q])-(int(vari["blocoX"][q])%25) == posicX[vari3]:
                                    
                                    for vari4 in range (vari["cont"] - 4,vari["cont"]):
                                        vari["blocoX"][vari4] -= 25        
                                        

            if event.key == pygame.K_DOWN:
                for g in range (vari["cont"] - 4,vari["cont"]):
                    for qq in range(len(posicX)):
                        
                                    
                        if  int(vari["blocoX"][g]) == posicX[qq] and int(vari["blocoY"][g]) >= posicY[qq] - 50:
                            
                            vari["neg2"] = 1
                            
                                        
                                      
                for gg in range (vari["cont"] - 4,vari["cont"]):
                    if vari["neg2"] == 0:
                        vari["blocoY"][gg] += 25
                    
                            
                            
            if event.key == pygame.K_UP:
                
                if vari["fim"] == 0:
                    for v in range (vari["cont"] - 4,vari["cont"]):
                        if vari["bloco"][(vari["cont"] //4) - 1] == 0:
                            vira,vari = bloco1_change(vari,v,vira)
                        if vari["bloco"][(vari["cont"] //4) - 1] == 1:
                            vira,vari = bloco2_change(vari,vira,v)
                        if vari["bloco"][(vari["cont"] //4) - 1] == 2:
                            vira,vari = bloco3_change(vari,vira,v)
                        if vari["bloco"][(vari["cont"] //4) - 1] == 3:
                            vira,vari = bloco4_change(vari,vira,v)
                        if vari["bloco"][(vari["cont"] //4) - 1] == 4:
                            vira,vari = bloco5_change(vari,vira,v)
                        if vari["bloco"][(vari["cont"] //4) - 1] == 5:
                            vira,vari = bloco6_change(vari,vira,v)
                    for v in range(vari["cont"] - 4,vari["cont"]):
                        
                        for vari7 in range(len(posicY)):
                            
                            if int(vari["blocoX"][v]) == posicX[vari7] and (int(vari["blocoY"][v])) - ((int(vari["blocoY"][v])% 25)) == posicY[vari7]- 25:
                                for t in range(3):
                                    for v in range(vari["cont"] - 4,vari["cont"]):
                                        
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 0:
                                            
                                            vira,vari = bloco1_change(vari,v,vira)
                                            
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 1:
                                            vira,vari = bloco2_change(vari,vira,v)
                                            
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 2:
                                            vira,vari = bloco3_change(vari,vira,v)
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 3:
                                            vira,vari = bloco4_change(vari,vira,v)
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 4:
                                            vira,vari = bloco5_change(vari,vira,v)
                                        if vari["bloco"][(vari["cont"] //4) - 1] == 5:
                                            vira,vari = bloco6_change(vari,vira,v)
                        

                
                vari["neg3"] = 0
                                    
        
    
        
            

    
    for t in range(512):
        
        vari,t,neg = bloco(vari,t,neg)
        
                        
    r = 0
    for vari9 in range(len(posicY)):
        if posicY[vari9] < 0:
            running = False
    for r in range(vari["cont"] - 4,vari["cont"]):
        for tt in range(len(posicX)):
            
            if int(vari["blocoX"][r]) == posicX[tt] and int(vari["blocoY"][r]) == posicY[tt] - 25:
                neg = 1
        if neg == 0:
            vari["blocoY"][r] += 0.03
    
    if neg == 1:
        for rr in range(vari["cont"] - 4,vari["cont"]):
                
                
            
            posicY.append(int(vari["blocoY"][rr]))
            posicX.append(int(vari["blocoX"][rr]))
            
        qq += 1
        vari["fim"] = 1
        vira = 0
        
    
    qqq = 19
    ttt = 0
    if neg == 1:            
        while qqq >= 0:
            
            for www in range(len(posicX)):
                if posicY[www] == qqq*25:
                    if posicY[www] == 475:
                        ttt += 1
                        
                    for qw in range(10):
                        if posicX[www] == 25*qw:
                            
                            
                            compl[qqq] += 1
                        
            if compl[qqq] == 10:
               
                for z in range(len(posicX)):
                    
                    if posicY[z] == qqq * 25:
                        
                        vari["blocoY"][z - 50] = 525
                        posicY[z] = 525
                        
                        altura = qqq * 25
                        vari["neg4"] = 1
                        
                            
                for z in range(len(posicX)):
                    if vari["blocoY"][z - 50] < altura and z >= 50:
                        vari["blocoY"][z - 50] += 25
                        posicY[z] += 25
                                                
                    if z == len(posicX) - 1:
                        qqq = qqq + 1
                        
                        for ty in range(20):
                            compl[ty] = 0
                    
                
                    
            qqq -= 1
        qqq = 19
        
        
        vari["neg4"] = 0
        
                
    for ty in range(20):
        compl[ty] = 0
                
                        
        
        
        
           
        
    pygame.display.update()

pygame.display.quit()
pygame.quit()
