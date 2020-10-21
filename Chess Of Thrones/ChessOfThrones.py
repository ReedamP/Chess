import pygame, sys,GameplayscreenFinal, copy,MainMenuStateFinal,shelve  # Importing the milestone 1 code (Main Menu State)
from pygame.locals import *

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess Of Thrones!")

Background = (255, 255, 104)
Buttons = (104, 198, 58)
Buttonshovered = (107, 149, 86)
buttonletters = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red=(255,0,0)
DISPLAYSURF.fill(Background)

font=pygame.font.SysFont("GROBOLD", 23)  # Font for board notation
winnerfont=pygame.font.SysFont("GROBOLD", 95)
Intitialbuttonsfont=pygame.font.SysFont("GROBOLD", 29)
quitbuttonfont=pygame.font.SysFont("GROBOLD", 40)
playernamedisplayfont=pygame.font.SysFont("GROBOLD", 23)  # Font for player name display


class Square():

    def __init__(self):
        self.x = 41  # X co-ordinates for drawing of each square
        self.y = 40  # Y co-ordinates for drawing of each square
        self.w = 64
        self.squares=[None]*72

    def create(self):
        counter=0
        for row in grid:
            for col in row: #Creates a visual board using the array
                square=pygame.Rect(self.x,self.y,self.w,self.w) #Creates a square shape for each of the squares
                self.squares[counter]=square #Adds that square on the array
                counter=counter+1
                self.x=self.x+(self.w+1) #The position of the next square is a width apart
            self.y=self.y+(self.w+1) #After a row has been created, the next coloumn is a width below
            self.x=40 #Start from the same x co-ordinate for the new row

        for r in range(0,8): #Removes all the none square shapes in the array 
            self.squares.pop(64) #Removes the index position and the NONE type inside 

        return self.squares

    def getposofsquare(self,possiblemoves):
        squarecor=[] #array containing index position of each square to be highlighted
        for counter in range(0, len(possiblemoves)):
            squarecor.append([(possiblemoves[counter][1])*8+(possiblemoves[counter][0])])
        return squarecor, self.squares

    def getoccupied(self,startx, starty,grid):
        self.startx=startx
        self.starty=starty
        if grid[self.starty][self.startx]!=1: #If the index position has a string representing a character
            return True #Then it's occupied
        else:
            return False #Otherwise it's an empty square

