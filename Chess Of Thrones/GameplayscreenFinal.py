import pygame, sys,MainMenuStateFinal#,Milestone5final# Importing the milestone 1 code (Main Menu State)
from pygame.locals import *
pygame.init()
DISPLAYSURF=pygame.display.set_mode((800,600))

Background=(255,255,104) 
Buttons=(104,198,58) 
Buttonshovered=(107,149,86) 
buttonletters=(255,255,255)
Title=(157,177,28)

playernamedisplayfont=pygame.font.Font("GROBOLD.ttf", 23)  # Font for player name display
algebricdisplay=pygame.font.Font("Game of Thrones.ttf", 23)  

class AlgebricDisplay(): #Creation of buttons in the Gameplay state  
    buttonxpos=0
    buttonypos=0
    buttonlength=0
    buttonheight=0
    buttoncolour=""
    buttonfont=""
    buttontextsize=0
    buttontext=""
    buttontextxpos=0
    buttontextypos=0

    def __init__(self, buttonxpos, buttonypos, buttonlength, buttonheight,buttoncolour,buttonfont, buttontextsize,buttontext, buttontextxpos, buttontextypos):
        self.buttonxpos=buttonxpos
        self.buttonypos=buttonypos
        self.buttonlength=buttonlength
        self.buttonheight=buttonheight
        self.buttoncolour=buttoncolour
        self.buttonfont=buttonfont
        self.buttontextsize=buttontextsize
        self.buttontext=buttontext
        self.buttontextxpos=buttontextxpos
        self.buttontextypos=buttontextypos

        fonts=pygame.font.SysFont(self.buttonfont, self.buttontextsize)

        buttontext=fonts.render(self.buttontext, True, buttonletters)

        notation=pygame.draw.ellipse(DISPLAYSURF, self.buttoncolour,(self.buttonxpos,self.buttonypos,self.buttonlength,self.buttonheight))
        DISPLAYSURF.blit(buttontext, (self.buttontextxpos, self.buttontextypos))


