# RULES OF THE GAME
print("Enter the position as a number")



# list of board spaces
board = ['-','-','-','-','-','-','-','-','-']


# function to display the board
def display():
    print(board[0],' ', board[1],' ', board[2])
    print(board[3],' ', board[4],' ', board[5])
    print(board[6],' ', board[7],' ', board[8])

display()


# function to determine if player 1 won
def win1():
    def win_check1():
        win_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
        count = 0
        for i in win_list:
            for j in i:
                if board[j] == 'X':
                    count += 1
            if count == 3:
                return True
                break
            count = 0

    abc = win_check1()

    if abc == True:
        return True
    
# function to determine if player 2 won
def win2():
    def win_check2():
        win_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
        count = 0
        for i in win_list:
            for j in i:
                if board[j] == 'O':
                    count += 1
            if count == 3:
                return True
                break
            count = 0

    abc = win_check2()

    if abc == True:
        return True

# function to determine if game is tied
def tied():
    count = 0
    for i in board:
        if i != '-':
            count += 1
    if count == 9:
        return True


# function to take input from player 1
def take_input():
    for i in range(1,10):
        marker1 = int(input('Player no. 1:- '))
        
        if (marker1 in range(1,10)) and board[marker1-1] == '-':
            board[marker1-1] = 'X'
            win = win1()
            tie = tied()
            if win == True:
                display()
                print('Player 1 wins')
                break
            if tie == True:
                display()
                print('Game is tied')
                break
            display()
        else:
            print('Invalid input')
            display()
            take_input()
        
        
        win2()
        abc = take_input2()
        if abc == True:
            return

# function to take input from player 2
def take_input2():
    marker2 = int(input('Player no. 2: -'))
    if (marker2 in range(1,10)) and (board[marker2-1] == '-'):
            board[marker2-1] = 'O'
            win = win2()
            if win == True:
                display()
                print('Player 2 wins')
                return True
            else:
                display()
    else:
            print('Invalid input')
            display()
            take_input2()
    
take_input()



    