class Board(): #Class to initalise the characters onto the grid array
    def __init__(self,spriterow):
        self.P1listchars = [""] * 16  # An array list for player 1 characters 
        self.P2listchars = [""] * 16  # For player 2 characters
        
        for pawns in range(0,8):
            self.blackpawn=MakeCharacter() #Makes an instance of the MakeCharacter class for each of the piece type
            self.blackpawn.setimage("spritesheet.jpg", spriterow, 0, 0) #1st argument is the file name, second is the array containing the rows for the house character images
            self.P1listchars[pawns]=self.blackpawn
            
            self.whitepawn=MakeCharacter() #White characters
            self.whitepawn.setimage("spritesheet.jpg", spriterow, 1, 0)
            self.P2listchars[pawns]=self.whitepawn
            
        for rooks in range(0,2):
            self.blackrook=MakeCharacter()
            self.blackrook.setimage("spritesheet.jpg", spriterow, 0, 59) #3rd is the array index position (0 for first player chars, 1 for second)
            self.whiterook=MakeCharacter()
            self.whiterook.setimage("spritesheet.jpg", spriterow, 1, 59)

            if rooks==0:
                self.P1listchars[8]=self.blackrook
                self.P2listchars[8]=self.whiterook
            else:
                self.P1listchars[15]=self.blackrook
                self.P2listchars[15]=self.whiterook

        for knights in range(0,2):
            self.blackknight=MakeCharacter()
            self.blackknight.setimage("spritesheet.jpg", spriterow, 0, 118) #3rd is the array index position (0 for first player chars, 1 for second)
            self.whiteknight=MakeCharacter()
            self.whiteknight.setimage("spritesheet.jpg", spriterow, 1, 118)

            if knights==0:
                self.P1listchars[9]=self.blackknight
                self.P2listchars[9]=self.whiteknight
            else:
                self.P1listchars[14]=self.blackknight
                self.P2listchars[14]=self.whiteknight

        for bishops in range(0,2):
            self.blackbishop=MakeCharacter()
            self.blackbishop.setimage("spritesheet.jpg", spriterow, 0, 177) #3rd is the array index position (0 for first player chars, 1 for second)
            self.whitebishop=MakeCharacter()
            self.whitebishop.setimage("spritesheet.jpg", spriterow, 1, 177)

            if bishops==0:
                self.P1listchars[10]=self.blackbishop
                self.P2listchars[10]=self.whitebishop
            else:
                self.P1listchars[13]=self.blackbishop
                self.P2listchars[13]=self.whitebishop
                
        self.blackking=MakeCharacter()
        self.blackking.setimage("spritesheet.jpg", spriterow, 0, 236) #3rd is the array index position (0 for first player chars, 1 for second)
        self.P1listchars[11]=self.blackking
        
        self.whiteking=MakeCharacter()
        self.whiteking.setimage("spritesheet.jpg", spriterow, 1, 236)
        self.P2listchars[11]=self.whiteking

        self.blackqueen=MakeCharacter()
        self.blackqueen.setimage("spritesheet.jpg", spriterow, 0, 295) #3rd is the array index position (0 for first player chars, 1 for second)
        self.P1listchars[12]=self.blackqueen
        
        self.whitequeen=MakeCharacter()
        self.whitequeen.setimage("spritesheet.jpg", spriterow, 1, 295)
        self.P2listchars[12]=self.whitequeen

    def initaliseplayers(self): #Displays all the characters in their original starting position
        P1firstrow = 433  # The y co-ordinates of the player 1 starting rows(bottom rows)
        P1secondrow = 497
        P2firstrow = 108  # Player 2 starting rows (top rows)
        P2secondrow = 43

        for col in range(0,8): 
            for row in range(0,8):
                if grid[row][col]!=1: #If square (a.k.a. the index in the 2D array ) is not empty 
                    if grid[row][col][0]=="B": #If square contains black piece
                        if grid[row][col][1]=="P": #If its a pawn
                            self.P1listchars[col].setpos((col*64.9)+44,(row*64.9)+43.6)
                                
                        if grid[row][col][1]=="R": #Rooks
                            self.P1listchars[8].setpos((col*64.9)+44,(row*64.9)+43.6)
                            self.P1listchars[15].setpos((col*64.9)+44,(row*64.9)+43.6)

                        if grid[row][col][1]=="K": 
                            if grid[row][col][2]=="N": #Knights
                                self.P1listchars[9].setpos((col*64.9)+44,(row*64.9)+43.6)
                                self.P1listchars[14].setpos((col*64.9)+44,(row*64.9)+43.6)
                                
                            if grid[row][col][2]=="I": #King
                                self.P1listchars[11].setpos((col*64.9)+44,(row*64.9)+43.6)
                        
                        if grid[row][col][1]=="B": #Bishop
                            self.P1listchars[10].setpos((col*64.9)+44,(row*64.9)+43.6)
                            self.P1listchars[13].setpos((col*64.9)+44,(row*64.9)+43.6)
                            
                        if grid[row][col][1]=="Q": #Queen
                            self.P1listchars[12].setpos((col*64.9)+44,(row*64.9)+43.6)
                            
                            
                    if grid[row][col][0]=="W": #If square contains white piece
                        if grid[row][col][1]=="P":                        
                            self.P2listchars[col].setpos((col*64.9)+44,(row*64.9)+43.6)
                                
                        if grid[row][col][1]=="R":
                            self.P2listchars[8].setpos((col*64.9)+44,(row*64.9)+43.6)
                            self.P2listchars[15].setpos((col*64.9)+44,(row*64.9)+43.6)
                            
                        if grid[row][col][1]=="K": 
                            if grid[row][col][2]=="N": #Knights
                                self.P2listchars[9].setpos((col*64.9)+44,(row*64.9)+43.6)
                                self.P2listchars[14].setpos((col*64.9)+44,(row*64.9)+43.6)
                                
                            if grid[row][col][2]=="I": #King
                                self.P2listchars[11].setpos((col*64.9)+44,(row*64.9)+43.6)
                        
                        if grid[row][col][1]=="B": #Bishop
                            self.P2listchars[10].setpos((col*64.9)+44,(row*64.9)+43.6)
                            self.P2listchars[13].setpos((col*64.9)+44,(row*64.9)+43.6)
                            
                        if grid[row][col][1]=="Q": #Queen
                            self.P2listchars[12].setpos((col*64.9)+44,(row*64.9)+43.6)

        return self.P1listchars,self.P2listchars #Returns the arrays containing each player's characters

    def update(self,grid,startx,starty,endx,endy,squareslist,P1listchars,P2listchars):
        self.grid=grid
        endsquareno=(endy*8)+endx
        startsquareno=(starty*8)+startx
        
        for col in range(0,8):
            for row in range(0,8):
                if grid[col][row]==grid[endy][endx]:
                    if grid[endy][endx][:2]=="BP":
                        self.P1listchars[int(grid[endy][endx][2])-1].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="BR":
                        if grid[endy][endx][2]=="1":
                            self.P1listchars[8].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][2]=="2":
                            self.P1listchars[15].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:3]=="BKN":
                        if grid[endy][endx][3]=="1":
                            self.P1listchars[9].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][3]=="2":
                            self.P1listchars[14].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="BB":
                        if grid[endy][endx][2]=="1":
                            self.P1listchars[10].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][2]=="2":
                            self.P1listchars[13].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:3]=="BKI":
                        self.P1listchars[11].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="BQ":
                        self.P1listchars[12].movepos(endx,endy,squareslist,endsquareno)

                    if grid[endy][endx][:2]=="WP":
                        self.P2listchars[int(grid[endy][endx][2])-1].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="WR":
                        if grid[endy][endx][2]=="1":
                            self.P2listchars[8].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][2]=="2":
                            self.P2listchars[15].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:3]=="WKN":
                        if grid[endy][endx][3]=="1":
                            self.P2listchars[9].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][3]=="2":
                            self.P2listchars[14].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="WB":
                        if grid[endy][endx][2]=="1":
                            self.P2listchars[10].movepos(endx,endy,squareslist,endsquareno)
                        if grid[endy][endx][2]=="2":
                            self.P2listchars[13].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:3]=="WKI":
                        self.P2listchars[11].movepos(endx,endy,squareslist,endsquareno)
                    if grid[endy][endx][:2]=="WQ":
                        self.P2listchars[12].movepos(endx,endy,squareslist,endsquareno)

                if grid[col][row]==grid[starty][startx]:
                    DISPLAYSURF.blit(boardmap,((squareslist[startsquareno].x)+3,(squareslist[startsquareno].y)+3),((squareslist[startsquareno].x)-36,(squareslist[startsquareno].y)-36,59,59))

        return self.grid
    
