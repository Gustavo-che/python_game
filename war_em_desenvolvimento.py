import pygame
import random
import copy
from time import sleep
pygame.init()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# 0 = alascax 1 = alascay mackenzie = 2 "VancouverX"= 4 "OttawaX" = 6 "LabradorX" = 8 "GroelandiaX" = 10 nova york = 12 california = 14 mexico = 16 venezuela = 18 "BrasilX" = 20 "PeruX" = 22 "ArgentinaX" = 24 "ArgeliaX" = 26 "EgitoX" = 28 "SudaoX" = 30 "CongoX" = 32 "Africa do SulX" = 34 "MadagascarX" = 36 "IslandiaX" = 38 "InglaterraX" = 40 "FrancaX" = 42 "AlemanhaX" = 44 "PoloniaX" = 46 "MoscouX" = 48 "SueciaX" = 50 "Oriente MedioX" = 52 "IndiaX" = 54 "AralX" = 56 "OmskX" = 58 "DudinkaX" = 60 "SiberiaX" = 62 "TchitaX" = 64 "MongoliaX" = 66 "ChinaX" = 68 "VietnaX" = 70 "JapaoX" = 72 "VladisvotokX" = 74 "SumatraX = 76 "BorneuX" = 78 "Nova GuineaX" = 80 "AustraliaX" = 82 
screen = pygame.display.set_mode((1200,600))
vari2 = {"exerc_am":0,"exerc_as":0,"exerc_af":0,"exerc_eu":0,"exerc_asi":0,"exerc_oc":0,"america_do_norte":{0:0,1:0,2:0,3:0,4:0,5:0},"america_do_sul":{0:0,1:0,2:0,3:0,4:0,5:0},"africa":{0:0,1:0,2:0,3:0,4:0,5:0},"europa":{0:0,1:0,2:0,3:0,4:0,5:0},"asia":{0:0,1:0,2:0,3:0,4:0,5:0},"oceania":{0:0,1:0,2:0,3:0,4:0,5:0}}


vari = {"run7":True,"run6":True,"prioridade":{0:[],1:[],2:[],3:[],4:[],5:[]},"running":False,"run5":False,"fim_do_jogo":False,"show_obj":False,"matou":{0:-1,1:-1,2:-1,3:-1,4:-1,5:-1},"obj_img":[],"objetivo":{0:0,1:0,2:0,3:0,4:0,5:0},"run4":False,"exerc_deslocado":[],"remanejo1":-1,"remanejo2":-1,"run3":False,"carta_troca":{0:[],1:[],2:[],3:[],4:[],5:[]},"troca":False,"cartas_pais":{0:[],1:[],2:[],3:[],4:[],5:[]},"show":False,"cartasown":{0:[],1:[],2:[],3:[],4:[],5:[]},"quadrado":[False,{0:0,1:0,2:0,3:0,4:0,5:0}],"circulo":[False,{0:0,1:0,2:0,3:0,4:0,5:0}],"triangulo":[False,{0:0,1:0,2:0,3:0,4:0,5:0}],"vitoria":0,"cartas":[],"ataqueacabou":False,"atacante_perdeu":0,"atacado_perdeu":0,"resultado":False,"alvo":False,"run2":True,"atacado":-1,"atacante":-1,"vezz":"","run1":True,"territorio":{0:[],1:[],2:[],3:[],4:[],5:[]},"result_luta":{0:[],1:[],2:[],3:[],},"rodada":0,"n":0,"cores":{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0},"quantidade_exerc":[],"mapaimg": pygame.image.load("mapawar.png"),"mapaX":0 ,"numjogad":0,"mapaY":0,0:{"pais":"Alasca","continente":"America do Norte","X":132,"Y":175,"limitX1":47,"limitX2":152,"limitY1":139,"limitY2":207,"fronteira":[37,2,1]},1:{"pais":"Mackenzie","continente":"America do Norte","X":251,"Y":177,"limitX1":172,"limitX2":285,"limitY1":147,"limitY2":187,"fronteira":[0,2,3,5]},2:{"pais":"Vancouver","continente":"America do Norte","X":238,"Y":221,"limitX1":156,"limitX2":249,"limitY1":193,"limitY2":233,"fronteira":[0,1,3,7]},3:{"pais":"Otawwa","continente":"America do Norte","X":309,"Y":228,"limitX1":251,"limitX2":315,"limitY1":199,"limitY2":235,"fronteira":[1,2,4,6,7]},4:{"pais":"Labrador","continente":"America do Norte","X":345,"Y":233,"limitX1":331,"limitX2":403,"limitY1":183,"limitY2":242,"fronteira":[3,5,6]},5:{"pais":"Groenlandia","continente":"America do Norte","X":438 ,"Y":142,"limitX1":379,"limitX2":495,"limitY1":66,"limitY2":171,"fronteira":[4,1,19]},6:{"pais":"Nova York","continente":"America do Norte","X":293  ,"Y":282,"limitX1":255,"limitX2":348,"limitY1":249,"limitY2":296,"fronteira":[7,3,4,8]},7:{"pais":"Calfornia","continente":"America do Norte","X":261,"Y":257,"limitX1":177,"limitX2":286,"limitY1":231,"limitY2":281,"fronteira":[2,3,6,8]},8:{"pais":"Mexico","continente":"America do Norte","X":271,"Y":317,"limitX1":228,"limitX2":317,"limitY1":297,"limitY2":341,"fronteira":[6,7,9]},9:{"pais":"Venezuela","continente":"America do Sul","X":375,"Y":342,"limitX1":319,"limitX2":389,"limitY1":333,"limitY2":359,"fronteira":[8,10,11]},10:{"pais":"Brasil","continente":"America do Sul","X":443,"Y":393,"limitX1":387,"limitX2":468,"limitY1":356,"limitY2":447,"fronteira":[9,11,12,13]},11:{"pais":"Peru","continente":"America do Sul","X":328,"Y":391,"limitX1":309,"limitX2":377,"limitY1":395,"limitY2":434,"fronteira":[10,12,9]},12:{"pais":"Argentina","continente":"America do Sul","X":371,"Y":425,"limitX1":353,"limitX2":395,"limitY1":416,"limitY2":525,"fronteira":[10,11]},13:{"pais":"Argelia","continente":"Africa","X":569,"Y":285,"limitX1":512,"limitX2":615,"limitY1":270,"limitY2":339,"fronteira":[10,14,15,16,21]},14:{"pais":"Egito","continente":"Africa","X":660,"Y":289,"limitX1":609,"limitX2":679,"limitY1":281,"limitY2":306,"fronteira":[13,15,21,23,26]},15:{"pais":"Sudao","continente":"Africa","X":684,"Y":333,"limitX1":623,"limitX2":707,"limitY1":304,"limitY2":355,"fronteira":[13,14,16,18,17]},16:{"pais":"Congo","continente":"Africa","X":653,"Y":369,"limitX1":607,"limitX2":667,"limitY1":348,"limitY2":387,"fronteira":[15,13,17]},17:{"pais":"Africa do Sul","continente":"Africa","X":666,"Y":405,"limitX1":615,"limitX2":676,"limitY1":394,"limitY2":447,"fronteira":[15,16,18]},18:{"pais":"Madagascar","continente":"Africa","X":719,"Y":403,"limitX1":713,"limitX2":733,"limitY1":382,"limitY2":414,"fronteira":[15,17]},19:{"pais":"Islandia","continente":"Europa","X":505,"Y":169,"limitX1":485,"limitX2":521,"limitY1":162,"limitY2":181,"fronteira":[5,20]},20:{"pais":"Inglaterra","continente":"Europa","X":530,"Y":185,"limitX1":510,"limitX2":551,"limitY1":178,"limitY2":221,"fronteira":[19,21,22,25]},21:{"pais":"Franca","continente":"Europa","X":557,"Y":257,"limitX1":542,"limitX2":594,"limitY1":228,"limitY2":266,"fronteira":[20,22,13,14]},22:{"pais":"Alemanha","continente":"Europa","X":597,"Y":229,"limitX1":589,"limitX2":616,"limitY1":216,"limitY2":243,"fronteira":[20,21,23]},23:{"pais":"Polonia","continente":"Europa","X":626,"Y":223,"limitX1":621,"limitX2":647,"limitY1":215,"limitY2":260,"fronteira":[22,24,21,14,26]},24:{"pais":"Moscou","continente":"Europa","X":680,"Y":217,"limitX1":641,"limitX2":731,"limitY1":188,"limitY2":243,"fronteira":[23,25,26,28,29]},25:{"pais":"Suecia","continente":"Europa","X":616,"Y":168,"limitX1":601,"limitX2":665,"limitY1":141,"limitY2":192,"fronteira":[24,20]},26:{"pais":"Oriente Medio","continente":"Asia","X":699,"Y":291,"limitX1":680,"limitX2":757,"limitY1":253,"limitY2":322,"fronteira":[23,24,27,28,14]},27:{"pais":"India","continente":"Asia","X":785,"Y":283,"limitX1":774,"limitX2":834,"limitY1":271,"limitY2":333,"fronteira":[26,28,34,35,38]},28:{"pais":"Aral","continente":"Asia","X":779,"Y":251,"limitX1":742,"limitX2":827,"limitY1":224,"limitY2":263,"fronteira":[24,26,27,29,34]},29:{"pais":"Omsk","continente":"Asia","X":749,"Y":165,"limitX1":724,"limitX2":781,"limitY1":151,"limitY2":213,"fronteira":[24,28,30,34,33]},30:{"pais":"Dudinka","continente":"Asia","X":840,"Y":188,"limitX1":784,"limitX2":854,"limitY1":132,"limitY2":203,"fronteira":[29,33,31,32]},31:{"pais":"Siberia","continente":"Asia","X":927,"Y":161,"limitX1":847,"limitX2":961,"limitY1":81,"limitY2":184,"fronteira":[30,32,37]},32:{"pais":"Tchita","continente":"Asia","X":923,"Y":215,"limitX1":873,"limitX2":944,"limitY1":194,"limitY2":228,"fronteira":[30,33,34,31,37]},33:{"pais":"Mongolia","continente":"Asia","X":923,"Y":239,"limitX1":863,"limitX2":943,"limitY1":230,"limitY2":248,"fronteira":[29,30,34,32]},34:{"pais":"China","continente":"Asia","X":920,"Y":273,"limitX1":821,"limitX2":952,"limitY1":253,"limitY2":305,"fronteira":[35,27,28,29,33,36,37,32]},35:{"pais":"Vietna","continente":"Asia","X":906,"Y":327,"limitX1":877,"limitX2":919,"limitY1":308,"limitY2":351,"fronteira":[39,34,27]},36:{"pais":"Japao","continente":"Asia","X":1029,"Y":295,"limitX1":1001,"limitX2":1057,"limitY1":266,"limitY2":313,"fronteira":[34,37]},37:{"pais":"Vladisvotok","continente":"Asia","X":1083,"Y":156,"limitX1":983,"limitX2":1133,"limitY1":139,"limitY2":243,"fronteira":[0,34,36,31,32]},38:{"pais":"Sumatra","continente":"Oceania","X":915,"Y":411,"limitX1":880,"limitX2":947,"limitY1":385,"limitY2":426,"fronteira":[27,41]},39:{"pais":"Borneu","continente":"Oceania","X":978,"Y":378,"limitX1":947,"limitX2":1014,"limitY1":369,"limitY2":415,"fronteira":[41,40,35]},40:{"pais":"Nova Guinea","continente":"Oceania","X":1060,"Y":401,"limitX1":1031,"limitX2":1112,"limitY1":390,"limitY2":421,"fronteira":[41,39]},41:{"pais":"Australia","continente":"Oceania","X":1064,"Y":462,"limitX1":967,"limitX2":1107,"limitY1":425,"limitY2":513,"fronteira":[40,39,38]}}
        
troca = 4
x = []
y = 0
v = 0

while len(x) < 6 :
    b = random.randrange(1, 15)
    
    v += 1
    
    if (b in x) == False:
        
        x.append(b)
        vari["objetivo"][y] = b
        
        y +=1
print(vari["objetivo"])


        

        
        
    
for i in range(42):
    vari["exerc_deslocado"].append(0)
for i in range(42):
    if i % 3 == 0:
        vari["cartas"].append("Triangulo")
    if i % 3 == 1:
        vari["cartas"].append("Circulo")
    if i % 3 == 2:
        vari["cartas"].append("Quadrado")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
qnt_rodada = -1                                                                                                                                                                                                                                                                                                                                                                               
run = True


for e in range(42):
    vari["quantidade_exerc"].append(1)



vez = 0
corfinal = []
num = [0,1,2,3,4,5]
b = 0
c = 1
erase = [100]
cor = [pygame.image.load("preto.png"),pygame.image.load("azul.png"),pygame.image.load("red.png"),pygame.image.load("verde.png"),pygame.image.load("amarelo.png"),pygame.image.load("branco.png")]
num1 = []
erase1 = [100]
for i in range(42):
    num1.append(i)

for i in range(42):
    b = 0
    aleatorio = random.choice(num1)
    
    
                
            
    for t in range(len(erase1)):
        if aleatorio > erase1[t]:
            b += 1
            
            
    erase1.append(aleatorio)
                
            
    del num1[aleatorio - b]

    
b = 0
erase = [100]
num = []
b = 0
for e in range(42):
    num.append(e)
def objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2):
    
        
    
    for i in range(6):
        vari["territorio"][i] = []
        
        for t in range(42):
            
        
            if vari["cores"][t] == i:
                vari["territorio"][i].append(t)
                
        
        if vari["objetivo"][i] == 1:
            

            vari["obj_img"].append(pygame.image.load("obj_01.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(1)
            
            if vari["matou"][1] == i:
                vari["fim_do_jogo"] = True
                
            
            
                
            if i == 1 or (vari["matou"][1] != i and vari["matou"][1] != -1):
                
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
                    
        if vari["objetivo"][i] == 2:
            vari["obj_img"].append(pygame.image.load("obj_02.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(4)
            if vari["matou"][4] == i:
                vari["fim_do_jogo"] = True
            if i == 4 or (vari["matou"][4] != i and vari["matou"][4] != -1):
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
        if vari["objetivo"][i] == 3:
            vari["obj_img"].append(pygame.image.load("obj_03.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(5)
            if vari["matou"][5] == i:
                vari["fim_do_jogo"] = True
            if i == 5 or (vari["matou"][5] != i and vari["matou"][5] != -1):
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
        if vari["objetivo"][i] == 4:
            vari["obj_img"].append(pygame.image.load("obj_04.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(3)
            if vari["matou"][3] == i:
                vari["fim_do_jogo"] = True
            if i == 3 or (vari["matou"][3] != i and vari["matou"][3] != -1):
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
        if vari["objetivo"][i] == 5:
            vari["obj_img"].append(pygame.image.load("obj_05.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(0)
            
            if vari["matou"][0] == i:
                vari["fim_do_jogo"] = True
            if i == 0 or (vari["matou"][0] != i and vari["matou"][0] != -1):
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
        if vari["objetivo"][i] == 6:
            vari["obj_img"].append(pygame.image.load("obj_06.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append(2)
            if vari["matou"][2] == i:
                vari["fim_do_jogo"] = True
            if i == 2 or (vari["matou"][2] != i and vari["matou"][2] != -1):
                if len(vari["territorio"][i]) >= 24:
                    vari["fim_do_jogo"] = True
                    vez = i
        if vari["objetivo"][i] == 7:
            vari["obj_img"].append(pygame.image.load("obj_07.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("America do Norte")
                vari["prioridade"][i].append("Africa")
            
            if vari2["america_do_norte"][i] == 9 and vari2["africa"][i] == 6:
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 8:
            vari["obj_img"].append(pygame.image.load("obj_08.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("Africa")
                vari["prioridade"][i].append("Asia")
            if vari2["africa"][i] == 6 and vari2["asia"][i] == 12:
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 9:
            vari["obj_img"].append(pygame.image.load("obj_09.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("America do Norte")
                vari["prioridade"][i].append("Oceania")

            if vari2["america_do_norte"][i] == 9 and vari2["oceania"][i] == 4:
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 10:
            vari["obj_img"].append(pygame.image.load("obj_10.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("Europa")
                vari["prioridade"][i].append("America do Sul")

            if vari2["europa"][i] == 7 and vari2["america_do_sul"][i] == 4 and(vari2["oceania"][i] == 4 or vari2["america_do_norte"][i] == 9 or  vari2["africa"][i] == 6 or vari2["asia"][i] == 12):
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 11:
            vari["obj_img"].append(pygame.image.load("obj_11.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("America do Sul")
                vari["prioridade"][i].append("Asia")

            if vari2["asia"][i] == 12 and vari2["america_do_sul"][i] == 4:
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 12:
            vari["obj_img"].append(pygame.image.load("obj_12.png"))
            if vari["prioridade"][i] == []:
                vari["prioridade"][i].append("Europa")
                vari["prioridade"][i].append("Oceania")

            if vari2["europa"][i] == 7 and vari2["oceania"][i] == 4 and(vari2["america_do_sul"][i] == 4 or vari2["america_do_norte"][i] == 9 or  vari2["africa"][i] == 6 or vari2["asia"][i] == 12):
                vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 13:
            vari["obj_img"].append(pygame.image.load("obj_13.png"))
            
            total = 0
            if len(vari["territorio"][i])>= 18:
                for t in range(len(vari["territorio"][i])):
                    if vari["quantidade_exerc"][vari["territorio"][i][t]] >= 2:
                        total += 1
                if total >= 18:
                    
                    vari["fim_do_jogo"] = True
        if vari["objetivo"][i] == 14:
            vari["obj_img"].append(pygame.image.load("obj_14.png"))
            if len(vari["territorio"][i])>= 24:
                vari["fim_do_jogo"] = True
        vari["territorio"][i] = []            
        if vari["fim_do_jogo"] == True:
        
            vez = i
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
def batalha(vari,cor,vez,vari2):
    vari["run2"] = True
    atacante = vari["atacante"]
    atacado = vari["atacado"]
    vari["atacante_perdeu"] = 0
    vari["atacado_perdeu"] = 0
    ataque = []
    defesa = []
    i = 0
    
    
    if vari["cores"] [atacante] != vari["cores"][atacado] and vari["rodada"] // vari["numjogad"] >= 1:
        
        if vari["quantidade_exerc"][atacante]>= 4:
            qnt_ataq = 3
        else:
            qnt_ataq = vari["quantidade_exerc"][atacante] - 1
        for i in range(qnt_ataq):
            ataque.append(random.randrange(1, 7))
        ataque.sort()
        if vari["quantidade_exerc"][atacado]>= 3:
            qnt_def = 3
        else:
            qnt_def = vari["quantidade_exerc"][atacado]
        for i in range(qnt_def):
            defesa.append(random.randrange(1, 7))
        defesa.sort()
        
        if len(defesa) < len(ataque):
            qnt = len(defesa)
        else:
            qnt = len(ataque)
        for i in range(qnt):
            if ataque[-1 - i] > defesa[-1 - i]:
                vari["quantidade_exerc"][atacado] -= 1
                vari["atacado_perdeu"] += 1
            else:
                vari["quantidade_exerc"][atacante] -= 1
                vari["atacante_perdeu"] += 1
        vari["ataqueacabou"] = True
        
        
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        vari["run5"] = True
        while vari["run5"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vari["run4"] = False
                    vari["running"] = False
                    vari["run5"] = False
                    vari["run2"] = False
                    vari["troca"] = False
                    vari2["exerc_am"] = 0
                    vari2["exerc_as"] = 0
                    vari2["exerc_af"] = 0
                    vari2["exerc_asi"] = 0
                    vari2["exerc_eu"] = 0
                    vari2["exerc_oc"] = 0
                    vari["run1"] = False
                    vari["run3"] = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        vari["run5"] = False
        for t in range(6):
            vari["territorio"][t] = []
            for i in range(42):
            
                if vari["cores"][i] == t:
                    vari["territorio"][t].append(i)
        

        vari["ataqueacabou"] = False
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
            
        
        if vari["quantidade_exerc"][atacado] == 0:
            
            
            for i in range(42):
                if vari["cores"][i] == vari["cores"][atacado]:
                    vari["territorio"][vari["cores"][atacado]].append(i)
            
            if len(vari["territorio"][vari["cores"][atacado]]) == 1:
                vari["matou"][vari["cores"][atacado]] = vez
                
            vari["vitoria"] = 1
            vari["territorio"][vez].append(atacado)
            vari["territorio"][vari["cores"][atacado]] = []
            vari["cores"][atacado] = vari["cores"][atacante]
            vari["resultado"] = True
            
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            if vari["rodada"] % vari["numjogad"] == 0:
                
                while vari["run2"]:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vari["run4"] = False
                            vari["running"] = False
                            vari["run5"] = False
                            vari["run2"] = False
                            vari["troca"] = False
                            vari2["exerc_am"] = 0
                            vari2["exerc_as"] = 0
                            vari2["exerc_af"] = 0
                            vari2["exerc_asi"] = 0
                            vari2["exerc_eu"] = 0
                            vari2["exerc_oc"] = 0
                            vari["run1"] = False
                            vari["run3"] = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_3:
                                if vari["quantidade_exerc"][atacante] > 3:
                                    vari["quantidade_exerc"][atacante] -= 3
                                    vari["quantidade_exerc"][atacado] += 3
                                    vari["run2"] = False
                            if event.key == pygame.K_1:
                                
                                vari["quantidade_exerc"][atacante] -= 1
                                vari["quantidade_exerc"][atacado] += 1
                                vari["run2"] = False
                            if event.key == pygame.K_2:
                                if vari["quantidade_exerc"][atacante] > 2:
                                    vari["quantidade_exerc"][atacante] -= 2
                                    vari["quantidade_exerc"][atacado] += 2
                                    vari["run2"] = False
            else:
                vari["quantidade_exerc"][atacante] -= 1
                vari["quantidade_exerc"][atacado] += 1
                
                    
                
         #len(vari[territorio][vari["cores"][atacado]]) == 1   
            
            
            
            vari["n"] += 1
    vari["atacante"] = -1
    vari["atacado"] = -1
    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
def jogada(vari,corfinal,qnt_rodada,erase1,c,troca,vari2):
    pass
    i = 0
    
    
    vari["run1"] = True
    
    
    vari["run4"] = True
    if vari["numjogad"] > 0:
        
        vez = vari["rodada"] % vari["numjogad"]
        objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        print("vez",vez)
        if vez == 0:
            vari["vezz"] = "vez do exercito preto"
        if vez == 1:
            vari["vezz"] = "vez do exercito azul"
        if vez == 2:
            vari["vezz"] = "vez do exercito vermelho"
        if vez == 3:
            vari["vezz"] = "vez do exercito verde"
        if vez == 4:
            vari["vezz"] = "vez do exercito amarelo"
        if vez == 5:
            vari["vezz"] = "vez do exercito branco"
        vari["triangulo"][1][vez] = 0
        vari["circulo"][1][vez] = 0
        vari["quadrado"][1][vez] = 0
        for i in range(len(vari["cartasown"][vez])):
            if vari["cartasown"][vez][i] == "Triangulo":
                vari["triangulo"][1][vez] += 1
            if vari["cartasown"][vez][i] == "Circulo":
                vari["circulo"][1][vez] += 1
            if vari["cartasown"][vez][i] == "Quadrado":
                vari["quadrado"][1][vez] += 1
        if vari["triangulo"][1][vez] >= 3 or vari["circulo"][1][vez] >= 3 or vari["quadrado"][1][vez] >= 3 or(vari["triangulo"][1][vez] >= 1 and vari["circulo"][1][vez] >= 1 and vari["quadrado"][1][vez] >= 1) :
            vari["troca"] = True
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
        for t in range(6):
            vari["territorio"][t] = []
            for i in range(42):
            
                if vari["cores"][i] == t:
                    vari["territorio"][t].append(i)
        if len(vari["territorio"][vez]) > 5:
            qnt_rodada = len(vari["territorio"][vez])//2
        elif len(vari["territorio"][vez]) > 0:
            qnt_rodada = 3
        else:
            qnt_rodada = 0
        vari2 = {"exerc_am":0,"exerc_as":0,"exerc_af":0,"exerc_eu":0,"exerc_asi":0,"exerc_oc":0,"america_do_norte":{0:0,1:0,2:0,3:0,4:0,5:0},"america_do_sul":{0:0,1:0,2:0,3:0,4:0,5:0},"africa":{0:0,1:0,2:0,3:0,4:0,5:0},"europa":{0:0,1:0,2:0,3:0,4:0,5:0},"asia":{0:0,1:0,2:0,3:0,4:0,5:0},"oceania":{0:0,1:0,2:0,3:0,4:0,5:0}}
        for t in range(6):
            for i in range(len(vari["territorio"][t])):
                if vari[vari["territorio"][t][i]]["continente"] == "America do Norte":
                    vari2["america_do_norte"][t] += 1
                if vari[vari["territorio"][t][i]]["continente"] == "America do Sul":
                    vari2["america_do_sul"][t] += 1
                if vari[vari["territorio"][t][i]]["continente"] == "Africa":
                    vari2["africa"][t] += 1
                if vari[vari["territorio"][t][i]]["continente"] == "Europa":
                    vari2["europa"][t] += 1
                if vari[vari["territorio"][t][i]]["continente"] == "Asia":
                    vari2["asia"][t] += 1
                if vari[vari["territorio"][t][i]]["continente"] == "Oceania":
                    vari2["oceania"][t] += 1       
            
        
        vari["alvo"] = False
        vari["atacante"] = -1
        vari["atacado"] = -1
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
        
        while vari["troca"] == True:
            objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            for i in range(6):
                vari["territorio"][i] = []
            for i in range(42):
                
                if vari["cores"][i] == vez:
                    vari["territorio"][vez].append(i)
            if 1 == 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    
                
                    if event.type == pygame.KEYDOWN:
                        if 1 == 1:
                            if event.key == pygame.K_s:
                                print("yooooooooooooooo")
                                qnt_rodada += troca
                                
                                troca += 2
                                q = 3
                                i = 0
                                if vari["triangulo"][1][vez] >= 3:
                                    
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Triangulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["circulo"][1][vez] >= 3 and vari["troca"] == True:
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Circulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["quadrado"][1][vez] >= 3 and vari["troca"] == True:
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["triangulo"][1][vez] >= 1 and vari["circulo"][1][vez] >= 1 and vari["quadrado"][1][vez] >= 1 and vari["troca"] == True:
                                    q = 1
                                    ci = 1
                                    t = 1
                                    while q > 0:
                                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    i = 0
                                    while ci > 0:
                                        if ci > 0 and vari["cartasown"][vez][i] == "Circulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            ci -= 1
                                            i -= 1
                                        i += 1
                                    i = 0
                                    while t > 0:
                                        if t > 0 and vari["cartasown"][vez][i] == "Triangulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            t -= 1
                                            i -= 1
                                        i += 1
                                for i in range(len(vari["territorio"][vez])):
                                    for a in range(3):
                                        if vari["territorio"][vez][i] == vari["carta_troca"][vez][a]:
                                            vari["quantidade_exerc"][vari["territorio"][vez][i]] += 2
                                for i in range(6):
                                    vari["carta_troca"][i] = []
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                print(qnt_rodada,"rodadadadadadada")
                                vari["troca"] = False
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            if event.key == pygame.K_n:
                                vari["troca"] = False
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                

        if vari2["america_do_norte"][vez] == 9:
            vari2["exerc_am"] = 5
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            
            while vari2["exerc_am"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:  
                                if qnt_rodada > 0:
                                    for t in range(len(vari["territorio"][vez])):
                                            if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "America do Norte":
                                                vari["quantidade_exerc"][i] += 1
                                                vari2["exerc_am"] -= 1
                                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
        if vari2["america_do_sul"][vez] == 4:
            vari2["exerc_as"] = 2
            print("foi")
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            print("ainao")
            while vari2["exerc_as"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                for t in range(len(vari["territorio"][vez])):
                                    if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "America do Sul":
                                        vari["quantidade_exerc"][i] += 1
                                        vari2["exerc_as"] -= 1
                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        if vari2["africa"][vez] == 6:
            vari2["exerc_af"] = 3
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari2["exerc_af"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                for t in range(len(vari["territorio"][vez])):
                                    if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "Africa":
                                        vari["quantidade_exerc"][i] += 1
                                        vari2["exerc_af"] -= 1
                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        if vari2["europa"][vez] == 7:
            vari2["exerc_eu"] = 5
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari2["exerc_eu"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                for t in range(len(vari["territorio"][vez])):
                                    if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "Europa":
                                        vari["quantidade_exerc"][i] += 1
                                        vari2["exerc_eu"] -= 1
                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        if vari2["asia"][vez] == 12:
            vari2["exerc_asi"] = 7
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari2["exerc_asi"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                for t in range(len(vari["territorio"][vez])):
                                    if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "Asia":
                                        vari["quantidade_exerc"][i] += 1
                                        vari2["exerc_asi"] -= 1
                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        if vari2["oceania"][vez] == 4:
            vari2["exerc_oc"] = 2
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari2["exerc_oc"] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(42):
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                for t in range(len(vari["territorio"][vez])):
                                    if i == vari["territorio"][vez][t] and vari[vari["territorio"][vez][t]]["continente"] == "Oceania":
                                        vari["quantidade_exerc"][i] += 1
                                        vari2["exerc_oc"] -= 1
                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
            
        while vari["run1"]:
            vari2 = {"exerc_am":0,"exerc_as":0,"exerc_af":0,"exerc_eu":0,"exerc_asi":0,"exerc_oc":0,"america_do_norte":{0:0,1:0,2:0,3:0,4:0,5:0},"america_do_sul":{0:0,1:0,2:0,3:0,4:0,5:0},"africa":{0:0,1:0,2:0,3:0,4:0,5:0},"europa":{0:0,1:0,2:0,3:0,4:0,5:0},"asia":{0:0,1:0,2:0,3:0,4:0,5:0},"oceania":{0:0,1:0,2:0,3:0,4:0,5:0}}
            for t in range(6):
                for i in range(len(vari["territorio"][t])):
                    if vari[vari["territorio"][t][i]]["continente"] == "America do Norte":
                        vari2["america_do_norte"][t] += 1
                    if vari[vari["territorio"][t][i]]["continente"] == "America do Sul":
                        vari2["america_do_sul"][t] += 1
                    if vari[vari["territorio"][t][i]]["continente"] == "Africa":
                        vari2["africa"][t] += 1
                    if vari[vari["territorio"][t][i]]["continente"] == "Europa":
                        vari2["europa"][t] += 1
                    if vari[vari["territorio"][t][i]]["continente"] == "Asia":
                        vari2["asia"][t] += 1
                    if vari[vari["territorio"][t][i]]["continente"] == "Oceania":
                        vari2["oceania"][t] += 1
                
            objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            for i in range(6):
                vari["territorio"][i] = []
            for i in range(42):
                
                if vari["cores"][i] == vez:
                    vari["territorio"][vez].append(i)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vari["run4"] = False
                    vari["running"] = False
                    vari["run5"] = False
                    vari["run2"] = False
                    vari["troca"] = False
                    vari2["exerc_am"] = 0
                    vari2["exerc_as"] = 0
                    vari2["exerc_af"] = 0
                    vari2["exerc_asi"] = 0
                    vari2["exerc_eu"] = 0
                    vari2["exerc_oc"] = 0
                    vari["run1"] = False
                    vari["run3"] = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("heheheheh")
                        vari["show_obj"] = True
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        vari["show_obj"] = False                    
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                
                    

                if qnt_rodada > 0:
                    if vari["troca"] == False:
                    
                    
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            
                            for i in range(42):
                                
                                if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:  
                                    
                                    if qnt_rodada > 0 and vari["troca"] == False:
                                            
                                        for t in range(len(vari["territorio"][vez])):
                                            if i == vari["territorio"][vez][t]:
                                                vari["quantidade_exerc"][i] += 1
                                                qnt_rodada -= 1
                                                print(qnt_rodada,1)
                                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                elif qnt_rodada == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        for i in range(42):
                            
                            if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:  
                                if qnt_rodada == 0:
                                    print(i,"iiii")
                                    
                                    if vari["rodada"] // vari["numjogad"] > 0:
                                        if vari["atacado"] == -1  and vari["troca"] == False and qnt_rodada == 0 :
                                            for t in range(len(vari["territorio"][vez])):
                                                if i == vari["territorio"][vez][t] and vari["quantidade_exerc"][vari["territorio"][vez][t]] > 1:
                                                    vari["atacante"] = i
                                                    print(i,"atacante")
                                                    vari["alvo"] = True
                                                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                        if vari["atacante"] != -1:        
                                            for t in range(len(vari[vari["atacante"]]["fronteira"])):
                                                
                                                if i ==vari[vari["atacante"]]["fronteira"][t] and vari["cores"][i] != vari["cores"][vari["atacante"]]:
                                                    vari["atacado"] = vari[vari["atacante"]]["fronteira"][t]
                                                    print(vari["atacado"],"atacado")                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if qnt_rodada == 0:
                            vari["run1"] = False
                            vari["run3"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.key == pygame.K_z:
                        print("heyyyyyyyyyyyyyy")
                        vari["show"] = True
                        
                        
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        
                        vari["quadrado"][0] = False
                        vari["circulo"][0] = False
                        vari["triangulo"][0] = False
                        
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_z:
                        vari["show"] = False
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)


                #if event.type == pygame.KEYUP:
                 #   if event.key == pygame.K_a:
                  #      
                   #     vari["show_obj"] = False
                    #    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            
                    
                                
                if vari["troca"] == True:
                    
                    
                
                    if event.type == pygame.KEYDOWN:
                        if 1 == 1:
                            if event.key == pygame.K_s:
                                print("yooooooooooooooo")
                                qnt_rodada += troca
                                
                                troca += 2
                                q = 3
                                i = 0
                                if vari["triangulo"][1][vez] >= 3:
                                    
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Triangulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["circulo"][1][vez] >= 3 and vari["troca"] == True:
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Circulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["quadrado"][1][vez] >= 3 and vari["troca"] == True:
                                    while q > 0:
                                        print(i,q,"i,q")
                                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    vari["troca"] = False
                                if vari["triangulo"][1][vez] >= 1 and vari["circulo"][1][vez] >= 1 and vari["quadrado"][1][vez] >= 1 and vari["troca"] == True:
                                    q = 1
                                    ci = 1
                                    t = 1
                                    while q > 0:
                                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            q -= 1
                                            i -= 1
                                        i += 1
                                    i = 0
                                    while ci > 0:
                                        if ci > 0 and vari["cartasown"][vez][i] == "Circulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            ci -= 1
                                            i -= 1
                                        i += 1
                                    i = 0
                                    while t > 0:
                                        if t > 0 and vari["cartasown"][vez][i] == "Triangulo":
                                            del vari["cartasown"][vez][i]
                                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                                            del vari["cartas_pais"][vez][i]
                                            t -= 1
                                            i -= 1
                                        i += 1
                                for i in range(len(vari["territorio"][vez])):
                                    for a in range(3):
                                        if vari["territorio"][vez][i] == vari["carta_troca"][vez][a]:
                                            vari["quantidade_exerc"][vari["territorio"][vez][i]] += 2
                                for i in range(6):
                                    vari["carta_troca"][i] = []
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                print(qnt_rodada,"rodadadadadadada")
                                vari["troca"] = False
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            if event.key == pygame.K_n:
                                vari["troca"] = False
                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                
            if vari["atacado"] != -1 and vari["atacante"] != -1 and vari["troca"] == False:
                print("oalalfldjfdkfndkfhdkfnd")
                vari["alvo"] = False
                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                #sleep(3)
                
                batalha(vari,cor,vez,vari2)
                print("heyy")
                
                vari["atacante"] = -1
                vari["atacado"] = -1
                vari["resultado"] = False
                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if qnt_rodada == 0:
                            vari["run1"] = False
                            vari["run3"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.key == pygame.K_z:
                        print("heyyyyyyyyyyyyyy")
                        vari["show"] = True
                        
                        
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        sleep(5)
                        vari["quadrado"][0] = False
                        vari["circulo"][0] = False
                        vari["triangulo"][0] = False
                        vari["show"] = False
                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        
                
            #else:
                #vari["run1"] = False
        print(vari["vitoria"],"vitoria")
        
        while vari["run3"]== True:
            objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            for i in range(6):
                vari["territorio"][i] = []
            for i in range(42):
                
                if vari["cores"][i] == vez:
                    vari["territorio"][vez].append(i)
            if 2 == 2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("heheheheh")
                            vari["show_obj"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        if event.key == pygame.K_z:
                            print("heyyyyyyyyyyyyyy")
                            vari["show"] = True
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                            vari["quadrado"][0] = False
                            vari["circulo"][0] = False
                            vari["triangulo"][0] = False
                            
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            vari["show_obj"] = False                    
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                        if event.key == pygame.K_z:
                            vari["show"] = False
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                    if vari["remanejo1"] == -1 or vari["remanejo2"] == -1:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            
                                
                            for i in range(42):
                                if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                    #if vari["rodada"] // vari["numjogad"] > 0:
                                    for t in range(len(vari["territorio"][vez])):
                                        print(vari["remanejo1"],vari["remanejo2"],"manejooo")
                                        if  vari["remanejo1"] == -1 and vari["remanejo2"] == -1:
                                            if i == vari["territorio"][vez][t] and vari["quantidade_exerc"][vari["territorio"][vez][t]] > 1:
                                                vari["remanejo1"] = i
                                                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                                
                                        if vari["remanejo1"] != -1 and vari["remanejo2"] == -1:
                                            for t in range(len(vari["territorio"][vez])):
                                                for m in range(len(vari[vari["remanejo1"]]["fronteira"])):
                                                    if i == vari["territorio"][vez][t] and i == vari[vari["remanejo1"]]["fronteira"][m] and i != vari["remanejo1"]:
                                                        vari["remanejo2"] = i
                                                        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if vari["remanejo1"] != -1 and vari["remanejo2"] != -1:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for i in range(42):
                                if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:
                                    print(vari["remanejo1"],vari["remanejo2"],2)
                                    if vari["exerc_deslocado"][vari["remanejo1"]] > 0:
                                        print(vari["exerc_deslocado"][vari["remanejo1"]],"deslocccccc")
                                        if i == vari["remanejo2"] and vari["quantidade_exerc"] [vari["remanejo1"]]- vari["exerc_deslocado"][vari["remanejo1"]]+ 1  > 1:
                                            vari["quantidade_exerc"] [vari["remanejo1"]] -= 1
                                            vari["quantidade_exerc"] [vari["remanejo2"]] += 1
                                            print("eiiiiiiiii",vari["remanejo1"],vari["remanejo2"])
                                            vari["exerc_deslocado"][vari["remanejo2"]] += 1
                                            
                                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                    else:
                                        if i == vari["remanejo2"] and vari["quantidade_exerc"] [vari["remanejo1"]]- vari["exerc_deslocado"][vari["remanejo1"]]  > 1:
                                            vari["quantidade_exerc"] [vari["remanejo1"]] -= 1
                                            vari["quantidade_exerc"] [vari["remanejo2"]] += 1
                                            print("eiiiiiiiii",vari["remanejo1"],vari["remanejo2"])
                                            vari["exerc_deslocado"][vari["remanejo2"]] += 1
                                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            vari["remanejo1"] = -1
                            vari["remanejo2"] = -1
                            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                            
                                
                        if event.key == pygame.K_c:
                            vari["run3"] = False
                            
                
        if vari["vitoria"] == 1:
            

            
            if vari["cartas"][erase[c]] == "Triangulo":
                vari["triangulo"][0] = True
                
            if vari["cartas"][erase[c]] == "Circulo":
                vari["circulo"][0] = True
            if vari["cartas"][erase[c]] == "Quadrado":
                vari["quadrado"][0] = True
            print(c,"ccccccccc")
            vari["cartasown"][vez].append(vari["cartas"][erase[c]])
            vari["cartas_pais"][vez].append(erase[c])
            vari["triangulo"][1][vez] = 0
            vari["circulo"][1][vez] = 0
            vari["quadrado"][1][vez] = 0
            for i in range(len(vari["cartasown"][vez])):
                if vari["cartasown"][vez][i] == "Triangulo":
                    vari["triangulo"][1][vez] += 1
                if vari["cartasown"][vez][i] == "Circulo":
                    vari["circulo"][1][vez] += 1
                if vari["cartasown"][vez][i] == "Quadrado":
                    vari["quadrado"][1][vez] += 1
            
            
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            
            c += 1
        
        vari["quadrado"][0] = False
        vari["circulo"][0] = False
        vari["triangulo"][0] = False
        vari["vitoria"] = 0
        vari["rodada"] += 1
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        print("heyhey")
    return c,troca
def Maquina(vari,corfinal,qnt_rodada,erase1,c,troca,vari2):
    vari["run1"] = True
    
    
    vari["run4"] = True
    i = 0
    if 5 == 5:
        
        vez = vari["rodada"] % vari["numjogad"]
        objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
        if vez == 0:
            vari["vezz"] = "vez do exercito preto"
        if vez == 1:
            vari["vezz"] = "vez do exercito azul"
        if vez == 2:
            vari["vezz"] = "vez do exercito vermelho"
        if vez == 3:
            vari["vezz"] = "vez do exercito verde"
        if vez == 4:
            vari["vezz"] = "vez do exercito amarelo"
        if vez == 5:
            vari["vezz"] = "vez do exercito branco"
        vari["triangulo"][1][vez] = 0
        vari["circulo"][1][vez] = 0
        vari["quadrado"][1][vez] = 0
        for i in range(len(vari["cartasown"][vez])):
            if vari["cartasown"][vez][i] == "Triangulo":
                vari["triangulo"][1][vez] += 1
            if vari["cartasown"][vez][i] == "Circulo":
                vari["circulo"][1][vez] += 1
            if vari["cartasown"][vez][i] == "Quadrado":
                vari["quadrado"][1][vez] += 1
        if vari["triangulo"][1][vez] >= 3 or vari["circulo"][1][vez] >= 3 or vari["quadrado"][1][vez] >= 3 or(vari["triangulo"][1][vez] >= 1 and vari["circulo"][1][vez] >= 1 and vari["quadrado"][1][vez] >= 1) :
            vari["troca"] = True
            #update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        #update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        
        for t in range(6):
            vari["territorio"][t] = []
            for i in range(42):
            
                if vari["cores"][i] == t:
                    vari["territorio"][t].append(i)
        if len(vari["territorio"][vez]) > 5:
            qnt_rodada = len(vari["territorio"][vez])//2
        elif len(vari["territorio"][vez]) > 0:
            qnt_rodada = 3
        else:
            qnt_rodada = 0
        if 3 == 3:
            
           
            if vari["troca"] == True:
                qnt_rodada += troca
                                    
                troca += 2
                q = 3
                i = 0
                if vari["triangulo"][1][vez] >= 3:
                                        
                    while q > 0:
                                            
                        if q > 0 and vari["cartasown"][vez][i] == "Triangulo":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            q -= 1
                            i -= 1
                        i += 1
                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                    vari["troca"] = False
                if vari["circulo"][1][vez] >= 3 and vari["troca"] == True:
                    while q > 0:
                                            
                        if q > 0 and vari["cartasown"][vez][i] == "Circulo":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            q -= 1
                            i -= 1
                        i += 1
                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                    vari["troca"] = False
                if vari["quadrado"][1][vez] >= 3 and vari["troca"] == True:
                    while q > 0:
                                            
                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            q -= 1
                            i -= 1
                        i += 1
                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                    vari["troca"] = False
                if vari["triangulo"][1][vez] >= 1 and vari["circulo"][1][vez] >= 1 and vari["quadrado"][1][vez] >= 1 and vari["troca"] == True:
                    q = 1
                    ci = 1
                    t = 1
                    while q > 0:
                        if q > 0 and vari["cartasown"][vez][i] == "Quadrado":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            q -= 1
                            i -= 1
                        i += 1
                    i = 0
                    while ci > 0:
                        if ci > 0 and vari["cartasown"][vez][i] == "Circulo":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            ci -= 1
                            i -= 1
                        i += 1
                    i = 0
                    while t > 0:
                        if t > 0 and vari["cartasown"][vez][i] == "Triangulo":
                            del vari["cartasown"][vez][i]
                            vari["carta_troca"][vez].append(vari["cartas_pais"][vez][i])
                            del vari["cartas_pais"][vez][i]
                            t -= 1
                            i -= 1
                        i += 1
                for i in range(len(vari["territorio"][vez])):
                    for a in range(3):
                        if vari["territorio"][vez][i] == vari["carta_troca"][vez][a]:
                            vari["quantidade_exerc"][vari["territorio"][vez][i]] += 2
                for i in range(6):
                    vari["carta_troca"][i] = []
                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            if 3 == 3:
                
                print(qnt_rodada,"rodadadadadadada")
                vari["troca"] = False
                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                                
                vari2 = {"exerc_am":0,"exerc_as":0,"exerc_af":0,"exerc_eu":0,"exerc_asi":0,"exerc_oc":0,"america_do_norte":{0:0,1:0,2:0,3:0,4:0,5:0},"america_do_sul":{0:0,1:0,2:0,3:0,4:0,5:0},"africa":{0:0,1:0,2:0,3:0,4:0,5:0},"europa":{0:0,1:0,2:0,3:0,4:0,5:0},"asia":{0:0,1:0,2:0,3:0,4:0,5:0},"oceania":{0:0,1:0,2:0,3:0,4:0,5:0}}
                for t in range(6):
                    for i in range(len(vari["territorio"][t])):
                        if vari[vari["territorio"][t][i]]["continente"] == "America do Norte":
                            vari2["america_do_norte"][t] += 1
                        if vari[vari["territorio"][t][i]]["continente"] == "America do Sul":
                            vari2["america_do_sul"][t] += 1
                        if vari[vari["territorio"][t][i]]["continente"] == "Africa":
                            vari2["africa"][t] += 1
                        if vari[vari["territorio"][t][i]]["continente"] == "Europa":
                            vari2["europa"][t] += 1
                        if vari[vari["territorio"][t][i]]["continente"] == "Asia":
                            vari2["asia"][t] += 1
                        if vari[vari["territorio"][t][i]]["continente"] == "Oceania":
                            vari2["oceania"][t] += 1       
                porcentagem = []
                porcentagem.append(vari2["america_do_norte"][vez]/9)
                porcentagem.append(vari2["america_do_sul"][vez]/4)
                porcentagem.append(vari2["africa"][vez]/6)
                porcentagem.append(vari2["europa"][vez]/7)
                porcentagem.append(vari2["asia"][vez]/12)
                porcentagem.append(vari2["oceania"][vez]/4)
                for i in range(6):
                    if porcentagem[i] == 1:
                        porcentagem[i] = 0
                if porcentagem.index(max(porcentagem)) == 0:
                    vari["prioridade"][vez].append("America do Norte")
                if porcentagem.index(max(porcentagem)) == 1:
                    vari["prioridade"][vez].append("America do Sul")
                if porcentagem.index(max(porcentagem)) == 2:
                    vari["prioridade"][vez].append("Africa")
                if porcentagem.index(max(porcentagem)) == 3:
                    vari["prioridade"][vez].append("Europa")
                if porcentagem.index(max(porcentagem)) == 4:
                    vari["prioridade"][vez].append("Asia")
                if porcentagem.index(max(porcentagem)) == 5:
                    vari["prioridade"][vez].append("Oceania")
                porc_pais = ["America do Norte","America do Sul","Africa","Europa","Asia","Oceania"]
                porc_prio = []
                for i in range (6):
                    porc_prio.append(porc_pais[porcentagem.index(max(porcentagem))])
                    del porc_pais[porcentagem.index(max(porcentagem))]
                    del porcentagem[porcentagem.index(max(porcentagem))]
                print(porc_prio,"manoooogof")
                porcentagem = []
                porcentagem.append(vari2["america_do_norte"][vez]/9)
                porcentagem.append(vari2["america_do_sul"][vez]/4)
                porcentagem.append(vari2["africa"][vez]/6)
                porcentagem.append(vari2["europa"][vez]/7)
                porcentagem.append(vari2["asia"][vez]/12)
                porcentagem.append(vari2["oceania"][vez]/4)
                for i in range(6):
                    if porcentagem[i] == 1:
                        porcentagem[i] = -1
                
                ter_fort = []
                if porcentagem[0] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "America do Norte":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    if len(ter_fort) == 0:
                        ter_fort.append(8)
                        ter_fort.append(5)
                        ter_fort.append(0)
                    for i in range(5):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                if porcentagem[1] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "America do Sul":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                print(vari[vari["territorio"][vez][i]]["fronteira"][t],3)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    if len(ter_fort) == 0:
                        ter_fort.append(9)
                        ter_fort.append(10)
                    for i in range(2):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                if porcentagem[2] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "Africa":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                print(vari[vari["territorio"][vez][i]]["fronteira"][t],4)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    if len(ter_fort) == 0:
                        ter_fort.append(14)
                        ter_fort.append(13)
                    for i in range(3):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                if porcentagem[3] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "Europa":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                print(vari[vari["territorio"][vez][i]]["fronteira"][t],5)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    print(ter_fort,"terfort")
                    if len(ter_fort) == 0:
                        ter_fort.append(19) 
                        ter_fort.append(21)
                        ter_fort.append(23)
                        ter_fort.append(24)
                    for i in range(5):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                if porcentagem[4] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "Asia":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                print(vari[vari["territorio"][vez][i]]["fronteira"][t],6)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    print(ter_fort,"terfort")
                    if len(ter_fort) == 0:
                        ter_fort.append(37) 
                        ter_fort.append(35)
                        ter_fort.append(26)
                        ter_fort.append(27)
                        ter_fort.append(28)
                        ter_fort.append(29)
                    for i in range(7):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                if porcentagem[5] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        if vari[vari["territorio"][vez][i]]["continente"] == "Oceania":
                            for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                print(vari[vari["territorio"][vez][i]]["fronteira"][t],7)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    ter_fort.append(vari["territorio"][vez][i])
                                    break
                    print(ter_fort,"terfort")
                    if len(ter_fort) == 0:
                        ter_fort.append(38) 
                        ter_fort.append(39)
                        
                        
                        
                    for i in range(2):
                        ale = random.randrange(len(ter_fort))
                        vari["quantidade_exerc"][ter_fort[ale]] += 1
                                    

                
                vari["alvo"] = False
                vari["atacante"] = -1
                vari["atacado"] = -1
                
                #update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                
                
                

    if len(vari["territorio"][vez]) > 0:
        total_exerc = 0
        total_an = 0
        total_as = 0
        total_af = 0
        total_eu = 0
        total_asi = 0
        total_oc = 0
        for i in range(42):
            total_exerc += vari["quantidade_exerc"][i]
        for i in range(42):
            if vari[i]["continente"] == "America do Norte":
                total_an += vari["quantidade_exerc"][i]
            if vari[i]["continente"] == "America do Sul":
                total_as += vari["quantidade_exerc"][i]
            if vari[i]["continente"] == "Africa":
                total_af += vari["quantidade_exerc"][i]
            if vari[i]["continente"] == "Asia":
                total_asi += vari["quantidade_exerc"][i]
            if vari[i]["continente"] == "Europa":
                total_eu += vari["quantidade_exerc"][i]
            if vari[i]["continente"] == "Oceania":
                total_oc += vari["quantidade_exerc"][i]
        if len(vari["territorio"][vez]) > 0:
            total_an = total_an /9
            total_as = total_as /4
            total_af = total_af /6
            total_eu = total_eu /7
            total_asi = total_asi /12
            total_oc = total_oc /4
            porcentagem2 = []
            porcentagem2.append(total_an)
            porcentagem2.append(total_as)
            porcentagem2.append(total_af)
            porcentagem2.append(total_eu)
            porcentagem2.append(total_asi)
            porcentagem2.append(total_oc)
            if porcentagem2.index(min(porcentagem2)) == 0:
                vari["prioridade"][vez].append("America do Norte")
            elif porcentagem2.index(min(porcentagem2)) == 1:
                vari["prioridade"][vez].append("America do Sul")
            elif porcentagem2.index(min(porcentagem2)) == 2:
                vari["prioridade"][vez].append("Africa")
            elif porcentagem2.index(min(porcentagem2)) == 3:
                vari["prioridade"][vez].append("Europa")
            elif porcentagem2.index(min(porcentagem2)) == 4:
                vari["prioridade"][vez].append("Asia")
            elif porcentagem2.index(min(porcentagem2)) == 5:
                vari["prioridade"][vez].append("Oceania")
            
            
            #objetivo(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            qnt_rod_inicial = qnt_rodada
            
            alea = random.randrange(1,8)
            
            ter_prio = []
            ter_prio2 = []
            qnt_exerc = []
            qnt_exerc2 = []
            
            inicial = True
            q = 1
            
            if vari["objetivo"][vez] >= 1 and vari["objetivo"][vez] <= 6:
                while inicial == True:
                    
                    
                    if alea == 1:
                        prio_max = vari["prioridade"][vez][-1]
                    if alea == 3 or alea == 2 or alea == 7:
                        prio_max = vari["prioridade"][vez][-2]
                    if alea == 2 or alea == 1 or alea == 3:
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                    if alea == 7:
                        for i in range (3):
                            ale = random.randrange(0, len(vari["territorio"][vez]))
                            vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                            qnt_rodada -= 1
                        break

                        
                    if alea == 5 or alea == 4 or alea == 6:
                        alvo = vari["prioridade"][vez][0]
                        if alvo + 1 <= vari["numjogad"]: 
                        
                            porcentagem = []
                            porcentagem.append(vari2["america_do_norte"][alvo]/9)
                            porcentagem.append(vari2["america_do_sul"][alvo]/4)
                            porcentagem.append(vari2["africa"][alvo]/6)
                            porcentagem.append(vari2["europa"][alvo]/7)
                            porcentagem.append(vari2["asia"][alvo]/12)
                            porcentagem.append(vari2["oceania"][alvo]/4)
                            if porcentagem.index(max(porcentagem)) == 0:
                                vari["prioridade"][vez].append("America do Norte")
                            if porcentagem.index(max(porcentagem)) == 1:
                                vari["prioridade"][vez].append("America do Sul")
                            if porcentagem.index(max(porcentagem)) == 2:
                                vari["prioridade"][vez].append("Africa")
                            if porcentagem.index(max(porcentagem)) == 3:
                                vari["prioridade"][vez].append("Europa")
                            if porcentagem.index(max(porcentagem)) == 4:
                                vari["prioridade"][vez].append("Asia")
                            if porcentagem.index(max(porcentagem)) == 5:
                                vari["prioridade"][vez].append("Oceania")
                            prio_max = vari["prioridade"][vez][-1]
                            
                            
                            del vari["prioridade"][vez][-1]
                            ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                            break
                
                alea = random.randrange(1, 8)
                while qnt_rodada > qnt_rod_inicial//2:
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    qnt_rodada,alea = maquina_exerc2(alea,vari,qnt_rodada,vez)
                        
                    
                alea = random.randrange(1, 8)
                while qnt_rodada > 1:
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    qnt_rodada,alea = maquina_exerc2(alea,vari,qnt_rodada,vez)
                if qnt_rodada == 1:
                    ale = random.randrange(0, len(vari["territorio"][vez]))
                    vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                    qnt_rodada -= 1
                
                
                
            if (vari["objetivo"][vez] >= 7 and vari["objetivo"][vez] <= 9) or vari["objetivo"][vez] == 11:
                while inicial == True:
                    
                    
                    if alea == 1:
                        prio_max = vari["prioridade"][vez][-1]
                    if alea == 3 or alea == 2 or alea == 7:
                        prio_max = vari["prioridade"][vez][-2]
                    if alea == 2 or alea == 1 or alea == 3:
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                    if alea == 7:
                        for i in range (3):
                            
                            ale = random.randrange(0, len(vari["territorio"][vez]))
                            vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                            qnt_rodada -= 1
                        break

                        
                    if alea == 5 or alea == 4 or alea == 6:
                        porc = []
                        i = 1
                        while vari["prioridade"][vez][0] == vari["prioridade"][vez][-2] or vari["prioridade"][vez][1] == vari["prioridade"][vez][-2]:
                            print(porc_prio, i)
                            vari["prioridade"][vez][-2] = porc_prio[i]
                            i += 1
                        
                        if vari["prioridade"][vez][0] == "America do Norte" or vari["prioridade"][vez][1] == "America do Norte":
                            porc.append(porcentagem[0])
                            porc.append("America do Norte")
                        if vari["prioridade"][vez][0] == "America do Sul" or vari["prioridade"][vez][1] == "America do Sul":
                            porc.append(porcentagem[1])
                            porc.append("America do Sul")
                        if vari["prioridade"][vez][0] == "Africa" or vari["prioridade"][vez][1] == "Africa":
                            porc.append(porcentagem[2])
                            porc.append("Africa")
                        if vari["prioridade"][vez][0] == "Europa" or vari["prioridade"][vez][1] == "Europa":
                            porc.append(porcentagem[3])
                            porc.append("Europa")
                        if vari["prioridade"][vez][0] == "Asia" or vari["prioridade"][vez][1] == "Asia":
                            porc.append(porcentagem[4])
                            porc.append("Asia")
                        if vari["prioridade"][vez][0] == "Oceania" or vari["prioridade"][vez][1] == "Oceania":
                            porc.append(porcentagem[5])
                            porc.append("Oceania")

                        if porc[0] >= porc[2]:
                            prio_max = porc[1]
                        else:
                            prio_max = porc[3]
                        
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                alea = random.randrange(1, 8)
                while qnt_rodada > qnt_rod_inicial//2:
                    print(qnt_rodada,qnt_rod_inicial,"um")
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    print(qnt_rodada,qnt_rod_inicial,"um")
                    qnt_rodada,alea = maquina_exerc3(alea,vari,qnt_rodada,vez,porcentagem)
                    print(qnt_rodada,qnt_rod_inicial,"um")    
                    
                alea = random.randrange(1, 8)
                while qnt_rodada > 1:
                    print("oi8")
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    qnt_rodada,alea = maquina_exerc3(alea,vari,qnt_rodada,vez,porcentagem)
                if qnt_rodada == 1:
                    print("oi9")
                    ale = random.randrange(0, len(vari["territorio"][vez]))
                    vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                    qnt_rodada -= 1


            if (vari["objetivo"][vez] == 10  or vari["objetivo"][vez] == 12):
                while inicial == True:
                    
                    if alea == 1:
                        prio_max = vari["prioridade"][vez][-1]
                    if alea == 3 or alea == 2 or alea == 7:
                        prio_max = vari["prioridade"][vez][-2]
                    if alea == 2 or alea == 1 or alea == 3:
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                    if alea == 7:
                        for i in range (3):
                            print("oi7")
                            ale = random.randrange(0, len(vari["territorio"][vez]))
                            vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                            qnt_rodada -= 1
                        break

                        
                    if alea == 5 or alea == 4 or alea == 6:
                        porc = []
                        i = 1
                        while vari["prioridade"][vez][0] == vari["prioridade"][vez][-2] or vari["prioridade"][vez][1] == vari["prioridade"][vez][-2]:
                            print(porc_prio, i)
                            vari["prioridade"][vez][-2] = porc_prio[i]
                            
                            i += 1
                        if vari["prioridade"][vez][0] == "America do Norte" or vari["prioridade"][vez][1] == "America do Norte" or vari["prioridade"][vez][-2] == "America do Norte":
                            porc.append(porcentagem[0])
                            porc.append("America do Norte")
                        if vari["prioridade"][vez][0] == "America do Sul" or vari["prioridade"][vez][1] == "America do Sul" or vari["prioridade"][vez][-2] == "America do Sul":
                            porc.append(porcentagem[1])
                            porc.append("America do Sul")
                        if vari["prioridade"][vez][0] == "Africa" or vari["prioridade"][vez][1] == "Africa" or vari["prioridade"][vez][-2] == "Africa":
                            porc.append(porcentagem[2])
                            porc.append("Africa")
                        if vari["prioridade"][vez][0] == "Europa" or vari["prioridade"][vez][1] == "Europa" or vari["prioridade"][vez][-2] == "Europa":
                            porc.append(porcentagem[3])
                            porc.append("Europa")
                        if vari["prioridade"][vez][0] == "Asia" or vari["prioridade"][vez][1] == "Asia" or vari["prioridade"][vez][-2] == "Asia":
                            porc.append(porcentagem[4])
                            porc.append("Asia")
                        if vari["prioridade"][vez][0] == "Oceania" or vari["prioridade"][vez][1] == "Oceania" or vari["prioridade"][vez][-2] == "Oceania":
                            porc.append(porcentagem[5])
                            porc.append("Oceania")

                        if porc[0] >= porc[2] and porc[0] >= porc[4]:
                            prio_max = porc[1]
                        elif porc[2] >= porc[0] and porc[2] >= porc[4]:
                            prio_max = porc[3]
                        elif porc[4] >= porc[2] and porc[4] >= porc[0]:
                            prio_max = porc[5]
                        
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                alea = random.randrange(1, 8)
                while qnt_rodada > qnt_rod_inicial//2:
                    
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    
                    qnt_rodada,alea = maquina_exerc3(alea,vari,qnt_rodada,vez,porcentagem)
                        
                    
                alea = random.randrange(1, 8)
                while qnt_rodada > 1:
                    print("oi")
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    qnt_rodada,alea = maquina_exerc3(alea,vari,qnt_rodada,vez,porcentagem)
                if qnt_rodada == 1:
                    ale = random.randrange(0, len(vari["territorio"][vez]))
                    print("oi")
                    vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                    qnt_rodada -= 1
            
            if (vari["objetivo"][vez] == 13  or vari["objetivo"][vez] == 14):
                while inicial == True:
                    print("seraa")        
                    if alea == 1 or alea == 2:
                        prio_max = vari["prioridade"][vez][-1]
                    if alea >= 3 and alea < 8 :
                        prio_max = vari["prioridade"][vez][-2]
                    if alea >= 1 and alea < 7:
                        ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea = maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial)
                        break
                    if alea == 7:
                        for i in range (3):
                            print("oi7")
                            ale = random.randrange(0, len(vari["territorio"][vez]))
                            vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                            qnt_rodada -= 1
                        break
                alea = random.randrange(1, 8)
                yyy = 0
                while qnt_rodada > qnt_rod_inicial//2:
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    if yyy < 3:
                        print("putaquepatiu1",alea)
                    yyy += 1
                yyy = 0
                alea = random.randrange(1, 8)
                while qnt_rodada > 1:
                    if yyy < 3:
                        print("putaquepatiu2")
                    yyy += 1
                    qnt_rodada,alea = maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max)
                    print("chegaaaaa")
                    
                if qnt_rodada == 1:
                    ale = random.randrange(0, len(vari["territorio"][vez]))
                    
                    vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
                    qnt_rodada -= 1
            dif = []
            exerc_vez = []
            for i in range(len(vari["territorio"][vez])):
                exerc_vez.append(vari["quantidade_exerc"][vari["territorio"][vez][i]])
            maior = max(exerc_vez) - 1
            print(maior,"maior")
            print(vari["objetivo"][vez],"ggogogogo")
            print(prio_max,8)
            if vari["rodada"] // vari["numjogad"] >= 1:
                while maior > 0:
                    print(12)
                    if maior >= 3:
                        for i in range(len(vari["territorio"][vez])):
                            #for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            j = 0
                            while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                                if vari["vitoria"] != 1:
                                    if vari["quantidade_exerc"][vari["territorio"][vez][i]] - vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == maior:
                                        if vari[vari[vari["territorio"][vez][i]]["fronteira"][j]]["continente"] == prio_max:
                                            if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    
                        
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(1,9)
                                if vari["vitoria"] == 1:
                                    break
                                
                                    
                                
                                    
                                j += 1
                            if vari["vitoria"] == 1:
                                break
                    if vari["vitoria"] == 1:
                        break        
                    
                    maior -= 1
                exerc_vez = []
                print(vari["vitoria"],10)
                for i in range(len(vari["territorio"][vez])):
                    exerc_vez.append(vari["quantidade_exerc"][vari["territorio"][vez][i]])
                maior = max(exerc_vez) - 1
                print(maior,"maior")
                print(exerc_vez,"exerc_vez")
                if vari["vitoria"] != 1:
                    while maior > 0:
                        print(13,"ola1")
                        if maior >= 3:
                            for i in range(len(vari["territorio"][vez])):
                                #for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                j = 0
                                while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                                    print(14,"ola2")
                                    if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                    
                                        if vari["quantidade_exerc"][vari["territorio"][vez][i]] - vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == maior:
                                            while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                vari["atacante"] = vari["territorio"][vez][i]
                                                vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                batalha(vari,cor,vez,vari2)
                                                print(2,"ola3")
                                        if vari["vitoria"] == 1:
                                            break
                                    j += 1
                                if vari["vitoria"] == 1:
                                    break
                        if vari["vitoria"] == 1:
                            break
                        maior -= 1
                exerc_vez = []
                exerc_def = []
                for i in range(len(vari["territorio"][vez])):
                    exerc_vez.append(vari["quantidade_exerc"][vari["territorio"][vez][i]])
                    if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4:
                        for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            if vari[vari[vari["territorio"][vez][i]]["fronteira"][j]]["continente"] == prio_max:
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                    exerc_def.append(vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]])
                print(exerc_def,11)
                print(prio_max,12)
                
                            
                maior = max(exerc_vez) - 1
                exerc_def2 = list(set(exerc_def))
                while len(exerc_def2) > 0:
                    print(10,"ola4")
                    for i in range(len(vari["territorio"][vez])):
                        j = 0
                        while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                            print(1,13)
                            if vari[vari[vari["territorio"][vez][i]]["fronteira"][j]]["continente"] == prio_max:
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                    if vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == exerc_def2[-1]:
                                        if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 8:
                                            if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 2*(vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]):
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(3,"ola5")
                                        elif vari["quantidade_exerc"][vari["territorio"][vez][i]] == 4:
                                            if (vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]) == 1:
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(4,"ola4")
                                        elif vari["quantidade_exerc"][vari["territorio"][vez][i]] > 4:
                                            if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 + (vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]):
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez > 0:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(5)
                            j += 1
                    del exerc_def2[-1]                            
                exerc_vez = []
                exerc_def = []
                for i in range(len(vari["territorio"][vez])):
                    exerc_vez.append(vari["quantidade_exerc"][vari["territorio"][vez][i]])
                    if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4:
                        
                        for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                exerc_def.append(vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]])
                exerc_def2 = list(set(exerc_def))
                maior = max(exerc_vez)
                while len(exerc_def2) > 0:
                    print(11)
                    for i in range(len(vari["territorio"][vez])):
                        if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4:
                            j = 0
                            while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                                print(2)
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                    if vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == exerc_def2[-1]:
                                        if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 8:
                                            if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 2*(vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]):
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(6)
                                        elif vari["quantidade_exerc"][vari["territorio"][vez][i]] == 4:
                                            if (vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]) == 1:
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(7)
                                        elif vari["quantidade_exerc"][vari["territorio"][vez][i]] > 4:
                                            if vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 + (vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]]):
                                                while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 4 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                                    vari["atacante"] = vari["territorio"][vez][i]
                                                    vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                                    batalha(vari,cor,vez,vari2)
                                                    print(8)
                                j += 1
                    del exerc_def2[-1] 
                
                  
                if vari["vitoria"] != 1:
                    while maior > 0:
                        print(6)
                        for i in range(len(vari["territorio"][vez])):
                            #for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            j = 0
                            while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                                print(3)
                               
                                if vari["quantidade_exerc"][vari["territorio"][vez][i]] - vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == maior:
                                    if vari[vari[vari["territorio"][vez][i]]["fronteira"][j]]["continente"] == prio_max:
                                        while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 3 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                            vari["atacante"] = vari["territorio"][vez][i]
                                            vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                            batalha(vari,cor,vez,vari2)
                                    
                                        if vari["vitoria"] == 1:
                                            break
                                j += 1
                            if vari["vitoria"] == 1:
                                break
                        if vari["vitoria"] == 1:
                            break

                        maior -= 1
                    exerc_vez = []
                    for i in range(len(vari["territorio"][vez])):
                        exerc_vez.append(vari["quantidade_exerc"][vari["territorio"][vez][i]])
                    maior = max(exerc_vez) - 1
                    if vari["vitoria"] != 1:
                        while maior > 0:
                            print(8)
                            for i in range(len(vari["territorio"][vez])):
                                #for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                                j = 0
                                while j < len(vari[vari["territorio"][vez][i]]["fronteira"]):
                                    print(4)
                                    if vari["quantidade_exerc"][vari["territorio"][vez][i]] - vari["quantidade_exerc"][vari[vari["territorio"][vez][i]]["fronteira"][j]] == maior:
                                        while vari["quantidade_exerc"][vari["territorio"][vez][i]] >= 3 and vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                                            vari["atacante"] = vari["territorio"][vez][i]
                                            vari["atacado"] = vari[vari["territorio"][vez][i]]["fronteira"][j]
                                            batalha(vari,cor,vez,vari2)
                                        if vari["vitoria"] == 1:
                                            break
                                    j += 1
                                if vari["vitoria"] == 1:
                                    break
                                    
                            if vari["vitoria"] == 1:
                                break

                            maior -= 1


                            
                        


                


                                
                                
            if vari["vitoria"] == 1:
                    

                    
                    if vari["cartas"][erase[c]] == "Triangulo":
                        vari["triangulo"][0] = True
                        
                    if vari["cartas"][erase[c]] == "Circulo":
                        vari["circulo"][0] = True
                    if vari["cartas"][erase[c]] == "Quadrado":
                        vari["quadrado"][0] = True
                    print(c,"ccccccccc")
                    vari["cartasown"][vez].append(vari["cartas"][erase[c]])
                    vari["cartas_pais"][vez].append(erase[c])
                    vari["triangulo"][1][vez] = 0
                    vari["circulo"][1][vez] = 0
                    vari["quadrado"][1][vez] = 0
                    for i in range(len(vari["cartasown"][vez])):
                        if vari["cartasown"][vez][i] == "Triangulo":
                            vari["triangulo"][1][vez] += 1
                        if vari["cartasown"][vez][i] == "Circulo":
                            vari["circulo"][1][vez] += 1
                        if vari["cartasown"][vez][i] == "Quadrado":
                            vari["quadrado"][1][vez] += 1
                    #print( vari["triangulo"][1][vez],vari["circulo"][1][vez],vari["quadrado"][1][vez])
                    
                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                    
                    c += 1
            
            vari["run6"] = True
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari["run6"] == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False
                        vari["run6"] = False
                        vari["run7"] = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            vari["run6"] = False
            remanejo_maquina(vari,corfinal,qnt_rodada,erase1,c,troca,vari2,vez)
                        
            vari["run7"] = True
            update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            while vari["run7"] == True:  
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        vari["run4"] = False
                        vari["running"] = False
                        vari["run5"] = False
                        vari["run2"] = False
                        vari["troca"] = False
                        vari2["exerc_am"] = 0
                        vari2["exerc_as"] = 0
                        vari2["exerc_af"] = 0
                        vari2["exerc_asi"] = 0
                        vari2["exerc_eu"] = 0
                        vari2["exerc_oc"] = 0
                        vari["run1"] = False
                        vari["run3"] = False
                        vari["run6"] = False
                        vari["run7"] = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            vari["run7"] = False
    vari["quadrado"][0] = False
    vari["circulo"][0] = False
    vari["triangulo"][0] = False
    vari["vitoria"] = 0            
    vari["rodada"] += 1
    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)

                            
    return troca
def remanejo_maquina(vari,corfinal,qnt_rodada,erase1,c,troca,vari2,vez):
    remanejo_nao = 0
    remanejo_sim = 0
    remanejo_ter = []
    q = 0
    for i in range(len(vari["territorio"][vez])):
        remanejo_sim = 0
        for j in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
            if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][j]] != vez:
                remanejo_nao = 1
                break
            else:
                remanejo_sim += 1
        #print(remanejo_sim,vari[vari["territorio"][vez][i]]["pais"],len(vari[vari["territorio"][vez][i]]["fronteira"]))
        if remanejo_sim == len(vari[vari["territorio"][vez][i]]["fronteira"]):
            remanejo_ter.append(vari["territorio"][vez][i])
    agrupamento = []
    #for i in range(len(remanejo_ter)):
    i = 0
    t = 0
    print(remanejo_ter,13)
    remanejo_ter2 = []
    for i in range(len(remanejo_ter)):
        remanejo_ter2.append(remanejo_ter[i])
    print(remanejo_ter,remanejo_ter2,"legal")
    i = 0
    while i < len(remanejo_ter):
        e = 0
        for j in range(len(vari[remanejo_ter[i]]["fronteira"])):
            
            if len(agrupamento) == 0:
                if vari[remanejo_ter[i]]["fronteira"][j] in remanejo_ter:
                    agrupamento.append([remanejo_ter[i]])
                    agrupamento[q].append(vari[remanejo_ter[i]]["fronteira"][j])
                    #print(remanejo_ter[i],vari[remanejo_ter[i]]["fronteira"][j])
                    remanejo_ter.remove(vari[remanejo_ter[i]]["fronteira"][j])
                    del remanejo_ter[i]
                    i -= 1
                    break
        
            else:
                p = 0
                if 3 == 3:
                    #print(remanejo_ter[i],vari[remanejo_ter[i]]["fronteira"][j])
                    t = 0
                    r = 0
                    while  len(remanejo_ter) > 0:
                        #print(p,len(agrupamento))
                        p = 0
                        while p < len(agrupamento):
                            e = 0
                            #print(t,r,remanejo_ter)
                            if len(remanejo_ter) == 0:
                                break
                            for r in range(len(vari[remanejo_ter[t]]["fronteira"])):
                                if vari[remanejo_ter[t]]["fronteira"][r] in agrupamento[p]:
                                    agrupamento[p].append(remanejo_ter[t])
                                    #print(remanejo_ter[t],vari[remanejo_ter[t]]["fronteira"][j])
                                    #agrupamento[p].append(vari[remanejo_ter[i]]["fronteira"][j])
                                    
                                    
                                    del remanejo_ter[t]
                                    
                                    
                                    e = 5
                                    break

                            
                                
                                
                            if e != 5:           
                                #print(t,remanejo_ter)
                                #print(remanejo_ter[t])
                                agrupamento.append([remanejo_ter[t]])
                                #agrupamento[q].append(vari[remanejo_ter[t]]["fronteira"][r])
                                #remanejo_ter.remove(vari[remanejo_ter[t]]["fronteira"][r])
                                del remanejo_ter[t]
                            
                                
                            p += 1
                            
                        #t += 1    
                        
                    
                    
                
                        
        i += 1
    for w in range(len(agrupamento)):
        for i in range(len(agrupamento)):
            for j in range(len(agrupamento[i])):
                for t in range(len(vari[agrupamento[i][j]]["fronteira"])):
                    for k in range(len(agrupamento)):
                        if vari[agrupamento[i][j]]["fronteira"][t] in agrupamento[k] and i != k:
                            for q in range(len(agrupamento[k])):
                                agrupamento[i].append(agrupamento[k][q])
                            agrupamento[k] = []
    i = 0
    while i < len(agrupamento):
        if len(agrupamento[i]) == 0:
            del agrupamento[i]
            i -= 1
        i += 1
    print(agrupamento)
    pontas = []
    for i in range(len(agrupamento)):
        pontas.append([])
        for j in range(len(agrupamento[i])):
            for h in range(len(vari[agrupamento[i][j]]["fronteira"])):
                if vari[agrupamento[i][j]]["fronteira"][h] not in remanejo_ter2:
                    pontas[i].append(vari[agrupamento[i][j]]["fronteira"][h])
    for i in range(len(pontas)):
        for j in range(len(pontas[i])):
            for t in range(len(vari[pontas[i][j]]["fronteira"])):
                if vari["cores"][vari[pontas[i][j]]["fronteira"][t]] == vez and vari[pontas[i][j]]["fronteira"][t] not in remanejo_ter2 and vari[pontas[i][j]]["fronteira"][t] not in pontas[i]:
                    pontas[i].append(vari[pontas[i][j]]["fronteira"][t])
                    print(vari[pontas[i][j]]["fronteira"][t])
    for i in range(len(pontas)):
        
        pontas[i] = list(set(pontas[i]))
    print(pontas,"pontas")
    #sleep(54954895)
    distancia = []
    qual_pais = []
    x = 0
    dist = 0
    pontas_maxi = []
    i = 0
    if len(pontas) != 0:
        for i in range(len(pontas)):
        
            pontas_maxi.append(len(agrupamento[i]))
        maximo_pontas = max(pontas_maxi)
        print(maximo_pontas,"maxiiiim")
    else:
        maximo_pontas = -1
    m = -1
    distancia = []
    recursao = -1
    restante = 0
    dist = 0
    h = 0
    j = 0
    i = 0
    q = 0
    importante = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7]
    print(agrupamento)
    print(pontas)
    caminhos = []
    caminho = []
    fimm = 0
    cont = -1
    principal = 101
    rerc = 0
    soma = 0
    valor_t = 0
    cami = []
    dista = []
    i,j,principal,valor_t = recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista)
    
    
    print(pontas)
    print(agrupamento)
    i = 0
    pontas_way = []
    if 1 == 1:
        agru2 = []
        pont2 = []
        terri = []
        if len(agrupamento) > 0:
            
            for i in range(len(agrupamentos)):
                for j in range(len(agrupamento[i])):
                    agru2.append(agrupamento[i][j])
        if len(pontas) > 0:
            
            for i in range(len(pontas)):
                for j in range(len(pontas[i])):
                    pont2.append(pontas[i][j])

        for i in range(len(vari["territorio"][vez])):
            if vari["territorio"][vez][i] not in agru2 and vari["territorio"][vez][i] not in pont2:
                terri.append(vari["territorio"][vez][i])
        
                    
        pontas_way.append([])
        for i in range(len(terri)):
            
            for q in range(len(vari[terri[i]]["fronteira"])):
                for t in range(len(terri)):
                    
                    if vari[terri[i]]["fronteira"][q] == terri[t] :
                            
                        pontas_way[0].append(terri[i])
                        pontas_way[0].append(terri[t])
        #and vari["quantidade_exerc"][pontas[i][j]] > vari["quantidade_exerc"][pontas[i][t]] + 1
        print(pontas_way,"pontas_Way")
        
        pontas_way[0] = list(set(pontas_way[0]))
        
        print(pontas_way,"pontas_way")
        
        pontas_way2 = []
        proximo = -10
        pontas_way3 = []
        proximo2 = -10
        conta = -1
        
        conta = recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2,conta)
        print(pontas_way2)
        remanej_specif2 = []
        remanej_specif1 = []
        sleep(500000)
        for i in range(len(pontas_way2)):
            for j in range(len(pontas_way2[i])):
                for t in range(len(pontas_way2[i])):
                    if pontas_way2[i][t] in vari[pontas_way2[i][j]]["fronteira"] and pontas_way2[i][t] not in remanej_specif2:
                        remanej_specif1.append(pontas_way2[i][t])
                        remanej_specif2.append(pontas_way2[i][t])
        print(remanej_specif1, remanej_specif2)
        
                
        if len(remanej_specif1) > 0:
            agora = remanej_specif1[0]
        remanej_pontas1 = []
        remanej_pontas2 = []
        remanej_pontas3 = []
        remanej_pontas4 = []
        remanej_pontas5 = []
        remanej_pontas6 = []
        remanej_exerc = []
        print(remanej_specif1,remanej_specif2,"olaaaa")
        for i in range(len(remanej_specif1)):
            #if i + 1 == len(remanej_specif1):
             #   segura = remanej_specif1[i]
              #  remanej_specif1[i] = -10
            if agora == remanej_specif1[i]:
                remanej_pontas1.append(vari["quantidade_exerc"][remanej_specif2[i]])
                remanej_pontas2.append(remanej_specif2[i])
                print(remanej_pontas1,remanej_pontas2,"velho")
            if agora != remanej_specif1[i] or i + 1 == len(remanej_specif1):
                print(remanej_pontas2,remanej_pontas1,"rrrrudy")
                while len(remanej_pontas1) > 0:
                    indice = remanej_pontas1.index(max(remanej_pontas1))
                    remanej_pontas3.append(remanej_pontas1[indice])
                    remanej_pontas4.append(remanej_pontas2[indice])
                    remanej_pontas5.append(0)
                    remanej_pontas6.append(0)
                    
                    
                    del remanej_pontas1[indice]
                    del remanej_pontas2[indice]
                #print(remanej_pontas3,remanej_pontas4,remanej_pontas5,"wiliam")
                if vari["quantidade_exerc"][remanej_specif1[i-1]] > 3:
                    exerc_passa = 3
                else:
                    exerc_passa = vari["quantidade_exerc"][remanej_specif1[i-1]] - 1
                
                if len(remanej_pontas4) >= 3:
                    while remanej_pontas3[-1] != remanej_pontas3[-2] and exerc_passa != 0:
                        remanej_pontas3[-1] += 1
                        remanej_pontas5[-1] += 1
                        remanej_pontas6[-1] -= 1
                        exerc_passa -= 1
                    while remanej_pontas3[-2] != remanej_pontas3[-3] and exerc_passa != 0:
                        if exerc_passa > 2:
                            remanej_pontas3[-1] += 1
                            remanej_pontas5[-1] += 1
                            remanej_pontas6[-1] -= 1
                            exerc_passa -= 1
                            remanej_pontas3[-2] += 1
                            remanej_pontas5[-2] += 1
                            remanej_pontas6[-2] -= 1
                            exerc_passa -= 1
                        else:
                            remanej_pontas3[-1] += 1
                            remanej_pontas5[-1] += 1
                            remanej_pontas6[-1] += 1
                            exerc_passa -= 1
                    contador = -1
                    while exerc_passa != 0:
                        remanej_pontas3[contador] += 1
                        remanej_pontas5[contador] += 1
                        remanej_pontas6[contador] -= 1
                        exerc_passa -= 1
                        contador -= 1
                if len(remanej_pontas4) == 2:
                    while remanej_pontas3[-1] != remanej_pontas3[-2] and exerc_passa != 0:
                        remanej_pontas3[-1] += 1
                        remanej_pontas5[-1] += 1
                        remanej_pontas6[-1] -= 1
                        exerc_passa -= 1
                    contador = -1
                    while exerc_passa != 0:
                        remanej_pontas3[contador] += 1
                        remanej_pontas5[contador] += 1
                        remanej_pontas6[contador] -= 1
                        exerc_passa -= 1
                        contador -= 1
                        if contador == -3:
                            contador = -1

                    #print(remanej_pontas3,remanej_pontas4,remanej_pontas5,"ttttt")
                #print(remanej_pontas4,"quiabo")
                for t in range(len(remanej_pontas4)):
                    remanej_exerc.append(remanej_specif1[i-1])
                    remanej_exerc.append(remanej_pontas4[t])
                    remanej_exerc.append(remanej_pontas5[t])
                    #print(remanej_specif1[i-1],remanej_pontas4[t],remanej_pontas5[t])
                print(remanej_pontas1,remanej_pontas2,remanej_pontas3,remanej_pontas4,remanej_pontas5,remanej_pontas6,"tylerrr")
                agora = remanej_specif1[i]
                remanej_pontas1 = []
                remanej_pontas2 = []
                remanej_pontas3 = []
                remanej_pontas4 = []
                remanej_pontas5 = []
                remanej_pontas6 = []
                if agora == remanej_specif1[i]:
                    remanej_pontas1.append(vari["quantidade_exerc"][remanej_specif2[i]])
                    remanej_pontas2.append(remanej_specif2[i])
        
        for i in range(len(remanej_exerc)):
            if i % 3 == 1:
                vari["quantidade_exerc"][remanej_exerc[i]] += remanej_exerc[i+1]
                vari["quantidade_exerc"][remanej_exerc[i-1]] -= remanej_exerc[i+1]
        print(remanej_exerc,"gggghhh")
        
        

    if len(distancia) > 0:
        while i <(len(distancia)):
            
            if len(distancia[i]) == 1:
                del distancia[i]
                i -= 1
            i += 1
        short_way = []
        remanej_way = []
        short = []
        print(distancia)
        for i in range(len(distancia)):
            for j in range(len(distancia[i])):
                if j % 4 == 1:
                    short_way.append(distancia[i][j])
            print(short_way,"shortway")
            for t in range(len(short_way)):
                if min(short_way) == short_way[t]:
                    short.append(t)
            short2 = []
            for aa in range(len(short)):
                short2.append(vari["quantidade_exerc"][distancia[i][4*short[aa]]])
            definitivo = short2.index(min(short2))
            
                
            remanej_way.append(distancia[i][4*short[definitivo]])
                                            
                                            #short_way.index(min(short_way))])
            remanej_way.append(distancia[i][4*short[definitivo]+2])
                                            #short_way.index(min(short_way))+2])
            remanej_way.append(distancia[i][4*short[definitivo]+3])
                                            #short_way.index(min(short_way))+3])
            short_way = []
            short = []
            short2= []
            pontas_way = []
        
        for i in range(len(pontas)):
            pontas_way.append([])
            for j in range(len(pontas[i])):
                for q in range(len(vari[pontas[i][j]]["fronteira"])):
                    for t in range(len(pontas[i])):
                        if pontas[i][j] == 27:
                            print(vari[pontas[i][j]]["fronteira"][q],pontas[i][t])
                        if vari[pontas[i][j]]["fronteira"][q] == pontas[i][t] :
                            
                            pontas_way[i].append(pontas[i][j])
                            pontas_way[i].append(pontas[i][t])
        #and vari["quantidade_exerc"][pontas[i][j]] > vari["quantidade_exerc"][pontas[i][t]] + 1
        print(pontas_way,"pontas_Way")
        for i in range(len(pontas_way)):
            pontas_way[i] = list(set(pontas_way[i]))
        
        print(pontas_way,"pontas_way")
        #sleep(600000)
        pontas_way2 = []
        proximo = -10
        pontas_way3 = []
        proximo2 = -10
        conta = -1
        conta = recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2,conta)
        print(pontas_way2)
        
        way_final = []
        for i in range(len(remanej_way)):
            if i % 3 == 0:
                way_final.append(remanej_way[i])
            if i % 3 == 2:
                if len(remanej_way[i]) == 1:
                    way_final.append(remanej_way[i-1])
                else:
                    way_final.append(remanej_way[i][1])
                    
        
        print(remanej_way)
        print(way_final,"wayfinal")
        print(distancia)
        remanej_exerc = []
        
        for i in range(len(way_final)):
            
            if i % 2 == 0:
                print(way_final[i],vari["quantidade_exerc"][way_final[i]])
                if vari["quantidade_exerc"][way_final[i]] > 3:
                    remanej_exerc.append(way_final[i])
                    remanej_exerc.append(way_final[i+1])
                    remanej_exerc.append(3)
                else:
                    remanej_exerc.append(way_final[i])
                    remanej_exerc.append(way_final[i+1])
                    remanej_exerc.append(vari["quantidade_exerc"][way_final[i]] - 1)
                
        
        
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        print(remanej_exerc,way_final)
        remanej_specif1 = []
        remanej_specif2 = []
        j = 0
        deletar = []
        t = 0
        for i in range(len(pontas)):
            for j in range(len(pontas[i])):
                while t < len(remanej_exerc):
                    if t % 3 == 1:
                        if len(remanej_exerc) > 0:
                            if pontas[i][j] == 1:
                                    print(remanej_exerc[t],"kkkk")
                            if pontas[i][j] == remanej_exerc[t]:
                                
                                for q in range(len(vari[remanej_exerc[t-1]]["fronteira"])):
                                    for ii in range(len(pontas)):
                                        for jj in range(len(pontas[ii])):
                                            if len(remanej_exerc) > 0:
                                            
                                                #print(remanej_exerc,t)
                                                #print(remanej_exerc[t-1])
                                                #print(vari[remanej_exerc[t-1]]["fronteira"],q)
                                                
                                                if vari[remanej_exerc[t-1]]["fronteira"][q] == pontas[ii][jj] and pontas[ii][jj] not in remanej_specif2:
                                                    remanej_specif1.append(remanej_exerc[t-1])
                                                    remanej_specif2.append(pontas[ii][jj])
                                                if q + 1 == len(vari[remanej_exerc[t-1]]["fronteira"]):
                                                    if len(remanej_specif1) > 0:
                                                        if len(remanej_specif1) == 1:
                                                            del remanej_specif1[-1]
                                                            del remanej_specif2[-1]
                                                        else:
                                                            
                                                            if remanej_specif1[-1] != remanej_specif1[-2]:
                                                                del remanej_specif1[-1]
                                                                del remanej_specif2[-1]
                                                    
                                                    
                                                    
                                                    #if q +1 == len(vari[remanej_exerc[t-1]]["fronteira"]):
                                                     #   del remanej_exerc[t-1]
                                                      #  del remanej_exerc[t-1]
                                                       # del remanej_exerc[t-1]
                                                        #t -= 1
                    t += 1
                t = 0
        i = 0
        
        while i < len(remanej_exerc):
            for j in range(len(remanej_specif1)):
                if i % 3 == 0:
                    if remanej_exerc[i] == remanej_specif1[j]:
                        del remanej_exerc[i]
                        del remanej_exerc[i]
                        del remanej_exerc[i]
                        i -= 1
            i += 1
        if len(remanej_specif1) > 0:
            agora = remanej_specif1[0]
        remanej_pontas1 = []
        remanej_pontas2 = []
        remanej_pontas3 = []
        remanej_pontas4 = []
        remanej_pontas5 = []
        remanej_pontas6 = []
        print(remanej_specif1,remanej_specif2,"olaaaa")
        for i in range(len(remanej_specif1)):
            #if i + 1 == len(remanej_specif1):
             #   segura = remanej_specif1[i]
              #  remanej_specif1[i] = -10
            if agora == remanej_specif1[i]:
                remanej_pontas1.append(vari["quantidade_exerc"][remanej_specif2[i]])
                remanej_pontas2.append(remanej_specif2[i])
            if agora != remanej_specif1[i] or i + 1 == len(remanej_specif1):
                print(remanej_pontas2,"rrrrudy")
                while len(remanej_pontas1) > 0:
                    indice = remanej_pontas1.index(max(remanej_pontas1))
                    remanej_pontas3.append(remanej_pontas1[indice])
                    remanej_pontas4.append(remanej_pontas2[indice])
                    remanej_pontas5.append(0)
                    remanej_pontas6.append(0)
                    
                    
                    del remanej_pontas1[indice]
                    del remanej_pontas2[indice]
                print(remanej_pontas3,remanej_pontas4,remanej_pontas5,"wiliam")
                if vari["quantidade_exerc"][remanej_specif1[i-1]] > 3:
                    exerc_passa = 3
                else:
                    exerc_passa = vari["quantidade_exerc"][remanej_specif1[i-1]] - 1
                
                if len(remanej_pontas4) >= 3:
                    while remanej_pontas3[-1] != remanej_pontas3[-2] and exerc_passa != 0:
                        remanej_pontas3[-1] += 1
                        remanej_pontas5[-1] += 1
                        remanej_pontas6[-1] -= 1
                        exerc_passa -= 1
                    while remanej_pontas3[-2] != remanej_pontas3[-3] and exerc_passa != 0:
                        if exerc_passa > 2:
                            remanej_pontas3[-1] += 1
                            remanej_pontas5[-1] += 1
                            remanej_pontas6[-1] -= 1
                            exerc_passa -= 1
                            remanej_pontas3[-2] += 1
                            remanej_pontas5[-2] += 1
                            remanej_pontas6[-2] -= 1
                            exerc_passa -= 1
                        else:
                            remanej_pontas3[-1] += 1
                            remanej_pontas5[-1] += 1
                            remanej_pontas6[-1] += 1
                            exerc_passa -= 1
                    contador = -1
                    while exerc_passa != 0:
                        remanej_pontas3[contador] += 1
                        remanej_pontas5[contador] += 1
                        remanej_pontas6[contador] -= 1
                        exerc_passa -= 1
                        contador -= 1
                if len(remanej_pontas4) == 2:
                    while remanej_pontas3[-1] != remanej_pontas3[-2] and exerc_passa != 0:
                        remanej_pontas3[-1] += 1
                        remanej_pontas5[-1] += 1
                        remanej_pontas6[-1] -= 1
                        exerc_passa -= 1
                    contador = -1
                    while exerc_passa != 0:
                        remanej_pontas3[contador] += 1
                        remanej_pontas5[contador] += 1
                        remanej_pontas6[contador] -= 1
                        exerc_passa -= 1
                        contador -= 1
                        if contador == -3:
                            contador = -1

                    #print(remanej_pontas3,remanej_pontas4,remanej_pontas5,"ttttt")
                print(remanej_pontas4,"quiabo")
                for t in range(len(remanej_pontas4)):
                    remanej_exerc.append(remanej_specif1[i-1])
                    remanej_exerc.append(remanej_pontas4[t])
                    remanej_exerc.append(remanej_pontas5[t])
                    print(remanej_specif1[i-1],remanej_pontas4[t],remanej_pontas5[t])
                
                agora = remanej_specif1[i]
                remanej_pontas1 = []
                remanej_pontas2 = []
                remanej_pontas3 = []
                remanej_pontas4 = []
                remanej_pontas5 = []
                remanej_pontas6 = []
                if agora == remanej_specif1[i]:
                    remanej_pontas1.append(vari["quantidade_exerc"][remanej_specif2[i]])
                    remanej_pontas2.append(remanej_specif2[i])
                    

        print(remanej_exerc,"gggghhh")
        
                
        
        
                                            
                                            
                                    
        remanej2_exerc = []
        
        pontas_way3 = []
        i = 0
        j = 0
        dist = 0
        for i in range(len(pontas_way2)):
            pontas_way3.append([])
            for j in range(len(pontas_way2[i])):
                pontas_way3[i].append(pontas_way2[i][j])
                pontas_way3[i].append(0)
                
        for i in range(len(pontas_way3)):
            for j in range(len(pontas_way3[i])):
                if j % 2 == 0:
                    for t in range(len(remanej_exerc)):
                        if t % 3 == 1:
                            if pontas_way3[i][j] == 1:
                                print(pontas_way3[i][j],remanej_exerc[t])
                            if pontas_way3[i][j] == remanej_exerc[t]:
                                pontas_way3[i][j+1] += remanej_exerc[t+1]
        
                #for t in range(len(remanej_exerc)):
                 #   if t % 3 == 1:
                  #      if remanej_exerc[t] == pontas_way2[i][j]:
                   #         if j == 0:
                    #            pontas_way3[i][1] = remanej_exerc[t+1]
                                
                     #       else:
                      #          pontas_way3[i][j*2+1] = remanej_exerc[t+1]
        print(pontas_way3)
        vari["run6"] = True
        update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
        while vari["run6"] == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vari["run4"] = False
                    vari["running"] = False
                    vari["run5"] = False
                    vari["run2"] = False
                    vari["troca"] = False
                    vari2["exerc_am"] = 0
                    vari2["exerc_as"] = 0
                    vari2["exerc_af"] = 0
                    vari2["exerc_asi"] = 0
                    vari2["exerc_eu"] = 0
                    vari2["exerc_oc"] = 0
                    vari["run1"] = False
                    vari["run3"] = False
                    vari["run6"] = False
                    vari["run7"] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        vari["run6"] = False

                                
                                
        
        exerc_pontas = []
        exerc_pontas2 = []
        valor_pontas = []
        for i in range(len(pontas_way3)):
            valor = 0
            exerc_pontas.append([])
            valor_pontas.append([])
            exerc_pontas2.append([])
            for j in range(len(pontas_way3[i])):
                if j % 2 == 0:
                    
                    
                    exerc_pontas[i].append(vari["quantidade_exerc"][pontas_way3[i][j]])
                    exerc_pontas2[i].append(vari["quantidade_exerc"][pontas_way3[i][j]] + pontas_way3[i][j+1])
                    
            

        print(exerc_pontas)
        print(exerc_pontas2,"pontaaaas2")
        
        passar_pais = []
        passar_exerc = []
        passar_anterior = []
        #for i in range(len(pontas_way3)):
         #   for j in range (len(pontas_way3)):
          #      if j % 2 == 1:
           #         pontas_way3[i][j] = 0
        print(pontas_way3,"wayyyy")
        pontas_way4 = []
        for i in range(len(pontas_way2)):
            pontas_way4.append([])
            for j in range(len(pontas_way2[i])):
                pontas_way4[i].append(pontas_way2[i][j])
        print(pontas_way4)
        
        
        i = 0
        while i < len(pontas_way4):
            nao = 0
            maxi = exerc_pontas[i].index(max(exerc_pontas[i]))
            
            passar_pais.append([])
            passar_exerc.append([])
            passar_anterior.append([])
            
            for j in range(len(pontas_way4[i])):
                
                for a in range(len(vari[pontas_way2[i][maxi]]["fronteira"])):
                    #print(passar_pais,pontas_way2,i,j,vari[pontas_way2[i][maxi]]["fronteira"],a,len(vari[pontas_way2[i][maxi]]["fronteira"]))
                    if vari[pontas_way2[i][maxi]]["fronteira"][a] == pontas_way4[i][j]:
                        
                        passar_pais[i].append(pontas_way4[i][j])
                        passar_exerc[i].append(vari["quantidade_exerc"][pontas_way4[i][j]] + pontas_way3[i][j*2+1])
                        passar_anterior[i].append(pontas_way3[i][j*2+1])
            
            minimos = []
            print(passar_exerc[i],passar_pais[i])
            passar_exerc2 = []
            passar_pais2 = []
            passar_anterior2 = []
            
            while len(passar_exerc[i]) > 0:
                indice = passar_exerc[i].index(max(passar_exerc[i]))
                passar_exerc2.append(passar_exerc[i][indice])
                passar_pais2.append(passar_pais[i][indice])
                passar_anterior2.append(passar_anterior[i][indice])
                del passar_exerc[i][indice]
                del passar_pais[i][indice]
                del passar_anterior[i][indice]
            
            tt = 0
            if len(pontas_way2[i]) == 1:
                print(pontas_way2[i],passar_exerc2,vari["quantidade_exerc"][pontas_way2[i][maxi]])
            if pontas_way2[i][maxi] == 21:
                print(passar_pais2)
            if pontas_way2[i][maxi] == 1:
                print(passar_pais2,passar_exerc2,vari["quantidade_exerc"][pontas_way2[i][maxi]])
            while tt < len(passar_exerc2):
                if passar_exerc2[tt] >= vari["quantidade_exerc"][pontas_way2[i][maxi]]:
                    del passar_exerc2[tt]
                    del passar_pais2[tt]
                    del passar_anterior2[tt]
            
                
                    tt -= 1
                tt += 1
            if pontas_way2[i][maxi] == 21:
                print(passar_pais2,len(passar_pais2))
                
            
                
                    
                
            if pontas_way2[i][maxi] == 1:
                print(passar_pais2,"michal",exerc_pontas[i][maxi],vari["quantidade_exerc"][pontas_way2[i][maxi]],pontas_way3[i][maxi*2+1])
                
            
            
            if exerc_pontas[i][maxi] > 3:
                if vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] > 5:
                    exerc_pass = 3
                    if pontas_way2[i][maxi] == 1:
                        print(passar_pais2,"michal",len(passar_pais2),exerc_pontas[i][maxi])
                        
                elif vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] == 5:
                    exerc_pass = 2
                    if len(passar_pais2) >= 3 and passar_exerc2[-1] == 1 and passar_exerc2[-2] == 1 and passar_exerc2[-3] == 1:
                        exerc_pass = 3
                elif vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] == 4:
                    if len(passar_pais2) >= 2:
                        if passar_exerc2[-1] == 1 and passar_exerc2[-2] == 1:
                            exerc_pass = 2
                        else:
                            exerc_pass = 1
                    else:
                        exerc_pass = 1
            elif exerc_pontas[i][maxi] == 3:
                if vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] > 5:
                    exerc_pass = 2
                elif vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] == 5:
                    exerc_pass = 2
                elif vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] == 4:
                    if len(passar_pais2) >= 2:
                        if passar_exerc2[-1] == 1 and passar_exerc2[-2] == 1:
                            exerc_pass = 2
                    else:
                        exerc_pass = 1
                elif vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] == 3:
                    exerc_pass = 1
            elif exerc_pontas[i][maxi]  == 2:
                if vari["quantidade_exerc"][pontas_way2[i][maxi]] + pontas_way3[i][maxi*2+1] > 1:
                    if pontas_way2[i][maxi] == 21:
                        print(pontas_way3[i][maxi*2+1],"oiii")
                        
                    exerc_pass = 1
            elif exerc_pontas[i][maxi] == 1:
                exerc_pass = 0
            if len(passar_pais2) > 0:
                if pontas_way2[i][maxi] == 1:
                    print(passar_pais2,"michal",len(passar_pais2),exerc_pontas[i][maxi])
                    
                if len(passar_pais2) >= 3:
                    
                    
                    
                    while passar_exerc2[-2] != passar_exerc2[-1] and exerc_pass != 0:
                        pontas_way3[i][maxi*2 + 1] -= 1
                        passar_exerc2[-1] += 1
                        passar_anterior2[-1] +=1
                        exerc_pass -= 1
                    while passar_exerc2[-3] != passar_exerc2[-2] and exerc_pass != 0:
                        if exerc_pass > 1:
                            
                            pontas_way3[i][maxi*2 + 1] -= 1
                            passar_exerc2[-1] += 1
                            passar_anterior2[-1] += 1
                            exerc_pass -= 1
                            pontas_way3[i][maxi*2 + 1] -= 1
                            passar_exerc2[-2] += 1
                            passar_anterior2[-2] += 1
                            exerc_pass -= 1
                        else:
                            pontas_way3[i][maxi*2 + 1] -= 1
                            passar_exerc2[-1] += 1
                            passar_anterior2[-1] += 1
                            exerc_pass -= 1
                    contad = -1
                    while exerc_pass != 0:
                        pontas_way3[i][maxi*2 + 1] -= 1
                        passar_exerc2[contad] += 1
                        passar_anterior2[contad] += 1
                        exerc_pass -= 1
                        contad -= 1
                
                    
                elif len(passar_pais2) == 2:
                    
                    while passar_exerc2[-2] != passar_exerc2[-1] and exerc_pass != 0:
                        pontas_way3[i][maxi*2 + 1] -= 1
                        passar_exerc2[-1] += 1
                        passar_anterior2[-1] +=1
                        exerc_pass -= 1
                    contad = -1
                    while exerc_pass != 0:
                        pontas_way3[i][maxi*2 + 1] -= 1
                        passar_exerc2[contad] += 1
                        passar_anterior2[contad] += 1
                        exerc_pass -= 1
                        contad -= 1
                        if contad == -3:
                            contad = -1
                    
                
                elif len(passar_pais2) == 1:
                        
                    if passar_pais2[-1] == 2:
                        print(passar_exerc2,passar_anterior2[-1],"obaoba")
                    while exerc_pass != 0:
                        pontas_way3[i][maxi*2 + 1] -= 1
                        passar_exerc2[-1] += 1
                        passar_anterior2[-1] += 1
                        exerc_pass -= 1
                    if passar_pais2[-1] == 2:
                        print(passar_exerc2,passar_anterior2[-1],"obaoba")
                        
                        
                    
                    
                
                for vv in range(len(pontas_way3)):
                    for yy in range(len(pontas_way3[vv])):
                        if yy % 2 == 0:
                            for zz in range(len(passar_pais2)):
                                
                                if pontas_way3[vv][yy] == passar_pais2[zz]:
                                    if passar_pais2[zz] == 2:
                                        print(pontas_way3)
                                    pontas_way3[vv][yy + 1] = passar_anterior2[zz]
                                    if passar_pais2[zz] == 2:
                                        print(pontas_way3)
                                        
                                    
            del exerc_pontas[i][maxi]
            del pontas_way2[i][maxi]
            if len(pontas_way2[i]) == 0:
                i += 1            
        pontas_way5 = []
        print(pontas_way3)
        
        for i in range(len(pontas_way3)):
            for j in range(len(pontas_way3[i])):
                if j % 2 == 0:
                    vari["quantidade_exerc"][pontas_way3[i][j]] += pontas_way3[i][j+1]
                    pontas_way5.append(pontas_way3[i][j])
                    
        print(pontas_way3,"oiiii")
        #for i in range(len(remanej_exerc)):
         #   if i % 3 == 1:
          #      for q in range(len(pontas_way4)):
           #         for y in range(len(pontas_way4[q])):
            #            if remanej_exerc[i] == pontas_way4[q][y]:
             #               remanej_exerc[i+1] = 0
        for i in range(len(remanej_exerc)):
            if i % 3 == 1:
                if remanej_exerc[i] not in pontas_way5:
                    vari["quantidade_exerc"][remanej_exerc[i]] += remanej_exerc[i+1]
                vari["quantidade_exerc"][remanej_exerc[i-1]] -= remanej_exerc[i+1]
        print(remanej_exerc,"wwwwwww")
        
            
        
            #for t in range(len(passar_exerc[-i])):
             #   if passar_exerc[i][t] == mini:
              #      minimos.append(passar_pais[i][j])
            #if len(minimos) < passar_exerc[maxi]:
             #   if len(minimos) >=3:
              #      if exerc_pontas[maxi] - 3 >= passar_exerc[mini] + 1:
                    
               #         for z in range(minimos):
                #            remanej_exerc2.append(minimos[z])
                 #           remanej_exerc2.append(1)
                  #      del exerc_pontas[i][maxi]
                   #     del pontas_way2[i][maxi]
                    #    nao = 1
                     #   i -= 1
            #if len(passar_pais) > 3 and nao == 0:
             #   if exerc_pontas[i][maxi] - 3 >= (max(passar_exerc[i]) + 1:
              #      del passar_exerc[i][passar_exerc[i].index(max(passar_exerc[i]))
               #     for c in range(3):
                #        if max
                 #       remanej_exerc2.append(passar_exerc[])
                    
                         
           # i += 1
                    
                
            #if exerc_pontas[i][maxi] - 3 >= passar_exerc[i][mini] + 3:
             #   remanej_exerc2.append(passar_pais[i][mini])
              #  remanej_exerc2.append(3)
            #elif 
                
                
                            
                            
                
                    
            
    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
                        

    
                    
                
def recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2,conta):
    
    #if len(pontas_way2) == 0:
        #pontas_way2.append([])
        #for i in range(len(pontas_way)):
            #for j in range(len(pontas_way[i])):
                #for t in range(len(vari[pontas_way[i][j]]["fronteira"])):
                    #for y in range(len(pontas_way)):
                        #for x in range(len(pontas_way[y])):
                            #if vari[pontas_way[i][j]]["fronteira"][t] == pontas_way[y][x]:
                                
                                
                                #print(pontas_way[i][j],pontas_way[y][x],"obaaaaa")
                                #if pontas_way[i][j] not in pontas_way2[-1] and pontas_way[y][x] not in pontas_way2[-1]:
                                    #print(pontas_way[i][j],pontas_way[y][x],"obaaaaa1")
                                    #pontas_way2[-1].append(pontas_way[i][j])
                                   # pontas_way2[-1].append(pontas_way[y][x])
                                  #  proximo = pontas_way[y][x]
                                 #   recursao_pontas(vari,pontas_way,pontas_way2,proximo)
                                #elif pontas_way[y][x] not in pontas_way2[-1]:
                                    #print(pontas_way[i][j],pontas_way[y][x],"obaaaaa2")
                                    #pontas_way2[-1].append(pontas_way[y][x])
                                   # proximo = pontas_way[y][x]
                                  #  recursao_pontas(vari,pontas_way,pontas_way2,proximo)
                                #elif pontas_way[i][j] not in pontas_way2[-1]:
                                 #   pass
                                
    foi = []

    
    acabou = 0
    
    if len(pontas_way3) == 0:
        pontas_way2.append([])
        
        for i in range(len(pontas_way)):
            for j in range(len(pontas_way[i])):
                if len(pontas_way2[-1]) != 0:
                    pontas_way2.append([])
                
                if 3 == 3:
                    if acabou == 1:
                        acabou = 0
                        foi = []
                        if len(pontas_way2[-1]) != 0:
                            pontas_way2.append([])
                        print("aquiii")
                    foi = []
                    print(pontas_way[i][j],"pontassssss")
                
                
                    
                        
                        
                    for o in range(len(pontas_way)):
                        if pontas_way[i][j] in pontas_way3:
                            if pontas_way[i][j] == 26:
                                print("tttt")
                            break
                        if acabou == 1:
                            acabou = 0
                            foi = []
                            if len(pontas_way2[-1]) != 0:
                                pontas_way2.append([])
                            print("aquiii")
                            break
                        for z in range(len(pontas_way[o])):
                            if acabou == 1:
                                break
                            
                            for t in range(len(vari[pontas_way[i][j]]["fronteira"])):
                                if acabou == 1:
                                    break
                                #if pontas_way[i][j] == 6 or pontas_way[i][j] == 7:
                                 #   print(vari[pontas_way[i][j]]["fronteira"][t],pontas[o][])
                                if pontas_way[i][j] == 14:
                                    print(vari[pontas_way[i][j]]["fronteira"][t],pontas_way[o][z],pontas_way3)
                                if vari[pontas_way[i][j]]["fronteira"][t] == pontas_way[o][z] and pontas_way[o][z] not in pontas_way3 :
                                    if pontas_way[i][j] not in pontas_way3:
                                        pontas_way2[-1].append(pontas_way[i][j])
                                    pontas_way2[-1].append(pontas_way[o][z])
                                    pontas_way3.append(pontas_way[i][j])
                                    pontas_way3.append(pontas_way[o][z])
                                    conta = -1
                                    proximo = pontas_way[o][z]
                                    print("here",len(pontas_way3))
                                    conta = recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2,conta)
                                
        if len(pontas_way2[-1]) == 0:
            del pontas_way2[-1]
    else:
        
        for x in range(len(pontas_way)):
            for w in range(len(pontas_way[x])):
                
                for a in range(len(vari[proximo]["fronteira"])):
                    #print(x,len(pontas_way),w,len(pontas_way[x]),a,len(vari[pontas_way2[-1][-1]]["fronteira"]),"cd")
                                                    
                    if vari[proximo]["fronteira"][a] == pontas_way[x][w] and pontas_way[x][w] not in pontas_way3 :
                        pontas_way2[-1].append(pontas_way[x][w])
                        pontas_way3.append(pontas_way[x][w])
                        foi.append(1)
                        print(conta,"entrando1",a,x,w,proximo,pontas_way3)
                        proximo = pontas_way[x][w]
                        print(conta,"entrando2",a,x,w,proximo)
                        conta = recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2,conta)
                        conta -= 1
                        proximo = pontas_way3[conta]
                        
                        print(conta,"ola1",a,len(vari[proximo]["fronteira"]),x,len(pontas_way),w,len(pontas_way[x]),proximo)
                #for a in range(len(vari[proximo2]["fronteira"])):
                 #   if vari[proximo2]["fronteira"][a] == pontas_way[x][w] and pontas_way[x][w] not in pontas_way3 :
                  #      print("god")
                   #     pontas_way2[-1].append(pontas_way[x][w])
                     #   pontas_way3.append(pontas_way[x][w])
                    #    proximo2 = pontas_way[x][w]
                      #  foi.append(1)
                       # recursao_pontas(vari,pontas_way,pontas_way2,proximo,pontas_way3,proximo2)
                        #proximo = proximo2
                        #proximo2 = pontas_way3[-2]
                        
                        #print("ola2",a)


            if x + 1 == len(pontas_way) :
                print(pontas_way2,"sacaso1",pontas_way3)
                acabou = 1
                return conta
                                            
            
    
    #for i in range(pontas_way2):
     #   for j in range(pontas_way2[i]):
      #      for q in range(pontas_way2):
       #         for w in range(pontas_way2[q]):
        #            for t in range(vari[pontas_way2[i][j]]["fronteira"]):
         #               if vari[pontas_way2[i][j]]["fronteira"][t] == pontas_way2[q][w]:
          #                  for e in range(pontas_way2[q]):
           #                     pontas_way2[i].append(pontas_way2[q][e])
            #                del pont
                            
                        
    
                                    
                                    
    print(pontas_way2,"eiiita")
                                   
                                                    
                                                    
                    #if proximo == 11:
                     #   print(vari[proximo]["fronteira"][t],pontas_way[i][j],"james")
                    
                        
                        
                       
            
        
                    
                    
                





    
def recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista):
    
    
    if 2 == 2:
        while i < len(agrupamento):
            if fimm == 50:
                break
        
                
            
                
            
            while j < len(agrupamento[i]):
                
                
                
                if dist >= maximo_pontas:
                    dist = 0 
                if recursao != 1:
                    restante = agrupamento[i][j]
                    m += 1
                    distancia.append([])
                    
                    cont = -1
                    caminhos = []
                    caminho = []
                    caminhos.append(agrupamento[i][j])
                    
                
                
                if len(distancia[m]) != 0:
                     
                    cont = -1
                    
                    
                    m +=1
                    dist = 0
                    
                    restante = agrupamento[i][j]
                    distancia.append([])
                    caminhos = []
                    caminho = []
                    caminhos.append(agrupamento[i][j])
                
                h = 0
                n = 0
                cont += 1
                
                caminho.append([])
                ttt = 0
                
                while dist < maximo_pontas:
                    if vari["quantidade_exerc"][agrupamento[i][j]] == 1:
                        
                        distancia[m].append(-10)
                        j += 1
                        break

                    dist +=1
                    
                    hh = 0
                    xx = -1
                    for q in range(len(pontas)):
                        if len(pontas[q]) == 0:
                            break
                            
                        if agrupamento[i][j] in agrupamento[q]:
                            break
                    
                    while hh < len(vari[restante]["fronteira"]):
                        
                        
                        
                            
                        
                        if vari[restante]["fronteira"][hh] in agrupamento[q] or vari[restante]["fronteira"][hh] in pontas[q]:
                            caminho[cont].append(vari[restante]["fronteira"][hh])
                            xx += 1
                            
                       
                            
                        
                        
                        
                           
                        for q in range(len(pontas)):
                            if len(pontas[q]) == 0:
                                break
                            
                            if agrupamento[i][j] in agrupamento[q]:
                                break
                        n = 0
                        
                        if len(caminho[cont]) != 0:
                            
                            while n <(len(pontas[q])):
                                
                                
                                if caminho[cont][xx] == pontas[q][n] and caminho[cont][xx] != agrupamento[i][j]:
                                    
                                    dista.append(dist)
                                    dista.append(caminho[cont][xx])
                                    caminhos_tempor = []
                                    for tm in range(len(caminhos)):
                                        caminhos_tempor.append(caminhos[tm])
                                    
                                    dista.append(caminhos_tempor)
                                    
                                    
                                   
                                    
                                    if len(pontas[q]) == 0:
                                        
                                        principal = agrupamento[i][j]
                                        
                                    
                                    soma += 1
                                    
                                        
                                    
                                    
                                    
                                    
                                n += 1
                                        
                                
                                
                        hh += 1
                        
                        
                        
                        
                                    
                         
                    
                    
                    
                    while h < len(caminho[cont]):
                        
                        
                        
                        if len(pontas[q]) != 0 and  dist < maximo_pontas:
                            
                                
                            if caminho[cont][h] not in caminhos  :
                                
                                if len(cami) >= 2:
                                    if cami[-1] == cami[-2]:

                                        
                                        del cami[-1]
                                        
                                        
                                    else:
                                
                                
                                        restante = caminho[cont][h]
                                        caminhos.append(caminho[cont][h])
                                        cami.append(caminho[cont][h])
                                        
                                        
                                        
                                        
                                        
                                        
                                        rerc += 1
                                        valor_t = rerc
                                        
                                        recursao = 1
                                        i,j,principal,valor_t = recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista)
                                        h += 1
                                        if valor_t == 1:
                                            rerc -= 1
                                        
                                        del caminhos[-1]
                                        
                                        
                                else:
                                
                                
                                    restante = caminho[cont][h]
                                    caminhos.append(caminho[cont][h])
                                    cami.append(caminho[cont][h])
                                        
                                        
                                        
                                    rerc += 1
                                    valor_t = rerc
                                    
                                    recursao = 1
                                    i,j,principal,valor_t = recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista)
                                    h += 1
                                    if valor_t == 1:
                                        rerc -= 1
                                    del caminhos[-1]
                                    

                                
                                    
                            else:
                                
                                while caminho[cont][h] in caminhos:
                                    
                                    
                                    h += 1
                                    
                                    if h >= len(caminho[cont]):
                                        
                                        
                                        del caminho[cont]
                                        nova_lis = []
                                        nova_lis2 = []
                                        if len(caminho) != 0:
                                        
                                            return i, j,principal,valor_t
                                        else:
                                            
                                            for wi in range(len(pontas[q])):
                                                nova_lis.append([])
                                                nova_lis2.append([])
                                                for we in range(len(dista)):
                                                    if we % 3 == 1:
                                                        if dista[we] == pontas[q][wi]:
                                                            nova_lis[-1].append(dista[we-1])
                                                            nova_lis2[-1].append(dista[we+1])
                                            
                                        
                                            for wt in range(len(nova_lis)):
                                                
                                                distancia[m].append(agrupamento[i][j])
                                                distancia[m].append(min(nova_lis[wt]))
                                                distancia[m].append(pontas[q][wt])
                                                distancia[m].append(nova_lis2[wt][nova_lis[wt].index(min(nova_lis[wt]))])
                                            
                                            
                                            
                                                                    
                                            dist = 100
                                            j += 1
                                            cami = []
                                            caminho = []
                                            caminhos = []
                                            h = 100
                                            dista = []
                                            
                                            break
                                            
                                            
                                    
                                if h < len(caminho[cont]):
                                    
                                    
                                    if len(cami) >= 2:
                                        if cami[-1] == cami[-2]:
                                            
                                            del cami[-1]
                                            
                                        else:
                                            cami.append(caminho[cont][h])
                                            restante = caminho[cont][h]
                                            caminhos.append(caminho[cont][h])
                                            
                                            
                                            
                                            rerc += 1
                                            valor_t = rerc
                                            
                                            recursao = 1
                                            i,j,principal,valor_t = recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista)
                                            h += 1
                                            if valor_t == 1:
                                                rerc -= 1
                                            
                                            
                                            
                                            del caminhos[-1]
                                            
                                    
                                    else:
                                        cami.append(caminho[cont][h])
                                        restante = caminho[cont][h]
                                        caminhos.append(caminho[cont][h])
                                            
                                            
                                        rerc += 1
                                        valor_t = rerc
                                        
                                        recursao = 1
                                        i,j,principal,valor_t = recursao_distancia(agrupamento,pontas,vari,maximo_pontas,recursao,restante,dist,j,i,h,importante,q,distancia,m,caminhos,fimm,cont,caminho,principal,rerc,soma,valor_t,cami,dista)
                                        h += 1   
                                        if valor_t == 1:
                                            rerc -= 1
                                            
                                            
                                            
                                        del caminhos[-1]
                                        

                    
                                        
                                    
                                    
                            
                    
                            
                            
                            
                            
                            
                            
                            
                                
                                
                                
                        
                            
                                
                        else:
                            

                            if dist >= maximo_pontas:
                                
                                del caminho[cont]
                                
                                
                                return i,j,principal,valor_t
                                
                                
                                
                                        
                            
                    
                      
                    del caminho[cont]
                    nova_lis = []
                    nova_lis2 = []
                    if len(caminho) == 0:
                        for wi in range(len(pontas[q])):
                            nova_lis.append([])
                            nova_lis2.append([])
                            for we in range(len(dista)):
                                if we % 3 == 1:
                                    if dista[we] == pontas[q][wi]:
                                        nova_lis[-1].append(dista[we-1])
                                        nova_lis2[-1].append(dista[we+1])
                        
                                        
                        for wt in range(len(nova_lis)):
                                                
                            distancia[m].append(agrupamento[i][j])
                            distancia[m].append(min(nova_lis[wt]))
                            distancia[m].append(pontas[q][wt])
                            distancia[m].append(nova_lis2[wt][nova_lis[wt].index(min(nova_lis[wt]))])
                        
                        dist = 100
                        j += 1
                        cami = []
                        caminho = []
                        caminhos = []
                        h = 100
                        dista = []
                        
                        break

                                
                    else:
                        return i,j,principal,valor_t
            i += 1
            
            
            if i != len(agrupamento):
                j = 0
            
        i = 0
        
        return i,j, principal,valor_t
