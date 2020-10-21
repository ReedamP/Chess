import pygame, sys,shelve #importing pygame modules used for game developments
from pygame.locals import *
pygame.init()
FPS=100
fpsClock=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((800,600)) #Creating a window
pygame.display.set_caption("Chess Of Thrones!") #Set title of the window

#Colours
Background=(255,255,104) #Yellowish
Title=(157,177,28) #Lime green-ish
Buttons=(104,198,58) #Light green
Buttonshovered=(107,149,86) #Dark green
buttonletters=(255,255,255) #White

DISPLAYSURF.fill(Background) #Background appearance for the whole program

#Gets font from the system directory (control panel/appereance/fonts)
Intitialbuttonsfont=pygame.font.Font("GROBOLD.ttf", 29) #Button font & text size for Menuscreen screen 1 & 2
buttonfont=pygame.font.Font("Game of Thrones.ttf", 22) #Button font & text size for Menu screen 3
maintitlefont=pygame.font.Font("Game of Thrones.ttf",70) #Game title font
titlefont=pygame.font.Font("Game of Thrones.ttf", 40) #"Choose House" title font for the Menu screen 3
elipsesfont=pygame.font.Font("GROBOLD.ttf", 80)
textboxchar=pygame.font.Font("Game of Thrones.ttf", 30) #Font to be used on the text box (when player enters name)
housechosenfont=pygame.font.Font("Game of Thrones.ttf", 45)
enterwhendonefont=pygame.font.Font("Game of Thrones.ttf", 30)

#Template for creating new buttons
class Buttonswithicon(): #11 parameters  
    buttonicon=""
    buttoniconxpos=0
    buttoniconypos=0
    buttonxpos=0
    buttonypos=0
    buttonlength=0
    buttonheight=0
    buttonfont=""
    buttontext=""
    buttontextxpos=0
    buttontextypos=0

    def __init__(self, buttonicon, buttoniconxpos, buttoniconypos, buttonxpos, buttonypos, buttonlength, buttonheight, buttonfont, buttontext, buttontextxpos, buttontextypos,house):
        self.buttonicon=buttonicon #Assigning passed on values to create an instance of the button
        self.buttoniconxpos=buttoniconxpos
        self.buttoniconypos=buttoniconypos
        self.buttonxpos=buttonxpos
        self.buttonypos=buttonypos
        self.buttonlength=buttonlength
        self.buttonheight=buttonheight
        self.buttonfont=buttonfont 
        self.buttontext=buttontext
        self.buttontextxpos=buttontextxpos
        self.buttontextypos=buttontextypos

        buttonpic=pygame.image.load(self.buttonicon) #seperate variable only used within the module
        buttontext=self.buttonfont.render(self.buttontext, True, buttonletters) #Rendering the text passed on with the global font variable
        mouse = pygame.mouse.get_pos() #local mouse variable
        if self.buttonxpos+self.buttonlength > mouse[0] > self.buttonxpos and self.buttonypos+self.buttonheight> mouse[1] > self.buttonypos: #If mouse hovered inside the button
            gamebutton=pygame.draw.ellipse(DISPLAYSURF, Buttonshovered,(self.buttonxpos,self.buttonypos,self.buttonlength,self.buttonheight)) #Then draw the button shape with the darker colour 
            DISPLAYSURF.blit(buttonpic, (self.buttoniconxpos, self.buttoniconypos)) #and display the icon passed on
            if house==True:
                sigilborder=pygame.draw.rect(DISPLAYSURF, Buttons, (595, 233, 188, 324), 8) #House icon border
        else:
            gamebutton=pygame.draw.ellipse(DISPLAYSURF, Buttons,(self.buttonxpos,self.buttonypos,self.buttonlength,self.buttonheight)) #Or draw the button shape with the lighter colour
        
        DISPLAYSURF.blit(buttontext, (self.buttontextxpos, self.buttontextypos)) #Display the text passed on


def returnproperties():
    return Playername, Playerhouse, spriterow,grid,playercounter