class MakeCharacter(): #Initalise a character
    def __init__(self):
        self.charwidth = 59
        self.charheight = 59
    def setimage(self, filename, spriterow, pindex,x): #Sets the image for the character 
        self.sprite_sheet = pygame.image.load(filename).convert()  # Load the spritesheet
        self.image = pygame.Surface((self.charwidth, self.charheight)).convert() #Creates a surface 
        self.image.blit(self.sprite_sheet, (0, 0),(x, ((spriterow[pindex]) - 1) * 59, 59, 59))#Blits the character image onto the surface
        self.rect = self.image.get_rect() #Gets the rect attribute for the surface (the x pos, ypos, width & height)
    def setpos(self,xpos,ypos):
        self.xpos=xpos
        self.ypos=ypos
        self.boardx = str(((self.xpos / 64) + 0.375)-1)
        self.boardy = str(((self.ypos / 64) + 0.375)-1)
        self.rect.x = self.xpos #Sets the co-ordinate of the image
        self.rect.y = self.ypos
        DISPLAYSURF.blit(self.image,(self.rect.x,self.rect.y)) #Blits the surface onto the main window surface 
    def movepos(self,endx,endy,squareslist,endsquareno):
        self.endx=endx
        self.endy=endy
        self.rect.x = self.endx
        self.rect.y = self.endy
        DISPLAYSURF.blit(self.image,((squareslist[endsquareno].x)+3,(squareslist[endsquareno].y)+3))
        self.boardx=str(self.endx)
        self.boardy=str(self.endy)
    def getrect(self):
        return self.rect
    def getxpos(self):
        return self.boardx[0]#,self.boardy[0]
    def getypos(self):
        return self.boardy[0]#,self.boardy[0]

def indicatechar(mousex,mousey,squareslist):
    pygame.draw.rect(DISPLAYSURF, Background, (600, 1, 200, 220)) #Covers the piece icon when not highlighted 
    squareno=(mousey*8)+mousex #Converts the square positions into the square index number of the same square hovered 

    if squareslist[squareno].collidepoint(pygame.mouse.get_pos()): #If the square's attributes collide with the mouse positions 
        pygame.draw.rect(DISPLAYSURF, Buttons, ((squareslist[squareno].x), (squareslist[squareno].y), 64, 64), 2) #Draw the transparent square with a green stroke to represent the square being highlighted
        if squares.getoccupied(mousex, mousey,grid)!=False: #If the position the mouse is on is occupied 
            if grid[mousey][mousex][0]=="B":
                if grid[mousey][mousex][1]=="P":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8) #Create the sigil border
                    blackpawn = pygame.image.load("blackpawn.jpg") #Load the pawn icon
                    DISPLAYSURF.blit(blackpawn, (615, 15)) #Display the icon
                if grid[mousey][mousex][1]=="R":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    blackrook = pygame.image.load("blackrook.jpg")
                    DISPLAYSURF.blit(blackrook, (615, 15))
                if grid[mousey][mousex][1]=="K":
                    if grid[mousey][mousex][2]=="N":
                        sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                        blackknight = pygame.image.load("blackknight.jpg")
                        DISPLAYSURF.blit(blackknight, (615, 15))
                    if grid[mousey][mousex][2]=="I":
                        sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                        blackking = pygame.image.load("blackking.jpg")
                        DISPLAYSURF.blit(blackking, (615, 15))
                if grid[mousey][mousex][1]=="B":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    blackbishop = pygame.image.load("blackbishop.jpg")
                    DISPLAYSURF.blit(blackbishop, (615, 15))
                if grid[mousey][mousex][1]=="Q":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    blackqueen = pygame.image.load("blackqueen.jpg")
                    DISPLAYSURF.blit(blackqueen, (615, 15))

            elif grid[mousey][mousex][0]=="W":
                if grid[mousey][mousex][1]=="P":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    whitepawn = pygame.image.load("whitepawn.jpg")
                    DISPLAYSURF.blit(whitepawn, (615, 15))
                if grid[mousey][mousex][1]=="R":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    whiterook = pygame.image.load("whiterook.jpg")
                    DISPLAYSURF.blit(whiterook, (615, 15))
                if grid[mousey][mousex][1]=="K":
                    if grid[mousey][mousex][2]=="N":
                        sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                        whiteknight = pygame.image.load("whiteknight.jpg")
                        DISPLAYSURF.blit(whiteknight, (615, 15))
                    if grid[mousey][mousex][2]=="I":
                        sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                        whiteking = pygame.image.load("whiteking.jpg")
                        DISPLAYSURF.blit(whiteking, (615, 15))
                if grid[mousey][mousex][1]=="B":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    whitebishop = pygame.image.load("whitebishop.jpg")
                    DISPLAYSURF.blit(whitebishop, (615, 15))
                if grid[mousey][mousex][1]=="Q":
                    sigilborder = pygame.draw.rect(DISPLAYSURF, Buttons, (610, 10, 155, 197), 8)
                    whitequeen = pygame.image.load("whitequeen.jpg")
                    DISPLAYSURF.blit(whitequeen, (615, 15))
    else:
        for count in range(0,len(squareslist)): #Else draw a transparent rectangle with a black stroke to remove the highlight 
            pygame.draw.rect(DISPLAYSURF, black, ((squareslist[count].x), (squareslist[count].y), 64, 64), 2)