def maquina_logica_inicio1(alea,vari,qnt_rodada,vez,ter_prio,ter_prio2,qnt_exerc2,q,prio_max,inicial):
    qnt_exerc = []
    while inicial == True:
        for i in range(len(vari["territorio"][vez])):
                        
            if vari[vari["territorio"][vez][i]]["continente"] == prio_max:
                ter_prio.append(vari["territorio"][vez][i])
                            
        if ter_prio != []:
            while q < 99:
                for i in range(len(vari["territorio"][vez])):
                        
                    if vari[vari["territorio"][vez][i]]["continente"] == prio_max:
                        ter_prio2.append(vari["territorio"][vez][i])
                for i in range(len(ter_prio)):
                    if len(qnt_exerc2) != len(ter_prio):
                        qnt_exerc2.append(vari["quantidade_exerc"][ter_prio[i]])
                z = qnt_exerc2.index(max(qnt_exerc2))

                          
                while len(ter_prio2) > 0:
                    for j in range(len(vari[ter_prio2[z]]["fronteira"])):
                        if vari["quantidade_exerc"][vari[ter_prio2[z]]["fronteira"][j]] == q:
                            if vari["cores"][vari[ter_prio2[z]]["fronteira"][j]] != vez:
                                while vari["quantidade_exerc"][ter_prio2[z]] < 4:
                                    
                                    vari["quantidade_exerc"][ter_prio2[z]] += 1
                                    qnt_rodada -= 1
                                    q = 100
                                    
                                                
                                            
                                q = 100
                                break
                                
                    del ter_prio2[z]
                                
                    del qnt_exerc2[z]
                    if len(ter_prio2) > 0:
                        z = qnt_exerc2.index(max(qnt_exerc2))
                    if q == 100:
                        break
                    if len(ter_prio2) == 0:
                        ter = []
                        qnt_exerc = []
                        for i in range(len(vari["territorio"][vez])):
                            ter.append(vari["territorio"][vez][i])
                        for i in range(len(ter)):
                            if len(qnt_exerc) != len(ter):
                                qnt_exerc.append(vari["quantidade_exerc"][ter[i]])
                        z = qnt_exerc.index(max(qnt_exerc))
                        while len(ter) > 0:
                            for j in range(len(vari[ter[z]]["fronteira"])):
                                if vari["quantidade_exerc"][vari[ter[z]]["fronteira"][j]] == q:
                                    if vari["cores"][vari[ter[z]]["fronteira"][j]] != vez:
                                        while vari["quantidade_exerc"][ter[z]] < 4:
                                            print("ola")     
                                            vari["quantidade_exerc"][ter[z]] += 1
                                            qnt_rodada -= 1
                                            q = 100
                                                        
                                                    
                                        q = 100
                                        break
                                        
                            del ter[z]
                                        
                            del qnt_exerc[z]
                            if len(ter) > 0:
                                z = qnt_exerc.index(max(qnt_exerc))
                            if q == 100:
                                break

                if q == 100:
                    break
                print(q)
                q += 1    
            break                    
                                            
                    
                    
                        
                
        else:
            alea = random.randrange(1,8)
            break
        ter_prio = []
        ter_prio2 = []
        qnt_exerc = []
        qnt_exerc2 = []
        print("heheu")
        break
    ter_prio = []
    ter_prio2 = []
    qnt_exerc = []
    qnt_exerc2 = []
    print("heheu")
    
        
    return ter_prio,ter_prio2,qnt_exerc,qnt_exerc2,qnt_rodada,alea
