# tictactoe-graphics-python
from graphics import *
import time


def window():
    win = GraphWin('TIC TAC TOE', 1000, 1000)
    win.setBackground('thistle1')
    return win

def draw_grid(win):
    lines = [
        Line(Point(400, 200), Point(400, 800)),
        Line(Point(600, 200), Point(600, 800)),
        Line(Point(200, 400), Point(800, 400)),
        Line(Point(200, 600), Point(800, 600))
    ]

    for line in lines:
        line.setWidth(5)
        line.draw(win)

    return lines



def victory(win, player):
    message = Text(Point(500, 100), f"🎉Victory!")
    message.setSize(36)
    message.setTextColor("DarkGreen")
    message.setStyle("bold")
    message.draw(win)

    return message

def check_vic(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def button(win):
    # bottom-left corner placement
    bp1 = Point(80, 790)    # moved down
    bp2 = Point(220, 890)   # moved down

    shadow = Oval(Point(90, 800), Point(230, 900))  # also moved down
    shadow.setWidth(0)
    shadow.setFill('DarkOliveGreen')
    shadow.draw(win)

    button = Oval(bp1, bp2)
    button.setWidth(0)
    button.setFill('DarkOliveGreen4')
    button.draw(win)

    label = Text(Point((80 + 220)//2, (790 + 890)//2), "Restart")  # midpoint of button
    label.setSize(20)
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    

    return bp1, bp2, button, label, shadow

def quitB(win):
    qp1 = Point(780, 790)
    qp2 = Point(920, 890)

   
    shadow = Oval(Point(790, 800), Point(930, 900))
    shadow.setWidth(0)
    shadow.setFill('darkorchid')  
    shadow.draw(win)

    button = Oval(qp1, qp2)
    button.setWidth(0)
    button.setFill('mediumpurple') 
    button.draw(win)

  
    label = Text(Point((780 + 920) // 2, (790 + 890) // 2), "Quit")
    label.setSize(20)
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    return qp1, qp2, button, label, shadow
    
'''Made this function for the counters for wins and tied games. This function called for the window
for the parameter. Then, at the end returns the messages that are used for later down in the code.'''
def counterWIN(win):
    
    Player1 = Text(Point(150,100), "Player 1 Wins: 0")  
    Player1.setSize(20)
    Player1.setStyle("bold")
    Player1.setTextColor("palegreen4")
    Player1.draw(win)

    Player2 = Text(Point(150,130), "Player 2 Wins: 0")  
    Player2.setSize(20)
    Player2.setStyle("bold")
    Player2.setTextColor("mediumpurple1")
    Player2.draw(win)

    Tiedgame = Text(Point(138, 160), "Tied Games: 0")
    Tiedgame.setSize(20)
    Tiedgame.setStyle("bold")
    Tiedgame.setTextColor("orchid")
    Tiedgame.draw(win)

    

    return Player1, Player2, Tiedgame

def clicked(win):
    
    if bp3.getX() <= click.getX() <= bp4.getX() and bp3.getY() <= click.getY() <= bp4.getY():
        button2.move(10, 10)
        label2.move(10, 10)
        time.sleep(.5)
        button2.move(-10, -10)
        label2.move(-10, -10)

def tictactoe():
    win = window()
    grid_lines = draw_grid(win)
    #Our buttons. 
    bp1, bp2, restart_button, restart_label, restart_shadow = button(win)
    qp1, qp2, quit_button, quit_label, quit_shadow = quitB(win)

    
#For the messages that are in our counterWIN(win) function. Start our count at 0 to be
#Updated as the game goes on.
    Player1c = 0
    Player2c = 0
    Tiedc = 0
#The gameover is currently set to false, and the end result message is set to none right now.
#I had to do this to have the messages undraw themselves after we restart the game.
    #Also,I neede to create a variable called gameover to have it be True or False so that once we get a result, the buttons will only work. 
    gameover = False
    resultmess= None

    
    player1wins, player2wins, Tiedwins = counterWIN(win)
    
    turn = 0
    board = [[None for _ in range(3)] for _ in range(3)]
    shapelist = []
    
    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()

        if qp1.getX() <= x <= qp2.getX() and qp1.getY() <= y <= qp2.getY():
            # 1. Animate the button press
            quit_button.move(10, 10)
            quit_label.move(10, 10)
            time.sleep(0.1)
            quit_button.move(-10, -10)
            quit_label.move(-10, -10)
            win.close()
            return

        if bp1.getX() <= x <= bp2.getX() and bp1.getY() <= y <= bp2.getY():
            # animate button press
            restart_button.move(10, 10)
            restart_label.move(10, 10)
            time.sleep(0.1)
            restart_button.move(-10, -10)
            restart_label.move(-10, -10)

            if resultmess is not None:
                resultmess.undraw()
                resultmess = None
                
            # reset board and undraw shapes
            for mark in shapelist:
                mark.undraw()
            shapelist.clear()
            board = [[None for _ in range(3)] for _ in range(3)]
            turn = 0
            #Another flag telling the program the game is still going. 
            gameover = False
#Once our game over equal false, then the only logic that will work is the code before it. 
        if gameover:   
            continue
        
        #create cells, #y or x - 200 shifts the starting point down
        #ie, y - 200 and x - 200 starts the board at 200, 200 and not 0, 0
        # // is floor division, seperates into 0, 1 and 2
        #ie, if i click point 300, 300, it is goint to set it to column 0 and row 0
        row = int((y - 200) // 200)
        col = int((x - 200) // 200)
        cell = [row, col]

        #make x
        #the math here, pemdas so 200 + col * 200 sets it to the front of a column then + 100 centers it
        centerx = 200 + col * 200 + 100
        centery = 200 + row * 200 + 100
       
        #set bounds to keep xs and os in
        if 299 < centerx < 701 and 299 < centery < 701:

            # don't allow playing in an already-filled cell
            if board[row][col] is not None:
                continue 



            #if turn is an even number make an x upon    
            if turn % 2 == 0:
                player = 'X'

                board[row][col] = "X"
           
                line1 = Line(Point(centerx - 40, centery - 40), Point(centerx + 40, centery + 40))
                line2 = Line(Point(centerx - 40, centery + 40), Point(centerx + 40, centery - 40))
                line1.setFill('PaleGreen4')
                line2.setFill('PaleGreen4')
                line1.setWidth(18)
                line2.setWidth(18)
                
                lines = [line1, line2]
                    
                for i in lines:
                    i.draw(win)
                    shapelist.append(i)



            #if niether other condition fits print O upon click
            else:
                board[row][col] = "O"
                player = 'O'

                circle = Circle(Point(centerx, centery), 40)
                circle.setWidth(18)
                circle.setOutline('MediumPurple1')
                circle.draw(win)

                shapelist.append(circle)

            if check_vic(board, player):
                
                resultmess = victory(win, f"Player {player} wins!")
                
               
                # 2. Update the Win Count and Text Display
                if player == 'X':
                    Player1c += 1
                    player1wins.setText(f"Player 1 Wins: {Player1c}") # Update screen text
                elif player == 'O':
                    Player2c += 1
                    player2wins.setText(f"Player 2 Wins: {Player2c}")
                
                colors = ['slateblue','lavender','thistle','plum','violet','orchid','lightgreen','palegreen','chartreuse','greenyellow','seagreen','lavenderblush','black']
                for i in range(2):
                    for color in colors:
                        for line in grid_lines:
                          line.setOutline(color)
                          time.sleep(.02)
#END THE GAME. Finally, our game ends after the result, and also our flicker effect.
#The gameover will now, run through this function again but this time, it will be true.
#Only having the restart button to work and the quit button.   
                gameover = True
                continue
                
        print(f"You clicked on row{row}, column {col}")

        
            #END THE GAME. Finally, our game ends after the result, and also our flicker effect.
            #The gameover will now, run through this function again but this time, it will be true.
            #Only having the restart button to work.             
          


        turn += 1

        if turn >= 9:
            Tiedc += 1
            Tiedwins.setText(f"Tied Games: {Tiedc}")
            
            tie = Text(Point(500,100),"Tied Game")
            tie.setSize(36)
            tie.setTextColor("orchid")
            tie.setStyle("bold")
            tie.draw(win)
            resultmess= tie

            gameover = True
            continue






def main():
    tictactoe()

main()