def getallmovesforpawn(xpos,ypos,grid):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[]
    
    if grid[ypos][xpos][0]=="B":
        if squares.getoccupied(xpos,ypos-1,grid)==False:
            allmoves.append([xpos,ypos-1])
            if ypos == 6 and squares.getoccupied(xpos,ypos-2,grid)==False:
                allmoves.append([xpos,ypos-2])
            
        if xpos!=0:
            if squares.getoccupied(xpos-1,ypos-1,grid)==True:  
                if grid[ypos-1][xpos-1][0]=="W":
                    allmoves.append([xpos-1,ypos-1])
        if xpos!=7:
            if squares.getoccupied(xpos+1,ypos-1,grid)==True:
                if grid[ypos-1][xpos+1][0]=="W":
                    allmoves.append([xpos+1,ypos-1])


    elif grid[ypos][xpos][0]=="W":
        if squares.getoccupied(xpos,ypos+1,grid)==False:
            allmoves.append([xpos,ypos+1])
            if ypos == 1 and squares.getoccupied(xpos,ypos+2,grid)==False:
                allmoves.append([xpos,ypos+2])

        if xpos!=0:
            if squares.getoccupied(xpos-1,ypos+1,grid)==True:
                if grid[ypos+1][xpos-1][0]=="B":
                    allmoves.append([xpos-1,ypos+1])

        if xpos!=7:
            if squares.getoccupied(xpos+1,ypos+1,grid)==True:
                if grid[ypos+1][xpos+1][0]=="B":
                    allmoves.append([xpos+1,ypos+1])
                    
    possiblemoves=allmoves
    return possiblemoves

def getallmovesforrook(xpos,ypos,grid,checking):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[]
    
    upblock=False
    for count in range(-1, -ypos-1,-1): #Checks squares vertically above the piece
        if upblock==False: #If the piece isn't blocked yet
            allmoves.append([xpos,ypos+count]) #The square above is a possible move
            if squares.getoccupied(xpos,ypos+count,grid)!=True: #If the square didn't contain a piece
                pass   
            else:
                upblock=True #Then the path is blocked

    rightblock=False
    xdiffromrightofboard=7-xpos
    for count in range(1, xdiffromrightofboard+1): #Checks to the right 
        if rightblock==False:
            allmoves.append([xpos+count,ypos])
            if squares.getoccupied(xpos+count,ypos,grid)!=True: 
                pass 
            else:
                rightblock=True

    downblock=False
    ydiffrombottomofboard=7-ypos 
    for count in range(1, ydiffrombottomofboard+1): #Checks vertically below
        if downblock==False:
            allmoves.append([xpos,ypos+count])
            if squares.getoccupied(xpos,ypos+count,grid)!=True: 
                pass
            else:
                downblock=True

    leftblock=False
    for count in range(-1, -xpos-1,-1): #Checks to the left
        if leftblock==False:
            allmoves.append([xpos+count,ypos])
            if squares.getoccupied(xpos+count,ypos,grid)!=True: 
                pass
            else:
                leftblock=True
    possiblemoves=allmoves
    
    if checking==False:
        possiblemoves=filtermove(allmoves,grid)

    return possiblemoves

def getallmovesforknight(xpos,ypos,grid,checking):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[]
    if ypos >=1:#If the knight is on the 2nd row or below
        if xpos<=6:#If the knight is on or to the left of the 7th coloumn 
            allmoves.append([xpos+1, ypos-2])#The square two above and one right is a possible move
        if xpos<=5:#If the knight is on or to the left of the 6th coloumn 
            allmoves.append([xpos+2, ypos-1])#The square one above and two right is a possible move
        if xpos>=1:#If the knight is on or to the right of the 2nd coloumn 
            allmoves.append([xpos-1, ypos-2])#The square two above and two left is a possible move
        if xpos>=2:#If the knight is on or to the right of the 3rd coloumn 
            allmoves.append([xpos-2, ypos-1])#The square one above and two left is a possible move
    if ypos<=6:#If the knight is on the 7th row or above
        if xpos<=6:
            allmoves.append([xpos+1, ypos+2])
        if xpos<=5:
            allmoves.append([xpos+2, ypos+1])
        if xpos>=1:
            allmoves.append([xpos-1, ypos+2])
        if xpos>=2:
            allmoves.append([xpos-2, ypos+1])
        
    possiblemoves=allmoves
    if checking==False:
        possiblemoves=filtermove(allmoves,grid)
    return possiblemoves
    
def getallmovesforbishop(xpos,ypos,grid,checking):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[] 

    uprightblock=False
    bottomrightblock=False
    bottomleftblock=False
    upleftblock=False
    
    for count in range(1,8):#Checks 7 times as thats the maximum number of squares it can move in diagonal direction
        if uprightblock==False:#If the up right diagonal path isn't blocked
            if xpos+count <=7 and ypos+(-count)>=0:#If not on the top row or last coloumn
                allmoves.append([xpos+count,ypos+(-count)])#Then the square to the top right is a possible move
                if squares.getoccupied(xpos+count,ypos+(-count),grid)!=True:#If the square was empty
                    pass
                else:
                    uprightblock=True#Then the path is now blocked

        if bottomrightblock==False:            
            if xpos+count <=7 and ypos+count <=7:#If not on the bottom row or last coloumn
                allmoves.append([xpos+count,ypos+count])
                if squares.getoccupied(xpos+count,ypos+count,grid)!=True:
                    pass
                else:
                    bottomrightblock=True

        if bottomleftblock==False:       
            if xpos+(-count)>=0 and ypos+count<=7:#If not on the bottom row or first coloumn
                allmoves.append([xpos+(-count),ypos+count])
                if squares.getoccupied(xpos+(-count),ypos+count,grid)!=True:
                    pass
                else:
                    bottomleftblock=True

        if upleftblock==False:       
            if xpos+(-count)>=0 and ypos+(-count)>=0:#If not on the top row or first coloumn
                allmoves.append([xpos+(-count),ypos+(-count)])
                if squares.getoccupied(xpos+(-count),ypos+(-count),grid)!=True:
                    pass
                else:
                    upleftblock=True
                    
    possiblemoves=allmoves              
    if checking==False:
        possiblemoves=filtermove(allmoves,grid)
                    
    return possiblemoves