def maquina_exerc1(alea,vari,qnt_rodada,vez,prio_max):
    
    
    ter_prio = []
    ter_prio2 = []
    ter_prio_prio = []
    qnt_exerc = []
    qnt_exerc2 = []
    j = 0
    if alea == 1:
        prio_max = vari["prioridade"][vez][-1]
    if alea == 2 or alea == 3:
        prio_max = vari["prioridade"][vez][-2]
    if alea == 2 or alea == 1 or alea == 3 or (vari["objetivo"][vez] == 13  or vari["objetivo"][vez] == 14):
        for i in range(len(vari["territorio"][vez])):
                    
            if vari[vari["territorio"][vez][i]]["continente"] == prio_max:
                ter_prio.append(vari["territorio"][vez][i])
                       
        if ter_prio != []:
            for i in range(len(ter_prio)):
                j = 0
                
                while j <(len(vari[ter_prio[i]]["fronteira"])):
                    
                    if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                        
                        ter_prio_prio.append(ter_prio[i])
                        if len(qnt_exerc) != len(ter_prio_prio):
                            qnt_exerc.append(vari["quantidade_exerc"][ter_prio[i]])
                            j = 100
                    j += 1

            for i in range(len(ter_prio)):
                j = 0
                
                while j <(len(vari[ter_prio[i]]["fronteira"])):
                    
                    if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                        
                        
                        
                            
                        if vari["quantidade_exerc"][vari[ter_prio[i]]["fronteira"][j]] > 2:
                            ter_prio2.append(ter_prio[i])
                            if len(qnt_exerc) != len(ter_prio2):
                                qnt_exerc2.append(vari["quantidade_exerc"][ter_prio[i]])
                                j = 100
                    j += 1
        else:
            alea = random.randrange(1,8)
        if len(qnt_exerc2) > 0:              
            i = qnt_exerc2.index(min(qnt_exerc2))
            if qnt_exerc2[i] < 3:
                vari["quantidade_exerc"][ter_prio2[i]] += 1
                qnt_rodada -= 1
        if len(qnt_exerc) > 0 and len(qnt_exerc2) > 0:
            j = qnt_exerc.index(min(qnt_exerc))
            if qnt_exerc2[i] > 2:
                    
                if qnt_exerc[j] < 3:
                    vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                    qnt_rodada -= 1
                else:
                    ale = random.randrange(0, len(ter_prio_prio))
                    vari["quantidade_exerc"][ter_prio_prio[ale]] += 1
                    qnt_rodada -= 1
        elif len(qnt_exerc) > 0 and len(qnt_exerc2) == 0:
            j = qnt_exerc.index(min(qnt_exerc))
            if qnt_exerc[j] < 3:
                vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                qnt_rodada -= 1
            else:
                ale = random.randrange(0, len(ter_prio_prio))
                vari["quantidade_exerc"][ter_prio[ale]] += 1
                qnt_rodada -= 1
            
                    
        
        
        
        
        ter_prio = []
        
    if alea ==7:
        ale = random.randrange(0, len(vari["territorio"][vez]))
        vari["quantidade_exerc"][vari["territorio"][vez][ale]] += 1
        qnt_rodada -= 1
    
    
    return qnt_rodada,alea