def displaymap(Playerhouse): #Function to display a map on the board
    #global boardmap
    if Playerhouse[0]=="1HOUSE STARK": 
        boardmap=pygame.image.load("TheNorthMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40)) #Loads an image of the map of the region, which the house chosen by the first player is in
        spriterownum=0 #The row on the spritesheet which the house is in 
    if Playerhouse[0]=="2HOUSE MARTELL":
        boardmap=pygame.image.load("DorneMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=1
    if Playerhouse[0]=="5HOUSE GREYJOY":
        boardmap=pygame.image.load("GreyjoyMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=2
    if Playerhouse[0]=="8HOUSE TULLY":
        boardmap=pygame.image.load("TullyMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=3
    if Playerhouse[0]=="6HOUSE TARGERYAN":
        boardmap=pygame.image.load("TargMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=4
    if Playerhouse[0]=="7HOUSE BARATHEON":
        boardmap=pygame.image.load("BaraMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=5
    if Playerhouse[0]=="4HOUSE LANNISTER":
        boardmap=pygame.image.load("LanniMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=6
    if Playerhouse[0]=="3HOUSE TYRELL":
        boardmap=pygame.image.load("TyrellMap.jpg")
        DISPLAYSURF.blit(boardmap,(40,40))
        spriterownum=7

    return boardmap
        
def algebricNotations(): #Algebric notations on the axis of the board
    A=AlgebricDisplay(55, 565, 30, 30,Buttons, "GROBOLD",35, "A", 61, 569)
    B=AlgebricDisplay(123, 565, 30, 30,Buttons,"GROBOLD",35, "B", 131, 569)
    C=AlgebricDisplay(190, 565, 30, 30,Buttons,"GROBOLD",35, "C", 196, 569)
    D=AlgebricDisplay(256, 565, 30, 30,Buttons,"GROBOLD",35,"D", 263, 569)
    E=AlgebricDisplay(321, 565, 30, 30,Buttons,"GROBOLD",35, "E", 328, 569)
    F=AlgebricDisplay(385, 565, 30, 30,Buttons,"GROBOLD",35, "F", 393, 569)
    G=AlgebricDisplay(449, 565, 30, 30,Buttons,"GROBOLD",35, "G", 454, 569)
    H=AlgebricDisplay(513, 565, 30, 30,Buttons,"GROBOLD",35, "H", 519, 569)
    One=AlgebricDisplay(5, 55, 30, 30,Buttons,"GROBOLD",35, "8", 13, 59)
    Two=AlgebricDisplay(5, 122, 30, 30,Buttons,"GROBOLD",35, "7", 13, 126)
    Three=AlgebricDisplay(5,185, 30, 30,Buttons,"GROBOLD",35, "6", 13, 189)
    Four=AlgebricDisplay(5, 250, 30, 30,Buttons,"GROBOLD",35, "5", 13, 254)
    Five=AlgebricDisplay(5, 314, 30, 30,Buttons,"GROBOLD",35, "4", 13, 318)
    Six=AlgebricDisplay(5, 380, 30, 30,Buttons,"GROBOLD",35, "3", 13, 384)
    Seven=AlgebricDisplay(5, 445, 30, 30,Buttons,"GROBOLD",35, "2", 13, 449)
    Eight=AlgebricDisplay(5, 510, 30, 30,Buttons,"GROBOLD",35, "1", 13, 514)

def displaynotations(mouse):
    mousex = str((mouse[0] / 64) + 0.375) 
    mousey = (mouse[1] / 64) + 0.375
    mouseydisplay = str(10 - mousey)
    
    if 560 > mouse[0] > 38 and 560 > mouse[1] > 39:  # If mouse inside the board
        if mousex[0] == "1":
            mx = "A"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "2":
            mx = "B"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "3":
            mx = "C"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "4":
            mx = "D"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "5":
            mx = "E"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "6":
            mx = "F"
            x = mx + mouseydisplay[0]
        elif mousex[0] == "7":
            mx = "G"
            x = mx + mouseydisplay[0]
        else:
            mx = "H"
            x = mx + mouseydisplay[0]

        notationbutton = AlgebricDisplay(648, 220, 60, 60, Buttons, "GROBOLD", 35, "", 662, 234)
        displaynotationfont = pygame.font.SysFont("GROBOLD", 50)
        notationtext = displaynotationfont.render(x, True, buttonletters)
        DISPLAYSURF.blit(notationtext, (658, 234))
        
    else:
        notationbutton =AlgebricDisplay(648, 220, 60, 60, Background, "GROBOLD", 35, "", 662,234)  # Else blit over the previous notations

    if 754 > mouse[0] > 604 and 559 > mouse[1] > 478:  # menu button
        Menu = AlgebricDisplay(605, 479, 150, 80, Buttonshovered, "GROBOLD", 65, "MENU", 616, 503)
    else:
        Menu = AlgebricDisplay(605, 479, 150, 80, Buttons, "GROBOLD", 65, "MENU", 616, 503)

    if 758 > mouse[0] > 602 and 459 > mouse[1] > 377:  # save button
        savebutton = AlgebricDisplay(605, 379, 150, 80, Buttonshovered, "GROBOLD", 65, "SAVE", 616, 399)
    else:
        savebutton = AlgebricDisplay(605, 379, 150, 80, Buttons, "GROBOLD", 65, "SAVE", 616, 399)  

    mousey=str(mousey)
    mousey=mousey[0]
    mousex=mousex[0]
    
    return mousex,mousey

def displayplayer(playercounter,Playername):    
    if playercounter==1:
        display="Turn: "+Playername[0]
        name=playernamedisplayfont.render(display,False,Buttons)
    if playercounter==2:
        display="Turn: "+Playername[1]
        name=playernamedisplayfont.render(display,False,Buttons)

    DISPLAYSURF.blit(name,(565,293))

def displayscreen(Playerhouse):
    algebricNotations()
    boardmap=displaymap(Playerhouse)

    return boardmap