def getallmovesforqueen(xpos,ypos,grid,checking):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[]
    bishopallmoves=getallmovesforbishop(xpos,ypos,grid,checking)
    rookallmoves=getallmovesforrook(xpos,ypos,grid,checking)
    
    for count in range(0,len(bishopallmoves)):
        allmoves.append(bishopallmoves[count])
    for count in range(0,len(rookallmoves)):
        allmoves.append(rookallmoves[count])
        
    possiblemoves=allmoves
    if checking==False:
        possiblemoves=filtermove(allmoves,grid)
        
    return possiblemoves

def getallmovesforking(xpos,ypos,grid,checking):
    xpos=int(xpos)
    ypos=int(ypos)
    allmoves=[]

    if xpos<=6:#The square on the top right is a possible move
        allmoves.append([xpos+1,ypos])#The square on the right is a possible move
    if xpos>=1:#If on the right side of the (or on the) second coloumn
        allmoves.append([xpos-1,ypos])#The square on the left is a possible move
    if ypos>=1:#If below the(or on the) second row...
        allmoves.append([xpos,ypos-1])#The square on the top is a possible move
        if xpos<=6:#...and on the left side of the (or on the) second last coloumn
            allmoves.append([xpos+1,ypos-1])#The square on the top right is a possible move
        if xpos>=1:#...and on the right side of the (or on the) second coloumn
            allmoves.append([xpos-1,ypos-1])#The square on the top left is a possible move

    if ypos<=6:
        allmoves.append([xpos,ypos+1])
        if xpos<=6:
            allmoves.append([xpos+1,ypos+1])
        if xpos>=1:
            allmoves.append([xpos-1,ypos+1])
    possiblemoves=allmoves
    if checking==False:
        possiblemoves=filtermove(allmoves,grid)
    return possiblemoves

def filtermove(allmoves,grid):
    possiblemoves=[]
    
    for count in range (len(allmoves)):
        if grid[(allmoves[count][1])][(allmoves[count][0])]==1:
            possiblemoves.append(allmoves[count])
        else:
            if playercounter==1:
                if grid[(allmoves[count][1])][(allmoves[count][0])][0]=="W":
                    possiblemoves.append(allmoves[count])
            if playercounter==2:
                if grid[(allmoves[count][1])][(allmoves[count][0])][0]=="B":
                    possiblemoves.append(allmoves[count])
                    
    return possiblemoves

def checkifclickedonpiece(mousex,mousey):
    legalmove=False
    possiblemoves=[]
    startx,starty=mousex,mousey 
    clickedonpiece=squares.getoccupied(startx, starty, grid)

    if clickedonpiece==True:#If the square is occupied
        if playercounter==1: #If black's turn
            if grid[starty][startx][0]=="B": #If clicked square is white piece
                legalmove=True
        elif playercounter==2:
            if grid[starty][startx][0]=="W":
                legalmove=True

    if legalmove==True:
        piecetype=grid[starty][startx][1]
        if piecetype =="K":
            knightorking=grid[starty][startx][2]
            piecetype=piecetype+knightorking

        if piecetype=="P":
            possiblemoves=getallmovesforpawn(startx,starty,grid)
        if piecetype=="R":
            possiblemoves=getallmovesforrook(startx,starty,grid,checking=False)
        if piecetype=="KN":
            possiblemoves=getallmovesforknight(startx,starty,grid,checking=False)
        if piecetype=="B":
            possiblemoves=getallmovesforbishop(startx,starty,grid,checking=False)
        if piecetype=="Q":
            possiblemoves=getallmovesforqueen(startx,starty,grid,checking=False)        
        if piecetype=="KI":
            possiblemoves=getallmovesforking(startx,starty,grid,checking=False)

    return clickedonpiece,startx,starty,possiblemoves

def highlight(possiblemoves, squares):
    squarecor,squareslist=squares.getposofsquare(possiblemoves)
    
    for counter in range(0, len(possiblemoves)):
        if grid[(possiblemoves[counter][1])][(possiblemoves[counter][0])]==1:
            highlight=pygame.draw.rect(DISPLAYSURF,Buttons,(squareslist[squarecor[counter][0]].x,squareslist[squarecor[counter][0]].y,64,64),3)
        else:
            highlight=pygame.draw.rect(DISPLAYSURF,red,(squareslist[squarecor[counter][0]].x,squareslist[squarecor[counter][0]].y,64,64),3)

    return squarecor,squareslist

def removehighlights(squarecor,squareslist,possiblemoves):
    for counter in range(0,len(possiblemoves)):
        removehighlight=pygame.draw.rect(DISPLAYSURF,black,(squareslist[squarecor[counter][0]].x,squareslist[squarecor[counter][0]].y,64,64),3)

def validatemove(endx,endy,possiblemoves):
    legalmove=False
    for count in range(0,len(possiblemoves)):
        if possiblemoves[count][0] == endx and possiblemoves[count][1]==endy:
            legalmove=True

    return legalmove

def movepiece(startx,starty,endx,endy,board,squareslist,P1listchars,P2listchars,grid):
    grid[endy][endx]=grid[starty][startx]
    grid[starty][startx]=1
    grid=board.update(grid,startx,starty,endx,endy,squareslist,P1listchars,P2listchars)
    return grid