def maquina_exerc2(alea,vari,qnt_rodada,vez):
    ter_prio = []
    ter_prio2 = []
    ter_prio_prio = []
    qnt_exerc = []
    qnt_exerc2 = []
    if alea == 5 or alea == 4 or alea == 6:
        alvo = vari["prioridade"][vez][0]
        if alvo + 1 <= vari["numjogad"]: 
            porcentagem = []
            porcentagem.append(vari2["america_do_norte"][alvo]/9)
            porcentagem.append(vari2["america_do_sul"][alvo]/4)
            porcentagem.append(vari2["africa"][alvo]/6)
            porcentagem.append(vari2["europa"][alvo]/7)
            porcentagem.append(vari2["asia"][alvo]/12)
            porcentagem.append(vari2["oceania"][alvo]/4)
            if porcentagem.index(max(porcentagem)) == 0:
                vari["prioridade"][vez].append("America do Norte")
            if porcentagem.index(max(porcentagem)) == 1:
                vari["prioridade"][vez].append("America do Sul")
            if porcentagem.index(max(porcentagem)) == 2:
                vari["prioridade"][vez].append("Africa")
            if porcentagem.index(max(porcentagem)) == 3:
                vari["prioridade"][vez].append("Europa")
            if porcentagem.index(max(porcentagem)) == 4:
                vari["prioridade"][vez].append("Asia")
            if porcentagem.index(max(porcentagem)) == 5:
                vari["prioridade"][vez].append("Oceania")
            prio_max = vari["prioridade"][vez][-1]
            del vari["prioridade"][vez][-1]
            for i in range(len(vari["territorio"][vez])):
                if vari[vari["territorio"][vez][i]]["continente"] == prio_max:
                    ter_prio.append(vari["territorio"][vez][i])
            
            if ter_prio != []:
                for i in range(len(ter_prio)):
                    j = 0
                    
                    while j <(len(vari[ter_prio[i]]["fronteira"])):
                        
                        if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                            
                            ter_prio_prio.append(ter_prio[i])
                            if len(qnt_exerc) != len(ter_prio_prio):
                                qnt_exerc.append(vari["quantidade_exerc"][ter_prio[i]])
                                j = 100
                        j += 1

                for i in range(len(ter_prio)):
                    j = 0
                    
                    while j <(len(vari[ter_prio[i]]["fronteira"])):
                        
                        if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                            
                            
                            
                                
                            if vari["quantidade_exerc"][vari[ter_prio[i]]["fronteira"][j]] > 2:
                                ter_prio2.append(ter_prio[i])
                                if len(qnt_exerc) != len(ter_prio2):
                                    qnt_exerc2.append(vari["quantidade_exerc"][ter_prio[i]])
                                    j = 100
                        j += 1
            else:       
                alea = random.randrange(1,8)
            if len(qnt_exerc2) > 0:              
                i = qnt_exerc2.index(min(qnt_exerc2))
                if qnt_exerc2[i] < 3:
                    vari["quantidade_exerc"][ter_prio2[i]] += 1
                    qnt_rodada -= 1
            if len(qnt_exerc) > 0 and len(qnt_exerc2) > 0:
                j = qnt_exerc.index(min(qnt_exerc))
                if qnt_exerc2[i] > 2:
                        
                    if qnt_exerc[j] < 3:
                        vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                        qnt_rodada -= 1
                    else:
                        ale = random.randrange(0, len(ter_prio_prio))
                        vari["quantidade_exerc"][ter_prio_prio[ale]] += 1
                        qnt_rodada -= 1
            elif len(qnt_exerc) > 0 and len(qnt_exerc2) == 0:
                j = qnt_exerc.index(min(qnt_exerc))
                if qnt_exerc[j] < 3:
                    vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                    qnt_rodada -= 1
                else:
                    ale = random.randrange(0, len(ter_prio_prio))
                    vari["quantidade_exerc"][ter_prio_prio[ale]] += 1
                    qnt_rodada -= 1


                
                                
            else:
                        
                alea = random.randrange(1,8)
        else:
            alea = random.randrange(1,8)
                        
        ter_prio = []
        ter_prio_prio = []
        ter_prio2 = []
        qnt_exerc = []
        qnt_exerc2 = []
        
    return qnt_rodada,alea