def load():
    savefile=shelve.open("ChessOfThronesSaveFile")
    Playername=savefile["PlayerNames"]
    Playerhouse=savefile["PlayerHouses"]
    playercounter=savefile["Turn"]
    grid=savefile["BoardState"]
    savefile.close()

    spriterow[0]=int(Playerhouse[0][:1])
    spriterow[1]=int(Playerhouse[1][:1])
    
    return Playername,Playerhouse,playercounter,grid,spriterow

def choosehouse(Playerhouse,event,Playerindex,spriterow): #Playerhouse array is passed on
    mousepos=pygame.mouse.get_pos()
    if (585>mouse[0]>1 and 600>mouse[1]>234) :
        if event.type==MOUSEBUTTONDOWN:
            pygame.draw.rect(DISPLAYSURF, Background, (180, 150, 600,80))
            if 234 > mousepos[0] > 15 and 327 > mousepos[1] > 247 and Playerhouse[0]!="1HOUSE STARK":
                Playerhouse[Playerindex]="1HOUSE STARK"
                spriterow[Playerindex]=1
            elif 572 > mousepos[0] > 245 and 327 > mousepos[1] > 247 and Playerhouse[0]!="7HOUSE BARATHEON":
                Playerhouse[Playerindex] = "7HOUSE BARATHEON"
                spriterow[Playerindex]=7
            elif 234 > mousepos[0] > 15 and 414 > mousepos[1] > 335 and Playerhouse[0]!="8HOUSE TULLY":
                Playerhouse[Playerindex] = "8HOUSE TULLY"
                spriterow[Playerindex]=8
            elif 572 > mousepos[0] > 245 and 414 > mousepos[1] > 335 and Playerhouse[0]!="4HOUSE LANNISTER":
                Playerhouse[Playerindex] = "4HOUSE LANNISTER"
                spriterow[Playerindex]=4
            elif 234 > mousepos[0] > 15 and 503 > mousepos[1] > 423 and Playerhouse[0]!="3HOUSE TYRELL":
                Playerhouse[Playerindex] = "3HOUSE TYRELL"
                spriterow[Playerindex]=3
            elif 572 > mousepos[0] > 245 and 503 > mousepos[1] > 423 and Playerhouse[0]!="6HOUSE TARGERYAN":
                Playerhouse[Playerindex] = "6HOUSE TARGERYAN"
                spriterow[Playerindex]=6
            elif 274 > mousepos[0] > 15 and 589 > mousepos[1] > 510 and Playerhouse[0]!="2HOUSE MARTELL":
                Playerhouse[Playerindex] = "2HOUSE MARTELL"
                spriterow[Playerindex]=2
            elif 545 > mousepos[0] > 286 and 589 > mousepos[1] > 510 and Playerhouse[0]!="5HOUSE GREYJOY":
                Playerhouse[Playerindex] = "5HOUSE GREYJOY"
                spriterow[Playerindex]=5

    return Playerhouse[Playerindex], spriterow #Returns the the string inside the index

def displaymenuone(): #Displays first menu
    house=False
    Newgame=Buttonswithicon("Normalmodeimg.jpg", 40, 295, 20, 400, 220, 130, Intitialbuttonsfont, "NEW GAME!", 30, 450,house)
    Load=Buttonswithicon("Loadgameimg.jpg", 325, 250, 288, 400, 220, 130, Intitialbuttonsfont, "LOAD GAME", 300, 450,house)
    Quitgame=Buttonswithicon("Quitbuttonimg.jpg", 585, 240, 560, 400, 220, 130, Intitialbuttonsfont, "QUIT GAME!", 580, 450,house)
    