def getallwhitemoves(P1listchars,P2listchars,grid,checking):
    allposmoveslist=[]
    for col in range(0,8): 
        for row in range(0,8):
            if squares.getoccupied(col,row,grid)==True:
                if grid[row][col][:3]=="WP1":
                    pawnmoves=getallmovesforpawn(P2listchars[0].getxpos(),P2listchars[0].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="WP2":
                    pawnmoves=getallmovesforpawn(P2listchars[1].getxpos(),P2listchars[1].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="WP3":
                    pawnmoves=getallmovesforpawn(P2listchars[2].getxpos(),P2listchars[2].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="WP4":
                    pawnmoves=getallmovesforpawn(P2listchars[3].getxpos(),P2listchars[3].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    

                if grid[row][col][:3]=="WP5":
                    pawnmoves=getallmovesforpawn(P2listchars[4].getxpos(),P2listchars[4].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="WP6":
                    pawnmoves=getallmovesforpawn(P2listchars[5].getxpos(),P2listchars[5].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="WP7":
                    pawnmoves=getallmovesforpawn(P2listchars[6].getxpos(),P2listchars[6].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="WP8":
                    pawnmoves=getallmovesforpawn(P2listchars[7].getxpos(),P2listchars[7].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                    
                if grid[row][col][:3]=="WR1":
                    rookmoves=getallmovesforrook(P2listchars[8].getxpos(),P2listchars[8].getypos(),grid,checking)
                    if not rookmoves:
                        pass
                    else:
                        allposmoveslist.append(rookmoves)

                if grid[row][col][:3]=="WR2":
                    rookmoves=getallmovesforrook(P2listchars[15].getxpos(),P2listchars[15].getypos(),grid,checking)
                    if not rookmoves:
                        pass
                    else:
                        allposmoveslist.append(rookmoves)

                if grid[row][col][:4]=="WKN1":
                    knightmoves=getallmovesforknight(P2listchars[9].getxpos(),P2listchars[9].getypos(),grid,checking)
                    if not knightmoves:
                        pass
                    else:
                        allposmoveslist.append(knightmoves)

                if grid[row][col][:4]=="WKN2":
                    knightmoves=getallmovesforknight(P2listchars[14].getxpos(),P2listchars[14].getypos(),grid,checking)
                    if not knightmoves:
                        pass
                    else:
                        allposmoveslist.append(knightmoves)

                if grid[row][col][:3]=="WB1":
                    bishopmoves=getallmovesforbishop(P2listchars[10].getxpos(),P2listchars[10].getypos(),grid,checking)
                    if not bishopmoves:
                        pass
                    else:
                        allposmoveslist.append(bishopmoves)

                if grid[row][col][:3]=="WB2":
                    bishopmoves=getallmovesforbishop(P2listchars[13].getxpos(),P2listchars[13].getypos(),grid,checking)
                    if not bishopmoves:
                        pass
                    else:
                        allposmoveslist.append(bishopmoves)
                        
                if grid[row][col][:3]=="WKI":
                    kingmoves=getallmovesforking(P2listchars[11].getxpos(),P2listchars[11].getypos(),grid,checking=False)
                    if not kingmoves:
                        pass
                    else:
                        allposmoveslist.append(kingmoves)

                if grid[row][col][:2]=="WQ":
                    queenmoves=getallmovesforqueen(P2listchars[12].getxpos(),P2listchars[12].getypos(),grid,checking)
                    if not queenmoves:
                        pass
                    else:
                        allposmoveslist.append(queenmoves)

    return allposmoveslist

    
def getallblackmoves(P1listchars,P2listchars,grid,checking):
    allposmoveslist=[]
    for col in range(0,8): 
        for row in range(0,8):
            if squares.getoccupied(col,row,grid)==True:
                if grid[row][col][:3]=="BP1":
                    pawnmoves=getallmovesforpawn(P1listchars[0].getxpos(),P1listchars[0].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="BP2":
                    pawnmoves=getallmovesforpawn(P1listchars[1].getxpos(),P1listchars[1].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="BP3":
                    pawnmoves=getallmovesforpawn(P1listchars[2].getxpos(),P1listchars[2].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="BP4":
                    pawnmoves=getallmovesforpawn(P1listchars[3].getxpos(),P1listchars[3].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    

                if grid[row][col][:3]=="BP5":
                    pawnmoves=getallmovesforpawn(P1listchars[4].getxpos(),P1listchars[4].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)
                    
                if grid[row][col][:3]=="BP6":
                    pawnmoves=getallmovesforpawn(P1listchars[5].getxpos(),P1listchars[5].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="BP7":
                    pawnmoves=getallmovesforpawn(P1listchars[6].getxpos(),P1listchars[6].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                if grid[row][col][:3]=="BP8":
                    pawnmoves=getallmovesforpawn(P1listchars[7].getxpos(),P1listchars[7].getypos(),grid)
                    if not pawnmoves:
                        pass
                    else:
                        allposmoveslist.append(pawnmoves)

                    
                if grid[row][col][:3]=="BR1":
                    rookmoves=getallmovesforrook(P1listchars[8].getxpos(),P1listchars[8].getypos(),grid,checking)
                    if not rookmoves:
                        pass
                    else:
                        allposmoveslist.append(rookmoves)

                if grid[row][col][:3]=="BR2":
                    rookmoves=getallmovesforrook(P1listchars[15].getxpos(),P1listchars[15].getypos(),grid,checking)
                    if not rookmoves:
                        pass
                    else:
                        allposmoveslist.append(rookmoves)

                if grid[row][col][:4]=="BKN1":
                    knightmoves=getallmovesforknight(P1listchars[9].getxpos(),P1listchars[9].getypos(),grid,checking)
                    if not knightmoves:
                        pass
                    else:
                        allposmoveslist.append(knightmoves)

                if grid[row][col][:4]=="BKN2":
                    knightmoves=getallmovesforknight(P1listchars[14].getxpos(),P1listchars[14].getypos(),grid,checking)
                    if not knightmoves:
                        pass
                    else:
                        allposmoveslist.append(knightmoves)

                if grid[row][col][:3]=="BB1":
                    bishopmoves=getallmovesforbishop(P1listchars[10].getxpos(),P1listchars[10].getypos(),grid,checking)
                    if not bishopmoves:
                        pass
                    else:
                        allposmoveslist.append(bishopmoves)

                if grid[row][col][:3]=="BB2":
                    bishopmoves=getallmovesforbishop(P1listchars[13].getxpos(),P1listchars[13].getypos(),grid,checking)
                    if not bishopmoves:
                        pass
                    else:
                        allposmoveslist.append(bishopmoves)
                        
                if grid[row][col][:3]=="BKI":
                    kingmoves=getallmovesforking(P1listchars[11].getxpos(),P1listchars[11].getypos(),grid,checking=False)
                    if not kingmoves:
                        pass
                    else:
                        allposmoveslist.append(kingmoves)

                if grid[row][col][:2]=="BQ":
                    queenmoves=getallmovesforqueen(P1listchars[12].getxpos(),P1listchars[12].getypos(),grid,checking)
                    if not queenmoves:
                        pass
                    else:
                        allposmoveslist.append(queenmoves)    
            
    return allposmoveslist

def checkifplayerwillbeincheck(startx,starty,endx,endy,P1listchars,P2listchars,grid):
    allmoves=[]
    allposmoves=[]
    checking=True
    incheck=False
    ghostgrid=copy.deepcopy(grid)
    ghostgrid[endy][endx]=ghostgrid[starty][startx]
    ghostgrid[starty][startx]=1

    if playercounter==1:
        allposmoveslist=getallwhitemoves(P1listchars,P2listchars,ghostgrid,checking)
    else:
        allposmoveslist=getallblackmoves(P1listchars,P2listchars,ghostgrid,checking)
        
    for count in range(0, (len(allposmoveslist))):
        for count2 in range(0, (len(allposmoveslist[count]))):
            allposmoves.append(allposmoveslist[count][count2])

    for count in range(0,len(allposmoves)):
        if ghostgrid[(allposmoves[count][1])][(allposmoves[count][0])]==1:
            allmoves.append(allposmoves[count])
        else:
            if ghostgrid[(allposmoves[count][1])][(allposmoves[count][0])][0]=="W" and playercounter==2:
                allmoves.append(allposmoves[count])

            if ghostgrid[(allposmoves[count][1])][(allposmoves[count][0])][0]=="B" and playercounter==1:
                allmoves.append(allposmoves[count])
    
        
    if grid[starty][startx][:3]=="WKI":
        whitekingxpos=endx
        whitekingypos=endy
    else:
        whitekingxpos=int(P2listchars[11].getxpos())
        whitekingypos=int(P2listchars[11].getypos())

    if grid[starty][startx][:3]=="BKI":
        blackkingxpos=endx
        blackkingypos=endy
    else:
        blackkingxpos=int(P1listchars[11].getxpos())
        blackkingypos=int(P1listchars[11].getypos())

    for count in range(0,len(allmoves)-1):
        if playercounter==2:
            if allmoves[count][0]==whitekingxpos and whitekingypos==allmoves[count][1]:
                print("White will be in check")
                incheck=True #White King in check

        else:
            if allmoves[count][0]==blackkingxpos and blackkingypos==allmoves[count][1]:
                print("Black will be in check")
                incheck=True #Black King in check


    return incheck

def checkifcheckmate(playercounter,P1listchars,P2listchars,grid):
    checkmate=False
    allposmoveslist=[]
    allposmoves=[]
    allmoves=[]

    if playercounter==2:#the one in check
        allposmoveslist=getallblackmoves(P1listchars,P2listchars,grid,checking=True)
        kingxpos,kingypos=int(P2listchars[11].getxpos()),int(P2listchars[11].getypos())
    else:
        allposmoveslist=getallwhitemoves(P1listchars,P2listchars,grid,checking=True)
        kingxpos,kingypos=int(P1listchars[11].getxpos()),int(P1listchars[11].getypos())

    for count in range(0, (len(allposmoveslist))):
        for count2 in range(0, (len(allposmoveslist[count]))):
            allposmoves.append(allposmoveslist[count][count2])

    for count in range(0,len(allposmoves)):
        if grid[(allposmoves[count][1])][(allposmoves[count][0])]==1:
            allmoves.append(allposmoves[count])
        else:
            if grid[(allposmoves[count][1])][(allposmoves[count][0])][0]=="W" and playercounter==2:
                allmoves.append(allposmoves[count])

            if grid[(allposmoves[count][1])][(allposmoves[count][0])][0]=="B" and playercounter==1:
                allmoves.append(allposmoves[count])

    kingmoves=getallmovesforking(kingxpos,kingypos,grid,checking=False)

    poskingmoves=len(kingmoves)

    for count in range (len(kingmoves)):
        for count2 in range (len(allmoves)-1):
            if kingmoves[count-1][0]==allmoves[count2][0] and kingmoves[count-1][1]==allmoves[count2][1]:
                poskingmoves=poskingmoves-1

    if poskingmoves==0:
        checkmate=True

    return checkmate

def endgame(Playername,playercounter):
    pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
    displayendgamescreen(playercounter,Playername)

def setup():
    global grid
    global playercounter
    playercounter=1
    MainMenuStateFinal.run()
    Playername, Playerhouse, spriterow,grid,playercounter = MainMenuStateFinal.returnproperties()
    boardmap=GameplayscreenFinal.displayscreen(Playerhouse)
    return Playername, Playerhouse, boardmap,spriterow,playercounter

def initalise(spriterow):
    global playerindex
    global squareslist
    playerindex = 0  # For setting up the characters on the board
    
    squares = Square()  #Creates an instance of the Square class
    squareslist=squares.create() #Creates the squares for the board
    board = Board(spriterow) #Creates an instance of the Board class
    P1listchars,P2listchars=board.initaliseplayers() #Initalises players

    return P1listchars,P2listchars,board,squareslist,squares

def restart():
    Playername, Playerhouse, boardmap, spriterow,playercounter=setup()
    P1listchars,P2listchars,board,squareslist,squares=initalise(spriterow)
    return Playername, Playerhouse, boardmap, spriterow,P1listchars,P2listchars,board,squareslist,squares

def displayendgamescreen(playercounter,Playername):
    pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
    endgamestate=True
    
    if playercounter==2:#If the first player was checkmated
        winner=Playername[0]#then other player has won
    else:
        winner=Playername[1]

    winnername=winnerfont.render(winner,True,Buttons)
    winnerdisplay=winnerfont.render("wins!",True,Buttons)
    swordsicon=pygame.image.load("swords.jpg")
    DISPLAYSURF.blit(winnername,(60,40))
    DISPLAYSURF.blit(winnerdisplay,(140,140))
    DISPLAYSURF.blit(swordsicon,(500,50))

    while endgamestate==True:
        mouse=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and 652 > mouse[0] > 432 and 547 > mouse[1] > 417:#If quit button is clicked
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN and 342 > mouse[0] > 122 and 547 > mouse[1] > 417:
                endgamestate=False

        Menu=MainMenuStateFinal.Buttonswithicon("backarrow.jpg",160, 285, 122, 417, 220, 130, Intitialbuttonsfont, "MAIN MENU", 138, 460,house=False)
        Menu=MainMenuStateFinal.Buttonswithicon("Quitbuttonimg.jpg",460, 255, 432, 417, 220, 130, quitbuttonfont, "QUIT", 490, 460,house=False)

        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.draw.rect(DISPLAYSURF, Background, (160, 285, 250,150))
        pygame.draw.rect(DISPLAYSURF, Background, (460, 265, 250,150))

def savegame(grid,Playername,Playerhouse,playercounter):
    savefile=shelve.open("ChessOfThronesSaveFile")
    savefile["PlayerNames"]=Playername
    savefile["PlayerHouses"]=Playerhouse
    savefile["Turn"]=playercounter
    savefile["BoardState"]=grid
    savefile.close()    


clickedonpiece=False 

Playername, Playerhouse, boardmap, spriterow,playercounter=setup()
P1listchars,P2listchars,board,squareslist,squares=initalise(spriterow)

while True:
    playagain=False
    mouse = pygame.mouse.get_pos()
    mousex, mousey = GameplayscreenFinal.displaynotations(mouse)  # Checks if mouse is hovered over characters/buttons
    mousex=int(mousex) 
    mousex-=1
    mousey=int(mousey)
    mousey-=1

    GameplayscreenFinal.displayplayer(playercounter,Playername)
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if 550>=mouse[0]>=50 and 550>=mouse[1]>=50: #If inside board 
            if clickedonpiece==False: #If not clicked on piece
                indicatechar(mousex,mousey,squareslist) #Then highlight/show the icon of the char
            if event.type==MOUSEBUTTONDOWN and clickedonpiece==False:
                clickedonpiece,startx,starty,possiblemoves=checkifclickedonpiece(mousex,mousey)
                if clickedonpiece==True:
                    squarecor,squareslist=highlight(possiblemoves, squares)

            elif clickedonpiece==True:
                if event.type==MOUSEBUTTONDOWN:
                    endx,endy=mousex,mousey
                    if not(startx == endx and starty == endy):
                        legalmove=validatemove(endx,endy,possiblemoves)
                        if legalmove==True:
                            legalmove=False
                            incheck=checkifplayerwillbeincheck(startx,starty,endx,endy,P1listchars,P2listchars,grid)
                            if incheck==False:
                                pygame.draw.rect(DISPLAYSURF,Background,(565,313,300,60))
                                legalmove=True
                                grid=movepiece(startx,starty,endx,endy,board,squareslist,P1listchars,P2listchars,grid)
                                if playercounter==1:
                                    playercounter=2
                                else:
                                    playercounter=1
                            else:
                                name=playernamedisplayfont.render("Invalid move! Your",False,Buttons)
                                DISPLAYSURF.blit(name,(565,323))
                                name=playernamedisplayfont.render("king will be in check",False,Buttons)
                                DISPLAYSURF.blit(name,(565,348))
                                
                                checkmate=checkifcheckmate(playercounter,P1listchars,P2listchars,grid)
                                if checkmate==True:
                                    displayendgamescreen(playercounter,Playername)
                                    playagain=True
                        
                                    
                    removehighlights(squarecor,squareslist,possiblemoves)
                    clickedonpiece=False
                    pygame.draw.rect(DISPLAYSURF,Background,(565,293,300,30))
                    

        elif 754 > mouse[0] > 604 and 559 > mouse[1] > 478: 
            if event.type==MOUSEBUTTONDOWN:
                pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
                playagain=True

        elif 754 > mouse[0] > 604 and 460>mouse[1]>376:
            if event.type==MOUSEBUTTONDOWN:
                savegame(grid,Playername,Playerhouse,playercounter)

    if playagain==True:
        playgain=False
        pygame.draw.rect(DISPLAYSURF, Background, (0,0,800,600))
        Playername, Playerhouse, boardmap, spriterow,P1listchars,P2listchars,board,squareslist,squares=restart()

    pygame.display.update()
    fpsClock.tick(FPS)