def maquina_exerc3(alea,vari,qnt_rodada,vez,porcentagem):
    ter_prio = []
    ter_prio2 = []
    ter_prio_prio = []
    qnt_exerc = []
    qnt_exerc2 = []
    if alea == 5 or alea == 4 or alea == 6:
        porc = []
        if vari["prioridade"][vez][0] == "America do Norte" or vari["prioridade"][vez][1] == "America do Norte":
            porc.append(porcentagem[0])
            porc.append("America do Norte")
        if vari["prioridade"][vez][0] == "America do Sul" or vari["prioridade"][vez][1] == "America do Sul":
            porc.append(porcentagem[1])
            porc.append("America do Sul")
        if vari["prioridade"][vez][0] == "Africa" or vari["prioridade"][vez][1] == "Africa":
            porc.append(porcentagem[2])
            porc.append("Africa")
        if vari["prioridade"][vez][0] == "Europa" or vari["prioridade"][vez][1] == "Europa":
            porc.append(porcentagem[3])
            porc.append("Europa")
        if vari["prioridade"][vez][0] == "Asia" or vari["prioridade"][vez][1] == "Asia":
            porc.append(porcentagem[4])
            porc.append("Asia")
        if vari["prioridade"][vez][0] == "Oceania" or vari["prioridade"][vez][1] == "Oceania":
            porc.append(porcentagem[5])
            porc.append("Oceania")

        if porc[0] >= porc[2]:
            prio_max = porc[1]
        else:
            prio_max = porc[3]
        for i in range(len(vari["territorio"][vez])):
            if vari[vari["territorio"][vez][i]]["continente"] == prio_max:
                ter_prio.append(vari["territorio"][vez][i])
            
            if ter_prio != []:
                for i in range(len(ter_prio)):
                    j = 0
                    
                    while j <(len(vari[ter_prio[i]]["fronteira"])):
                        
                        if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                            
                            ter_prio_prio.append(ter_prio[i])
                            if len(qnt_exerc) != len(ter_prio_prio):
                                qnt_exerc.append(vari["quantidade_exerc"][ter_prio[i]])
                                j = 100
                        j += 1

                for i in range(len(ter_prio)):
                    j = 0
                    
                    while j <(len(vari[ter_prio[i]]["fronteira"])):
                        
                        if vari["cores"][vari[ter_prio[i]]["fronteira"][j]] != vez:
                                                       
                            
                                
                            if vari["quantidade_exerc"][vari[ter_prio[i]]["fronteira"][j]] > 2:
                                ter_prio2.append(ter_prio[i])
                                if len(qnt_exerc) != len(ter_prio2):
                                    qnt_exerc2.append(vari["quantidade_exerc"][ter_prio[i]])
                                    j = 100
                        j += 1
            else:
                        
                alea = random.randrange(1,8)
        if len(qnt_exerc2) > 0:              
            i = qnt_exerc2.index(min(qnt_exerc2))
            if qnt_exerc2[i] < 3:
                vari["quantidade_exerc"][ter_prio2[i]] += 1
                print(qnt_rodada,"qnt1")
                qnt_rodada -= 1
        if len(qnt_exerc) > 0 and len(qnt_exerc2) > 0:
            j = qnt_exerc.index(min(qnt_exerc))
            if qnt_exerc2[i] > 2:
                        
                if qnt_exerc[j] < 3:
                    vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                    print(qnt_rodada,"qnt2")
                    qnt_rodada -= 1
                            
                else:
                    ale = random.randrange(0, len(ter_prio_prio))
                    vari["quantidade_exerc"][ter_prio_prio[ale]] += 1
                    print(qnt_rodada,"qnt3")
                    qnt_rodada -= 1
        elif len(qnt_exerc) > 0 and len(qnt_exerc2) == 0:
            j = qnt_exerc.index(min(qnt_exerc))
            if qnt_exerc[j] < 3:
                vari["quantidade_exerc"][ter_prio_prio[j]] += 1
                print(qnt_rodada,"qnt4")
                qnt_rodada -= 1
            else:
                ale = random.randrange(0, len(ter_prio_prio))
                vari["quantidade_exerc"][ter_prio_prio[ale]] += 1
                print(qnt_rodada,"qnt5")
                qnt_rodada -= 1


                
                                
            
        
                        
        ter_prio = []
        ter_prio_prio = []
        ter_prio2 = []
        qnt_exerc = []
        qnt_exerc2 = []
        
    return qnt_rodada,alea