def displaymenutwo(Playername,Playerindex,event): #Choose house menu
    pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
    choosehousetitle=titlefont.render("CHOOSE YOUR HOUSE", True, Title)#Title
    DISPLAYSURF.blit(choosehousetitle,(130,10))
    house=True

    HStark=Buttonswithicon("HouseStark.jpg", 600, 238, 15, 248, 220, 80, buttonfont, "HOUSE STARK", 33, 272,house)
    HBara=Buttonswithicon("HouseBara.jpg", 600, 238, 245, 248, 328, 80, buttonfont ,"HOUSE  BARATHEON", 270, 272,house)
    HTully=Buttonswithicon("HouseTully.jpg", 600, 238, 15, 335, 220, 80, buttonfont ,"HOUSE  Tully", 33, 365,house)
    HLanni=Buttonswithicon("HouseLanni.jpg", 600, 238, 245, 335, 328, 80, buttonfont ,"HOUSE  LANNISTER", 275, 365,house)
    HTyrell=Buttonswithicon("HouseTyrell.jpg", 600, 238, 15, 423, 220, 80, buttonfont, "HOUSE TYRELL", 29, 451,house)
    HTarg=Buttonswithicon("HouseTarg.jpg", 600, 238, 245, 423, 328, 80, buttonfont ,"HOUSE  TARGERYAN", 270, 451,house)
    HMartell=Buttonswithicon("HouseMartell.jpg", 600, 238, 15, 510, 260, 80, buttonfont ,"HOUSE  MARTELL", 33, 538,house)
    HGreyjoy=Buttonswithicon("HouseGreyjoy.jpg", 600, 238, 285, 510, 260, 80, buttonfont ,"HOUSE  GREYJOY", 299, 538,house)
    
    Nextbutton=Buttonswithicon("Nextbutton.jpg", 680, 60, 540, 67, 120, 83, Intitialbuttonsfont, "NEXT", 560, 95,house=False)

    Playerbutton=pygame.draw.ellipse(DISPLAYSURF, Buttons, (15,60,150,80))
    Playerbuttontext=Intitialbuttonsfont.render("Player:", True, buttonletters)
    DISPLAYSURF.blit(Playerbuttontext, (30, 85)) #The player button, left of the text box

    Housebutton=pygame.draw.ellipse(DISPLAYSURF, Buttons, (15, 150, 150, 80))
    Housebuttontext=Intitialbuttonsfont.render("House:", True, buttonletters)
    DISPLAYSURF.blit(Housebuttontext, (45, 175))

    #Input name
    
    Textbox=pygame.draw.rect(DISPLAYSURF, buttonletters, (180 ,67, 340, 70)) #Text box
    
    if Textbox.left < mouse[0] < Textbox.right and Textbox.top < mouse[1] < Textbox.bottom: #When mouse is clicked inside text box
        if event.type==MOUSEBUTTONDOWN:
            Entered=False
            while Entered==False: #While name not entered
                for evt in pygame.event.get():
                    Housebuttontext=enterwhendonefont.render("PRESS ENTER WHEN DONE", True, Buttons)
                    DISPLAYSURF.blit(Housebuttontext, (190,170))
                    if evt.type == KEYDOWN:
                        if evt.unicode.isalpha(): #Validation for user name 
                            if len(Playername[Playerindex])<7:
                                if evt.unicode == 7:
                                    Playername[Playerindex]=Playername[Playerindex]+0
                                else:
                                    Playername[Playerindex]= Playername[Playerindex]+evt.unicode
                        elif evt.key == K_BACKSPACE: 
                            Playername[Playerindex] = "" #Clears the text box 
                            pygame.draw.rect(DISPLAYSURF, buttonletters, (180 ,68, 340, 60))
                            pygame.display.update()
                        elif evt.key==K_RETURN:
                            pygame.mouse.set_pos([488,164])
                            Entered=True
                            
                showletter=textboxchar.render(Playername[Playerindex], True, Buttons) 
                DISPLAYSURF.blit(showletter, (190,87))#Displays each letter as it's typed
                pygame.display.update()
                
    playernamedisplay=textboxchar.render(Playername[Playerindex], True, Buttons)
    DISPLAYSURF.blit(playernamedisplay, (190,87))
    Playername[Playerindex]=Playername[Playerindex].upper()
    
    return Playername[Playerindex] #Returns player name array with the updated index (the player's name)