def num_jogad(screen):
    font = pygame.font.Font("freesansbold.ttf",18)
    num_jogad = font.render("Quantos jogadores?3 ou 4 ou 5 ou 6",True,(255,255,255))
    screen.blit(num_jogad, (50, 50))

def update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("freesansbold.ttf",14)
    font2 = pygame.font.Font("freesansbold.ttf",7)
    font3 = pygame.font.Font("freesansbold.ttf",25)
    screen.blit(vari["mapaimg"],( vari["mapaX"], vari["mapaY"]))
    for t in range(6):
        vari["territorio"][t] = []
        for i in range(42):
            
            if vari["cores"][i] == t:
                vari["territorio"][t].append(i)
    ter_pret = len(vari["territorio"][0])
    ter_azul = len(vari["territorio"][1])
    ter_verm = len(vari["territorio"][2])
    ter_verd = len(vari["territorio"][3])
    ter_amar = len(vari["territorio"][4])
    ter_bran = len(vari["territorio"][5])
    ter_pret_qnt = 0
    ter_azul_qnt = 0
    ter_verm_qnt = 0
    ter_verd_qnt = 0
    ter_amar_qnt = 0
    ter_bran_qnt = 0
    for i in range(ter_pret):
        ter_pret_qnt += vari["quantidade_exerc"][vari["territorio"][0][i]]
    for i in range(ter_azul):
        ter_azul_qnt += vari["quantidade_exerc"][vari["territorio"][1][i]]
    for i in range(ter_verm):
        ter_verm_qnt += vari["quantidade_exerc"][vari["territorio"][2][i]]
    for i in range(ter_verd):
        ter_verd_qnt += vari["quantidade_exerc"][vari["territorio"][3][i]]
    for i in range(ter_amar):
        ter_amar_qnt += vari["quantidade_exerc"][vari["territorio"][4][i]]
    for i in range(ter_bran):
        ter_bran_qnt += vari["quantidade_exerc"][vari["territorio"][5][i]]
    txt_pret = font.render(str(ter_pret)+":"+str(ter_pret_qnt),True,(255,255,255))
    txt_azul = font.render(str(ter_azul)+":"+str(ter_azul_qnt),True,(255,255,255))
    txt_verm = font.render(str(ter_verm)+":"+str(ter_verm_qnt),True,(255,255,255))
    txt_verd = font.render(str(ter_verd)+":"+str(ter_verd_qnt),True,(255,255,255))
    txt_amar = font.render(str(ter_amar)+":"+str(ter_amar_qnt),True,(255,255,255))
    txt_bran = font.render(str(ter_bran)+":"+str(ter_bran_qnt),True,(255,255,255))
    screen.blit(txt_pret,(50,50))
    screen.blit(txt_azul,(50,70))
    screen.blit(txt_verm,(50,90))
    screen.blit(txt_verd,(90,50))
    screen.blit(txt_amar,(90,70))
    screen.blit(txt_bran,(90,90))
    if vari["troca"] == True:
        txt_trocao = font.render("Trocaaaaaaaaaa",True,(255,255,255))
        screen.blit(txt_trocao,(300,300))
    if vari2["exerc_am"] > 0:
        txt_exerc_bonus = font.render("Coloque 5 tropas em paises da America do Norte",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "America do Norte":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"] - 20))
                
    if vari2["exerc_as"] > 0:
        txt_exerc_bonus = font.render("Coloque 2 tropas em paises da America do Sul",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "America do Sul":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"]  - 20))
    if vari2["exerc_af"] > 0:
        txt_exerc_bonus = font.render("Coloque 3 tropas em paises da Africa",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "Africa":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"]  - 20))
    if vari2["exerc_eu"] > 0:
        txt_exerc_bonus = font.render("Coloque 5 tropas em paises da Europa",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "Europa":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"]  - 20))
    if vari2["exerc_asi"] > 0:
        txt_exerc_bonus = font.render("Coloque 7 tropas em paises da Asia",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "Asia":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"]  - 20))
    if vari2["exerc_oc"] > 0:
        txt_exerc_bonus = font.render("Coloque 2 tropas em paises da Oceania",True,(255,255,255))
        screen.blit(txt_exerc_bonus,(500, 70))
        for i in range(42):
            if vari[i]["continente"] == "Oceania":
                screen.blit(pygame.image.load("circle2.png"),(vari[i]["X"] - 20,vari[i]["Y"]  - 20))


    if vari["run3"] == True:
        if vari["remanejo1"] == -1 and vari["remanejo2"] == -1:
            txt_remanejo = font.render("Escolha um pais para serem passadas as suas tropas para outro",True,(255,255,255))
        if vari["remanejo1"] != -1 and vari["remanejo2"] == -1:
            txt_remanejo = font.render("Escolha para qual pais voce quer passar suas tropas",True,(255,255,255))
        if vari["remanejo1"] != -1 and vari["remanejo2"] != -1:
            txt_remanejo = font.render("A cada clique no pais escolhido voce passa um exercito,aperte x quando acabar de remanejar entre os dois territorios",True,(255,255,255))
        screen.blit(txt_remanejo,(500, 70))
    if vari["troca"] == True:
        txt_troca = font.render("Voce tem uma troca, aperte s para aceitar ou n para negar",True,(255,255,255))
        screen.blit(txt_troca,(500, 70))
    
    if vari["show"] == True and len(vari["cartasown"][vez]) > 0:
        
        for i in range(len(vari["cartasown"][vez])):
            txt_pais = font2.render(str(vari[vari["cartas_pais"][vez][i]]["pais"]),True,(0,0,0))
            if vari["cartasown"][vez][i] == "Triangulo":
               
                screen.blit(pygame.image.load("cartatriangulo1.png"),(400 + (i*75), 520 ))
                screen.blit(txt_pais,(413 + (i*75), 525 ))
            if vari["cartasown"][vez][i] == "Quadrado":
                screen.blit(pygame.image.load("cartasquare.png"),(400 + i*75, 520 ))
                screen.blit(txt_pais,(413 + (i*75), 525 ))
            if vari["cartasown"][vez][i] == "Circulo":
                screen.blit(pygame.image.load("cartacicle1.png"),(400 + i*75, 520 ))
                screen.blit(txt_pais,(413 + (i*75), 525 ))
    
    if vari["show"] == False and vari["vitoria"] == 1 and vari["triangulo"][0] == True:
        txt_pais = font2.render(str(vari[vari["cartas_pais"][vez][-1]]["pais"]),True,(0,0,0))
        screen.blit(pygame.image.load("cartatriangulo1.png"),(800, 520))
        screen.blit(txt_pais,(813 , 525 ))
    if  vari["show"] == False and  vari["vitoria"] == 1 and vari["quadrado"][0] == True:
        screen.blit(pygame.image.load("cartasquare.png"),(875, 520))
        txt_pais = font2.render(str(vari[vari["cartas_pais"][vez][-1]]["pais"]),True,(0,0,0))
        screen.blit(txt_pais,(888, 525 ))
    if vari["show"] == False and vari["vitoria"] == 1 and vari["circulo"][0] == True:
        screen.blit(pygame.image.load("cartacicle1.png"),(950, 520))
        txt_pais = font2.render(str(vari[vari["cartas_pais"][vez][-1]]["pais"]),True,(0,0,0))
        screen.blit(txt_pais,(963, 525 ))
    
    
    
    txt_rodada = font.render(vari["vezz"],True,(255,255,255))
    
    txt_ataque = font.render("",True,(255,255,255))
    screen.blit(txt_rodada, (500, 50))
    if vari["troca"] == False:
        if vari["atacado"] != -1 and vari["atacante"] != -1 and vari["cores"][vari["atacante"]] != vari["cores"][vari["atacado"]]  :
            
            txt_ataque = font.render(vari[vari["atacante"]]["pais"]+" ataca "+vari[vari["atacado"]]["pais"],True,(255,255,255))
            
        if vari["ataqueacabou"] == True and vari["atacado"] != -1 and vari["atacante"] != -1:
            txt_ataque = font.render(vari[vari["atacante"]]["pais"]+" perdeu "+str(vari["atacante_perdeu"]) +" "+vari[vari["atacado"]]["pais"]+ " perdeu "+str(vari["atacado_perdeu"]) ,True,(255,255,255))
            txt_ataque2 = font.render("Aperte espaço para continuar jogada",True,(255,255,255))
            screen.blit(txt_ataque2,(500, 90))
        if vari["resultado"] == True and vari["atacado"] != -1 and vari["atacante"] != -1 and vez == 0:
            
            txt_ataque = font.render(vari[vari["atacante"]]["pais"]+" dominou "+vari[vari["atacado"]]["pais"]+ " Aperte 1 para passar uma peça, 2 para duas e 3 para tres",True,(255,255,255))
        if vari["atacado"] != -1 and vari["atacante"] != -1:
            screen.blit(txt_ataque,(500, 70))
        if vari["run3"] == False and qnt_rodada == 0 and vari["atacante"] == -1 and vari["rodada"] // vari["numjogad"] > 0 :
            txt_preataque = font.render("Escolha um pais seu para atacar com ele",True,(255,255,255))
            screen.blit(txt_preataque, (500, 70))
        if qnt_rodada > 0 and vari2["exerc_am"] == 0 and vari2["exerc_as"] == 0 and vari2["exerc_af"] == 0 and vari2["exerc_eu"] == 0 and vari2["exerc_asi"] == 0 and vari2["exerc_oc"] == 0:
            txt_qnt = font.render("Escolha um pais para colocar exercitos.Voce tem disponivel "+str(qnt_rodada),True,(255,255,255))
            screen.blit(txt_qnt, (500, 70))
    #pais = font2.render(vari[i]["pais"],True,(255,255,255))
    #screen.blit(pais, (500, 100))
    if qnt_rodada == 0 and vari["run3"] == False:
        txt_finalizar = font.render("Aperte espaço para ir para o remanejamento",True,(255,255,255))
        screen.blit(txt_finalizar, (800, 500))
    if qnt_rodada == 0 and vari["run3"] == True:
        txt_finalizar = font.render("Aperte c para acabar com sua rodada",True,(255,255,255))
        screen.blit(txt_finalizar, (800, 500))
    if vari["numjogad"] == 0:
        num_jogad(screen)
    
    if vari["numjogad"] != 0 :
        if vari2["exerc_am"] == 0 and vari2["exerc_as"] == 0 and vari2["exerc_af"] == 0 and vari2["exerc_eu"] == 0 and vari2["exerc_asi"] == 0 and vari2["exerc_oc"] == 0 and vari["troca"] == False :
                    
        
            
            if vari["alvo"] == True:
                
                for i in range(len(vari[vari["atacante"]]["fronteira"])):
                   
                    if vari["cores"][vari[vari["atacante"]]["fronteira"][i]] != vari["cores"][vari["atacante"]]:
                        txt_preataque = font.render("Escolha um pais para atacar",True,(255,255,255))
                        screen.blit(txt_preataque, (500, 120))
                        screen.blit(pygame.image.load("circle1.png"), (vari[vari[vari["atacante"]]["fronteira"][i]]["X"]-20,vari[vari[vari["atacante"]]["fronteira"][i]]["Y"]-20))
                    
            if vari["atacado"] == -1 and vari["run3"] == False :
                
                for i in range(len(vari["territorio"][vez])):
                    
                    if qnt_rodada > 0:
                        screen.blit(pygame.image.load("circle2.png"),(vari[vari["territorio"][vez][i]]["X"] - 20,vari[vari["territorio"][vez][i]]["Y"] - 20))
                    else:
                        for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            if vari["quantidade_exerc"][vari["territorio"][vez][i]] > 1 and vari["rodada"]//vari["numjogad"] > 0:
                                if vari["cores"][vari[vari["territorio"][vez][i]]["fronteira"][t]] != vez:
                                    screen.blit(pygame.image.load("circle2.png"),(vari[vari["territorio"][vez][i]]["X"] - 20,vari[vari["territorio"][vez][i]]["Y"] - 20))                
            if vari["run3"] == True:
                if vari["remanejo1"] == -1 and vari["remanejo2"] == -1:
                    for i in range(len(vari["territorio"][vez])):
                        for t in range(len(vari[vari["territorio"][vez][i]]["fronteira"])):
                            for v in range(len(vari["territorio"][vez])):
                                
                                if vari[vari["territorio"][vez][i]]["fronteira"][t] == vari["territorio"][vez][v] and vari["quantidade_exerc"][vari["territorio"][vez][v]] > 1:
                                    
                                
                                    screen.blit(pygame.image.load("circle2.png"),(vari[vari["territorio"][vez][v]]["X"] - 20,vari[vari["territorio"][vez][v]]["Y"] - 20))
                if vari["remanejo1"] != -1 and vari["remanejo2"] == -1:
                    for i in range(len(vari[vari["remanejo1"]]["fronteira"])):
                        for t in range(len(vari["territorio"][vez])):
                            if vari[vari["remanejo1"]]["fronteira"][i] == vari["territorio"][vez][t]:
                               screen.blit(pygame.image.load("circle2.png"),(vari[vari["territorio"][vez][t]]["X"] - 20,vari[vari["territorio"][vez][t]]["Y"] - 20))
                if vari["remanejo1"] != -1 and vari["remanejo2"] != -1:
                    screen.blit(pygame.image.load("circle2.png"),(vari[vari["remanejo2"]]["X"] - 20,vari[vari["remanejo2"]]["Y"] - 20))
        for i in range(42):
            b = 0
            if len(num) >= 1:
                aleatorio = random.choice(num)
                
            
                for t in range(len(erase)):
                    if aleatorio > erase[t]:
                        b += 1
            
            
                erase.append(aleatorio)
                
                
                del num[aleatorio - b]
                vari["cores"][erase[i + 1]] = i//(42//vari["numjogad"])
                
                if vari["numjogad"] == 4 or vari["numjogad"] == 5:
                    if i == 40:
                        vari["cores"][erase[i + 1]] = 0
                    if i == 41:
                        vari["cores"][erase[i + 1]] = 1
                        

                

            if vari["numjogad"] % 3 == 0:
                screen.blit(cor[vari["cores"][erase[i + 1]]],(vari[erase[i + 1]]["X"], vari[erase[i + 1]]["Y"]))
                
            if vari["numjogad"] == 4 or vari["numjogad"] == 5:
                if i < 40:
                    screen.blit(cor[vari["cores"][erase[i + 1]]],(vari[erase[i + 1]]["X"], vari[erase[i + 1]]["Y"]))
                else:
                    screen.blit(cor[vari["cores"][erase[i + 1]]],(vari[erase[i + 1]]["X"], vari[erase[i + 1]]["Y"]))
            
            qnt_exerc = font.render(str(vari["quantidade_exerc"][erase[i+1]]),True,(0,0,0))

            screen.blit(qnt_exerc, (vari[erase[i + 1]]["X"] + 15, vari[erase[i + 1]]["Y"]))
        if vari["show_obj"] == True:
            screen.blit(vari["obj_img"][vez],( 500, 300))
        if vari["fim_do_jogo"] == True:
            font3 = pygame.font.Font("freesansbold.ttf",25)
            if vez == 0:
                txt_end = font3.render("Jogo acabou !! exercito preto venceu",True,(255,255,255))
            if vez == 1:
                txt_end = font3.render("Jogo acabou !! exercito azul venceu",True,(255,255,255))
            if vez == 2:
                txt_end = font3.render("Jogo acabou !! exercito vermelho venceu",True,(255,255,255))
            if vez == 3:
                txt_end = font3.render("Jogo acabou !! exercito verde venceu",True,(255,255,255))
            if vez == 4:
                txt_end = font3.render("Jogo acabou !! exercito amarelo venceu",True,(255,255,255))
            if vez == 5:
                txt_end = font3.render("Jogo acabou !! exercito branco venceu",True,(255,255,255))
            
            
            screen.blit(txt_end, (500 ,300))
            screen.blit(vari["obj_img"][vez],( 200, 300))
            
        pygame.display.update()
    pygame.display.update()
    if vari["fim_do_jogo"] == True:
        sleep(100)
    #if vari["n"] > 0:
        #for i in range(vari["n"]):
            
            #screen.blit(vari["result_luta"][i][(i)*5 + 2],(vari["result_luta"][i][(i)*5 + 3], vari["result_luta"][i][(i)*5 + 4]))
    
update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
vari["running"] = True
while vari["running"]:
    
    
    if vari["numjogad"] == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vari["run4"] = False
                vari["running"] = False
                vari["run5"] = False
                vari["run2"] = False
                vari["troca"] = False
                vari2["exerc_am"] = 0
                vari2["exerc_as"] = 0
                vari2["exerc_af"] = 0
                vari2["exerc_asi"] = 0
                vari2["exerc_eu"] = 0
                vari2["exerc_oc"] = 0
                vari["run1"] = False
                vari["run3"] = False
                vari["run6"] = False
                vari["run7"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    vari["numjogad"] = 3
                if event.key == pygame.K_4:
                    vari["numjogad"] = 4
                if event.key == pygame.K_5:
                    vari["numjogad"] = 5
                if event.key == pygame.K_6:
                    vari["numjogad"] = 6
                    
            
                update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
    else:
        c,troca = jogada(vari,corfinal,qnt_rodada,erase,c,troca,vari2)
        if vari["running"] == False:
            break
        for i in range(vari["numjogad"] - 1):
            troca = Maquina(vari,corfinal,qnt_rodada,erase1,c,troca,vari2)
            if vari["running"] == False:
                break
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(42):
                if event.pos[0]> vari[i]["limitX1"] and event.pos[0]<vari[i]["limitX2"] and event.pos[1]>vari[i]["limitY1"] and event.pos[1]<vari[i]["limitY2"]:  
                    print(vari[i]["pais"])
                    update_screen(screen,vari,num,erase,cor,i,vez,qnt_rodada,vari2)
            print(event.pos)
        
            
        if event.type == pygame.QUIT:
            vari["run4"] = False
            vari["running"] = False
            vari["run5"] = False
            vari["run2"] = False
            vari["troca"] = False
            vari2["exerc_am"] = 0
            vari2["exerc_as"] = 0
            vari2["exerc_af"] = 0
            vari2["exerc_asi"] = 0
            vari2["exerc_eu"] = 0
            vari2["exerc_oc"] = 0
            vari["run1"] = False
            vari["run3"] = False
            vari["run6"] = False
            vari["run7"] = False
            

            
    
    
    
    
    
        
    
            
        
       
    pygame.display.update()
pygame.display.quit()
#pygame.quit()