def run():
    global Playername
    global Playerhouse
    global spriterow
    global playercounter
    global grid
    global loaded
    
    Menustate=True
    Menuscreen=1
    Playerindex=0
    
    Playername=["",""] #Array to store the two player names
    Playerhouse=["",""] #Array to store the two player houses
    Normal=True #Boolean to specify game mode
    spriterow=[0,0]

    chessof=maintitlefont.render("Chess of", True, Title) #2nd argument Anti-aliased or not
    thrones=maintitlefont.render("Thrones", True, Title)
    elipses=elipsesfont.render("...", True, Title) #Custom themed font doesn't have elipses hence different font used

    DISPLAYSURF.blit(chessof,(20,30)) #Displays top bit of the title
    DISPLAYSURF.blit(thrones,(150,130)) #Bottom bit 
    DISPLAYSURF.blit(elipses,(100,140)) #Bottom elipses
    DISPLAYSURF.blit(elipses,(400,40)) #Top elipses
    
    #Main game loop
    while Menustate==True: #While programs running
        global mouse
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): #Handles all the events
            if event.type ==  QUIT:
                pygame.quit()
                sys.exit()

            if Menuscreen==1: #Buttons: Play game, High Scores, Quit 
                if event.type==MOUSEBUTTONDOWN and 240> mouse[0] > 20 and 531 > mouse[1]> 401: #If new game button is clicked
                    Menuscreen=2

                if event.type==MOUSEBUTTONDOWN and 399>mouse[0]>292 and 531 > mouse[1]> 401:
                    Playername,Playerhouse,playercounter,grid,spriterow=load()
                    Menuscreen=4

                if event.type==MOUSEBUTTONDOWN and 760 > mouse[0] > 560 and 530 > mouse[1] > 400:#If quit button is clicked
                    pygame.quit()
                    sys.exit()
                    
            elif Menuscreen==2: #Choose house screen
                if Playerindex <= 1: #If both players haven't chosen their properties 
                    if event.type==MOUSEBUTTONDOWN and 659 > mouse[0] > 538 and 149>mouse[1]>66: #If the player clicks next
                        if Playername[Playerindex] != "" and Playerhouse[Playerindex] != "":  #And have inputed their name and house
                            Playerindex=Playerindex+1 #Player counter incremented by one, to signify the second player
                        
                if Playerindex==2: #Once both players have chosen their properties 
                    Menuscreen=4 #Initalise the game

        if Menuscreen==1:
            displaymenuone() 

        if Menuscreen==2:
            grid = [[1] * 8 for n in range(8)]  # Creates a 2D array

            for counter in range(0, 8):  # 8 pawns
                grid[6][counter]="BP"+str(counter+1) #Numbers the pawns from 1 to 8
                grid[1][counter]="WP"+str(counter+1) #Index starts with 0 hence +1

                grid[7][0]="BR1" #Black pieces
                grid[7][7]="BR2" #Stores the character on the 2D array (remember y index first and then x)
                grid[7][1]="BKN1"
                grid[7][6]="BKN2"
                grid[7][2]="BB1"
                grid[7][5]="BB2"
                grid[7][3]="BKI"
                grid[7][4]="BQ"

                grid[0][0]="WR1" #White pieces
                grid[0][7]="WR2"
                grid[0][1]="WKN1"
                grid[0][6]="WKN2"
                grid[0][2]="WB1"
                grid[0][5]="WB2"
                grid[0][3]="WKI"
                grid[0][4]="WQ"
                
            playercounter=1

            Playername[Playerindex]=displaymenutwo(Playername,Playerindex,event) 
            Playerhouse[Playerindex],spriterow=choosehouse(Playerhouse,event,Playerindex,spriterow)
            playerhousedisplay=housechosenfont.render(Playerhouse[Playerindex], True, Buttons)
            DISPLAYSURF.blit(playerhousedisplay, (190,160))
            pygame.draw.rect(DISPLAYSURF, Background, (171, 175, 40,40))

        if Menuscreen==4:
            pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
            Menustate=False
            returnproperties()
            
        pygame.display.update() #Updates game state
        
        pygame.draw.rect(DISPLAYSURF, Background, (20, 240, 250,150))
        pygame.draw.rect(DISPLAYSURF, Background, (330, 219, 250,180))
        pygame.draw.rect(DISPLAYSURF, Background, (600, 219, 250,180))
        
        fpsClock.tick(FPS)
